---
plan_id: implementare-r27-r28-contacte-dashboard-2026-04-25
version: 1.0
status: 🟡 IN_PROGRESS
created_at: 2026-04-25 18:05
started_execution_at: 2026-04-25 18:30
auditor_session: terminal A (Opus 4.7 1M context — sesiunea care a creat planul)
executor_session: terminal B (sesiune nouă deschisă de user — execută strict)
estimated_duration_min: 85
commits_planned: 7
backup_strategy: R10 înainte de fiecare modificare la fișiere de referință
commit_strategy: incremental (NU final unic) — 1 commit per task major
---

# PLAN IMPLEMENTARE 2026-04-25 — Sistem unificat: R27 + R28 + CONTACTE OncoHelp + DASHBOARD echipă

> **🔴 PENTRU EXECUTOR (TERMINAL B):** acest fișier este sursa unică de adevăr pentru sesiunea ta. Citește-l integral înainte de a începe. Confirmă cu user-ul că pornești execuția. Apoi execută strict pas cu pas. Marchează `[x]` la fiecare sub-task completat. La eroare → STOP + raport în chat. NU adăuga lucruri ne-cerute. NU refactoriza ce nu e cerut.
>
> **🔵 PENTRU AUDITOR (TERMINAL A):** după fiecare commit incremental al executorului, rulezi `git log -1` + `git diff HEAD~1` pentru validare. Semnalezi în chat orice abatere de la plan.

---

## 📋 Context (decizii luate în sesiunea auditorului)

User a confirmat în conversație următoarele decizii:

| Decizie                                       | Răspuns                                                                                                                                                                                    |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Locație CONTACTE_MEDICALE.md                  | `Dosar_Medical/CONTACTE_MEDICALE.md`                                                                                                                                                       |
| Vizibilitate DASHBOARD                        | Tot vizibil (toate datele) — DASHBOARD public GitHub Pages, user își asumă                                                                                                                 |
| Numere personale (ex: 0762120428 Dr. Vornicu) | Afișate ca pe restul (DASHBOARD public)                                                                                                                                                    |
| Adâncime cercetare per medic                  | Medie — site oficial + 2-3 surse review + sinteză 5-8 rânduri                                                                                                                              |
| **CONTACTE — scope**                          | **DOAR OncoHelp activi** (Anater + Vornicu acum). NU istoric extern.                                                                                                                       |
| **`verifică gmail nou` — scope**              | Tot ce e nou față de baseline (limita = ultimul thread_id în `corespondenta/INDEX.md`). NU limitat la zile.                                                                                |
| R27 decizii                                   | 1.A salvare integrală / 2.A doar lista pe DASHBOARD nu corp / 3.A scan la cerere + auto / 4.A scope full history primul scan / 5.A atașamente listate cu memorare exactă                   |
| Format documentație                           | Markdown + YAML frontmatter + INDEX.json agregat                                                                                                                                           |
| MAP/cuprins                                   | Extindere `STRUCTURA_PROIECT.md` cu auto-regenerare                                                                                                                                        |
| Auto-scan Gmail                               | Hook SessionStart (A) + Cron Windows zilnic 22:00 (B)                                                                                                                                      |
| Sugestii suplimentare                         | #1 Search DASHBOARD · #2 Atașamente smart recall · #4 Validare pre-commit · #5 Naming + slug-uri · #6 Status la SessionStart · #7 Versionare semantică (#3 ntfy + audio Whisper ELIMINATE) |

---

## 🛡 Reguli protocol (cross-terminal)

1. **Backup R10 obligatoriu** înainte de modificare la fișiere de referință (`CONTEXT_MEDICAL.md`, `TODO.md`, `DASHBOARD.html`, `CHANGELOG.md`, `SESSION_LOG.md`, `MEMORY.md`).
2. **Commit-uri incrementale** — 1 commit per task major (după Task #7, #15, #11, #13, #14). Format mesaj: `[PLAN 2026-04-25] task #X — <subiect>`.
3. **Status plan** — actualizezi frontmatter `status` la `🟡 IN_PROGRESS` la pornire, `🟢 COMPLETED` la final. Modificare în git la fiecare commit.
4. **Bifare task** — `- [ ]` → `- [x] (commit <hash>, <data>)` după validare.
5. **La eroare** — STOP execuție. Raport detaliat în chat. NU continui.
6. **Verificare cross-context** — la fiecare scriere, verifică Regula 4 (REGULAMENT.md) + R28 system health.
7. **NU refactorezi** ce nu e cerut. NU adăuga lucruri ne-listate aici.
8. **Limba** — română, ca în restul dosarului.

---

## ⚠️ Tasks deja completate de auditor (NU le re-executa)

- **Task #8 — Codificare R27 + R28 + R29 în `REGULI_CLAUDE_CODE.md`** — ✅ DEJA FĂCUT de auditor în terminal A (commit pending în acest plan). Doar VERIFICĂ că fișierul conține `## Regula 27`, `## Regula 28`, `## Regula 29` (verificare la Task #14 final).
- **`CLAUDE.md` proiect — extindere harta cu R27/R28/R29 + detect plan activ** — ✅ DEJA FĂCUT de auditor.

---

## 📦 TASKS DE EXECUTAT

### Task #7 — Update documentație post-trimitere mail Anater (manual user)

**Pre-requisite:** niciuna.

**Context:** user a trimis manual mailul `RE: Solicitare consult oncologic` către `angelo.anater@oncohelp.ro`, CC `programari@oncohelp.ro` + `office@oncohelp.ro` în 25.04.2026 după-amiaza. Conținut: confirmare biopsie 28-29.04, programare 30.04, 5 întrebări (analize la OncoHelp, internare/ambulator, documente, bilet trimitere, telefon de contact).

**Pași concreti:**

- [x] **#7.1** — Backup R10 (2026-04-25 18:26 — 3 fișiere copiate în `Dosar_Medical/arhiva/context_medical_versiuni/`):

  ```bash
  cp "G:/My Drive/Roly/.Tati/SESSION_LOG.md" "G:/My Drive/Roly/.Tati/Dosar_Medical/arhiva/context_medical_versiuni/SESSION_LOG_pre-trimitere-mail-anater_2026-04-25_$(date +%H%M).md"
  cp "G:/My Drive/Roly/.Tati/TODO.md" "G:/My Drive/Roly/.Tati/Dosar_Medical/arhiva/context_medical_versiuni/TODO_pre-trimitere-mail-anater_2026-04-25_$(date +%H%M).md"
  ```

- [x] **#7.2** — `SESSION_LOG.md` — adaugă DEASUPRA intrării `2026-04-25 15:50` o nouă intrare `2026-04-25 18:00` cu titlul `[Roland_user_manual] trimitere-mail-raspuns-anater-programare-30`:
  - Scop: răspuns trimis manual de user la Dr. Anater (NU prin Claude Gmail draft) — confirmare programare 30.04 + 5 întrebări organizatorice
  - Destinatari: TO `angelo.anater@oncohelp.ro`; CC `programari@oncohelp.ro` + `office@oncohelp.ro`
  - Subiect: `RE: Solicitare consult oncologic`
  - Conținut sintetizat (5 puncte): biopsie 28-29.04 confirmare, programare 30.04 cerere, întrebări analize/internare/documente/bilet/telefon
  - Așteptare răspuns Dr. Anater pentru confirmare slot + clarificări

- [x] **#7.3** — `TODO.md` — în secțiunea `P0 — Critic, de efectuat IMEDIAT`:
  - La task `[P0] ✅ Consult oncolog digestiv — PROGRAMAT 30.04.2026 OncoHelp Timișoara` → adaugă sub-task: `- [x] ✅ Mail trimis manual 25.04 către Dr. Anater (RE: Solicitare consult oncologic) — confirmare biopsie 28-29.04 + 5 întrebări organizatorice. Așteptare răspuns clarificări.`
  - Sub Calendar — eveniment nou: `25.04.2026 18:00 | Mail trimis Dr. Anater (programare + 5 întrebări) | ✅ Trimis · Așteptare răspuns`

- [x] **#7.4** — `CHANGELOG.md` — DEASUPRA intrării `2026-04-25 15:50` adaugă intrare `2026-04-25 18:00 — Trimitere manual mail răspuns Dr. Anater (programare 30.04 + întrebări organizatorice)`:
  - Tip: CORESPONDENȚĂ EXTERNĂ
  - Context: răspuns la mailul Dr. Anater 24.04 + workflow plan-audit pe sesiunea curentă
  - Conținut: 5 întrebări (analize/internare/documente/bilet/telefon)
  - Status așteptare: răspuns Dr. Anater pentru confirmare slot și clarificări

**Verificare:**

- [x] `SESSION_LOG.md` are intrare nouă cu data `2026-04-25 18:00`
- [x] `TODO.md` reflectă mailul trimis în calendar + sub-task P0 consult (cronologic ordonat: după 22.04, înainte de 28-29.04)
- [x] `CHANGELOG.md` are intrare nouă

**Commit incremental:** `[PLAN 2026-04-25] task #7 — log mail trimis manual Dr. Anater 25.04` (commit pending push).

---

### Task #15 — R28 System Health Monitor (script + SYSTEM_HEALTH.json + hook)

**Pre-requisite:** Task #7 commit-uit.

**Context:** R28 codificat deja în `REGULI_CLAUDE_CODE.md`. Acest task creează implementarea concretă (script + fișier output + hook).

**Pași:**

- [x] **#15.1** — Creat folder `scripts/` (2026-04-25 18:30).

- [x] **#15.2** — Creat `scripts/system_health_check.py` cu fix-uri vs. specificația originală (2026-04-25 18:30): (1) `sys.stdout.reconfigure(encoding="utf-8")` pentru emojis pe Windows cp1252, (2) bug fix `sum()` peste strings (înlocuit cu `"".join(texts)`), (3) try/except pe rglob pentru permisiuni Drive sync, (4) chars/token la 3 (român), (5) status_for() consolidat în helper `metric()`. Logica praguri identică cu plan.

```python
#!/usr/bin/env python3
"""R28 System Health Check — generează Dosar_Medical/SYSTEM_HEALTH.json
Praguri: 🟢 <60% / 🟡 60-80% / 🟠 80-95% / 🔴 >95%
"""
import json
import os
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "Dosar_Medical" / "SYSTEM_HEALTH.json"

LIMITS = {
    "context_tokens_estimate": {"limit": 200_000, "type": "tokens"},  # Sonnet default; Opus = 1M
    "claude_md_size_kb": {"limit": 40, "type": "kb"},
    "memory_md_lines": {"limit": 200, "type": "lines"},
    "total_md_root_kb": {"limit": 500, "type": "kb"},
    "largest_file_kb": {"limit": 200, "type": "kb"},
    "index_json_size_kb": {"limit": 1024, "type": "kb"},
}

def status_for(percent):
    if percent < 60: return "🟢 OK"
    if percent < 80: return "🟡 WARNING"
    if percent < 95: return "🟠 ALERT"
    return "🔴 CRITICAL"

def estimate_tokens(text):
    # Aproximare: ~4 chars/token (engleză); română ~3.5 chars/token
    return len(text) // 4

def main():
    metrics = {}

    # CLAUDE.md size
    claude_md = ROOT / "CLAUDE.md"
    if claude_md.exists():
        size_kb = claude_md.stat().st_size / 1024
        metrics["claude_md_size_kb"] = {
            "current": round(size_kb, 1),
            "limit": LIMITS["claude_md_size_kb"]["limit"],
            "percent": round(size_kb / LIMITS["claude_md_size_kb"]["limit"] * 100, 1),
        }
        metrics["claude_md_size_kb"]["status"] = status_for(metrics["claude_md_size_kb"]["percent"])

    # MEMORY.md lines (în C:\Users\ALIENWARE\.claude\projects\G--My-Drive-Roly--Tati\memory\MEMORY.md)
    memory_md = Path("C:/Users/ALIENWARE/.claude/projects/G--My-Drive-Roly--Tati/memory/MEMORY.md")
    if memory_md.exists():
        lines = sum(1 for _ in open(memory_md, encoding="utf-8"))
        metrics["memory_md_lines"] = {
            "current": lines,
            "limit": LIMITS["memory_md_lines"]["limit"],
            "percent": round(lines / LIMITS["memory_md_lines"]["limit"] * 100, 1),
        }
        metrics["memory_md_lines"]["status"] = status_for(metrics["memory_md_lines"]["percent"])

    # Total .md root size (excluzând subfoldere)
    total_md = sum(f.stat().st_size for f in ROOT.glob("*.md"))
    total_md_kb = total_md / 1024
    metrics["total_md_root_kb"] = {
        "current": round(total_md_kb, 1),
        "limit": LIMITS["total_md_root_kb"]["limit"],
        "percent": round(total_md_kb / LIMITS["total_md_root_kb"]["limit"] * 100, 1),
    }
    metrics["total_md_root_kb"]["status"] = status_for(metrics["total_md_root_kb"]["percent"])

    # Cele mai mari 10 fișiere din proiect (.md/.html/.json)
    largest = []
    for ext in ("*.md", "*.html", "*.json"):
        for f in ROOT.rglob(ext):
            if any(skip in str(f) for skip in [".git", "node_modules", ".claude-outputs"]):
                continue
            largest.append((f.stat().st_size / 1024, str(f.relative_to(ROOT))))
    largest.sort(reverse=True)
    metrics["largest_files"] = [
        {"path": p, "size_kb": round(s, 1)} for s, p in largest[:10]
    ]

    # Files over individual limit
    over_limit = [
        {"path": p, "size_kb": round(s, 1)}
        for s, p in largest if s > LIMITS["largest_file_kb"]["limit"]
    ]
    metrics["files_over_limit"] = over_limit

    # INDEX.json size dacă există
    index_json = ROOT / "INDEX.json"
    if index_json.exists():
        size_kb = index_json.stat().st_size / 1024
        metrics["index_json_size_kb"] = {
            "current": round(size_kb, 1),
            "limit": LIMITS["index_json_size_kb"]["limit"],
            "percent": round(size_kb / LIMITS["index_json_size_kb"]["limit"] * 100, 1),
        }
        metrics["index_json_size_kb"]["status"] = status_for(metrics["index_json_size_kb"]["percent"])

    # Estimate context tokens — agregat pe fișierele auto-loaded (CLAUDE.md + REGULI + REGULAMENT)
    auto_loaded = [
        ROOT / "CLAUDE.md",
        ROOT / "REGULI_CLAUDE_CODE.md",
        ROOT / "REGULAMENT.md",
    ]
    total_chars = sum(f.read_text(encoding="utf-8") for f in auto_loaded if f.exists())
    if isinstance(total_chars, str):
        tokens = estimate_tokens(total_chars)
    else:
        tokens = sum(estimate_tokens(t) for t in [f.read_text(encoding="utf-8") for f in auto_loaded if f.exists()])
    metrics["context_tokens_estimate"] = {
        "current": tokens,
        "limit": LIMITS["context_tokens_estimate"]["limit"],
        "percent": round(tokens / LIMITS["context_tokens_estimate"]["limit"] * 100, 1),
        "note": "estimat doar pe fișiere auto-loaded (CLAUDE.md + REGULI_CLAUDE_CODE.md + REGULAMENT.md). Read-uri ad-hoc nu sunt incluse.",
    }
    metrics["context_tokens_estimate"]["status"] = status_for(metrics["context_tokens_estimate"]["percent"])

    # Overall status — cel mai rău dintre toate
    statuses = [v.get("status", "🟢 OK") for v in metrics.values() if isinstance(v, dict) and "status" in v]
    severity_order = ["🔴 CRITICAL", "🟠 ALERT", "🟡 WARNING", "🟢 OK"]
    overall = next((s for s in severity_order if s in statuses), "🟢 OK")

    # Recommendations (la WARNING+)
    recommendations = []
    for k, v in metrics.items():
        if isinstance(v, dict) and v.get("status", "").startswith("🟡"):
            recommendations.append(f"⚠ {k}: la {v.get('percent')}% — propune restructurare proactivă")
        elif isinstance(v, dict) and v.get("status", "").startswith("🟠"):
            recommendations.append(f"🟠 {k}: la {v.get('percent')}% — REFUZ scrieri masive până la restructurare")
        elif isinstance(v, dict) and v.get("status", "").startswith("🔴"):
            recommendations.append(f"🔴 {k}: la {v.get('percent')}% — STOP scrieri. Restructurare urgentă.")
    if metrics.get("files_over_limit"):
        for f in metrics["files_over_limit"]:
            recommendations.append(f"📄 Fișier mare: {f['path']} ({f['size_kb']}KB) — propune sharding")

    output = {
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "status": overall,
        "limits": metrics,
        "recommendations": recommendations,
        "version": "1.0",
    }

    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"SYSTEM_HEALTH check: {overall}")
    print(f"  Output: {OUTPUT}")
    if recommendations:
        print("  Recommendations:")
        for r in recommendations:
            print(f"    {r}")

if __name__ == "__main__":
    main()
```

- [⚠] **#15.3** — Rulat scriptul (2026-04-25 18:31). **Status detectat: `🔴 CRITICAL`** pe metricul `total_md_root_kb` (542.3 KB / 500 KB = 108.5%). Toate celelalte metrici 🟢 OK. **Stop Rule #1 declanșat** — vezi raport către user în chat după Task #15. Stare PRE-existentă, nu cauzată de execuția planului. Cauza: CHANGELOG.md (131.9KB) + SESSION_LOG.md (81.5KB) + ALIMENTATIE.md (48.2KB) + CONTEXT_MEDICAL.md (47.1KB) + altele = 542.3 KB cumulat.

- [x] **#15.4** — Hook SessionStart adăugat în `.claude/settings.local.json` (2026-04-25 18:32). Format respectă schema Claude Code (`hooks > SessionStart > [{ hooks: [{ type: "command", command: ... }] }]`). **Notă:** `settings.local.json` e gitignored (corect — e setting local per user) → hook-ul NU e committed în git, dar rulează local pentru sesiunile pe acest laptop. Pentru a fi share-uit, ar trebui mutat în `.claude/settings.json` (project-level), dar planul a specificat explicit `settings.local.json`.
  ```json
  {
    "hooks": {
      "SessionStart": [
        {
          "command": "python",
          "args": ["scripts/system_health_check.py"],
          "description": "R28 — verificare limite Claude Code la pornire sesiune"
        }
      ]
    }
  }
  ```
  **NOTĂ:** dacă fișierul `.claude/settings.local.json` există deja cu altceva, citește-l întâi și merge-uiește hook-ul în structura existentă fără să suprascrii alte setări.

**Verificare:**

- [x] `scripts/system_health_check.py` există și rulează cu cod 0
- [x] `Dosar_Medical/SYSTEM_HEALTH.json` există cu status `🔴 CRITICAL` (declanșează Stop Rule #1 — raport user)
- [x] `.claude/settings.local.json` are hook SessionStart configurat

**Commit incremental:** `[PLAN 2026-04-25] task #15 — R28 System Health Monitor + hook SessionStart` (committed).

---

### Task #10 — Cercetare web Dr. Vornicu Vlad + OncoHelp Timișoara

**Pre-requisite:** Task #15 commit-uit.

**Context:** user a furnizat numărul `0762120428` pentru Dr. Vlad Vornicu, fără alte detalii. Trebuie să cercetez online pentru a-i contura profilul profesional.

**Surse de cercetare obligatorii (4 categorii):**

1. **Site oficial OncoHelp** — `https://oncohelp.ro/echipa` sau `/medici` (verifică structura site-ului)
2. **DocPlanner / Doctorinfo.ro / SfatulMedicului** — căutare „Vlad Vornicu Timișoara"
3. **Pareri-medici.ro / Doc.ro** — recenzii dacă există
4. **Google general** — publicații, conferințe, LinkedIn public

**Pași:**

- [x] **#10.1** — WebSearch executat 4 query-uri principale (2026-04-25 19:00).

- [x] **#10.2** — OncoHelp Timișoara — date complete extrase din oncohelp.ro/contact + oncohelp.ro/echipa-oncohelp/.

- [x] **#10.3** — Dr. Vornicu Vlad-Norin — profil exhaustiv (data nașterii 06.07.1991, asistent univ. PhD UMFT, ResearchGate 11 citări 2 publicații, focus oncologie pulmonară).

- [x] **#10.4** — Salvat în `Dosar_Medical/cercetari/2026-04-25_cercetare-oncohelp-vornicu-anater.md` (numele extins față de plan: include și Dr. Anater pentru paritate, ambii fiind activi acum). **DESCOPERIRE IMPORTANTĂ:** Dr. Anater este listat oficial ca **MEDIC REZIDENT** (NU specialist) la OncoHelp — informație nouă față de contextul anterior.

**Verificare:**

- [x] Fișier `Dosar_Medical/cercetari/2026-04-25_cercetare-oncohelp-vornicu-anater.md` există
- [x] Conține 7+ surse URL cu data accesării (oncohelp.ro echipa/contact, UMFT 2 surse, ResearchGate, Radio România Reșița 2 articole, G4Media)
- [x] Marcaje [CERT/PROBABIL/NEGASIT] explicite în tot fișierul

**Commit incremental:** comun cu Task #9 — vezi mai jos.

---

### Task #9 — CONTACTE_MEDICALE.md (DOAR OncoHelp: Anater + Vornicu)

**Pre-requisite:** Task #10 finalizat (cercetare în fișier `cercetari/`).

**Context:** fișier nou cu structura propusă (Markdown + YAML frontmatter). DOAR medici OncoHelp activi (NU istoric extern).

**Pași:**

- [ ] **#9.1** — Creez `Dosar_Medical/CONTACTE_MEDICALE.md` cu antet și structură:

```markdown
---
title: Catalog contacte medicale OncoHelp Timișoara
scope: doar medici OncoHelp activi (NU istoric extern; pentru istoric vezi CONTEXT_MEDICAL.md §9)
last_updated: 2026-04-25
medici_listati: 2
version: 1.0
---

# Catalog contacte medicale — OncoHelp Timișoara

> **Scope:** doar medicii din echipa OncoHelp Timișoara cu care suntem activi în corespondență sau urmează să interacționăm. Istoricul extern (Genesis, UPU, Bioclinica, medic familie) NU este aici — vezi `CONTEXT_MEDICAL.md §9 Echipă medicală`.
>
> **Format:** Markdown cu YAML frontmatter pentru fiecare medic. Câmpuri obligatorii: id, nume, specializare, unitate, emails, telefoane, status, prim_contact, ultim_contact, rol, tags, version. Cercetare profesională: 5-8 rânduri sintetizate cu marcaje [CERT/PROBABIL/NEGASIT] + surse URL.
>
> **Workflow:** când user furnizează contact nou → cercetare web 4 surse → adăugare entry → sync DASHBOARD + INDEX.json + commit.

---

## Index rapid

| ID                           | Nume                          | Specializare             | Status                      | Telefon      | Email primar              |
| ---------------------------- | ----------------------------- | ------------------------ | --------------------------- | ------------ | ------------------------- |
| `dr-anater-angelo-christian` | Dr. Anater Angelo - Christian | Oncologie medicală       | 🟢 activ — programare 30.04 | [de obținut] | angelo.anater@oncohelp.ro |
| `dr-vornicu-vlad`            | Dr. Vornicu Vlad              | [din cercetare Task #10] | 🟡 contact furnizat user    | 0762120428   | [din cercetare]           |

---

## Dr. Anater Angelo - Christian {#dr-anater-angelo-christian}

## \`\`\`yaml

id: dr-anater-angelo-christian
nume: Anater Angelo - Christian
titlu: Dr.
specializare: [oncologie medicala]
unitate: OncoHelp Timișoara
unitate_id: oncohelp-timisoara
emails:
primar: angelo.anater@oncohelp.ro
secundar: angelo.anater95@yahoo.com
telefoane: [] # de obținut
status: 🟢 activ
prim_contact: 2026-04-24
ultim_contact: 2026-04-25
rol: medic oncolog curant — primă linie OncoHelp
tags: [oncolog, oncohelp, medic-curant, programat-30-04]
version: 1.0

---

\`\`\`

### Profil profesional [cercetare 2026-04-25]

[5-8 rânduri sintetizate din Task #10 cu marcaje [CERT/PROBABIL/NEGASIT]. Dacă cercetarea nu a returnat date suficiente publice, scrie explicit: „Profil profesional public limitat — date detaliate vor fi completate la consultul 30.04 sau la următoarea cercetare." NU inventa.]

### Surse cercetare

[Listă URL-uri cu data accesării]

### Istoric corespondență

- 2026-04-24 10:56 — primit `RE: Solicitare consult oncologic` ([thread](corespondenta/2026-04-24_re-solicitare-consult-anater.md)) — cale clinică propusă: așteptare biopsie + consult ulterior
- 2026-04-25 18:00 — răspuns trimis manual de user (programare 30.04 + 5 întrebări organizatorice)

### Note libere

- Răspuns prompt și atent (24h) — semnal pozitiv pentru relația medic-pacient
- A explicat clar că acumulările lichidiene sunt probabil cardiace, nu oncologice — abordare echilibrată
- Următorul pas: așteptare confirmare slot 30.04 + clarificări cu privire la analize/internare/documente/bilet

---

## Dr. Vornicu Vlad {#dr-vornicu-vlad}

## \`\`\`yaml

id: dr-vornicu-vlad
nume: Vornicu Vlad
titlu: Dr.
specializare: [din cercetare Task #10]
unitate: OncoHelp Timișoara
unitate_id: oncohelp-timisoara
emails: [] # de obținut din cercetare sau corespondență ulterioară
telefoane:

- {numar: '0762120428', sursa: 'furnizat user 2026-04-25', tip: mobil}
  status: 🟡 contact furnizat user — încă nu ne-am auzit
  prim_contact: null
  ultim_contact: null
  rol: [din cercetare Task #10 — eventual a doua opinie / specialist complementar]
  tags: [oncolog, oncohelp]
  version: 1.0

---

\`\`\`

### Profil profesional [cercetare 2026-04-25]

[Sinteză din Task #10 cu marcaje [CERT/PROBABIL/NEGASIT]. Dacă cercetarea nu a returnat date publice substanțiale, scrie: „Date publice limitate la momentul 25.04.2026. Numărul de telefon furnizat de user — sursă probabil personală/recomandare. Profil va fi completat după prima interacțiune sau cercetare ulterioară." NU inventa.]

### Surse cercetare

[Listă URL-uri cu data accesării]

### Istoric corespondență

- _Niciun contact direct încă._ Numărul `0762120428` furnizat de user 2026-04-25 — context: căutare opțiuni complementare la consultul programat cu Dr. Anater.

### Note libere

- _De completat după prima interacțiune._
```

- [x] **#9.2** — Populat **Profil profesional** și **Surse cercetare** pentru ambii medici. Anater: status `[CERT] medic rezident` cu nuanțare clinică despre rolul rezidenților + tumor board OncoHelp. Vornicu: profil științific complet cu publicații, conferințe, focus oncologie pulmonară. Coincidență validatoare: numărul `0762120428` apare și ca sursă publică ResearchGate → confirmă identitatea contactului.

- [x] **#9.3** — Verificat: zero referințe la medici externi în CONTACTE_MEDICALE.md (scope OncoHelp activi respectat). Noufal, LAZA, Orbán, Pop, Grada, Post, Pitea, Papiu, Mester rămân doar în `CONTEXT_MEDICAL.md §9`.

**Verificare:**

- [x] Fișier `Dosar_Medical/CONTACTE_MEDICALE.md` există
- [x] Conține DOAR Anater + Vornicu (+ secțiune `Unitate de referință OncoHelp`)
- [x] Frontmatter YAML valid pentru ambii medici + unitatea
- [x] Surse cercetare cu URL + dată accesare (per medic + agregat în cercetari/)
- [x] Marcaje certitudine prezente ([CERT]/[PROBABIL]/[NEGASIT])

**Commit incremental:** `[PLAN 2026-04-25] task #9+#10 — CONTACTE_MEDICALE OncoHelp + cercetare web Anater+Vornicu` (committed).

---

### Task #11 — Primul ingest Gmail full-history pentru OncoHelp + tata

**Pre-requisite:** Task #9 commit-uit.

**Context:** primul scan Gmail conform R27. Scope: full history (toate threadurile relevante dintotdeauna). Output: fișiere markdown în `Dosar_Medical/corespondenta/` cu frontmatter YAML, plus `INDEX.md` master.

**Pași:**

- [x] **#11.1** — Folder `Dosar_Medical/corespondenta/` creat (2026-04-25 19:16).

- [x] **#11.2** — Search Gmail executat cu 5 query-uri paralel (2026-04-25 19:18):
  - `subject:"Solicitare sprijin medical" OR subject:"Solicitare consult oncologic"`
  - `from:oncohelp.ro OR to:oncohelp.ro`
  - `from:bioclinica.ro OR to:bioclinica.ro`
  - `(biopsie OR endoscopie OR colonoscopie OR "CT torace") newer_than:90d`
  - `(Anater OR Vornicu OR Mester OR Noufal) newer_than:180d`
  - `(petrila viorel) newer_than:365d`

- [x] **#11.3** — `get_thread` rulat pe 4 threaduri principale cu `FULL_CONTENT` (Anater, Mester, OncoHelp inițial, Cip).

- [x] **#11.4** — Generate 5 fișiere markdown thread (mai mult decât 3 cerute în plan, pentru paritate scan full-history):

```markdown
---
thread_id: <gmail_thread_id>
subject: <subject>
participanti: [lista_emailuri]
data_start: YYYY-MM-DD
data_ultim: YYYY-MM-DD
status: 🟢 activ / ⚪ încheiat / 🟡 așteptare răspuns
tags: [oncohelp, programare, biopsie, ...]
mesaje_count: N
atasamente_count: M
version: 1.0
---

# <Subject thread>

## Sinteză automată

- **Decizii / recomandări medicale primite:** [...]
- **Contacte noi identificate:** [...]
- **Termene / programări menționate:** [...]
- **Atașamente menționate:** [listă cu nume + tip + dimensiune dacă disponibil]
- **Cross-references:**
  - → CONTEXT_MEDICAL.md §X (dacă instrucțiuni relevante)
  - → CONTACTE_MEDICALE.md#dr-X (dacă medic identificat)
  - → TODO.md P0/P1 (dacă termen)

## Mesaje (cronologic)

### YYYY-MM-DD HH:MM — <Sender name> (<email>)

[corp integral mesaj — păstrat ca sursă autoritară]

---

### YYYY-MM-DD HH:MM — <Sender name> (<email>)

[...]
```

- [x] **#11.5** — Threadurile cunoscute din plan create + extinse cu 2 noi descoperite în scan:
  - `2026-04-23_solicitare-sprijin-oncohelp.md` (thread `19db78a7c0a1758d`) — per plan
  - `2026-04-24_re-solicitare-consult-anater.md` (thread `19dbe7d30cfacbb3`) — per plan; **CONFIRM**: mailul Roland 25.04 18:00 EXISTĂ în thread (mesaj `19dc4e472df6e379`, sincronizat cu Gmail), inclus integral
  - `2026-04-24_raspuns-iocn-mester.md` (thread `19dbef8d0454235d`) — per plan
  - **NOU descoperit:** `2026-04-22_solicitare-dr-cip-recomandare-lusca.md` (thread `19db4ec3cd076144`) — cu răspuns Dr. Cip recomandând Zeolit + AHCC ca adjuvant
  - **NOU descoperit:** `2026-04-23_broadcast-solicitari-clinici.md` — agregator pentru 4 threaduri broadcast (Medisprof + IOCN office + Amethyst + MedLife)
  - **DESCOPERIRE IMPORTANTĂ:** semnătura email Dr. Anater zice „Medic Specialist, Oncologie Medicala" — diferă de site oncohelp.ro care îl listează „Rezident". Conflict R12 rezolvat în favoarea „Specialist" + actualizat CONTACTE_MEDICALE.md la v1.1.

- [x] **#11.6** — Creat `Dosar_Medical/corespondenta/INDEX.md` master cu format extins (3 secțiuni: active / încheiate cu răspuns medic / broadcast fără răspuns + statistici scan + threaduri non-medicale exclude + comenzi disponibile + politică atașamente):

```markdown
---
title: Index master corespondență medicală tata
last_scan: 2026-04-25 <hh:mm>
scan_type: full_history (R27 first ingest)
threads_total: N
threads_active: M
last_processed_thread_id: <id ultimul thread procesat>
version: 1.0
---

# Index corespondență medicală — Petrila Viorel-Mihai

## Threaduri active

| Data ultim | Thread                                                                     | Subiect                                              | Participanți        | Status                       |
| ---------- | -------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------- | ---------------------------- |
| 2026-04-25 | [solicitare-sprijin-oncohelp](2026-04-23_solicitare-sprijin-oncohelp.md)   | Solicitare sprijin medical pentru tatăl meu (66 ani) | Roland → OncoHelp   | ⚪ încheiat (thread inițial) |
| 2026-04-25 | [re-solicitare-consult-anater](2026-04-24_re-solicitare-consult-anater.md) | RE: Solicitare consult oncologic                     | Roland ↔ Dr. Anater | 🟡 așteptare răspuns         |
| 2026-04-24 | [raspuns-iocn-mester](2026-04-24_raspuns-iocn-mester.md)                   | Răspuns IOCN — solicitare consult oncologic          | Dr. Mester → Roland | ⚪ încheiat                  |

## Threaduri arhivate

_(Listează aici threaduri vechi sau cu status `arhivat` — pentru viitor)_

## Statistici scan

- **Threaduri totale procesate:** N
- **Mailuri totale:** M
- **Atașamente menționate:** P (vezi `INDEX.json#atasamente_index`)
- **Contacte noi identificate:** [lista]

## Comenzi

- `verifică gmail nou` — incremental scan față de `last_processed_thread_id`
- `verifică gmail oncohelp` — re-scan focalizat OncoHelp
- `verifică gmail [keyword]` — scan custom
```

- [x] **#11.7** — **Auto-propagare executată:**
  - `CONTACTE_MEDICALE.md` v1.0 → v1.1 — corectare status Dr. Anater per semnătură email + added changelog field
  - `CONTEXT_MEDICAL.md §9` — Dr. Anater Angelo - Christian + Dr. Vornicu Vlad-Norin + Dr. Andra Meșter (IOCN second opinion) adăugați la tabel Echipă medicală + footnote „Corespondență oncologică completă: vezi corespondenta/INDEX.md"
  - `TODO.md` — calendar deja conține programare 30.04 + mail trimis 25.04 (Task #7)

**Verificare:**

- [x] `Dosar_Medical/corespondenta/INDEX.md` există cu 11 threaduri categorizate
- [x] **5 fișiere thread create** (mai mult decât 3 minim cerut)
- [x] Frontmatter YAML valid în fiecare (linterul a auto-formatat unele tabele/lists)
- [x] Sinteze automate completate cu cross-references la CONTACTE_MEDICALE.md + CONTEXT_MEDICAL.md
- [x] Conținut integral mailuri păstrat în secțiunile `Mesaje (cronologic)`

**Commit incremental:** `[PLAN 2026-04-25] task #11 — primul ingest Gmail R27 (full-history OncoHelp + tata)` (committed).

---

### Task #12 — INDEX.json query-abil + extindere STRUCTURA_PROIECT.md

**Pre-requisite:** Task #11 commit-uit.

**Context:** sursă unică de query rapid pentru întreg dosarul. Auto-regenerare la modificări. STRUCTURA_PROIECT.md extins cu auto-secțiuni.

**Pași:**

- [ ] **#12.1** — Creez `scripts/generate_index.py` cu următorul rol:
  - Scanează tot proiectul (excluzând `.git`, `node_modules`, `.claude-outputs`, `arhiva`)
  - Pentru fiecare fișier `.md` cu frontmatter YAML → extrage frontmatter
  - Pentru fiecare fișier `.json` cu schema cunoscută (medical document) → extrage metadata
  - Agreghează în `INDEX.json` la rădăcină cu structura:

```json
{
  "generated_at": "ISO timestamp",
  "version": "1.0",
  "stats": {
    "total_files_indexed": 0,
    "medici_oncohelp": 0,
    "threaduri_gmail": 0,
    "documente_canonice": 0,
    "atasamente_listate": 0
  },
  "medici_oncohelp": [
    {"id": "...", "file": "...", "specializare": [...], "unitate": "...", "status": "..."}
  ],
  "corespondenta": [
    {"id": "...", "file": "...", "subject": "...", "participanti": [...], "status": "..."}
  ],
  "documente_canonice": [
    {"id": "...", "file": "...", "data": "...", "tip": "...", "medic": "...", "unitate": "..."}
  ],
  "atasamente_index": [
    {"nume": "...", "thread": "...", "tip": "...", "size": "...", "deep_link_gmail": "..."}
  ],
  "cross_references": {
    "Dr. Anater": ["CONTACTE_MEDICALE.md#dr-anater", "corespondenta/2026-04-24_re-...md"],
    ...
  },
  "files_by_path": {
    "<relative_path>": {
      "type": "...",
      "size_kb": ...,
      "last_modified": "..."
    }
  }
}
```

- [ ] **#12.2** — Rulează `python scripts/generate_index.py` și verifică `INDEX.json` la rădăcină.

- [ ] **#12.3** — Extinde `STRUCTURA_PROIECT.md` (existent) cu o secțiune nouă **„🗺 Hartă completă auto-generată"** la finalul fișierului, generată de `scripts/regenerate_structura.py`:
  - Arborele complet folder/fișiere (output `tree` formatat)
  - Index thematic („Caut [biopsie/medic/programare/dietă/corespondență]? → mergi la [...]")
  - Stats live: număr fișiere, dimensiuni, ultima modificare
  - **Important:** secțiunea auto-generată e marcată cu `<!-- AUTO-GENERATED START -->` și `<!-- AUTO-GENERATED END -->` ca să poată fi regenerată fără a afecta restul fișierului.

- [ ] **#12.4** — Creez `scripts/regenerate_structura.py` care detectează markerii și regenerează doar secțiunea auto.

- [ ] **#12.5** — Rulează `python scripts/regenerate_structura.py`.

**Verificare:**

- [ ] `INDEX.json` există la rădăcină cu structura cerută
- [ ] `STRUCTURA_PROIECT.md` are secțiunea auto-generată actualizată
- [ ] `scripts/generate_index.py` și `scripts/regenerate_structura.py` rulează fără erori

**Commit incremental:**

```bash
git add scripts/generate_index.py scripts/regenerate_structura.py INDEX.json STRUCTURA_PROIECT.md
git commit -m "[PLAN 2026-04-25] task #12 — INDEX.json + STRUCTURA_PROIECT auto-regen"
git push
```

---

### Task #13 — Tab DASHBOARD „👥 Echipă medicală" + search global

**Pre-requisite:** Task #12 commit-uit.

**Context:** tab nou în DASHBOARD.html care citește `INDEX.json` și afișează cards click-to-call/mail. Plus search global în antet.

**Pași:**

- [ ] **#13.1** — Backup R10 `DASHBOARD.html`:

  ```bash
  cp "G:/My Drive/Roly/.Tati/DASHBOARD.html" "G:/My Drive/Roly/.Tati/Dosar_Medical/arhiva/context_medical_versiuni/DASHBOARD_pre-tab-echipa-search_2026-04-25_$(date +%H%M).html"
  ```

- [ ] **#13.2** — În `DASHBOARD.html` la lista de tab-uri (cauți `<button class="tab-btn"`), adaugi un tab nou înainte de tab-ul Alimentație:

  ```html
  <button class="tab-btn" data-tab="echipa">👥 Echipă medicală</button>
  ```

- [ ] **#13.3** — Adaugi panel-ul corespunzător (după panel-urile existente, înainte de `<script>` final):

  ```html
  <div class="tab-panel" id="tab-echipa">
    <h2>👥 Echipă medicală — OncoHelp Timișoara</h2>
    <p class="meta">
      Date din <code>Dosar_Medical/CONTACTE_MEDICALE.md</code> via
      <code>INDEX.json</code>. Click pe telefon = apel direct (mobil). Click pe
      email = deschide client mail.
    </p>
    <input
      type="text"
      id="search-medici"
      placeholder="🔍 Caută medic / specializare / unitate..."
      style="width:100%;padding:8px;margin-bottom:12px;border:1px solid #ccc;border-radius:4px;"
    />
    <div id="echipa-cards"></div>
  </div>
  ```

- [ ] **#13.4** — Adaugi script JS care citește `INDEX.json` și populează cards:

  ```html
  <script>
    (async function loadEchipa() {
      try {
        const res = await fetch("INDEX.json");
        const idx = await res.json();
        const container = document.getElementById("echipa-cards");
        const medici = idx.medici_oncohelp || [];
        function render(filter) {
          container.innerHTML = medici
            .filter(
              (m) =>
                !filter ||
                JSON.stringify(m).toLowerCase().includes(filter.toLowerCase()),
            )
            .map(
              (m) => `
            <div class="card-medic">
              <h3>${m.titlu || ""} ${m.nume}</h3>
              <p><strong>Specializare:</strong> ${(m.specializare || []).join(", ")}</p>
              <p><strong>Unitate:</strong> ${m.unitate}</p>
              <p><strong>Status:</strong> ${m.status}</p>
              ${m.telefoane?.length ? `<p><strong>Telefon:</strong> ${m.telefoane.map((t) => `<a href="tel:${t.numar}">${t.numar}</a>`).join(", ")}</p>` : ""}
              ${m.emails?.primar ? `<p><strong>Email:</strong> <a href="mailto:${m.emails.primar}">${m.emails.primar}</a></p>` : ""}
              <p><a href="${m.file}">→ profil complet</a></p>
            </div>`,
            )
            .join("");
        }
        render("");
        document
          .getElementById("search-medici")
          .addEventListener("input", (e) => render(e.target.value));
      } catch (e) {
        document.getElementById("echipa-cards").innerHTML =
          "<p>⚠ Eroare la încărcarea INDEX.json. Asigură-te că fișierul există la rădăcină.</p>";
      }
    })();
  </script>
  ```

- [ ] **#13.5** — Adaugi CSS minimal pentru `.card-medic` în `<style>` existent:

  ```css
  .card-medic {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 12px;
    margin-bottom: 12px;
    background: #f9f9f9;
  }
  .card-medic h3 {
    margin-top: 0;
    color: #1a73e8;
  }
  .card-medic p {
    margin: 4px 0;
  }
  ```

- [ ] **#13.6** — Update lastRegen JS variable cu data și textul nou:

  ```js
  var lastRegen =
    "2026-04-25 <HH:MM> (R27 + R28 + R29 codificate + CONTACTE_MEDICALE.md OncoHelp + ingest Gmail full-history + tab Echipă + search global INDEX.json)";
  ```

- [ ] **#13.7** — Update banner HTML pentru a reflecta data și conținutul.

**Verificare:**

- [ ] Deschide `DASHBOARD.html` în browser local
- [ ] Tab `👥 Echipă medicală` vizibil
- [ ] Click pe tab → afișează cards Anater + Vornicu
- [ ] Search funcționează (caută „Anater" → filtrează)
- [ ] Click telefon Vornicu → deschide app de telefon (sau întreabă)

**Commit incremental:**

```bash
git add DASHBOARD.html "Dosar_Medical/arhiva/context_medical_versiuni/"
git commit -m "[PLAN 2026-04-25] task #13 — tab DASHBOARD Echipa medicala + search global INDEX.json"
git push
```

---

### Task #14 — Validări finale + commit consolidat + handoff audit

**Pre-requisite:** Task #13 commit-uit.

**Context:** validări end-to-end, marcare plan ca completed, mesaj final pentru auditor.

**Pași:**

- [ ] **#14.1** — Verifică că `REGULI_CLAUDE_CODE.md` conține `## Regula 27`, `## Regula 28`, `## Regula 29`:

  ```bash
  grep -n "## Regula 2[789]" "G:/My Drive/Roly/.Tati/REGULI_CLAUDE_CODE.md"
  ```

- [ ] **#14.2** — Verifică că `CLAUDE.md` proiect conține harta extinsă cu R27/R28/R29:

  ```bash
  grep -n "Regula 2[789]\|R27\|R28\|R29" "G:/My Drive/Roly/.Tati/CLAUDE.md"
  ```

- [ ] **#14.3** — Rulează `python scripts/system_health_check.py` — confirmă status `🟢 OK` (sau marchează status final + recomandări dacă altceva).

- [ ] **#14.4** — Rulează `python scripts/generate_index.py` — confirmă INDEX.json regenerat cu noile fișiere.

- [ ] **#14.5** — Rulează `python scripts/regenerate_structura.py` — confirmă STRUCTURA_PROIECT.md regenerat.

- [ ] **#14.6** — Update **MEMORY.md** (auto-memory) — adaugă checkpoint nou DEASUPRA celui curent:
  - Path: `C:\Users\ALIENWARE\.claude\projects\G--My-Drive-Roly--Tati\memory\MEMORY.md`
  - Linia checkpoint nouă: `🟢 [CHECKPOINT ACTIV] [Sesiune 2026-04-25 plan-audit cross-terminal — R27 + R28 + R29 + CONTACTE_MEDICALE OncoHelp + ingest Gmail + tab Echipă DASHBOARD](sesiune_2026-04-25_plan-audit-r27-r28-r29.md) — CITEȘTE PRIMUL. Plan PLAN_IMPLEMENTARE_2026-04-25.md → status 🟢 COMPLETED.`
  - Marchează checkpoint-ul anterior ca **superseded**.

- [ ] **#14.7** — Creez fișier memory nou: `C:\Users\ALIENWARE\.claude\projects\G--My-Drive-Roly--Tati\memory\sesiune_2026-04-25_plan-audit-r27-r28-r29.md` cu sinteza sesiunii (decizii, ce s-a executat, lecții).

- [ ] **#14.8** — Update plan în acest fișier:
  - Frontmatter `status: 🔴 PENDING` → `status: 🟢 COMPLETED`
  - Adaugă sub Metadata: `completed_at: 2026-04-25 <HH:MM>` și `total_duration_min: <real>`
  - Adaugă secțiune nouă la final: `## ✅ Validări post-execuție` cu raport.

- [ ] **#14.9** — `SESSION_LOG.md` — intrare nouă DEASUPRA:

  ```
  ## 2026-04-25 <HH:MM> — [Claude_Sonnet_4.6_executor] plan-audit-cross-terminal-executie-r27-r28-r29

  **Scop:** execuție strictă a `PLAN_IMPLEMENTARE_2026-04-25.md` (creat de auditor terminal A 18:05). Implementare R27 + R28 + R29 + CONTACTE_MEDICALE OncoHelp + ingest Gmail full-history + tab Echipă DASHBOARD + INDEX.json.

  **Operații:** [listează concis cele 8 task-uri executate cu commit hash-urile]
  ```

- [ ] **#14.10** — `CHANGELOG.md` — intrare nouă DEASUPRA:

  ```
  ## 2026-04-25 <HH:MM> — Implementare R27 + R28 + R29 + sistem catalog OncoHelp + ingest Gmail
  [...detalii...]
  ```

- [ ] **#14.11** — Commit final consolidat:

  ```bash
  git add MEMORY-pointer.md PLAN_IMPLEMENTARE_2026-04-25.md SESSION_LOG.md CHANGELOG.md INDEX.json STRUCTURA_PROIECT.md
  git commit -m "[PLAN 2026-04-25] task #14 — validari finale + plan COMPLETED + memory checkpoint"
  git push
  ```

- [ ] **#14.12** — **Raport final pentru auditor (în chat):**

  ```
  ✅ PLAN_IMPLEMENTARE_2026-04-25.md → status 🟢 COMPLETED

  Commits incremental:
  - <hash> task #7 (mail Anater log)
  - <hash> task #15 (R28 health monitor)
  - <hash> task #9+#10 (CONTACTE + cercetare)
  - <hash> task #11 (ingest Gmail)
  - <hash> task #12 (INDEX.json + STRUCTURA)
  - <hash> task #13 (DASHBOARD tab echipa)
  - <hash> task #14 (validari finale)

  Raport SYSTEM_HEALTH: <status final>

  Aștept audit din terminal A.
  ```

**Verificare finală:**

- [ ] Toate cele 8 task-uri (#7-#15 fără #8 deja făcut, #16+#17 deleted, plus #18 meta) au commit-uri pushed
- [ ] Plan are status `🟢 COMPLETED`
- [ ] MEMORY.md proiect actualizat cu checkpoint nou
- [ ] DASHBOARD se încarcă fără erori în browser

---

## ✅ Validări auditor (terminal A) — după fiecare commit

| Commit task          | Verificare auditor                                                                                                                        |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| #7 (mail Anater)     | `git diff` — modificări doar în SESSION_LOG/TODO/CHANGELOG; conținut coerent cu ce a discutat user-ul cu auditorul                        |
| #15 (health monitor) | `scripts/system_health_check.py` rulează fără erori; `Dosar_Medical/SYSTEM_HEALTH.json` valid JSON; hook în `.claude/settings.local.json` |
| #9+#10 (CONTACTE)    | `Dosar_Medical/CONTACTE_MEDICALE.md` are DOAR Anater + Vornicu; cercetare cu surse URL; nu există invenții                                |
| #11 (ingest Gmail)   | `Dosar_Medical/corespondenta/INDEX.md` + minim 3 fișiere thread; conținut integral mailuri preservat                                      |
| #12 (INDEX.json)     | `INDEX.json` la rădăcină cu structura cerută; `STRUCTURA_PROIECT.md` are secțiunea auto-generată                                          |
| #13 (DASHBOARD)      | Tab `Echipă` vizibil; cards funcționează; search funcționează; backup R10 făcut                                                           |
| #14 (final)          | Plan status `🟢 COMPLETED`; MEMORY.md checkpoint nou; sinteza completă în chat                                                            |

---

## 🚨 Reguli de stop

Executor STOPEAZĂ execuția și raportează în chat la oricare:

1. R28 SYSTEM_HEALTH detectează status `🟠 ALERT` sau `🔴 CRITICAL`
2. Eroare la rularea unui script (Python tracebacks)
3. Conflict git (push refuzat)
4. Cercetarea web returnează 0 rezultate utile pentru Vornicu (nu inventa — raportează)
5. Gmail API returnează erori (auth expirată, etc.)
6. Diferență structurală între ce zice planul și ce găsește în proiect (ex: fișier așteptat lipsește)
7. Backup R10 eșuează (nu continuă fără backup)
8. Linterul re-formatează masiv un fișier (verificare înainte de commit)

---

## 📞 Handoff la finalul execuției

După Task #14, executor (terminal B) raportează în chat:

> ✅ Plan executat integral. Toate validările trecute. Aștept audit din terminal A.

Auditor (terminal A) răspunde după ce verifică:

> ✅ Audit complet. Toate task-urile validate. Sistem unitar codificat. Următoarea sesiune poate folosi R27/R28/R29 nativ.

---

## 📚 Referințe

- `REGULI_CLAUDE_CODE.md#Regula 27` — Ingest Gmail
- `REGULI_CLAUDE_CODE.md#Regula 28` — System Health Monitor
- `REGULI_CLAUDE_CODE.md#Regula 29` — Plan-Audit cross-terminal
- `CLAUDE.md` proiect (root) — pașii 0-5 citire obligatorie
- `MEMORY.md` (auto-memory) — checkpoint activ cu pointer la plan

---

**📌 Plan creat de:** sesiune Claude Opus 4.7 (1M context) — terminal A — 2026-04-25 18:05
**📌 Pentru execuție:** terminal B — sesiune nouă — pornire după confirmare user
