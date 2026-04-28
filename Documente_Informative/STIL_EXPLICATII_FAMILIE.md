# STIL_EXPLICATII_FAMILIE.md — Ghid de stil pentru documente educaționale familie

**Versiune:** 2.0 | **Data:** 2026-04-28 | **Validat prin:** `2026-04-22_explicatie_consult_oncolog_scenarii.docx` (476 paragrafe, 12 tabele, 65 KB) — ales de user pe 2026-04-28 ca exemplu reprezentativ pentru stil

> **Acest fișier descrie stilul standard pentru documente medicale destinate user-ului (Roland Petrilă) sau familiei (Maria), când e cerută o abordare narativă/educațională.**
>
> NU se aplică la briefing-uri pentru medici, rapoarte tehnice, ghiduri operaționale.
>
> Document referit on-demand din memoria feedback `feedback_explicatii_familie_fir_narativ.md` și din Regula 17 (REGULI_CLAUDE_CODE.md). Nu este auto-loaded.
>
> **Versiune anterioară (v1.0):** `Dosar_Medical/arhiva/context_medical_versiuni/STIL_EXPLICATII_FAMILIE_v1_pre-revize-poveste-integrata_2026-04-28_1500.md` — folosea callouts „Pe firul nostru" + structură rigidă termen-cu-termen. Înlocuită cu stilul „poveste curgătoare integrată" pe baza feedback-ului user.

---

## 1. Trigger — când aplici stilul

### Aplici automat când user cere explicit:

- „explică-mi" / „explică ca să înțeleg" / „explică pe înțelesul meu"
- „cu exemple" / „cu analogii" / „prin exemple din viața reală"
- „ca o poveste" / „povestește" / „ca un necunoscător"
- „vreau să înțeleg fiecare X" / „să înțeleg exact ce înseamnă"
- „pentru familie" + cerere de explicație (NU briefing)

### NU aplici (păstrezi stilul tehnic profesional):

- Briefing-uri pentru medici: Anater, comisie tumor board, Mate Endre, Vornicu, Glăja
- Rapoarte tehnice: `CONTEXT_MEDICAL.md`, JSON-uri canonice `Dosar_Medical/`, sinteze clinice
- Ghiduri operaționale acțiune-imediată: `GHID_TELEFOANE_*.md`, `GHID_CARDIOLOG_*.md`, `GHID_APEL_ONCOHELP.md`, `GHID_CONSULT_ONCOLOG.md`
- Documente cu marcaj „pentru medici" în nume sau header

---

## 2. Workflow obligatoriu — `AskUserQuestion` ÎNAINTE de execuție

**Regulă critică validată 2026-04-28:** la detectarea unui trigger, NU începe direct execuția. Întâi propune user-ului un meniu de opțiuni prin `AskUserQuestion`, apoi execută strict ce s-a confirmat.

### Pași obligatorii la cerere cu trigger:

1. **Citește sursele** (PDF medical, JSON canonice, transcrieri MD existente) pentru a avea context complet
2. **Identifică termenii necesari de explicat** (numar, complexitate)
3. **Propune meniu `AskUserQuestion`** cu opțiunile de mai jos (3-4 întrebări max conform R7)
4. **Așteaptă confirmarea user**
5. **Execută strict ce s-a confirmat**
6. **Actualizează memoria** dacă apare un nou pattern

### Lista standard de aspecte de propus în meniu

#### Întrebare 1 — Capitole de inclus (multiSelect)

Lista capitole tipice (selectabile):

- ☑ **Cover + cuprins explicit** (toate listate)
- ☑ **Mesaj principal — în 30 secunde** (TL;DR esențializat)
- ☑ **Capitol „Povestea"** — narativă curgătoare cu metafora centrală integrată în text (NU callouts)
- ☑ **„Anatomia raportului" / „Raportul — bucată cu bucată"** — fiecare termen explicat în format 4-paragrafe (Analogie / Medical / Cum se face / Impact)
- ☑ **„Întrebările tale — răspunsuri directe"** — DA/NU + motivare la întrebări tipice
- ☐ **„Investigațiile posibile — explicate simplu"** — IHC, rebiopsie, EUS, PET-CT, paracenteză cu format „Cum se face / Ce vede / Risc / Cost / Durată"
- ☐ **„Scenarii combinatorii cu plan de tratament"** — variante cu probabilități + plan
- ☐ **„FAQ familie — răspunsuri pregătite"** — întrebări tipice (10 sau mai puține)
- ☐ **„Ce trebuie să faci tu (Roland) — concret"** — secțiune „ACUM" / „După ce ai datele"
- ☐ **Timeline vizual** — tabel cronologic 2-coloane (Data / Eveniment)
- ☑ **Glossar tabel 3-coloane** — „Termen medical / Explicație simplă / Analogia"
- ☑ **Surse citate + „Ce NU am inclus"** — transparență
- ☑ **Atenționare R17 finală**

> **Default Recomandat (✓):** Cover+Cuprins + Mesaj 30s + Povestea + Anatomia raportului + Întrebări tale + Glossar + Surse + R17. Restul depinde de complexitatea cazului.

#### Întrebare 2 — Lungime estimată

- **Scurt** (~30 KB, ~10 pagini, focus pe esențial)
- **Mediu** (~60 KB, ~20 pagini, echilibrat)
- **Extins** (~100 KB, ~30 pagini, exhaustiv)

#### Întrebare 3 — Metafora centrală

Propun 2-3 opțiuni adecvate subiectului (vezi tabelul de mai jos), user alege sau propune alta.

| Subiect                                    | Metaforă centrală propusă                                                                                        | Status                                 |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| Biopsie / histopatologie                   | „Casa cu o pată suspectă pe perete" — inspector ia firimituri de tencuială pentru analiză la laborator           | ✅ Validat 28.04                       |
| CT / RMN / imagistică                      | „Casa scanată cu drone" / „raze X" — radiograful e fotograf cu echipament special care vede prin pereți          | ✅ Validat 22.04 (în exemplul de stil) |
| Chemoterapie (FLOT, paclitaxel)            | „Antibiotic pentru celulele rebele" / „Ploaie de substanțe care afectează ce crește repede"                      | 📌 Propus                              |
| Imunoterapie (PD-L1, checkpoint inhibitor) | „Steagul invizibilității tumorii" / „Ridicăm steagul alb" — sistem imun antrenat să recunoască inamicul deghizat | ✅ Validat 22.04                       |
| Markeri moleculari (HER2, MSI)             | „Cheile care deschid tratamente" / „Defecte în fotocopiator" / „Lacăte cu antene"                                | ✅ Validat 22.04                       |
| Chirurgie esofagiană (esofagectomie)       | „Reconstrucție arhitectonică" — repară un perete deteriorat conectând capete sănătoase                           | 📌 Propus                              |
| Stadializare TNM                           | „Scara cu 3 trepte" — T = mărime ranii, N = câte încăperi vecine afectate, M = dacă a ajuns în alte case         | 📌 Propus                              |
| Ascită                                     | „Apa din subsol" — borcan cu organe + folie peritoneu + găleți gravitaționale                                    | ✅ Validat 22.04                       |
| Investigații (paracenteza, laparoscopia)   | „Pipeta din acvariu" / „Camera video în subsol"                                                                  | ✅ Validat 22.04                       |

#### Întrebare 4 (opțional) — Format livrare

- **Doar DOCX** (printabil, cover profesional)
- **DOCX + MD** (pentru chat web/mobil R30 + git tracking)
- **Doar MD** (rar — pierde formatare)

**La dubiu:** întrebi user-ul O SINGURĂ DATĂ cu opțiunile de mai sus, apoi aplici. NU asuma defaults dacă nu sunt explicit confirmate.

---

## 3. Cele 5 principii fundamentale ale stilului

### 3.1 Poveste curgătoare integrată (regula #1)

Capitolul „Povestea" e narativă fluidă — analogiile sunt EMBED-uite ÎN propoziții, nu separate în callouts:

✅ **CORECT (stilul exemplu):**

> „Tatăl tău e ca o casă bine construită, care a rezistat 66 de ani. În ultima lună au apărut semne că ceva nu e în regulă pe interior. Endoscopia a fost ca și cum ai trimis un meșter cu o lanternă pe hol — a găsit o zidărie dăunată în coridorul principal..."

❌ **GREȘIT (stilul vechi v1.0):**

> „Pe firul nostru: pacientul = casa. Esofagul = un perete. Leziunea = pată pe perete..."
> [callout separat]
> „Pe firul nostru: la endoscopie, inspectorul vine cu lanterna..."
> [alt callout]

### 3.2 Format 4-paragrafe pentru concepte tehnice (regula #2)

Pentru fiecare concept tehnic important (termen medical, procedură, marker), folosești format consistent cu 4 paragrafe / sub-secțiuni:

```
### NumeConcept — „Titlu cu analogie"

**Analogie:** [explicarea metaforei aplicate, 2-3 propoziții]

**Medical:** [definiția științifică concisă, 1-2 propoziții]

**Cum recunoaște laboratorul / Cum se face / Ce vede:** [practic, ce face medicul/aparatul]

**Impact clinic:** [ce înseamnă pentru pacient]
```

Variante per tip de concept:

- **Procedură (paracenteza, EUS, IHC):** Analogie + Cum se face (pas cu pas) + Ce vede + Risc + Durată + Cost
- **Marker molecular (HER2, MSI):** Analogie + De ce e util + Frecvență + Medicament țintit + Beneficiu
- **Cauză patologică (necroza fibrinoidă, granulație):** Analogie + Medical + Cum recunoaște + Impact
- **Scenariu (4 scenarii biopsie/ascită):** Analogie casă + Probabilitate + Diagnostic clinic + Plan tratament

### 3.3 Acoperire integrală a termenilor (regula #3)

NU lăsa termeni medicali fără explicație. Dacă raportul are 15 termeni microscopici, toți cei 15 primesc cele 4 paragrafe.

Excepție acceptabilă: termen menționat o singură dată într-un context unde sensul e clar din proză — explică inline, nu separat.

### 3.4 Marcaje certitudine R17 integrate fluid (regula #4)

Marcajele `[CERT]` / `[PROBABIL]` / `[INCERT]` / `[NEGASIT]` apar ca PREFIXE la afirmații, NU în callouts separate:

✅ **CORECT:**

> „[PROBABIL] Frecvență: 5–15% din adenocarcinoame. Dacă MSI-H, pembrolizumab singur poate fi suficient. Răspuns durabil la 40–50% din pacienți."

❌ **GREȘIT:**

> [callout `info`]: „[PROBABIL] Frecvență..."

### 3.5 Limbaj direct, conversațional (regula #5)

Vorbește direct cu user-ul prin:

- „Tatăl tău" / „Familia" / „Tu (Roland)"
- „Vești bune:" / „Vești de urmărit:"
- „NU ESTE RENUNȚARE" / „Esențialul:"
- „Suni mâine" / „Citești acest document"
- „Întrebare 1:" / „Răspuns simplu: DA, ..."

NU stil academic distant („Pacientul prezintă..." / „Se observă...").

---

## 4. Structura standard a documentului

```
# COVER (titlu + atenționare R17 sus)

# CUPRINS (listă explicită capitole)

# Mesaj principal — în 30 secunde (TL;DR esențializat)

# 1. Povestea — <metaforă centrală în titlu>
   <narativă curgătoare 1-3 paragrafe + sub-secțiuni Ce a văzut X / Ce a găsit Y>

# 2. <Subiect tehnic principal> — bucată cu bucată
   ## 2.1-N <Element>
      ### NumeConcept — „Analogie"
      Analogie / Medical / Cum se face / Impact (4 paragrafe)

# 3. Întrebările tale — răspunsuri directe
   ## 3.1 „Întrebare?"
      Răspuns DA/NU + Motivare (1-3 paragrafe)

# 4. Investigațiile posibile — explicate simplu (opțional)
   ## 4.1 Procedură — „nume cu analogie"
      Analogie + Cum se face + Ce vede + Risc + Durată + Cost

# 5. <Scenarii / Plan de tratament> (opțional)
   ## SCENARIU X — combinație
      Analogie + Probabilitate [marcaj] + Diagnostic + Plan

# 6. Ce trebuie să faci TU (Roland) — concret
   ACUM (în 48h): ...
   La consult: ...
   După ce ai datele: ...

# 7. Timeline vizual (opțional)
   <tabel 2-col Data / Eveniment>

# 8. Mesajul principal — în 30 secunde (recap final)

# 9. Glossar — termeni medicali explicați simplu
   <tabel 3-col: Termen / Explicație simplă / Analogia>

# Surse citate + „Ce NU am inclus" (transparență)

# Footer R17 atenționare („NU înlocuiește consultul medical")
```

---

## 5. Reguli tehnice (pentru scripturi Python)

### Paleta DOCX (din `python-docx` cu `set_cell_bg`)

| Tip      | Fill (hex) | Border (hex) | Folosit pentru                                           |
| -------- | ---------- | ------------ | -------------------------------------------------------- |
| `info`   | D9E2F3     | 2E75B6       | Citate textuale, definiții importante (USE PARSIMONIOUS) |
| `warn`   | FCE4D6     | C05504       | Limitări, ce NU înseamnă, atenționări                    |
| `ok`     | E2EFDA     | 38761D       | Lucruri favorabile, recomandări pozitive                 |
| `urgent` | FADBD8     | C00000       | Întrebări prioritare, decizii critice                    |

**ELIMINAT v2.0:** `analogy` callouts. Analogiile merg în PROZA, nu în cutii. (Validat 28.04 prin exemplu.)

### Convenții ortografice

- Ghilimele românești tipografice: `„...”` (U+201E + U+201D)
- NU folosi ghilimele drepte ASCII `"..."` (U+0022) în textul afișat — vezi feedback U+0022
- Em dash românesc: `—` (U+2014)
- Funcția helper `q(text)` în scripturi: returnează `„text"` cu ghilimele tipografice

### Estimare lungime

- Document scurt: 25-40 KB (8-12 pagini, ~150 paragrafe)
- Document mediu: 50-70 KB (15-22 pagini, ~250 paragrafe)
- Document extins: 80-120 KB (25-35 pagini, ~400-500 paragrafe + 10-15 tabele)

---

## 6. Exemple validate

### 6.1 EXEMPLU REPREZENTATIV — `2026-04-22_explicatie_consult_oncolog_scenarii.docx` ✅

- **Locație originală:** `Dosar_Medical/rapoarte_generate/`
- **Generator:** `scripts/generate_explicatie_scenarii.py`
- **Dimensiune:** 65 KB
- **Structură:** 476 paragrafe, 12 tabele
- **Capitole:** Povestea casa veche → Ascita → Întrebările tale (4) → Investigațiile (4) → Markerii moleculari (5) → 4 scenarii combinatorii → FLOT → Imunoterapia → Nutriția → Semnale alarmă → FAQ familie (10) → Tabel sumarizat → Ce să faci tu → Timeline → Mesaj 30s → Glossar (40 termeni)
- **Validat de user:** 2026-04-28 ca standard de stil

### 6.2 EXEMPLU vechi (v1.0) — `EXPLICATIE_REZULTAT_BIOPSIE_2026-04-28.docx` ⚠️

- Folosea structura termen-cu-termen + callouts „Pe firul nostru" — superseded de v2.0
- Rămâne în proiect ca document funcțional, dar stilul v2.0 e standardul pentru viitor
- Va fi actualizat la cerere user (NU automat)

---

## 7. Versionare și update

La modificare a stilului:

1. Backup R10 acest fișier în `Dosar_Medical/arhiva/context_medical_versiuni/STIL_EXPLICATII_FAMILIE_vN_pre-<slug>_<data>.md`
2. Update versiune + data în antet
3. Log în `CHANGELOG.md` + `SESSION_LOG.md`
4. Update memoria `feedback_explicatii_familie_fir_narativ.md` în paralel
5. Update R17 (REGULI_CLAUDE_CODE.md) dacă schimbarea afectează triggerul sau workflow-ul

---

## 8. Atenționare obligatorie (R17)

Documentele generate cu acest stil NU înlocuiesc consultul medical. Stilul are scop EDUCATIV pentru familie. Diagnosticul, tratamentul și deciziile clinice aparțin EXCLUSIV medicilor curanți.

Toate documentele generate cu acest stil includ obligatoriu:

- Atenționare la început (sub titlu, în antet) — „NU înlocuiește consultul medical"
- Atenționare la final (callout `warn`) — același mesaj + responsabilitate medici curanți
- Marcaje certitudine R17 integrate fluid în text
- Secțiune „Surse citate" cu URL/citare + data
- Secțiune „Ce NU am inclus" pentru transparență
