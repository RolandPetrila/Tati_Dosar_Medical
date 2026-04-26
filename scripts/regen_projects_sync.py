#!/usr/bin/env python3
"""R30 — Regen Projects Sync folder.

Regenerează `_projects_sync/` pentru upload în Claude Projects (chat web/mobile).
Sursa de adevăr rămâne în folderele originale; acest script doar mirror-ează
+ generează STATUS_SNAPSHOT.md (sumar agregat one-page).

Utilizare:
    python scripts/regen_projects_sync.py

Recomandare: rulare după modificări medicale majore (ingest mail, update CONTEXT_MEDICAL,
update TODO). Opțional: integrare în git post-commit hook pentru auto-regen.
"""

import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Forțează UTF-8 pe Windows (pentru emojis 🟢/✅/📁)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
SYNC_DIR = ROOT / "_projects_sync"

# Fișiere de mirror-uit: (sursa absolută, target name în SYNC_DIR)
FILES_TO_COPY = [
    (ROOT / "CONTEXT_MEDICAL.md", "CONTEXT_MEDICAL.md"),
    (ROOT / "TODO.md", "TODO.md"),
    (ROOT / "REGULAMENT.md", "REGULAMENT.md"),
    (ROOT / "INDEX.json", "INDEX.json"),
    (ROOT / "Dosar_Medical" / "CONTACTE_MEDICALE.md", "CONTACTE_MEDICALE.md"),
    (
        ROOT / "Documente_Informative" / "EXPLICATIE_CONSULT_ONCOLOG_SCENARII.md",
        "EXPLICATIE_CONSULT_ONCOLOG_SCENARII.md",
    ),
]


def get_git_info():
    """Returns (hash_short, iso_date, message) of HEAD commit."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%h|%ci|%s"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
            encoding="utf-8",
        )
        parts = result.stdout.strip().split("|", 2)
        if len(parts) == 3:
            return parts[0], parts[1], parts[2]
        return "?", "?", "(parse error)"
    except Exception as e:
        return "?", "?", f"(git unavailable: {e})"


def extract_between(text, start_pattern, end_pattern):
    """Extract substring from start_pattern (inclusive) up to end_pattern (exclusive).
    Returns None if start not found."""
    start_match = re.search(start_pattern, text, re.MULTILINE)
    if not start_match:
        return None
    rest = text[start_match.end():]
    end_match = re.search(end_pattern, rest, re.MULTILINE)
    end_offset = end_match.start() if end_match else len(rest)
    return (text[start_match.start():start_match.end()] + rest[:end_offset]).strip()


def strip_first_header(text):
    """Drop primul rând dacă e header markdown (## sau ###) — evită dublura
    de header când STATUS_SNAPSHOT.md adaugă propriul header de secțiune."""
    if not text:
        return text
    parts = text.split("\n", 1)
    if parts and re.match(r"^#{2,4}\s", parts[0]):
        return parts[1].lstrip("\n") if len(parts) > 1 else ""
    return text


def extract_p0_active(todo_text):
    """Extract P0 sections without ✅ in title (active actions)."""
    # Match each ### [P0] block until next ### or ## or ---
    blocks = re.findall(
        r"^### \[P0\][^\n]*\n.*?(?=^### |^## |^---)",
        todo_text,
        re.DOTALL | re.MULTILINE,
    )
    active = [b.strip() for b in blocks if "✅" not in b.split("\n", 1)[0]]
    return active


def generate_status_snapshot():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    git_hash, git_date, git_msg = get_git_info()

    context_text = (ROOT / "CONTEXT_MEDICAL.md").read_text(encoding="utf-8")
    todo_text = (ROOT / "TODO.md").read_text(encoding="utf-8")

    # §1 Date pacient
    date_pacient = strip_first_header(extract_between(
        context_text, r"^## 1\. Date pacient", r"^## 2\."
    ))
    # §2.1 Findings principale (TNM)
    status_clinic = strip_first_header(extract_between(
        context_text, r"^### 2\.1 ", r"^### 2\.2"
    ))
    # §4 Medicație
    medicatie = strip_first_header(extract_between(
        context_text, r"^## 4\. ", r"^## 5"
    ))
    # Calendar TODO
    calendar = strip_first_header(extract_between(
        todo_text, r"^## Calendar", r"^---"
    ))
    # P0 active
    p0_active = extract_p0_active(todo_text)

    p0_block = (
        "\n\n".join(p0_active)
        if p0_active
        else "_(niciuna activă — vezi TODO.md)_"
    )

    snapshot = f"""# STATUS SNAPSHOT — Petrilă Viorel-Mihai

**Generat automat:** {now}
**Ultim commit git:** `{git_hash}` ({git_date})
**Mesaj commit:** {git_msg}
**Sursă de adevăr:** fișierele originale din proiect `.Tati`. Acest snapshot e mirror sintetic generat de `scripts/regen_projects_sync.py` pentru chat Claude Projects (web/mobil).

> **Ordine consultare în chat:** STATUS_SNAPSHOT.md (aici) → CONTEXT_MEDICAL.md (detaliu clinic) → TODO.md (calendar) → CONTACTE_MEDICALE.md (medici) → REGULAMENT.md (reguli) → INDEX.json (index documente) → EXPLICATIE_CONSULT_ONCOLOG_SCENARII.md (glosar + scenarii prognostice).

---

## 🧑 Date pacient

{date_pacient or '_(secțiune nedetectată — vezi CONTEXT_MEDICAL.md §1)_'}

---

## 🏥 Status clinic curent (sumar TNM)

{status_clinic or '_(secțiune nedetectată — vezi CONTEXT_MEDICAL.md §2.1)_'}

> **Detalii complete:** CONTEXT_MEDICAL.md §2 (findings principale + secundare + colaterale + parametri tehnici CT).

---

## 💊 Medicație activă

{medicatie or '_(secțiune nedetectată — vezi CONTEXT_MEDICAL.md §4)_'}

---

## 📅 Calendar — date cheie

{calendar or '_(secțiune nedetectată — vezi TODO.md)_'}

---

## 🔴 Acțiuni P0 active

{p0_block}

---

## 📚 Cum răspunzi (instrucțiuni Claude Projects)

- **Limba:** română strict (excepție: termeni medicali tehnici fără echivalent comun)
- **Marcaje certitudine OBLIGATORII** pe afirmații medicale (R17 — REGULAMENT.md):
  - `[CERT]` — confirmat din sursă primară (JSON canonic, RCP/SmPC, ghid ESMO/NCCN, studiu peer-reviewed)
  - `[PROBABIL]` — susținut de literatura medicală standard
  - `[INCERT]` — conflict surse / extrapolare / lacună
  - `[NEGASIT]` — căutat și neidentificat
- **NU PRESUPUNE** — la neclaritate întreabă explicit (R7); niciodată nu inventa cifre, doze, nume medic, date
- **La conflict între acest snapshot și fișierele originale** → CONTEXT_MEDICAL.md / TODO.md prevalează (autoritate)
- **Detalii operaționale extinse:** PROJECTS_PRIMER.md

---

_Pentru actualizare: editezi fișiere originale pe laptop → rulezi `python scripts/regen_projects_sync.py` → push git → Google Drive sync → Drive Connector re-index Projects ([PROBABIL] 5-30 min)._
"""
    return snapshot


def main():
    if not SYNC_DIR.exists():
        SYNC_DIR.mkdir(parents=True)
        print(f"📁 Creat folder: {SYNC_DIR.relative_to(ROOT)}")

    print(f"\n🔄 Sync sursă → {SYNC_DIR.name}/\n")

    # 1. Copiază fișierele originale (mirror)
    copied = 0
    missing = 0
    for src, target_name in FILES_TO_COPY:
        if not src.exists():
            print(f"  ⚠️  LIPSĂ: {src.relative_to(ROOT)} — skip")
            missing += 1
            continue
        target = SYNC_DIR / target_name
        shutil.copy2(src, target)
        size_kb = target.stat().st_size / 1024
        print(f"  ✅ Copiat: {target_name} ({size_kb:.1f} KB)")
        copied += 1

    # 2. Generează STATUS_SNAPSHOT.md
    snapshot = generate_status_snapshot()
    snapshot_path = SYNC_DIR / "STATUS_SNAPSHOT.md"
    snapshot_path.write_text(snapshot, encoding="utf-8")
    size_kb = snapshot_path.stat().st_size / 1024
    print(f"  ✅ Generat: STATUS_SNAPSHOT.md ({size_kb:.1f} KB)")

    # 3. Verificare PROJECTS_PRIMER.md (manual; NU regenerat de script)
    primer = SYNC_DIR / "PROJECTS_PRIMER.md"
    if not primer.exists():
        print("  ⚠️  LIPSĂ: PROJECTS_PRIMER.md (de creat manual)")
    else:
        size_kb = primer.stat().st_size / 1024
        print(f"  ✅ Prezent: PROJECTS_PRIMER.md ({size_kb:.1f} KB) [neatins]")

    # 4. Sumar
    total_kb = sum(f.stat().st_size for f in SYNC_DIR.glob("*")) / 1024
    print(f"\n📊 Total {SYNC_DIR.name}/: {total_kb:.1f} KB")
    print(f"   Mirror-uite: {copied} | Lipsă: {missing} | Generat: 1 (STATUS_SNAPSHOT)")
    print(
        "\n✅ Sync complet. Următor pas: commit + push → Drive Connector re-index automat în Projects."
    )


if __name__ == "__main__":
    main()
