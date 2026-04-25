#!/usr/bin/env python3
"""Generator INDEX.json — sursă unică query-abil pentru întreg dosarul.

Scanează proiectul, extrage frontmatter YAML din .md + metadata din .json
medical, agreghează în INDEX.json la rădăcina proiectului.

Folosit de:
  - DASHBOARD.html tab Echipă medicală (fetch INDEX.json client-side)
  - Search global INDEX.json (Task #13)
  - Future automation (R27 auto-propagare ingest Gmail)

Execuție: `python scripts/generate_index.py`
Output:   `INDEX.json` la rădăcina proiectului
"""

import json
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
OUTPUT = ROOT / "INDEX.json"
SKIP_DIRS = {".git", "node_modules", ".claude-outputs", "__pycache__", "arhiva"}

# Regex pentru detectare frontmatter YAML simplu (fără safe_load — lightweight)
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text):
    """Parsează frontmatter YAML simplu (key: value) — NU obiecte/liste imbricate.

    Returnează dict cu chei top-level. Liste pe o linie [a, b, c] și liste
    multi-linie cu '-' sunt suportate la nivel top.
    """
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    raw = m.group(1)
    data = {}
    current_list_key = None
    for raw_line in raw.split("\n"):
        if not raw_line.strip():
            current_list_key = None
            continue
        # Continuare listă cu indent + dash
        if current_list_key and raw_line.lstrip().startswith("-"):
            item = raw_line.lstrip()[1:].strip()
            if item:
                data[current_list_key].append(item)
            continue
        # Element cheie: valoare
        if ":" in raw_line and not raw_line.startswith(" "):
            key, _, value = raw_line.partition(":")
            key = key.strip()
            value = value.strip()
            if not value:
                # Listă multi-linie va urma
                data[key] = []
                current_list_key = key
            elif value.startswith("[") and value.endswith("]"):
                # Listă inline
                items = [x.strip().strip("'\"") for x in value[1:-1].split(",") if x.strip()]
                data[key] = items
                current_list_key = None
            else:
                # Valoare simplă (string, număr)
                data[key] = value.strip("'\"")
                current_list_key = None
        else:
            current_list_key = None
    return data


def relpath_str(path):
    return str(path.relative_to(ROOT)).replace("\\", "/")


def safe_walk(start, ext_glob):
    """rglob cu try/except pentru sync issues Drive."""
    try:
        for f in start.rglob(ext_glob):
            if any(skip in f.parts for skip in SKIP_DIRS):
                continue
            try:
                yield f
            except OSError:
                continue
    except OSError:
        return


def main():
    medici_oncohelp = []
    corespondenta = []
    documente_canonice = []
    cross_references = {}
    files_by_path = {}

    # 1. Medici OncoHelp — extrage din Dosar_Medical/CONTACTE_MEDICALE.md
    contacte_md = ROOT / "Dosar_Medical" / "CONTACTE_MEDICALE.md"
    if contacte_md.exists():
        try:
            text = contacte_md.read_text(encoding="utf-8")
            # Caut blocurile YAML cu id: dr-...
            for match in re.finditer(
                r"```yaml\s*\n(.*?)```", text, re.DOTALL
            ):
                yaml_block = match.group(1)
                # Parse simplu pe blocul YAML medical
                medic = {}
                for line in yaml_block.split("\n"):
                    if ":" in line and not line.startswith(" ") and not line.startswith("\t"):
                        key, _, value = line.partition(":")
                        medic[key.strip()] = value.strip()
                if medic.get("id", "").startswith("dr-"):
                    medic["file"] = relpath_str(contacte_md) + f"#{medic['id']}"
                    medici_oncohelp.append(medic)
        except (OSError, UnicodeDecodeError):
            pass

    # 2. Corespondență — Dosar_Medical/corespondenta/*.md (NU INDEX.md)
    coresp_dir = ROOT / "Dosar_Medical" / "corespondenta"
    if coresp_dir.exists():
        for f in coresp_dir.glob("*.md"):
            if f.name == "INDEX.md":
                continue
            try:
                text = f.read_text(encoding="utf-8")
                fm = parse_frontmatter(text)
                if fm:
                    fm["file"] = relpath_str(f)
                    corespondenta.append(fm)
            except (OSError, UnicodeDecodeError):
                continue

    # 3. Documente canonice — Dosar_Medical/*.json (excl. .meta.json + arhiva + corespondenta)
    dosar_dir = ROOT / "Dosar_Medical"
    if dosar_dir.exists():
        for f in dosar_dir.glob("*.json"):
            if f.name.endswith(".meta.json") or f.name == "SYSTEM_HEALTH.json":
                continue
            try:
                with open(f, encoding="utf-8") as fh:
                    doc = json.load(fh)
                # Schema v2 are uneori metadata.{date,type,...} sau direct la rădăcină
                meta = doc.get("metadata", doc)
                entry = {
                    "id": f.stem,
                    "file": relpath_str(f),
                    "data": meta.get("date") or meta.get("data") or meta.get("data_examinare"),
                    "tip": meta.get("type") or meta.get("tip") or meta.get("tip_document"),
                    "medic": meta.get("medic") or meta.get("medic_emitent"),
                    "unitate": meta.get("unitate") or meta.get("unitate_emitenta"),
                }
                documente_canonice.append({k: v for k, v in entry.items() if v is not None})
            except (OSError, UnicodeDecodeError, json.JSONDecodeError):
                continue

    # 4. files_by_path — agregat tot proiectul .md/.json/.html (excl. arhiva/.git)
    for ext_glob in ("*.md", "*.json", "*.html"):
        for f in safe_walk(ROOT, ext_glob):
            try:
                stat = f.stat()
                files_by_path[relpath_str(f)] = {
                    "type": f.suffix.lstrip("."),
                    "size_kb": round(stat.st_size / 1024, 1),
                    "last_modified": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
                }
            except OSError:
                continue

    # 5. cross_references — linkuri medic → fișiere care îl menționează
    medic_names = []
    for m in medici_oncohelp:
        nume = m.get("nume", "")
        if nume:
            # Format „Anater Angelo-Christian" — cheamă „Anater" pentru match simplu
            medic_names.append((nume.split()[0], m.get("id", "")))
    for short_name, medic_id in medic_names:
        if not short_name:
            continue
        refs = []
        for path_str in files_by_path:
            full_path = ROOT / path_str
            try:
                if full_path.suffix in (".md", ".json"):
                    text = full_path.read_text(encoding="utf-8", errors="ignore")
                    if short_name in text:
                        refs.append(path_str)
            except (OSError, UnicodeDecodeError):
                continue
        cross_references[short_name] = refs[:20]  # cap la 20 pentru claritate

    # Stats
    stats = {
        "total_files_indexed": len(files_by_path),
        "medici_oncohelp": len(medici_oncohelp),
        "threaduri_gmail": len(corespondenta),
        "documente_canonice": len(documente_canonice),
        "atasamente_listate": 0,  # TODO Task viitor — extras din corespondenta + atașamente
    }

    output = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "version": "1.0",
        "stats": stats,
        "medici_oncohelp": medici_oncohelp,
        "corespondenta": corespondenta,
        "documente_canonice": documente_canonice,
        "cross_references": cross_references,
        "files_by_path": files_by_path,
    }

    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"INDEX.json generated: {OUTPUT}")
    print(f"  Stats: {stats}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
