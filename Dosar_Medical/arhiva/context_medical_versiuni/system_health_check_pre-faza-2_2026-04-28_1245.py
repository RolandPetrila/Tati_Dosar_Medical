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

# Limite — vezi Regula 28 (REGULI_CLAUDE_CODE.md)
# Rafinare 2026-04-26 (ticket P2 din TODO închis):
#   - INTRODUS metric `auto_loaded_md_kb` (suma fișierelor REALMENTE auto-loaded
#     la pornire sesiune) cu prag 100 KB. Aceasta este alertă REALĂ pentru
#     risc context window — independent de logs istorice.
#   - DEMOTE `total_md_root_kb` la metric INFORMATIV (fără limit/status). Suma
#     brută `.md` la rădăcină include CHANGELOG.md + SESSION_LOG.md care cresc
#     natural cu activitatea proiectului și NU sunt auto-injected. Pragul
#     anterior 1024 KB declanșa fals-pozitive predictibile.
LIMITS = {
    "context_tokens_estimate": {"limit": 200_000, "type": "tokens"},
    "claude_md_size_kb": {"limit": 40, "type": "kb"},
    "memory_md_lines": {"limit": 200, "type": "lines"},
    # auto_loaded_md_kb prag 150 KB: 5 fișiere auto-loaded × ~40 KB CLAUDE.md
    # oficial = ~200 KB teoretic; 150 KB lasă headroom ~50% pentru creștere
    # naturală (reguli noi, update-uri nested) fără fals-pozitive. La 150 KB
    # ≈ 50K tokens = 25% Sonnet 200k / 5% Opus 1M — încă mult sub critic.
    "auto_loaded_md_kb": {"limit": 150, "type": "kb"},
    "largest_file_kb": {"limit": 200, "type": "kb"},
    "index_json_size_kb": {"limit": 1024, "type": "kb"},
}

# Fișiere REALMENTE auto-încărcate la sesiune (CLAUDE.md + nested + reference reads
# declanșate de CLAUDE.md root la prima interacțiune). Nested CLAUDE.md sunt
# încărcate contextual (când Claude lucrează în subfolder), dar le includem în
# total deoarece pot fi sumate la o sesiune obișnuită care traversează folderul.
AUTO_LOADED_FILES = [
    "CLAUDE.md",                            # always-on root
    "REGULAMENT.md",                        # citit la prima interacțiune (per ordine din CLAUDE.md root)
    "REGULI_CLAUDE_CODE.md",                # citit la prima interacțiune
    "Dosar_Medical/CLAUDE.md",              # nested contextual
    "Documente_Informative/CLAUDE.md",      # nested contextual
]

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

    # auto_loaded_md_kb — suma fișierelor REALMENTE auto-loaded la sesiune
    # (alertă REALĂ pentru risc context window; independent de logs istorice)
    auto_loaded_total_kb = 0.0
    auto_loaded_breakdown = []
    for rel_path in AUTO_LOADED_FILES:
        f = ROOT / rel_path
        if f.exists():
            try:
                size_kb = round(f.stat().st_size / 1024, 1)
                auto_loaded_total_kb += size_kb
                auto_loaded_breakdown.append({"path": rel_path, "size_kb": size_kb})
            except OSError:
                continue
    metrics["auto_loaded_md_kb"] = {
        **metric(round(auto_loaded_total_kb, 1), "auto_loaded_md_kb"),
        "breakdown": auto_loaded_breakdown,
        "note": "suma fișierelor auto-loaded la pornire sesiune (CLAUDE.md root + REGULAMENT + REGULI + nested CLAUDE.md). Pragul 150 KB e alertă reală pentru risc context window.",
    }

    # total_md_root_kb — INFORMATIV (NU declanșează status; vezi auto_loaded_md_kb pentru alertă reală)
    total_md = sum(f.stat().st_size for f in ROOT.glob("*.md"))
    total_md_kb = round(total_md / 1024, 1)
    metrics["total_md_root_kb"] = {
        "current": total_md_kb,
        "note": "informativ — suma brută `.md` la rădăcină; include logs istorice (CHANGELOG, SESSION_LOG) care NU sunt auto-loaded. Pentru alertă reală vezi `auto_loaded_md_kb`. Demotează 2026-04-26 (ticket P2 închis).",
    }

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

    # Estimate context tokens — aliniat cu AUTO_LOADED_FILES (5 fișiere) pentru
    # consistency cu auto_loaded_md_kb
    texts = []
    for rel_path in AUTO_LOADED_FILES:
        f = ROOT / rel_path
        if f.exists():
            try:
                texts.append(f.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError):
                continue
    all_text = "".join(texts)
    tokens = estimate_tokens(all_text)
    metrics["context_tokens_estimate"] = {
        **metric(tokens, "context_tokens_estimate"),
        "note": "estimat pe AUTO_LOADED_FILES (5 fișiere: CLAUDE.md root + REGULAMENT + REGULI + nested CLAUDE.md). Read-uri ad-hoc, MEMORY.md auto-injection, sistem-reminders nu sunt incluse — context real e mai mare.",
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
