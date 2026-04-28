# HISTORY_CLAUDE_MD.md — Istoric evoluție reguli proiect `.Tati`

**Scop:** istoric cronologic al evoluției regulilor din `CLAUDE.md` + `REGULI_CLAUDE_CODE.md` + nested CLAUDE.md-uri. Extras din `CLAUDE.md` v11 (pre-reorganizare 2026-04-23) ca parte a restructurării v12 (fișier dedicat pentru a nu împovăra contextul always-on).

**Referință:** pentru reguli curente, vezi `CLAUDE.md` + `REGULI_CLAUDE_CODE.md` la rădăcina proiectului.

---

## Changelog versiuni

### 2026-04-28 v12.4 — Cleanup post-PLAN: arhivare kit inițial v1 (L1)

**Trigger:** AUDIT FINAL `2026-04-28_131500` (scor 95/100) a confirmat L1 pendant din audit anterior 03:19 — `Documentatie_Initiala/CLAUDE.md` kit inițial v1 (5.7 KB) auto-load redundant când Claude atinge folderul, conține referințe pre-v12 obsolete (foldere `interpretari/` inexistente).

**Modificări:**

- `Documentatie_Initiala/CLAUDE.md` → `Documentatie_Initiala/INSTRUCTIUNI_INITIALE_v1_archived.md` (git rename — istoric păstrat)
- Conținutul rămâne accesibil pentru referință istorică, dar NU mai e auto-loaded contextual (numele nu mai e `CLAUDE.md`)
- Beneficiu: ~1500 tokens economiseți la auto-load când Claude lucrează în `Documentatie_Initiala/`

**Notă:** acest fișier (kit inițial v1) datează din 2026-04-17, înainte de restructurarea v12 (2026-04-23). De la v12, regulile efective sunt în `CLAUDE.md` root + `REGULI_CLAUDE_CODE.md` + nested CLAUDE.md (Dosar_Medical/, Documente_Informative/). Kit inițial v1 = relicvă istorică păstrată pentru context auditat.

**Pereche:** L2 cleanup în același commit — `AUDIT_EXTRAGERE_2026-04-24.md` + `AUDIT_EXTRAGERE_2026-04-26.md` mutate în `Dosar_Medical/arhiva/audituri_extragere/` (igienă R21 — ambele rapoarte COMPLETED).

---

### 2026-04-23 v12 — Restructurare arhitectură CLAUDE.md

**Trigger:** avertisment Claude Code „Large CLAUDE.md will impact performance (43.4k chars > 40.0k)".

**Context:** user a oferit ca sursă de inspirație (1) workspace-ul paralel `.Tati_Documente_Medicale` (care folosește pattern CLAUDE.md 2k + REGULAMENT.md 11k) și (2) `Regulamente_Globale/` cu `REGULAMENT_TERMINALE.md` (4k) + nested CLAUDE.md/GEMINI.md per subfolder. User a cerut aplicare a filozofiei lui mature (minimalism global + specificitate locală, separație roluri fișiere, nested CLAUDE.md, format per tip informație).

**Modificări:**

- `CLAUDE.md` reconstruit ca **auto-loader minimalist** (~7k vs 43.4k anterior): identitate proiect + ordine citire + harta regulilor + pointers
- **Creat** `REGULI_CLAUDE_CODE.md` la rădăcină — Regulile 6-22 compactate always-on (~16k)
- **Creat** `Dosar_Medical/CLAUDE.md` — Regulile 8, 9, 10, 11, 13, 14, 15 (nested, contextual, ~8k)
- **Creat** `Documente_Informative/CLAUDE.md` — Regula 19 + shortcut Regula 17 (~3k)
- **Creat** `Documentatie_Initiala/REGULI_DETALIATE.md` — exemple complete, matrici, protocoale extinse (~13k, on-demand)
- **Creat** `Documentatie_Initiala/HISTORY_CLAUDE_MD.md` — acest fișier (~4k)
- **REGULAMENT.md** existent (11k, Regulile 1-10 medicale) NEATINS — rămâne cum era
- **Zero modificări** la date medicale: `CONTEXT_MEDICAL.md`, `TODO.md`, JSON-urile din `Dosar_Medical/`, `DASHBOARD.html` neatinse
- Backup CLAUDE.md anterior (v11) arhivat în `Dosar_Medical/arhiva/versiuni_config/CLAUDE_pre-reorganizare-v12_2026-04-23_0320.md`

**Impact măsurat:**

|                                | Înainte      | După         | Reducere |
| ------------------------------ | ------------ | ------------ | -------- |
| CLAUDE.md rădăcină (always-on) | 45,178 bytes | ~7,300 bytes | -84%     |
| Avertisment 40k                | ❌ declanșat | ✅ sub prag  |          |

**Principii aplicate (din sursa de inspirație user):**

1. CLAUDE.md = pointer, nu depozit
2. Separație roluri fișiere (guvernanță / autoritate / stare / istoric / detaliu on-demand)
3. Nested CLAUDE.md în zone specializate
4. Format per tip informație (narativ→`.md`, structurat→`.yaml`/`.json`, colecții→`.jsonl`, config Python→`.toml`, secrete→`.env`)
5. Detalii extinse → fișiere dedicate citite on-demand

---

### 2026-04-23 v11 — Regula 22 (verificare proactivă `[INCERT]`)

Adăugată **Regula 22** (verificare proactivă + eliminare informații neverificate; aplicabilă pe tot proiectul, nu doar sinteze).

**Trigger:** user a constatat în review Obs 2 că rolurile interne ale Dr. Sîrbu „Șef Spitalizare Continuă" și Dr. Oprean „Șef Spitalizare de Zi" erau marcate `[INCERT]` „preluat din sinteza anterioară" — sursă explicit ștearsă ca neverificată.

**Verificarea suplimentară efectuată** (WebSearch + WebFetch pe oncohelp.ro + timpolis.ro + medichub.ro + medical-virtual.ro) a **confirmat ambele roluri** + info nouă (Dr. Oprean membru fondator + studii clinice fază 1 la OncoHelp). Marcajele upgrade-ate la `[CERT]` + surse adăugate.

**Principiul codificat:** `[INCERT]` = task de verificare, nu stare de repaus; verificare la audit/review/integrare; decizie explicită confirmat/infirmat/imposibil + log `CHANGELOG.md`.

---

### 2026-04-23 v10 — Regula 21 (curățenie fluidă, zero ciorne)

Adăugată **Regula 21** (curățenie fluidă folder; zero ciorne; o singură sursă de adevăr per subiect).

**Trigger:** user a solicitat explicit protocol de curățenie în timpul integrării sintezei Gemini `SINTEZA_ONCOHELP_TIMISOARA.md`.

**Principii:** orice fișier extra se auditează, se extrag informațiile utile, apoi se șterge (fără arhivare în `arhiva/` pentru ciorne — git păstrează istoric). Excepții clare pentru arhivare: versiuni anterioare ale fișierelor de referință modificate structural, rapoarte DOCX istorice.

---

### 2026-04-23 v9 — Regula 20 (mod de lucru în 5 pași)

Adăugată **Regula 20** (mod de lucru: cercetare → status → AskUserQuestion → confirmare → execuție).

**Trigger:** user a solicitat explicit acest protocol pentru orice sarcină care implică integrare de informații noi în documentație, cerut în timpul auditului sinteza `SINTEZA_ONCOHELP_TIMISOARA.md`.

**Include:** protocol în 5 pași + cerință semnalare proactivă nereguli cu sugestii documentate + cerință stop-and-ask în timpul execuției pentru decizii neacoperite în meniul inițial.

---

### 2026-04-22 v8 — Regula 19 (`Documente_Informative/`)

Adăugată **Regula 19** (documente informative se salvează în `Documente_Informative/`, nu la rădăcina proiectului).

**Trigger:** user a cerut explicit separarea materialelor operaționale (ghiduri pentru familie/consulturi) de fișierele structurale ale dosarului. Folder `Documente_Informative/` creat simultan + `GHID_CONSULT_ONCOLOG.md` mutat acolo + `GHID_PREZENTARE_CT_FAMILIE.md` șters (la cerere).

---

### 2026-04-18 v7 — GitHub Pages + Dashboard live

Actualizată **Regula 16.4** (repo public intenționat pentru GitHub Pages); **Regula 18** completată cu URL distribuție live + context GitHub Pages; adăugat `index.html` redirect la rădăcina repo-ului.

**Trigger:** user a ales GitHub Pages ca metodă de distribuție live-sync a dashboardului.

---

### 2026-04-18 v6 — Tab Alimentație

Extinsă **Regula 18** — adăugat declanșator #9 (modificare `ALIMENTATIE.md` → regenerare parțială tab Alimentație din dashboard). Clarificată strategia hibridă fetch+embed a tab-urilor.

**Trigger:** user a cerut tab dedicat Alimentație în dashboard cu auto-update la modificarea `ALIMENTATIE.md`.

---

### 2026-04-18 v5 — Regula 18 (sincronizare DASHBOARD)

Adăugată **Regula 18** (sincronizare `DASHBOARD.html` la fiecare actualizare medicală relevantă).

**Trigger:** user a solicitat vizualizare rapidă HTML a dosarului + regulă explicită pentru a preveni divergența dashboard vs. documentație sursă.

---

### 2026-04-18 v4 — Regula 17 (marcaje certitudine)

Adăugată **Regula 17** (marcaj certitudine `[CERT]`/`[PROBABIL]`/`[INCERT]`/`[NEGASIT]` pentru informații medicale în documente generate).

**Trigger:** user a cerut un raport despre reacții adverse Jamesi + Triplixam și a solicitat explicit ca informațiile nesigure să fie marcate ca atare; Regula 17 operaționalizează R3 global pentru outputul medical al dosarului.

---

### 2026-04-18 v3.1 — Clarificări Regula 16 timestamp

Clarificări **Regula 16 sub-clauza 7** (timestamp narativ): adăugat câmp `_metadata.data_procesare` în lista fișierelor afectate; fix typo „intermediar" → „intermediare"; specificat frecvența rulării `date` (refresh >15 min); tabel format per fișier (SESSION_LOG/CHANGELOG trunchiat la `HH:MM`, JSON ISO 8601 complet).

**Trigger:** audit utilizator care a detectat ambiguitățile și commit-ul 478048f nelogat în SESSION_LOG/CHANGELOG (remediat simultan).

---

### 2026-04-18 v3 — Regula 16 (git auto-commit + push)

Adăugată **Regula 16** (git auto-commit + push la finalul fiecărei sesiuni, după crearea repo-ului privat `RolandPetrila/Tati_Dosar_Medical`).

**Pre-autorizare:** user a pre-autorizat Claude să facă `git add + commit + push` automat fără confirmare individuală pe sesiune, la finalul fiecărei sesiuni care a modificat fișiere de referință.

---

### 2026-04-17 v2 — Regulile 8-15 (suita OCR + coordonare + chain)

Adăugate regulile **8-15:**

- **Regula 8** — OCR anti-halucinație
- **Regula 9** — Coordonare Claude ↔ Gemini
- **Regula 10** — Backup pre-modificare
- **Regula 11** — Valabilitate clinică temporală
- **Regula 12** — Conflict surse autoritare
- **Regula 13** — Transcriere manuscrise
- **Regula 14** — Chain of custody
- **Regula 15** — Log cercetări web (`WEB_QUERIES.md`)

Scoped Regulile 6-7 pentru a elimina overhead pe decizii triviale (era „orice neclaritate" — devenit „dubiu factual medical").

---

### 2026-04-17 v1 — Prima versiune

**Prima versiune** — Regulile 6 și 7 preluate din `REGULAMENT.md` al dosarului paralel `.Tati_Dosar_Medical` (sursa originală).

Conținut inițial:

- Regula 6 — Confirmare fișiere la final de mesaj
- Regula 7 — AskUserQuestion pentru decizii medicale

---

## Relația cu celelalte regulamente (cronologic)

- **`REGULAMENT.md`** (rădăcina proiectului, creat 2026-04-17) — conține Regulile 1-10 fundamentale medicale (siguranță, limbaj, cercetare, documentare, interacțiune, confidențialitate, documente, escaladare, feedback, principiu director). **Neatins la restructurarea v12.**
- **Regulamentul global `~/.claude/CLAUDE.md`** — reguli universale Claude Code (R1-R6 + R-RISK/R-SEC/R-RECOVERY/R-COLLAB/R-MINIMAL/R-PLAN), sistem API keys central, auto-memory, auto-doc.
- **`~/.claude/rules/*.md`** (01-05) — reguli globale on-demand: project & quality, sugestii contextuale, reference docs, memory protocol, performance awareness.

**La conflict direct pentru `.Tati`:** regulile proiectului au prioritate.

---

## Referințe

- Reguli curente: `CLAUDE.md` + `REGULI_CLAUDE_CODE.md` + `Dosar_Medical/CLAUDE.md` + `Documente_Informative/CLAUDE.md`
- Exemple extinse + matrici: `REGULI_DETALIATE.md` (alături de acest fișier)
- Plan restructurare v12: `PLAN_reorganizare_claude_md_2026-04-23.md` (alături de acest fișier)
- Backup CLAUDE.md v11 (pre-restructurare): `Dosar_Medical/arhiva/versiuni_config/CLAUDE_pre-reorganizare-v12_2026-04-23_0320.md`
