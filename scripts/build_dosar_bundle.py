#!/usr/bin/env python3
"""R31 — Build DOSAR_DATE_BRUTE.md bundle from canonical JSONs.

Concatenează toate JSON-urile canonice medicale din Dosar_Medical/*.json într-un
fișier MD narativ structurat, optim pentru retrieval Claude Projects (chunking pe
headere markdown ##/###).

Excluse: .meta.json companions, MANIFEST.json, SYSTEM_HEALTH.json, carte_identitate
+ talon_pensie (admin redundante cu CONTEXT_MEDICAL.md §1).

Output: _projects_sync/DOSAR_DATE_BRUTE.md
Trigger: orice modificare la Dosar_Medical/*.json (auto via pre-commit hook).
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

# Forțează UTF-8 pe Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
DOSAR_DIR = ROOT / "Dosar_Medical"
OUTPUT = ROOT / "_projects_sync" / "DOSAR_DATE_BRUTE.md"

# JSON-uri excluse (admin redundante / non-medical)
EXCLUDE_NAMES = {
    "MANIFEST.json",
    "SYSTEM_HEALTH.json",
    "2023-06-12_carte_identitate.json",
    "2025-11-01_talon_pensie_asigurare.json",
}


def collect_canonical_jsons():
    """Returnează lista JSON canonice medicale, sortate cronologic."""
    files = []
    for f in DOSAR_DIR.glob("*.json"):
        if f.name in EXCLUDE_NAMES:
            continue
        if f.name.endswith(".meta.json"):
            continue
        files.append(f)
    files.sort(key=lambda p: p.name)
    return files


def get_data_doc(meta, json_path):
    """Returnează data_document; fallback la pattern YYYY-MM-DD din nume fișier."""
    val = meta.get("data_document")
    if val:
        return val
    m = re.match(r"(\d{4}-\d{2}-\d{2})", json_path.stem)
    return m.group(1) if m else "????-??-??"


def render_value(val, depth=0):
    """Render recursiv valoare JSON în MD, cu indentare."""
    indent = "  " * depth
    if val is None:
        return "_(null)_"
    if isinstance(val, bool):
        return "✅ true" if val else "❌ false"
    if isinstance(val, (int, float, str)):
        s = str(val).strip()
        if not s:
            return "_(empty)_"
        if "\n" in s:
            return "\n" + "\n".join(indent + "  > " + line for line in s.splitlines())
        return s
    if isinstance(val, list):
        if not val:
            return "_(listă goală)_"
        lines = []
        for item in val:
            if isinstance(item, dict):
                lines.append(f"\n{indent}- " + render_dict_inline(item, depth + 1))
            else:
                lines.append(f"\n{indent}- {render_value(item, depth + 1)}")
        return "".join(lines)
    if isinstance(val, dict):
        return "\n" + render_dict_block(val, depth + 1)
    return str(val)


def render_dict_inline(d, depth):
    """Render dict scurt inline pentru list items."""
    indent = "  " * depth
    parts = []
    for k, v in d.items():
        if isinstance(v, (dict, list)) and v:
            parts.append(f"\n{indent}- **{k}:** {render_value(v, depth + 1)}")
        else:
            parts.append(f"**{k}:** {render_value(v, depth)}")
    return " · ".join(p for p in parts if not p.startswith("\n")) + "".join(p for p in parts if p.startswith("\n"))


def render_dict_block(d, depth):
    """Render dict ca bullet list."""
    indent = "  " * depth
    lines = []
    for k, v in d.items():
        if v is None or v == "":
            continue
        if isinstance(v, (dict, list)):
            lines.append(f"{indent}- **{k}:**{render_value(v, depth + 1)}")
        else:
            lines.append(f"{indent}- **{k}:** {render_value(v, depth)}")
    return "\n".join(lines)


def render_section(json_path):
    """Render un JSON canonic ca secțiune MD."""
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except Exception as e:
        return f"\n## ❌ {json_path.name} — eroare parsing\n\n```\n{e}\n```\n"

    meta = data.get("_metadata", {})
    data_doc = get_data_doc(meta, json_path)
    tip = meta.get("tip_document", "necunoscut")
    specialitate = meta.get("specialitate", "")
    nume_fisier = meta.get("nume_fisier", json_path.name)

    # Slug pentru anchor
    slug = json_path.stem.replace("_", "-")

    title = f"{data_doc} — {tip.replace('_', ' ').title()}"
    if specialitate:
        title += f" ({specialitate})"

    out = [f"\n---\n\n## <a name=\"{slug}\"></a> {title}\n"]
    out.append(f"**Sursă:** `Dosar_Medical/{nume_fisier}`")
    if meta.get("numar_buletin"):
        out.append(f" · **Buletin:** {meta['numar_buletin']}")
    if meta.get("confidence_overall"):
        out.append(f" · **Confidence:** {meta['confidence_overall']}")
    if meta.get("flags"):
        flags = ", ".join(meta["flags"]) if isinstance(meta["flags"], list) else str(meta["flags"])
        out.append(f" · **Flags:** {flags}")
    out.append("\n")

    if meta.get("notes"):
        out.append(f"\n> {meta['notes']}\n")

    # Secțiuni standard schema v2
    sections = [
        ("pacient", "👤 Pacient"),
        ("diagnostic", "🩺 Diagnostic"),
        ("analize_laborator", "🧪 Analize laborator"),
        ("tratament", "💊 Tratament / Procedură"),
        ("recomandari", "📋 Recomandări"),
        ("medici_unitati", "👥 Medici / Unități"),
        ("analize_in_curs", "⏳ Analize în curs"),
        ("numere_referinta", "🔢 Numere referință"),
        ("context_clinic", "🏥 Context clinic"),
        # Câmpuri specifice altor scheme
        ("findings", "🔍 Findings"),
        ("interventie", "🔧 Intervenție"),
        ("examinari_efectuate", "🔬 Examinări efectuate"),
        ("parametri_tehnici", "⚙️ Parametri tehnici"),
        ("concluzie", "📝 Concluzie"),
        ("recomandari_post", "📌 Recomandări post-procedură"),
    ]

    for key, header in sections:
        if key in data and data[key]:
            out.append(f"\n### {header}\n")
            out.append(render_value(data[key]))
            out.append("\n")

    # Câmpuri suplimentare nemapate (catch-all)
    handled = {"_metadata"} | {k for k, _ in sections}
    extras = {k: v for k, v in data.items() if k not in handled and v}
    if extras:
        out.append("\n### 📦 Date suplimentare\n")
        out.append(render_value(extras))
        out.append("\n")

    return "".join(out)


def build_bundle():
    files = collect_canonical_jsons()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Header bundle
    lines = [
        "# DOSAR_DATE_BRUTE — Bundle JSON canonice medicale\n",
        f"\n**Generat automat:** {now}",
        " · **Sursă:** `Dosar_Medical/*.json` (excluse: meta.json, MANIFEST, SYSTEM_HEALTH, carte_identitate, talon_pensie)",
        f" · **Total documente:** {len(files)}\n",
        "\n> **Scop:** retrieval direct în Claude Projects pentru date medicale brute (analize, imagistică, biopsie, medicație, scrisori medicale, intervenții). Sursa primară rămâne JSON-urile canonice individuale; acest bundle e mirror narativ pentru parcurs RAG eficient.",
        "\n>",
        "\n> **NU edita acest fișier direct** — e regenerat la fiecare commit cu modificare în `Dosar_Medical/*.json` (R31 + pre-commit hook).\n",
        "\n---\n\n## 📚 Cuprins\n",
    ]

    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            meta = data.get("_metadata", {})
            data_doc = get_data_doc(meta, f)
            tip = meta.get("tip_document", "necunoscut").replace("_", " ")
            slug = f.stem.replace("_", "-")
            lines.append(f"\n- [{data_doc} — {tip}](#{slug})")
        except Exception:
            lines.append(f"\n- ⚠️ {f.name} (parse error)")

    # Conținut secțiuni
    for f in files:
        section = render_section(f)
        lines.append(section)

    # Footer
    lines.append("\n---\n")
    lines.append(f"\n_Sfârșit bundle. {len(files)} documente canonice incluse._\n")

    return "".join(lines)


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    bundle = build_bundle()
    OUTPUT.write_text(bundle, encoding="utf-8")
    size_kb = OUTPUT.stat().st_size / 1024
    files_count = len(collect_canonical_jsons())
    print(f"  ✅ Generat: DOSAR_DATE_BRUTE.md ({size_kb:.1f} KB, {files_count} JSON-uri canonice)")


if __name__ == "__main__":
    main()
