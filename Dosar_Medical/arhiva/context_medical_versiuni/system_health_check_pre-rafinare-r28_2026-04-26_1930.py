#!/usr/bin/env python3
"""R28 System Health Check — generează Dosar_Medical/SYSTEM_HEALTH.json

Praguri (vezi REGULI_CLAUDE_CODE.md §Regula 28):
  🟢 OK         <60%
  🟡 WARNING    60-80%
  🟠 ALERT      80-95%
  🔴 CRITICAL   >=95%

Output: Dosar_Medical/SYSTEM_HEALTH.json (auto-generat la SessionStart hook).
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Forțează stdout/stderr UTF-8 pe Windows (pentru emojis status 🟢/🟡/🟠/🔴)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "Dosar_Medical" / "SYSTEM_HEALTH.json"

# Limite — vezi Regula 28
# Notă (rafinare 2026-04-25): total_md_root_kb ridicat de la 500 → 1024 KB.
# Justificare: suma brută `.md` la rădăcină include loguri istorice (CHANGELOG.md,
# SESSION_LOG.md) care NU sunt auto-loaded la pornire sesiune (doar CLAUDE.md e).
# Metricul care contează cu adevărat pentru context window e
# `context_tokens_estimate`, care urmărește auto-loaded files. 500KB brut era
# prea agresiv pentru un proiect cu logs istorice naturale.
# Refinare ulterioară planificată: metric nou `auto_loaded_md_kb` (doar fișierele
# realmente auto-loaded la sesiune) cu prag 100KB ca alertă reală — ticket P2 TODO.
LIMITS = {
    "context_tokens_estimate": {"limit": 200_000, "type": "tokens"},
    "claude_md_size_kb": {"limit": 40, "type": "kb"},
    "memory_md_lines": {"limit": 200, "type": "lines"},
    "total_md_root_kb": {"limit": 1024, "type": "kb"},
    "largest_file_kb": {"limit": 200, "type": "kb"},
    "index_json_size_kb": {"limit": 1024, "type": "kb"},
}

SKIP_DIRS = (".git", "node_modules", ".claude-outputs", "__pycache__")


def status_for(percent):
    if percent < 60:
        return "🟢 OK"
    if percent < 80:
        return "🟡 WARNING"
    if percent < 95:
        return "🟠 ALERT"
    return "🔴 CRITICAL"


def estimate_tokens(text):
    # Aproximare conservatoare: ~3.5 chars/token în română (limba dominantă în proiect)
    return len(text) // 3 if text else 0


def metric(current, limit_key):
    limit = LIMITS[limit_key]["limit"]
    percent = round(current / limit * 100, 1)
    return {
        "current": current,
        "limit": limit,
        "percent": percent,
        "status": status_for(percent),
    }


def main():
    metrics = {}

    # CLAUDE.md size
    claude_md = ROOT / "CLAUDE.md"
    if claude_md.exists():
        size_kb = round(claude_md.stat().st_size / 1024, 1)
        metrics["claude_md_size_kb"] = metric(size_kb, "claude_md_size_kb")

    # MEMORY.md lines (calea pentru auto-memory)
    memory_md = Path(
        "C:/Users/ALIENWARE/.claude/projects/G--My-Drive-Roly--Tati/memory/MEMORY.md"
    )
    if memory_md.exists():
        try:
            with open(memory_md, encoding="utf-8") as fh:
                lines = sum(1 for _ in fh)
            metrics["memory_md_lines"] = metric(lines, "memory_md_lines")
        except OSError as exc:
            metrics["memory_md_lines"] = {"error": str(exc)}

    # Total .md root size (doar fișiere din rădăcină, NU subfoldere)
    total_md = sum(f.stat().st_size for f in ROOT.glob("*.md"))
    total_md_kb = round(total_md / 1024, 1)
    metrics["total_md_root_kb"] = metric(total_md_kb, "total_md_root_kb")

    # Cele mai mari fișiere din proiect (.md / .html / .json)
    largest = []
    for ext in ("*.md", "*.html", "*.json"):
        try:
            for f in ROOT.rglob(ext):
                if any(skip in str(f) for skip in SKIP_DIRS):
                    continue
                try:
                    largest.append((f.stat().st_size / 1024, str(f.relative_to(ROOT))))
                except (OSError, ValueError):
                    continue
        except OSError:
            continue
    largest.sort(reverse=True)
    metrics["largest_files"] = [
        {"path": p.replace("\\", "/"), "size_kb": round(s, 1)}
        for s, p in largest[:10]
    ]
    over_limit_threshold = LIMITS["largest_file_kb"]["limit"]
    metrics["files_over_limit"] = [
        {"path": p.replace("\\", "/"), "size_kb": round(s, 1)}
        for s, p in largest
        if s > over_limit_threshold
    ]

    # INDEX.json size (dacă există — generat în Task #12)
    index_json = ROOT / "INDEX.json"
    if index_json.exists():
        size_kb = round(index_json.stat().st_size / 1024, 1)
        metrics["index_json_size_kb"] = metric(size_kb, "index_json_size_kb")

    # Estimate context tokens — fișiere auto-loaded la pornire sesiune
    auto_loaded = [
        ROOT / "CLAUDE.md",
        ROOT / "REGULI_CLAUDE_CODE.md",
        ROOT / "REGULAMENT.md",
    ]
    texts = []
    for f in auto_loaded:
        if f.exists():
            try:
                texts.append(f.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError):
                continue
    all_text = "".join(texts)
    tokens = estimate_tokens(all_text)
    metrics["context_tokens_estimate"] = {
        **metric(tokens, "context_tokens_estimate"),
        "note": "estimat doar pe fișiere auto-loaded (CLAUDE.md + REGULI_CLAUDE_CODE.md + REGULAMENT.md). Read-uri ad-hoc, MEMORY.md auto-injection, sistem-reminders nu sunt incluse — context real e mai mare.",
    }

    # Overall status — cel mai rău dintre toate metricile cu status
    severity_order = ["🔴 CRITICAL", "🟠 ALERT", "🟡 WARNING", "🟢 OK"]
    statuses = [
        v["status"]
        for v in metrics.values()
        if isinstance(v, dict) and "status" in v
    ]
    overall = next((s for s in severity_order if s in statuses), "🟢 OK")

    # Recomandări
    recommendations = []
    for key, val in metrics.items():
        if not isinstance(val, dict) or "status" not in val:
            continue
        st = val["status"]
        pc = val.get("percent")
        if st.startswith("🟡"):
            recommendations.append(
                f"⚠ {key}: la {pc}% — propune restructurare proactivă"
            )
        elif st.startswith("🟠"):
            recommendations.append(
                f"🟠 {key}: la {pc}% — REFUZ scrieri masive până la restructurare"
            )
        elif st.startswith("🔴"):
            recommendations.append(
                f"🔴 {key}: la {pc}% — STOP scrieri. Restructurare urgentă."
            )
    for f in metrics.get("files_over_limit", []):
        recommendations.append(
            f"📄 Fișier mare: {f['path']} ({f['size_kb']}KB) — propune sharding"
        )

    output = {
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "status": overall,
        "limits": metrics,
        "recommendations": recommendations,
        "version": "1.0",
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"SYSTEM_HEALTH check: {overall}")
    print(f"  Output: {OUTPUT}")
    if recommendations:
        print("  Recommendations:")
        for r in recommendations:
            print(f"    {r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
