#!/usr/bin/env python3
"""Audit foldere Dosar_Medical/documente_sursa/ — detect violări R14, R26.

Output: Dosar_Medical/AUDIT_DOCUMENTE_SURSA.md (regenerat la fiecare rulare).

R14 = chain of custody (.meta.json companion obligatoriu).
R26 = consistență structură foldere (NN_categorie_data/ + YYYY-MM-DD_descriere.ext).

Acceptă `intermediate_artifacts` în .meta.json al unui PDF master ca acoperire pentru
JPEG-uri pagini intermediare (ex: 14_UPU_2024_05_30/2024-05-30_dosar_upu_pag*.jpeg
acoperite de meta-ul `2024-05-30_dosar_upu_complet.pdf.meta.json`).

Creat 2026-04-28 ca parte din Faza 2 plan implementare cross-terminal (recomandare N4
din .claude-outputs/imbunatatiri/2026-04-28_032030/).
"""

import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "Dosar_Medical" / "documente_sursa"
OUTPUT = ROOT / "Dosar_Medical" / "AUDIT_DOCUMENTE_SURSA.md"

FOLDER_PATTERN = re.compile(r"^\d{2}_[a-zA-Z][a-zA-Z0-9_]*$")
FILE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}_[a-zA-Z0-9_-]+\.(pdf|jpe?g|png)$", re.IGNORECASE)


def collect_intermediate_files(folder):
    """Citește toate .meta.json din folder + extrage intermediate_artifacts.files (R14 indirect)."""
    intermediate = set()
    for meta_file in folder.glob("*.meta.json"):
        try:
            data = json.loads(meta_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        ia = data.get("intermediate_artifacts")
        if isinstance(ia, dict) and isinstance(ia.get("files"), list):
            intermediate.update(ia["files"])
    return intermediate


def audit():
    if not DOCS.exists():
        print("documente_sursa/ does not exist")
        return None

    cutoff_empty = datetime.now() - timedelta(days=30)
    issues = {
        "empty_folders_long": [],
        "non_canonical_folder": [],
        "non_canonical_file": [],
        "missing_meta_json": [],
        "stats": {"total_folders": 0, "populated": 0, "total_files": 0, "with_meta": 0, "intermediate_artifacts": 0},
    }

    for folder in sorted(DOCS.iterdir()):
        if not folder.is_dir():
            continue
        issues["stats"]["total_folders"] += 1

        if not FOLDER_PATTERN.match(folder.name):
            issues["non_canonical_folder"].append(folder.name)

        media_files = [
            f for f in folder.iterdir()
            if f.suffix.lower() in (".pdf", ".jpeg", ".jpg", ".png")
        ]

        if not media_files:
            mtime = datetime.fromtimestamp(folder.stat().st_mtime)
            if mtime < cutoff_empty:
                issues["empty_folders_long"].append({
                    "folder": folder.name,
                    "last_modified": mtime.strftime("%Y-%m-%d"),
                    "days_empty": (datetime.now() - mtime).days,
                })
            continue

        issues["stats"]["populated"] += 1
        issues["stats"]["total_files"] += len(media_files)

        intermediate_files = collect_intermediate_files(folder)

        for f in media_files:
            if not FILE_PATTERN.match(f.name):
                issues["non_canonical_file"].append(str(f.relative_to(DOCS)).replace("\\", "/"))
            meta = f.parent / f"{f.name}.meta.json"
            if meta.exists():
                issues["stats"]["with_meta"] += 1
            elif f.name in intermediate_files:
                issues["stats"]["with_meta"] += 1
                issues["stats"]["intermediate_artifacts"] += 1
            else:
                issues["missing_meta_json"].append(str(f.relative_to(DOCS)).replace("\\", "/"))

    return issues


def render_report(issues):
    s = issues["stats"]
    md = f"""# AUDIT documente_sursa/ — Raport automat

**Generat:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Script:** `scripts/audit_documente_sursa.py` (R14 chain of custody + R26 consistență structură)

## Stats

| Metric | Valoare |
|---|---|
| Total foldere | {s['total_folders']} |
| Foldere populate | {s['populated']} ({s['populated']*100//max(s['total_folders'],1)}%) |
| Total fișiere PDF/JPEG | {s['total_files']} |
| Cu `.meta.json` direct | {s['with_meta'] - s['intermediate_artifacts']} |
| Acoperite prin `intermediate_artifacts` | {s['intermediate_artifacts']} |
| **Coverage R14 total** | **{s['with_meta']}/{s['total_files']} ({s['with_meta']*100//max(s['total_files'],1)}%)** |

## 🟠 Foldere goale > 30 zile (R26 — semnal P1)

"""
    if not issues["empty_folders_long"]:
        md += "_(niciun folder gol > 30 zile)_\n\n"
    else:
        for item in issues["empty_folders_long"]:
            md += f"- **{item['folder']}** — gol de {item['days_empty']} zile (ultima modificare: {item['last_modified']})\n"
        md += "\n"

    md += "## 🔴 Foldere cu nume non-canonic (R26 violation)\n\n"
    if not issues["non_canonical_folder"]:
        md += "_(toate folderele sunt canonice — `NN_categorie_data/`)_\n\n"
    else:
        for f in issues["non_canonical_folder"]:
            md += f"- `{f}` — așteaptă format `NN_categorie_data/`\n"
        md += "\n"

    md += "## 🔴 Fișiere fără `.meta.json` (R14 violation)\n\n"
    if not issues["missing_meta_json"]:
        md += "_(toate fișierele au companion `.meta.json` direct sau acoperire prin `intermediate_artifacts`)_\n\n"
    else:
        for f in issues["missing_meta_json"][:20]:
            md += f"- `{f}` — lipsește chain of custody\n"
        if len(issues["missing_meta_json"]) > 20:
            md += f"\n_... și încă {len(issues['missing_meta_json']) - 20} fișiere_\n"
        md += "\n"

    md += "## 🟡 Fișiere cu nume non-canonic\n\n"
    if not issues["non_canonical_file"]:
        md += "_(toate fișierele respectă format `YYYY-MM-DD_descriere.ext`)_\n\n"
    else:
        for f in issues["non_canonical_file"][:20]:
            md += f"- `{f}` — așteaptă format `YYYY-MM-DD_descriere.{{pdf,jpeg,png}}`\n"
        md += "\n"

    md += """## Acțiuni propuse

- Foldere goale > 30 zile → adăugare în `TODO.md` ca P1 (obținere documente lipsă)
- `.meta.json` lipsă → completare chain of custody (R14) la următoarea procesare. Pentru artefacte intermediare derivate dintr-un PDF master, declarați-le în `intermediate_artifacts.files` în meta-ul PDF-ului master (acoperire R14 indirectă).
- Nume non-canonice → redenumire cu confirmare user (R26 + R7)

---

_Raport regenerat automat la fiecare rulare a `scripts/audit_documente_sursa.py`. Înlocuiește versiunea anterioară. Pentru istoric, consultă git log._
"""
    return md


def main():
    issues = audit()
    if not issues:
        return 1
    report = render_report(issues)
    OUTPUT.write_text(report, encoding="utf-8")
    print(f"Raport scris: {OUTPUT.relative_to(ROOT)}")
    print(f"  Empty folders > 30d: {len(issues['empty_folders_long'])}")
    print(f"  Missing .meta.json: {len(issues['missing_meta_json'])}")
    print(f"  Intermediate artifacts (acoperire R14 indirectă): {issues['stats']['intermediate_artifacts']}")
    print(f"  Non-canonical folders: {len(issues['non_canonical_folder'])}")
    print(f"  Non-canonical files: {len(issues['non_canonical_file'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
