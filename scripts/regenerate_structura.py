#!/usr/bin/env python3
"""Regenerator STRUCTURA_PROIECT.md — secțiunea auto-generată „🗺 Hartă completă".

Detectează markerii `<!-- AUTO-GENERATED START -->` / `<!-- AUTO-GENERATED END -->`
în STRUCTURA_PROIECT.md și înlocuiește conținutul dintre ei cu un raport actualizat:

  - Arborele complet folder/fișiere (formatat tree)
  - Index thematic (caut [biopsie/medic/programare/dietă/corespondență]?)
  - Stats live (număr fișiere, dimensiuni, ultima modificare)

Execuție: `python scripts/regenerate_structura.py`
"""

import re
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "STRUCTURA_PROIECT.md"
SKIP_DIRS = {".git", "node_modules", ".claude-outputs", "__pycache__"}
START_MARKER = "<!-- AUTO-GENERATED START -->"
END_MARKER = "<!-- AUTO-GENERATED END -->"

THEMATIC_INDEX = [
    ("biopsie", ["Dosar_Medical/documente_sursa/12_biopsie_2026/", "TODO.md", "Documente_Informative/EXPLICATIE_CONSULT_ONCOLOG_SCENARII.md"]),
    ("medic / oncolog / programare", ["Dosar_Medical/CONTACTE_MEDICALE.md", "CONTEXT_MEDICAL.md (§9 Echipă medicală)", "TODO.md (Calendar + P0)"]),
    ("corespondență email medici", ["Dosar_Medical/corespondenta/INDEX.md", "Dosar_Medical/corespondenta/2026-04-*.md"]),
    ("dietă / alimentație", ["ALIMENTATIE.md", "DASHBOARD.html (tab Alimentație)"]),
    ("CT 20.04.2026", ["Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json", "Dosar_Medical/documente_sursa/11_CT_stadializare_2026/", "CONTEXT_MEDICAL.md §2"]),
    ("endoscopie / colonoscopie 17.04.2026", ["Dosar_Medical/2026-04-17_examen_gastroscopic.json", "Dosar_Medical/2026-04-17_examen_colonoscopic.json", "Dosar_Medical/documente_sursa/09_endoscopie_2026_04/"]),
    ("medicație + interacțiuni", ["CONTEXT_MEDICAL.md §4", "Dosar_Medical/2025-11-10_schema_medicamente.json", "Dosar_Medical/rapoarte_generate/2026-04-18_raport_reactii_adverse_jamesi_triplixam.docx"]),
    ("monitor automat biopsie ntfy.sh", ["TODO.md (secțiunea Monitor automat)", "C:\\Users\\ALIENWARE\\Desktop\\Roly\\Sistem_Notificari_Telefon\\ (repo extern)"]),
    ("DASHBOARD live (familie)", ["DASHBOARD.html", "https://rolandpetrila.github.io/Tati_Dosar_Medical/"]),
    ("reguli + protocol", ["CLAUDE.md (loader)", "REGULAMENT.md (R1-10 medicale)", "REGULI_CLAUDE_CODE.md (R6-29 specifice)"]),
    ("system health monitor R28", ["Dosar_Medical/SYSTEM_HEALTH.json", "scripts/system_health_check.py"]),
    ("plan execuție curent", ["PLAN_IMPLEMENTARE_2026-04-25.md (status în frontmatter)"]),
]


def build_tree(start, prefix="", max_depth=3, depth=0):
    """Construiește arbore folder text simplu cu indent + emoji."""
    if depth >= max_depth:
        return ""
    if any(skip in start.parts for skip in SKIP_DIRS):
        return ""
    lines = []
    try:
        children = sorted(start.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    except OSError:
        return ""
    file_count = sum(1 for c in children if c.is_file())
    folder_count = sum(1 for c in children if c.is_dir() and c.name not in SKIP_DIRS)
    if depth == 0:
        lines.append(f"{start.name}/  ({folder_count} subfoldere, {file_count} fișiere root)")
    for child in children:
        if child.name in SKIP_DIRS:
            continue
        if child.is_dir():
            n_files = sum(1 for f in child.rglob("*") if f.is_file())
            lines.append(f"{prefix}├── {child.name}/  ({n_files} fișiere)")
            sub = build_tree(child, prefix + "│   ", max_depth, depth + 1)
            if sub:
                lines.append(sub)
        else:
            try:
                size_kb = round(child.stat().st_size / 1024, 1)
                lines.append(f"{prefix}├── {child.name}  ({size_kb} KB)")
            except OSError:
                lines.append(f"{prefix}├── {child.name}")
    return "\n".join(lines)


def collect_stats():
    n_files_total = 0
    n_md = 0
    n_json = 0
    n_html = 0
    total_size = 0
    for f in ROOT.rglob("*"):
        if any(skip in f.parts for skip in SKIP_DIRS):
            continue
        if f.is_file():
            n_files_total += 1
            try:
                total_size += f.stat().st_size
            except OSError:
                continue
            if f.suffix == ".md":
                n_md += 1
            elif f.suffix == ".json":
                n_json += 1
            elif f.suffix == ".html":
                n_html += 1
    return {
        "total_files": n_files_total,
        "md": n_md,
        "json": n_json,
        "html": n_html,
        "total_size_kb": round(total_size / 1024, 1),
    }


def build_section():
    now = datetime.now().isoformat(timespec="seconds")
    stats = collect_stats()
    tree = build_tree(ROOT, max_depth=3)

    parts = [
        START_MARKER,
        "",
        "## 🗺 Hartă completă auto-generată",
        "",
        f"> ⚙️ **Generat automat:** {now} de `scripts/regenerate_structura.py`. NU edita manual această secțiune — modificările se pierd la următoarea regenerare. Pentru cuprinsul fix vezi secțiunile non-auto de mai sus.",
        "",
        "### 📊 Statistici live",
        "",
        f"- **Total fișiere proiect (excl. .git):** {stats['total_files']}",
        f"- **Markdown (.md):** {stats['md']}",
        f"- **JSON (.json):** {stats['json']}",
        f"- **HTML (.html):** {stats['html']}",
        f"- **Total size:** {stats['total_size_kb']} KB",
        "",
        "### 🧭 Index thematic (caut...)",
        "",
        "| Caut...                                        | Mergi la                                                                 |",
        "| ---------------------------------------------- | ------------------------------------------------------------------------ |",
    ]
    for theme, locations in THEMATIC_INDEX:
        loc_str = " · ".join(f"`{loc}`" for loc in locations)
        parts.append(f"| {theme}  | {loc_str} |")
    parts.extend([
        "",
        "### 🌳 Arbore folder (depth 3)",
        "",
        "```",
        tree,
        "```",
        "",
        END_MARKER,
    ])
    return "\n".join(parts)


def main():
    if not TARGET.exists():
        print(f"ERROR: {TARGET} nu există", file=sys.stderr)
        return 1

    text = TARGET.read_text(encoding="utf-8")
    new_section = build_section()

    if START_MARKER in text and END_MARKER in text:
        # Înlocuire între markeri — folosesc callable pentru a evita
        # interpretarea backslash escapes în new_section (Windows paths C:\Users)
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            re.DOTALL,
        )
        new_text = pattern.sub(lambda _m: new_section, text)
    else:
        new_text = text.rstrip() + "\n\n---\n\n" + new_section + "\n"

    TARGET.write_text(new_text, encoding="utf-8")
    print(f"STRUCTURA_PROIECT.md regenerated: {TARGET}")
    print(f"  Section size: ~{len(new_section)} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())
