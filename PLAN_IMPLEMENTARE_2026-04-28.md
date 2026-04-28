---
plan_id: implementare-audit-cleanup-dashboard-pre-consult-2026-04-28
version: 1.0
status: 🟢 COMPLETED
created_at: 2026-04-28 11:45
started_at: 2026-04-28 12:00
completed_at: 2026-04-28 13:10
created_by: Claude_Opus_4.7_1M (terminal de planificare — auditor)
executed_by: Claude_Opus_4.7_1M (terminal executor — sesiune curată 28.04 12:00)
estimated_duration_min: 180
auditor_terminal: ROL — terminal nou cu context curat (A)
executor_terminal: ROL — terminal nou cu context curat (B)
sync_file: EXECUTOR_AUDIT_LOG_2026-04-28.md
backup_strategy: R10 obligatoriu pre-fază (3 backups: pre-Faza-1, pre-Faza-2, pre-Faza-3)
commit_strategy: incremental — 1 commit per fază (3 commit-uri totale, mesaj `[PLAN 2026-04-28] Faza N — <subiect>`)
fazele: 3 (Faza 1 audit+redenumire ~45min · Faza 2 quick wins ~45min · Faza 3 DASHBOARD pre-4.05 ~90min)
sources_filtered:
  - .claude-outputs/audit/2026-04-28_031943/audit_report.md (90/100, 1 MEDIUM + 3 LOW)
  - .claude-outputs/imbunatatiri/2026-04-28_032030/RECOMANDARI_IMBUNATATIRI.md (31 recomandări)
  - .claude-outputs/improve/2026-04-28_032615/{improve_report.md,roadmap.md} (13 task-uri 4 săpt)
filtre_aplicate: [RELEVANT pentru consult 4.05, UTIL ROI≥7, NATIV stack existent, LOGIC nu rupe workflow]
recomandari_implementate: 10 (din ~50 candidate)
recomandari_amânate: ~17 (→ ROADMAP_POST_2026-04-28.md la final)
deadline_critic: 4 mai 2026 — consult oncolog OncoHelp Timișoara
---

# PLAN IMPLEMENTARE 2026-04-28 — Audit + Cleanup + DASHBOARD pre-consult 4.05

> **🔴 PENTRU EXECUTOR (TERMINAL B):** acest fișier este sursa unică de adevăr pentru sesiunea ta. Citește-l integral înainte de a începe. Confirmă cu user-ul că pornești. Apoi execută strict pas cu pas. Marchează `[x]` la fiecare sub-task completat. La eroare → STOP + raport în `EXECUTOR_AUDIT_LOG_2026-04-28.md` + chat. NU adăuga lucruri ne-cerute. NU refactoriza ce nu e cerut.
>
> **🔵 PENTRU AUDITOR (TERMINAL A):** după fiecare commit incremental al executorului (la final de fază), citești `EXECUTOR_AUDIT_LOG_2026-04-28.md` + rulezi `git log -1` + `git diff HEAD~1` pentru validare. Semnalezi în `EXECUTOR_AUDIT_LOG_2026-04-28.md` (secțiunea AUDIT corespunzătoare) orice abatere de la plan sau regresie. Folosește `/audit` skill pentru audit periodic dacă util.
>
> **📞 SYNC:** atât executorul cât și auditorul comunică EXCLUSIV prin `EXECUTOR_AUDIT_LOG_2026-04-28.md`. User citește acest log periodic pentru transparență.

---

## 📋 CONTEXT COMPLET — Sesiunea de planificare 2026-04-28 (preluat din chat)

### Linia evenimentelor sesiunii care a generat acest plan

User a deschis sesiunea cu /onboard + atașament `biopsie_2026.jpeg` (28.04.2026 ~08:30). Pe parcursul sesiunii s-au procesat 4 evenimente clinice majore + 3 documente noi:

1. **Rezultat biopsie esofagiană 17.04 PRIMIT 28.04 — INCONCLUZIV** (Bioclinica buletin 26417A0362 / cod T26H06044 / Dr. Glăja Romanița 27.04). Concluzie: „țesut de granulație pe fond de ulcerație cronică, doar SUGESTIV pentru infiltrat carcinomatos". Recomandare: IHC pe blocul T26H06044 sau rebiopsie. Suspiciunea clinico-imagistică persistă.

2. **Mail trimis Dr. Anater 28.04 09:37** (To Anater + yahoo + CC programari + office) cu PDF biopsie atașat — 5 întrebări deschise (pași post-biopsie, cardiolog 30.04, dată/oră consult, mâncare/medicație pre-consult). **Ingest retroactiv mail anterior 27.04 10:51** descoperit la verificare integrală thread Gmail (lecție: verifică thread-ul integral, nu doar mesajul anunțat).

3. **PDF Vichy 2012 procesat integral** (10 pagini, traducere autorizată Blidar Ioana 705/2002) — **stent confirmat BMS** (Bare Metal Stent) RX VISION 3.5×28 mm Abbott Nr. 1110341 — schimbă substanțial calculul perioperator pentru chirurgia esofagiană (DAPT scurt, risc tromboză in-stent <1%). Echipa franceză identificată: Dr. Marcaggi (operator angioplastie), Dr. Lavaud (coronarografie), Dr. Bitar, etc.

4. **Programare nouă 30.04.2026 ora 12:00 OncoHelp** cu Dr. Mate Endre (Medic Rezident, training UMFT + Marseille + Paris Saint-Louis AP-HP) — recomandare Vornicu telefonic. Scop: înregistrare pacient + pași suplimentari diagnostic. Cardiolog confirmat ora 08:30.

5. **OPIS oficial OncoHelp** procesat (8 puncte documente necesare pre-consult) — mutat din rădăcina `Dosar_Medical/` în folder dedicat `15_consult_initial_oncologie_2026/`.

### Calendar critic

| Data             | Eveniment                                                     | Status                 |
| ---------------- | ------------------------------------------------------------- | ---------------------- |
| 29.04.2026       | Analize sânge Bioclinica (CEA + CA 19-9 + HbA1c)              | 🟢 PROGRAMAT           |
| 30.04.2026 08:30 | Cardiolog ambulator Arad                                      | 🟢 PROGRAMAT           |
| 30.04.2026 12:00 | **Consult inițial OncoHelp Timișoara — Dr. Mate Endre**       | 🟢 PROGRAMAT NOU 28.04 |
| 4.05.2026        | **Consult oncolog OncoHelp Timișoara — Dr. Anater + comisie** | 🔴 PROGRAMAT           |
| post-4.05        | Decizie IHC pe blocul T26H06044 sau rebiopsie țintită         | 🔴 PENDENT             |

### Cererea explicită care a generat acest plan

User a cerut (28.04 ~11:30):

1. Audit complet `documente_sursa/` (15 foldere) — verificare completitudine + redenumire conform convenției R26
2. Cercetare cele 3 documente din `.claude-outputs/` (audit, imbunatatiri, improve generate noaptea 28.04 03:19-03:26)
3. Stabilire metodologie de implementare „relevant/util/nativ/logic"
4. Folosire MCP sequential-thinking pentru planificare
5. Plan-Audit cross-terminal (R29) cu 2 terminale paralele

### Filtrare 50+ recomandări → 10 acțiuni

Aplicat 4 filtre (RELEVANT pentru consult 4.05 / UTIL ROI≥7 / NATIV stack existent / LOGIC nu rupe workflow). Rezultat: 10 acțiuni concrete + audit/redenumire imediat.

**EXCLUSE 17 recomandări → roadmap viitor:**

- Funcții noi: N2 restore_json, N5 Fuse search, N6 email→TODO, N7 trend analize, N8 heartbeat extern, N9 /dosar slash, N10 reverse-lookup, N11 hook audit
- Existente: E1 logger struct, E3 boundary regex, E5 countdown auto, E7 LIMITS extins, E8 R23+R25 thresholds, E9 ARIA WCAG, E10 Q&A primer
- Tehnice: T2 split DASHBOARD, T3 CSP, T4-T7 logging+types+deps+tests, T8-T10 README/Lighthouse/CHANGELOG

La final Faza 3 → executor creează `Documentatie_Initiala/ROADMAP_POST_2026-04-28.md` cu cele 17 amânate.

---

## 🛡 REGULI PROTOCOL CROSS-TERMINAL (R29)

1. **Backup R10 obligatoriu** înainte de fiecare fază: `Dosar_Medical/arhiva/context_medical_versiuni/<file>_pre-faza-N_2026-04-28_HHMM.<ext>`
2. **Commit-uri incrementale** — 1 commit per fază. Format mesaj: `[PLAN 2026-04-28] Faza N — <subiect> (auto-co-author Claude)`
3. **Status plan** — `🔴 PENDING` (acum) → `🟡 IN_PROGRESS` (start Faza 1) → `🟢 COMPLETED` (final Faza 3). Update în frontmatter la fiecare push.
4. **Bifare task** — `- [ ]` → `- [x] (commit <hash>, <data ora>)` după validare auditor.
5. **La eroare** — STOP execuție; raport în `EXECUTOR_AUDIT_LOG_2026-04-28.md` la secțiunea „⚠️ INCIDENTE" + alert chat user. NU continui până user/auditor confirmă rezolvarea.
6. **Verificare SYSTEM_HEALTH** — după fiecare fază. La 🟠/🔴 — STOP + raport.
7. **NU refactorezi** ce nu e cerut. NU adăuga lucruri ne-listate aici.
8. **Limba** — română.
9. **Audit final** — auditorul rulează `/audit` skill după Faza 3 pentru raport final scor.
10. **Sesiune curată** — atât executor cât și auditor pornesc cu context fresh (terminale noi). NU folosesc memory locale ad-hoc; se bazează pe acest PLAN + memory persistent + sync log.

---

## 🔍 INVENTAR DISCREPANȚE — `Dosar_Medical/documente_sursa/`

Audit manual al celor 15 foldere (28.04.2026 ~11:30). Folder cu issues:

| #   | Folder                         | Issue                                                                     | Acțiune Faza 1                  |
| --- | ------------------------------ | ------------------------------------------------------------------------- | ------------------------------- |
| 02  | cardiologie_2012               | `Document_Cardiologie_Vichy_2012.pdf` non-canonic + lipsă `_extragere.md` | REDENUMIRE + creare MD          |
| 11  | CT_stadializare_2026           | `CT - Genesys.{pdf,pdf.meta.json,_extragere.md}` non-canonic (spații!)    | REDENUMIRE 3 fișiere            |
| 12  | biopsie_2026                   | `..._histopatologic.md` lipsește sufix `_extragere`                       | REDENUMIRE 1 fișier             |
| 14  | UPU_2024_05_30                 | 10 JPEG `pag*` fără `.meta.json` (artefacte intermediare)                 | NOTĂ în meta.json al PDF master |
| 15  | consult_initial_oncologie_2026 | lipsă `_extragere.md`                                                     | CREARE MD extragere             |
| 03  | hernie_anterior                | gol intenționat (per user — documente vechi pierdute)                     | **SKIP**                        |

Restul (01, 04, 05, 06, 07, 08, 09, 10, 13) — ✅ canonic.

---

## 📦 TASKS DE EXECUTAT — 3 FAZE

### 🟦 FAZA 1 — Audit + redenumire + completare extragere (~45 min)

**Pre-requisite:** niciuna. Backup R10 obligatoriu la pasul 1.1.

#### Task #1.1 — Backup R10 pre-Faza-1

- [ ] Backup `CONTEXT_MEDICAL.md` → `arhiva/context_medical_versiuni/CONTEXT_MEDICAL_pre-faza-1_2026-04-28_HHMM.md`
- [ ] Backup `Dosar_Medical/2012-02-17_cardiologie_vichy_stent.json` → `arhiva/context_medical_versiuni/`
- [ ] Backup `Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json` → `arhiva/context_medical_versiuni/`
- [ ] Confirmare backup în `EXECUTOR_AUDIT_LOG_2026-04-28.md` (secțiunea EXEC-1.1)

#### Task #1.2 — Redenumire `02_cardiologie_2012/`

- [ ] `Document_Cardiologie_Vichy_2012.pdf` → `2012-02-17_cardiologie_vichy_stent.pdf`
- [ ] `Document_Cardiologie_Vichy_2012.pdf.meta.json` → `2012-02-17_cardiologie_vichy_stent.pdf.meta.json`
- [ ] UPDATE field `source_document` în `.meta.json` cu noul nume
- [ ] UPDATE field `_metadata.sursa_pdf` în `Dosar_Medical/2012-02-17_cardiologie_vichy_stent.json` (canonic)
- [ ] CREARE `2012-02-17_cardiologie_vichy_stent_extragere.md` (transcriere strict-extractivă R23 din PDF — 10 pagini Blidar Ioana traducere)

#### Task #1.3 — Redenumire `11_CT_stadializare_2026/`

- [ ] `CT - Genesys.pdf` → `2026-04-20_ct_torace_abdomen_pelvis.pdf`
- [ ] `CT - Genesys.pdf.meta.json` → `2026-04-20_ct_torace_abdomen_pelvis.pdf.meta.json`
- [ ] `CT - Genesys_extragere.md` → `2026-04-20_ct_torace_abdomen_pelvis_extragere.md`
- [ ] UPDATE field `source_document` în `.meta.json` cu noul nume
- [ ] UPDATE field `_metadata.sursa_pdf` în `Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json` (canonic)
- [ ] UPDATE referințe în `CONTEXT_MEDICAL.md §2.5` (`CT - Genesys.pdf` → noul nume)
- [ ] Verificare cross-references prin `Grep "CT - Genesys"` — TOATE updatate

#### Task #1.4 — Redenumire `12_biopsie_2026/`

- [ ] `2026-04-17_biopsie_esofagiana_histopatologic.md` → `2026-04-17_biopsie_esofagiana_histopatologic_extragere.md`
- [ ] UPDATE field `extragere_md` în `2026-04-17_biopsie_esofagiana_histopatologic.pdf.meta.json` cu noul nume
- [ ] UPDATE referințe în `Dosar_Medical/2026-04-17_biopsie_esofagiana_histopatologic.json` (dacă există)

#### Task #1.5 — Notă pentru `14_UPU_2024_05_30/` (artefacte JPEG intermediare)

- [ ] Adaugă în `2024-05-30_dosar_upu_complet.pdf.meta.json` câmp `intermediate_artifacts`:
  ```json
  "intermediate_artifacts": {
    "files": ["2024-05-30_dosar_upu_pag0.jpeg", "...pag1.jpeg", ..., "...pag9.jpeg"],
    "note": "Cele 10 JPEG-uri sunt artefacte intermediare ale conversiei PDF master (paginile individuale ale dosarului UPU). PDF-ul master e sursa autoritară R23. JPEG-urile NU au .meta.json companion individual — sunt referință vizuală suplimentară.",
    "decision_date": "2026-04-28"
  }
  ```

#### Task #1.6 — Creare MD extragere `15_consult_initial_oncologie_2026/`

- [ ] CREARE `2026-04-28_opis_consult_initial_oncohelp_extragere.md` cu transcriere strict-extractivă a celor 8 puncte OPIS:
  1. Bilet de trimitere către Oncologie
  2. Buletin
  3. Card de sănătate
  4. Adeverință de salariat (de la locul de muncă) SAU cupon de pensie
  5. COPIE după rezultatul examenului histopatologic (BIOPSIE)
  6. COPIE după scrisoarea medicală/biletul de ieșire din spital unde s-a efectuat biopsia/operația
  7. COPIE după ALTE DOCUMENTE MEDICALE care susțin diagnosticul altor boli cronice (diabet zaharat, boli renale, pulmonare, hipertensiune arterială, infarct miocardic, hipercolesterolemie, boli neurologice, digestive, psihiatrice sau alte boli cronice)
  8. Schemă cu medicamentele pe care și le administrează și modul în care și le administrează (momentul de administrare pe parcursul zilei și doza medicamentului)

#### Task #1.7 — Verificare finală + commit Faza 1

- [ ] `git status --short` — verificare 8-10 fișiere modificate (3 redenumiri PDF/MD + 4 meta.json updates + 2 MD-uri noi extragere + 1 nota meta UPU)
- [ ] Regenerare `INDEX.json` via `python scripts/generate_index.py`
- [ ] Verificare SYSTEM_HEALTH 🟢
- [ ] Commit: `[PLAN 2026-04-28] Faza 1 — Audit + redenumire 4 fișiere + 2 MD extragere noi + nota UPU`
- [ ] Push origin/main
- [ ] Update status plan `🔴 PENDING` → `🟡 IN_PROGRESS` (înainte de Task #1.1) și verificare `🟡 IN_PROGRESS` păstrat
- [ ] Raport final Faza 1 în `EXECUTOR_AUDIT_LOG_2026-04-28.md` (secțiunea EXEC-FAZA-1-FINAL)

---

### 🟦 FAZA 2 — Quick wins automate (~45 min)

**Pre-requisite:** Faza 1 completă + auditor a aprobat.

#### Task #2.1 — Backup R10 pre-Faza-2

- [ ] Backup `CONTEXT_MEDICAL.md` (re-backup post-Faza-1, capturare stare nouă)
- [ ] Backup `scripts/system_health_check.py`

#### Task #2.2 — Fix M3 (audit 28.04) — CONTEXT_MEDICAL §4 sub-header `30.04` → `4.05`

- [ ] Edit `CONTEXT_MEDICAL.md` linia ~291: `### Observație clinică — statină nealuată curent (de evaluat la consult oncolog 30.04)` → `4.05`
- [ ] Edit linia ~299: `De ridicat la consultul oncolog 30.04.2026 OncoHelp Timișoara` → `4.05.2026 (luni)`
- [ ] Verificare `Grep "consult oncolog 30.04"` — ZERO match (toate updatate sau deja istorice changelog)

#### Task #2.3 — Fix E2 — eliminare path Windows hardcoded `MEMORY.md` în `scripts/system_health_check.py`

- [ ] Citește `scripts/system_health_check.py` linia 102-104 (path hardcoded `C:/Users/ALIENWARE/...`)
- [ ] Înlocuire cu funcție `find_memory_md()` per recomandarea E2 din `RECOMANDARI_IMBUNATATIRI.md` (env var fallback + slug detection + manual search)
- [ ] Test: rulează `python scripts/system_health_check.py` — verifică că `memory_md_lines` apare valid în `SYSTEM_HEALTH.json`
- [ ] Commit-ul include și `SYSTEM_HEALTH.json` regenerat

#### Task #2.4 — N4 creare `scripts/audit_documente_sursa.py`

- [ ] Creează scriptul per spec din `RECOMANDARI_IMBUNATATIRI.md` (linia 1278-1425 — `audit()` + `render_report()` cu detect violări R14+R26)
- [ ] Test: rulează `python scripts/audit_documente_sursa.py` — verifică că generează `Dosar_Medical/AUDIT_DOCUMENTE_SURSA.md`
- [ ] Verificare raport: post-Faza-1 ar trebui să arate **0 violări** (toate canonice acum, exceptând `03_hernie_anterior/` gol intenționat)

#### Task #2.5 — T1 setup pre-commit `check-jsonschema` (escaladat user TODO P3)

- [ ] Verificare `pip show check-jsonschema` — dacă lipsește, prompt user pentru `pip install check-jsonschema` (NU instalez automat fără confirmare)
- [ ] Creează `schemas/dosar_medical_v2.json` cu schema minimă (extracts pattern din 21 JSON-uri canonice — câmpuri obligatorii: `_metadata.schema_version`, `_metadata.tip_document`, `pacient` cu `cnp`+`data_nasterii`)
- [ ] Creează `.pre-commit-config.yaml` la rădăcină per spec T1 (linia 2080-2096)
- [ ] Test: rulare `pre-commit run --all-files` (dacă `pre-commit` framework instalat) sau manual `check-jsonschema --schemafile schemas/dosar_medical_v2.json Dosar_Medical/*.json`
- [ ] Update `TODO.md` — închidere [P3] „Pre-commit hook pentru lint JSON" → ✅ REZOLVAT 28.04

#### Task #2.6 — Verificare finală + commit Faza 2

- [ ] `git status --short` — verificare 5-7 fișiere modificate
- [ ] Regenerare `INDEX.json`
- [ ] Verificare SYSTEM_HEALTH 🟢
- [ ] Commit: `[PLAN 2026-04-28] Faza 2 — Fix M3 CONTEXT + E2 path Windows + N4 audit script + T1 jsonschema`
- [ ] Push origin/main
- [ ] Raport final Faza 2 în `EXECUTOR_AUDIT_LOG_2026-04-28.md`

---

### 🟦 FAZA 3 — DASHBOARD pre-consult 4.05 (~90 min)

**Pre-requisite:** Faza 2 completă + auditor a aprobat.

#### Task #3.1 — Backup R10 pre-Faza-3

- [ ] Backup `DASHBOARD.html` → `arhiva/context_medical_versiuni/DASHBOARD_pre-faza-3_2026-04-28_HHMM.html`
- [ ] Backup `Dosar_Medical/CONTACTE_MEDICALE.md`

#### Task #3.2 — E6 tel: și mailto: clickable în DASHBOARD

- [ ] Identifică zona tab Echipă medicală în `DASHBOARD.html` (probabil ~linia 4000+)
- [ ] Modifică funcția de render medic per spec E6 (`RECOMANDARI_IMBUNATATIRI.md` linia 446-475) — telefon devine `tel:+4...` link, email devine `mailto:...?subject=...` link
- [ ] Adaugă CSS `.medic-link` per spec (linia 480-495)
- [ ] Verificare meta `<meta name="format-detection" content="telephone=yes" />` în `<head>` (deja prezent per audit)

#### Task #3.3 — E4 badge sursă date DASHBOARD

- [ ] Identifică `getIndexData()` în `DASHBOARD.html` (linia 4056-4087 per audit)
- [ ] Adaugă funcția `showDataSourceBadge(source, timestamp)` per spec E4 (linia 290-340)
- [ ] Adaugă `createDataSourceBadge()` + `formatRelative()` helpers
- [ ] Modifică `getIndexData()` să apeleze `showDataSourceBadge()` la fiecare branch (file:// embedded / http:// fetch / fallback)
- [ ] Test manual: deschide DASHBOARD în file:// — vezi badge 🟡 cache; HTTP — vezi 🟢 live (dacă disponibil)

#### Task #3.4 — N3 tab DASHBOARD „📋 Antecedente" agregat 5-7 linii

- [ ] Adaugă tab button + tabpanel în zona taburilor existente (înainte de tab Echipă)
- [ ] Adaugă array `ANTECEDENTE_DATA` per spec N3 (linia 1162-1211) — 6 înregistrări: stent 2012, UPU 2024, H. pylori 2024, schemă 2025, hernie 2025, suspiciune 2026
- [ ] Adaugă funcția `renderAntecedente()` per spec
- [ ] Adaugă CSS `.antecedente-table` cu severity coloring + print-friendly @media print
- [ ] Test: click pe tab Antecedente — verificare 6 rânduri cu link la JSON canonic

#### Task #3.5 — N1 creare `scripts/generate_consult_briefing.py` + DOCX 4.05

- [ ] Creează scriptul per spec N1 (`RECOMANDARI_IMBUNATATIRI.md` linia 776-968) — argparse + `extract_section()` + `build_docx()` + 3 template-uri (oncolog, cardiolog, endocrin)
- [ ] Verificare `python-docx` instalat (deja folosit la `EXPLICATIE_REZULTAT_BIOPSIE_2026-04-28.docx`)
- [ ] Rulare:
  ```bash
  python scripts/generate_consult_briefing.py \
    --consult oncolog \
    --data 2026-05-04 \
    --medic "Dr. Anater Angelo-Christian" \
    --unitate "OncoHelp Timișoara"
  ```
- [ ] Verificare output: `Dosar_Medical/rapoarte_generate/2026-05-04_briefing_consult_oncolog.docx` + `.meta.json`
- [ ] Verificare DOCX deschide în Word/LibreOffice fără erori — conține 6 secțiuni (date pacient, status TNM, medicație, checklist dosar, întrebări, notes consult)

#### Task #3.6 — Update CONTACTE_MEDICALE.md cu Dr. Mate Endre (al 3-lea medic OncoHelp)

- [ ] Citește `Dosar_Medical/CONTACTE_MEDICALE.md` v1.2 (curent)
- [ ] Adaugă secțiune nouă `## Dr. Mate Endre {#dr-mate-endre}` cu YAML block similar Anater + profil profesional cercetat (Medic Rezident OncoHelp, training UMFT + Marseille + Saint-Louis Paris, focus imunoterapie, programare 30.04 12:00)
- [ ] Update tabel Index rapid (rândurile 30-32) cu rândul nou
- [ ] Bump versiune frontmatter `version: 1.2` → `1.3`
- [ ] Bump `medici_listati: 2` → `3`

#### Task #3.7 — ROADMAP_POST_2026-04-28.md (cele 17 amânate)

- [ ] Creează `Documentatie_Initiala/ROADMAP_POST_2026-04-28.md` cu cele 17 recomandări amânate, organizate pe categorii:
  - **Funcții noi amânate (8):** N2, N5, N6, N7, N8, N9, N10, N11 — fiecare cu ID, titlu, complexitate, impact, condiție declanșare
  - **Existente amânate (7):** E1, E3, E5, E7, E8, E9, E10
  - **Tehnice amânate (10):** T2, T3, T4, T5, T6, T7, T8, T9, T10
- [ ] Formatare per coloane: ID | Titlu | Complexitate | Impact | Condiție | Sursa
- [ ] Frontmatter cu `target_review_date: 2026-05-26` (după consult 4.05 + 3 săpt)

#### Task #3.8 — Verificare finală + commit Faza 3

- [ ] `git status --short` — verificare 8-12 fișiere modificate
- [ ] Test browser: deschide `DASHBOARD.html` local (file://) — verificare tab Antecedente apare + tel/mailto links funcționale + badge sursă 🟡
- [ ] Test browser: deschide https://rolandpetrila.github.io/Tati_Dosar_Medical/ — verifică badge 🟢 live (după push)
- [ ] Regenerare `INDEX.json`
- [ ] Verificare SYSTEM_HEALTH 🟢
- [ ] Commit: `[PLAN 2026-04-28] Faza 3 — DASHBOARD: E6 tel/mailto + E4 badge + N3 Antecedente + N1 briefing DOCX + ROADMAP_POST`
- [ ] Push origin/main
- [ ] Update status plan `🟡 IN_PROGRESS` → `🟢 COMPLETED`
- [ ] Update `MEMORY.md` cu pointer la sesiune COMPLETED

---

## 🎯 VALIDĂRI FINALE (auditor — după Faza 3)

- [ ] **Audit complet `/audit`** — scor ≥90 (la fel sau mai bun decât 90 din audit 28.04 03:19)
- [ ] **R28 SYSTEM_HEALTH 🟢 OK** — toate metricile sub limite
- [ ] **R14 chain of custody** — toate fișierele `documente_sursa/*.{pdf,jpeg}` au `.meta.json` companion (exceptând UPU JPEG-uri intermediare per nota Task #1.5)
- [ ] **R26 consistență structură** — toate folderele canonice `NN_categorie_data/`, toate fișierele `YYYY-MM-DD_descriere.ext`
- [ ] **R23 coverage** — toate JSON-urile au `completeness_verified` + `coverage: 100%`
- [ ] **Cross-references** — `Grep "Document_Cardiologie_Vichy_2012\|CT - Genesys"` → 0 match (toate updatate)
- [ ] **Pre-commit hook** — `check-jsonschema` validare trecută la commit final
- [ ] **DASHBOARD render OK** — file:// + http:// — 0 erori console; toate taburile funcționale
- [ ] **DOCX briefing 4.05** — generat, lizibil, ~6 secțiuni
- [ ] **Toate 3 commit-uri push-uite** pe `origin/main`
- [ ] **`MEMORY.md`** updatat cu noul checkpoint sesiune

---

## 📞 HANDOFF PENTRU EXECUTOR (Terminal B)

### Mesaj inițial sugerat user → executor

```
Salut! Te rog să execuți planul activ din rădăcina proiectului.

Verifică PLAN_IMPLEMENTARE_2026-04-28.md cu status 🔴 PENDING sau 🟡 IN_PROGRESS,
citește-l integral și începe execuția strict pas cu pas.

Folosește EXECUTOR_AUDIT_LOG_2026-04-28.md pentru rapoartele tale (format definit în plan).

Confirmă-mi că ai citit planul și pornește.
```

### Ce face executor automat la SessionStart

- Hook SessionStart rulează `system_health_check.py` (R28) — afișează status 🟢/🟡/🟠/🔴
- Auto-load `CLAUDE.md` root (instrucție explicită): „dacă există PLAN\_\*.md cu status 🔴/🟡, citește-l ÎNAINTE"
- Memory `MEMORY.md` injectat automat — include checkpoint activ ultima sesiune
- Executor citește acest plan + EXECUTOR_AUDIT_LOG (gol la start) → execută

### `/onboard` necesar?

**NU strict necesar.** Detectarea PLAN-ului activ + auto-load CLAUDE.md acoperă majoritatea contextului. Dar `/onboard` adaugă: status git (last 5 commits + modificări necomise) + sumar memory cheie.

**Recomandare:** **NU rula /onboard** la executor — adaugă timp + context inutil. Mesajul inițial de mai sus e suficient.

---

## 📞 HANDOFF PENTRU AUDITOR (Terminal A)

### Mesaj inițial sugerat user → auditor

```
Salut! Te rog să auditezi execuția planului PLAN_IMPLEMENTARE_2026-04-28.md.

Citește planul + EXECUTOR_AUDIT_LOG_2026-04-28.md pentru rapoartele executorului.

După fiecare commit incremental al executorului (3 fișiere planificate), verifică:
1. git diff HEAD~1 — modificările respectă spec din plan?
2. SYSTEM_HEALTH 🟢?
3. Cross-references intact?
4. Bifare task-uri în plan corespunzătoare commit-ului?

Scrie raportul tău de audit în EXECUTOR_AUDIT_LOG_2026-04-28.md (secțiunile AUDIT-FAZA-N).

La final Faza 3, rulează skill /audit pentru raport complet scor.
```

### `/onboard` necesar pentru auditor?

**NU.** Auditorul citește direct PLAN + EXECUTOR_AUDIT_LOG. Memory persistent + auto-load CLAUDE.md sunt suficiente.

---

## 💡 SUGESTII SUPLIMENTARE / COMPLETĂRI (Claude propune, user decide)

1. **Audit periodic în Faze:** după Faza 1 (commit 1) auditorul rulează `git diff HEAD~1` MANUAL înainte ca executorul să pornească Faza 2. Asta evită cascadarea erorilor.

2. **Test browser obligatoriu Faza 3:** modificările DASHBOARD.html pot rupe rendering. Recomand ca user să deschidă manual `DASHBOARD.html` (dublu-click) după commit Faza 3 și să verifice vizual înainte ca auditorul să marcheze ca COMPLETED.

3. **Skill `/audit` la final:** auditorul rulează `/audit` (skill existent) după Task #3.8 commit. Output în `.claude-outputs/audit/<timestamp>/` — comparare cu auditul 28.04 03:19 (scor 90/100). Țintă: ≥92.

4. **Memory checkpoint la final:** executorul (după ultimul commit) salvează în memory `sesiune_2026-04-28_implementare-plan-cross-terminal.md` cu pointer la PLAN COMPLETED. Auditorul confirmă în chat user.

5. **Limită upper rolling window context:** dacă context terminale executor sau auditor depășește 70% (R28), STOP + restart terminal nou + reluare de la ultimul commit-ed task. Plan e recuperabil oricând (status în frontmatter).

6. **Rolloff documentation cleanup:** la final Faza 3, executorul adaugă o secțiune `📚 Documente generate post-implementare` în acest plan cu lista commit-urilor + fișierele noi create (transparency).

7. **Verificare cross-references atomică:** după Faza 1 (Task #1.7 commit), executorul rulează:

   ```bash
   grep -rn "Document_Cardiologie_Vichy_2012\|CT - Genesys" --include="*.md" --include="*.json" --include="*.html"
   ```

   Rezultat așteptat: ZERO match (afară de istoric `arhiva/` + `.claude-outputs/` care nu se modifică).

8. **NU rula `pip install` automat:** Task #2.5 (T1 check-jsonschema) cere instalare PyPI package. Executorul **NU** instalează automat — prompt user în chat pentru confirmare. Dacă user spune NU → SKIP Task #2.5 + notează în EXECUTOR_AUDIT_LOG ca `🟡 SKIPPED — user declined pip install`.

---

## 📚 ELEMENTE NOI APĂRUTE PE PARCURS (se completează aici)

> Această secțiune se actualizează de executor sau auditor dacă apar lucruri ne-listate în planul inițial. Format: `### [DATA HHMM] [EXEC/AUDIT] [ID] Titlu` + descriere + decizie.

_(gol la creare)_

---

## 📊 Status global

| Fază                 | Status  | Început | Sfârșit | Commit hash | Validat auditor                                                                                                            |
| -------------------- | ------- | ------- | ------- | ----------- | -------------------------------------------------------------------------------------------------------------------------- |
| Faza 1               | 🟢 DONE | 12:00   | 12:30   | 4c9bdd8     | 🟡 PASS_WITH_NOTES (12:25 — 4 INFO neblocante, vezi AUDIT-FAZA-1)                                                          |
| Faza 2               | 🟢 DONE | 12:45   | 12:55   | df817d0     | 🟢 PASS (12:58 — BONUS BUG biopsie reparat de schema T1)                                                                   |
| Faza 3               | 🟢 DONE | 13:00   | 13:10   | 24af7e9     | 🟢 PASS (13:15 — 5 INFO neblocante, vezi AUDIT-FAZA-3)                                                                     |
| Audit final `/audit` | 🟢 DONE | 13:15   | 13:25   | (skill)     | 🟢 SCOR 95/100 (+5 vs 90 anterior — `.claude-outputs/audit/2026-04-28_131500/`)                                            |
| Memory checkpoint    | 🟢 DONE | 13:10   | 13:10   | 7613ea0     | salvat `~/.claude/projects/G--My-Drive-Roly--Tati/memory/sesiune_2026-04-28_plan-implementare-cross-terminal-completat.md` |

---

## 🔚 La final

Executorul, după Task #3.8 commit + push:

1. Update frontmatter `status: 🟢 COMPLETED` + `completed_at: 2026-04-28 HH:MM`
2. Bifare TOATE task-urile cu commit hash + dată
3. Salvare memory checkpoint
4. Comunicare în chat user: „Plan COMPLETED. Toate 3 faze validate. Comandă `/audit` ai recomandat la auditor pentru raport final scor."

Auditorul, după validare finală:

1. Rulează skill `/audit`
2. Scrie raport final în `EXECUTOR_AUDIT_LOG_2026-04-28.md` (secțiune `## ✅ AUDIT FINAL`)
3. Comunicare în chat user: scor + delta vs 28.04 03:19 + recomandări post-4.05 (din ROADMAP_POST_2026-04-28.md)
