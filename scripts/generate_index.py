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

try:
    import yaml  # PyYAML — parser robust pentru frontmatter cu obiecte/liste imbricate
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "INDEX.json"
SKIP_DIRS = {".git", "node_modules", ".claude-outputs", "__pycache__", "arhiva"}

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text):
    """Parsează frontmatter YAML.

    Folosește PyYAML dacă disponibil (suport complet pentru obiecte/liste imbricate).
    Fallback la parser lightweight dacă PyYAML lipsește.
    """
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    raw = m.group(1)
    if HAS_YAML:
        try:
            return yaml.safe_load(raw) or {}
        except yaml.YAMLError:
            pass
    # Fallback parser lightweight
    data = {}
    current_list_key = None
    for raw_line in raw.split("\n"):
        if not raw_line.strip():
            current_list_key = None
            continue
        if current_list_key and raw_line.lstrip().startswith("-"):
            item = raw_line.lstrip()[1:].strip()
            if item:
                data[current_list_key].append(item)
            continue
        if ":" in raw_line and not raw_line.startswith(" "):
            key, _, value = raw_line.partition(":")
            key, value = key.strip(), value.strip()
            if not value:
                data[key] = []
                current_list_key = key
            elif value.startswith("[") and value.endswith("]"):
                items = [x.strip().strip("'\"") for x in value[1:-1].split(",") if x.strip()]
                data[key] = items
                current_list_key = None
            else:
                data[key] = value.strip("'\"")
                current_list_key = None
        else:
            current_list_key = None
    return data


def parse_yaml_block(text):
    """Parsează un bloc YAML standalone (fără frontmatter)."""
    if HAS_YAML:
        try:
            return yaml.safe_load(text) or {}
        except yaml.YAMLError:
            pass
    return {}


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


CATEGORIE_LABELS = {
    "01_identitate": "Identitate",
    "02_cardiologie_2012": "Cardiologie (Vichy 2012)",
    "03_hernie_anterior": "Hernie (anterioară)",
    "04_helicobacter_2024": "Helicobacter pylori (2024)",
    "05_analize_laborator": "Analize laborator",
    "06_urologie_gastro_2025": "Urologie + gastro (2025)",
    "07_hernie_2025_11": "Hernie (noiembrie 2025)",
    "08_schema_tratament": "Schemă medicație",
    "09_endoscopie_2026_04": "Endoscopie (17.04.2026)",
    "10_administrativ_pensie": "Administrativ (pensie)",
    "11_CT_stadializare_2026": "CT stadializare (20.04.2026)",
    "12_biopsie_2026": "Biopsie esofagiană (2026)",
    "13_cardiologie_ambulator_2025": "Cardiologie ambulator (2025)",
    "14_UPU_2024_05_30": "UPU Arad (30.05.2024)",
    "15_consult_initial_oncologie_2026": "Consult inițial OncoHelp (30.04.2026)",
}


def strip_md_to_preview(md_text, max_chars=220):
    """Extrage primele ~max_chars caractere din MD ca preview text plain.

    Sare peste frontmatter + primul H1 + blockquotes meta (`> Notă...`) la început;
    păstrează primul paragraf narativ real.
    """
    text = md_text
    # Strip frontmatter
    fm_match = FRONTMATTER_RE.match(text)
    if fm_match:
        text = text[fm_match.end():]
    # Strip primele linii: H1, blockquotes meta, separatoare ---, până găsim narativ
    lines = text.split("\n")
    body_lines = []
    skipped_intro = False
    for line in lines:
        stripped = line.strip()
        if not skipped_intro:
            # Sărim peste H1, blockquotes (`> ...`), separatoare (`---`), gol
            if not stripped:
                continue
            if stripped.startswith("# ") or stripped.startswith(">") or stripped == "---":
                continue
            # Prima linie non-meta → începem
            skipped_intro = True
        body_lines.append(line)
    body = "\n".join(body_lines).strip()
    # Strip markdown syntax mărunt (bold/italic/code/links + headings rămase + listă)
    body = re.sub(r"\*\*([^*]+)\*\*", r"\1", body)
    body = re.sub(r"\*([^*]+)\*", r"\1", body)
    body = re.sub(r"`([^`]+)`", r"\1", body)
    body = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", body)
    body = re.sub(r"^#{1,6}\s+", "", body, flags=re.MULTILINE)
    body = re.sub(r"^[-*]\s+", "• ", body, flags=re.MULTILINE)
    body = re.sub(r"^\|.*\|\s*$", "", body, flags=re.MULTILINE)  # rânduri tabel
    body = re.sub(r"\n{2,}", " · ", body).replace("\n", " ")
    body = re.sub(r"\s{2,}", " ", body).strip()
    if len(body) > max_chars:
        cut = body[:max_chars].rsplit(" ", 1)[0]
        body = cut + "…"
    return body


def slug_to_titlu(slug):
    """Converti slug `2026-04-20_ct_torace_abdomen_pelvis` în titlu curat „CT torace abdomen pelvis (20.04.2026)".

    Strip data prefix + capitalize primul cuvânt + adaug data formatată la final.
    """
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})_(.*)", slug)
    if not m:
        return slug.replace("_", " ").strip().capitalize()
    yyyy, mm, dd, rest = m.groups()
    rest = rest.replace("_", " ").strip()
    # Capitalizează specific termenii medicali frecvenți
    upper_words = {"ct", "rmn", "iva", "upu", "hp", "ecg", "eco", "igg", "anti"}
    parts = rest.split(" ")
    fixed = []
    for w in parts:
        wl = w.lower()
        if wl in upper_words:
            fixed.append(wl.upper())
        elif fixed:
            fixed.append(wl)
        else:
            fixed.append(wl[:1].upper() + wl[1:])
    if fixed and fixed[0].lower() == fixed[0]:
        fixed[0] = fixed[0][:1].upper() + fixed[0][1:]
    return f"{' '.join(fixed)} ({dd}.{mm}.{yyyy})"


def extract_titlu_from_md(md_text, fallback_slug):
    """Caută titlu utilizabil din MD; sare peste „RAPORT EXTRAGERE", „N. METADATE", „1. ..." etc.

    Fallback: slug formatat via `slug_to_titlu`.
    """
    fm_match = FRONTMATTER_RE.match(md_text)
    text = md_text[fm_match.end():] if fm_match else md_text
    skip_pattern = re.compile(
        r"raport extragere|extragere strict|format v\d|metadate document|surs[ăa] (originar|primar)|^\d+\.\s|^opis\s|^borderou",
        re.IGNORECASE,
    )
    for line in text.split("\n")[:80]:
        stripped = line.strip()
        if stripped.startswith("# ") or stripped.startswith("## "):
            level_chars = 2 if stripped.startswith("# ") else 3
            t = stripped[level_chars:].strip()
            t = re.sub(r"\s*`?\[[^\]]+\]`?\s*$", "", t).strip()
            if skip_pattern.search(t):
                continue
            # Acceptă doar dacă conține un cuvânt clinic concret
            if re.search(r"\b(CT|RMN|ecograf|endoscop|gastroscop|colonoscop|biopsie|stent|hernie|consult|scrisoare|bilet|buletin|analize|schema|scheme|talon|carte|identitate|UPU|cardiologie|urologie|helicobacter|HP|trimitere|examen)\b", t, re.IGNORECASE):
                return t
    return slug_to_titlu(fallback_slug)


def extract_documente_pentru_dashboard(root, json_files):
    """Scanează Dosar_Medical/documente_sursa/ pentru *_extragere.md și produce metadata pentru DASHBOARD tab.

    Pentru fiecare MD: id, titlu, data, categorie, md_path, preview, size_kb,
    json_paths (JSON canonice cu același date prefix).
    """
    documente_dir = root / "Dosar_Medical" / "documente_sursa"
    if not documente_dir.exists():
        return []
    json_by_date = {}
    for jf in json_files:
        m = re.match(r"(\d{4}-\d{2}-\d{2})", Path(jf).stem)
        if m:
            json_by_date.setdefault(m.group(1), []).append(jf)
    docs = []
    for md_file in documente_dir.rglob("*_extragere.md"):
        try:
            text = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        try:
            stat = md_file.stat()
        except OSError:
            continue
        slug = md_file.stem.replace("_extragere", "")
        rel_path = relpath_str(md_file)
        # categorie din parent folder
        parent_folder = md_file.parent.name
        categorie_id = parent_folder if re.match(r"\d{2}_", parent_folder) else "altele"
        categorie_label = CATEGORIE_LABELS.get(categorie_id, categorie_id)
        # data din filename prefix
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})", slug)
        data = date_match.group(1) if date_match else None
        # JSON canonice asociate (același date prefix)
        json_paths = json_by_date.get(data, []) if data else []
        # titlu + preview
        titlu = extract_titlu_from_md(text, slug)
        preview = strip_md_to_preview(text, max_chars=220)
        docs.append({
            "id": slug,
            "titlu": titlu,
            "data": data,
            "categorie_id": categorie_id,
            "categorie_label": categorie_label,
            "md_path": rel_path,
            "size_kb": round(stat.st_size / 1024, 1),
            "preview": preview,
            "json_paths": json_paths,
        })
    # Sortare cronologică descrescătoare (cel mai recent primul)
    docs.sort(key=lambda d: (d.get("data") or "0000"), reverse=True)
    return docs


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
            for match in re.finditer(r"```yaml\s*\n(.*?)```", text, re.DOTALL):
                medic = parse_yaml_block(match.group(1))
                if isinstance(medic, dict) and isinstance(medic.get("id"), str) and medic["id"].startswith("dr-"):
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

    # 6. Documente pentru DASHBOARD — metadata MD extrageri pentru tab Dosar medical
    json_paths_canonice = [d.get("file") for d in documente_canonice if d.get("file")]
    documente_pentru_dashboard = extract_documente_pentru_dashboard(ROOT, json_paths_canonice)

    # Stats
    stats = {
        "total_files_indexed": len(files_by_path),
        "medici_oncohelp": len(medici_oncohelp),
        "threaduri_gmail": len(corespondenta),
        "documente_canonice": len(documente_canonice),
        "documente_pentru_dashboard": len(documente_pentru_dashboard),
        "atasamente_listate": 0,  # TODO Task viitor — extras din corespondenta + atașamente
    }

    output = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "version": "1.1",
        "stats": stats,
        "medici_oncohelp": medici_oncohelp,
        "corespondenta": corespondenta,
        "documente_canonice": documente_canonice,
        "documente_pentru_dashboard": documente_pentru_dashboard,
        "cross_references": cross_references,
        "files_by_path": files_by_path,
    }

    OUTPUT.write_text(
        json.dumps(output, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    print(f"INDEX.json generated: {OUTPUT}")
    print(f"  Stats: {stats}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
