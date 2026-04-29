"""Smoke test pentru scripts/system_health_check.py (R28 System Health Monitor).

Validează:
  - happy path: rulare main() pe proiectul real, output JSON valid cu structură R28
  - edge cases: pragurile status_for() la frontiere (60, 80, 95)
  - pure functions: estimate_tokens()
  - non-destructive: OUTPUT redirected în tmp_path, NU modifică Dosar_Medical/SYSTEM_HEALTH.json
"""

import json

import system_health_check


def test_main_returns_zero(tmp_path, monkeypatch):
    """Happy path: main() rulează pe proiectul real fără crash și returnează 0."""
    output_file = tmp_path / "SYSTEM_HEALTH.json"
    monkeypatch.setattr(system_health_check, "OUTPUT", output_file)

    rc = system_health_check.main()

    assert rc == 0
    assert output_file.exists()


def test_output_json_structure_complete(tmp_path, monkeypatch):
    """Output JSON conține toate câmpurile top-level cerute de R28."""
    output_file = tmp_path / "SYSTEM_HEALTH.json"
    monkeypatch.setattr(system_health_check, "OUTPUT", output_file)
    system_health_check.main()

    data = json.loads(output_file.read_text(encoding="utf-8"))

    for field in ("checked_at", "status", "limits", "recommendations", "version"):
        assert field in data, f"Missing top-level field: {field}"
    assert data["version"] == "1.0"
    assert isinstance(data["recommendations"], list)
    assert isinstance(data["limits"], dict)


def test_status_emoji_in_valid_set(tmp_path, monkeypatch):
    """Statusul global e unul din cele 4 valori valide."""
    output_file = tmp_path / "SYSTEM_HEALTH.json"
    monkeypatch.setattr(system_health_check, "OUTPUT", output_file)
    system_health_check.main()

    data = json.loads(output_file.read_text(encoding="utf-8"))
    valid_statuses = {"🟢 OK", "🟡 WARNING", "🟠 ALERT", "🔴 CRITICAL"}
    assert data["status"] in valid_statuses


def test_limits_contain_critical_metrics(tmp_path, monkeypatch):
    """Output limits conține metricile critice declarate în R28."""
    output_file = tmp_path / "SYSTEM_HEALTH.json"
    monkeypatch.setattr(system_health_check, "OUTPUT", output_file)
    system_health_check.main()

    data = json.loads(output_file.read_text(encoding="utf-8"))
    limits = data["limits"]

    expected_metrics = (
        "claude_md_size_kb",
        "auto_loaded_md_kb",
        "context_tokens_estimate",
    )
    for m in expected_metrics:
        assert m in limits, f"Missing critical metric: {m}"


def test_status_for_thresholds():
    """Edge cases la frontierele 60/80/95 (R28 limits boundaries)."""
    assert system_health_check.status_for(0) == "🟢 OK"
    assert system_health_check.status_for(59.9) == "🟢 OK"
    assert system_health_check.status_for(60) == "🟡 WARNING"
    assert system_health_check.status_for(79.9) == "🟡 WARNING"
    assert system_health_check.status_for(80) == "🟠 ALERT"
    assert system_health_check.status_for(94.9) == "🟠 ALERT"
    assert system_health_check.status_for(95) == "🔴 CRITICAL"
    assert system_health_check.status_for(150) == "🔴 CRITICAL"


def test_estimate_tokens_proportional():
    """estimate_tokens = len(text) // 3 — empty + linear + boundary."""
    assert system_health_check.estimate_tokens("") == 0
    assert system_health_check.estimate_tokens(None) == 0
    assert system_health_check.estimate_tokens("abc") == 1
    assert system_health_check.estimate_tokens("a" * 300) == 100
    assert system_health_check.estimate_tokens("a" * 600_000) == 200_000


def test_metric_returns_required_keys():
    """metric() returnează dict cu current/limit/percent/status."""
    result = system_health_check.metric(50, "claude_md_size_kb")
    assert "current" in result
    assert "limit" in result
    assert "percent" in result
    assert "status" in result
    assert result["current"] == 50
    assert result["limit"] == 40  # din LIMITS
    assert result["percent"] == 125.0  # 50/40 = 125%
    assert result["status"] == "🔴 CRITICAL"


def test_find_memory_md_via_env_var(tmp_path, monkeypatch):
    """find_memory_md prioritizează CLAUDE_MEMORY_PATH dacă fișierul există."""
    fake_memory = tmp_path / "MEMORY.md"
    fake_memory.write_text("test", encoding="utf-8")
    monkeypatch.setenv("CLAUDE_MEMORY_PATH", str(fake_memory))

    result = system_health_check.find_memory_md()
    assert result == fake_memory


def test_find_memory_md_invalid_env_var_falls_back(monkeypatch):
    """Dacă CLAUDE_MEMORY_PATH e setat dar fișierul nu există, fallback funcționează."""
    monkeypatch.setenv("CLAUDE_MEMORY_PATH", "/nonexistent/path/MEMORY.md")
    # Trebuie să găsească via slug standard sau search fallback (sau None)
    result = system_health_check.find_memory_md()
    # Acceptăm orice rezultat real: Path găsit sau None — important e să nu crash
    assert result is None or result.exists()
