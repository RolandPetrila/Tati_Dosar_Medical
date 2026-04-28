# STIL_EXPLICATII_FAMILIE.md — Ghid de stil pentru documente educaționale familie

**Versiune:** 1.0 | **Data:** 2026-04-28 | **Validat prin:** `EXPLICATIE_REZULTAT_BIOPSIE_2026-04-28.docx`

> **Acest fișier descrie stilul standard de scriere pentru documente medicale destinate user-ului (Roland Petrilă) sau familiei (Maria), când e cerută o abordare narativă/educațională.**
>
> NU se aplică la briefing-uri pentru medici, rapoarte tehnice, ghiduri operaționale.
>
> Document referit on-demand din memoria feedback `feedback_explicatii_familie_fir_narativ.md` și din Regula 17 (REGULI_CLAUDE_CODE.md). Nu este auto-loaded.

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
- Ghiduri operaționale acțiune-imediată: `GHID_TELEFOANE_27-04.md`, `GHID_CARDIOLOG_30-04.md`, `GHID_APEL_ONCOHELP.md`, `GHID_CONSULT_ONCOLOG.md`
- Documente cu marcaj „pentru medici" în nume sau header

---

## 2. Cele 4 principii fundamentale

### 2.1 Fir narativ unic (regula #1)

Alegi O SINGURĂ metaforă centrală adecvată subiectului și o aplici consistent pe parcurs prin callouts cu prefix „Pe firul nostru: ...".

**NU** folosi analogii distincte răzlețe (validat 2026-04-28: user a respins explicit această abordare).

#### Ghid alegere metaforă centrală (cele validate sau propuse)

| Subiect                                    | Metaforă centrală propusă                                                                                               | Status             |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Biopsie / histopatologie                   | „Casa cu o pată suspectă pe perete" — inspector ia firimituri de tencuială pentru analiză la laborator                  | ✅ Validat (28.04) |
| CT / RMN / imagistică                      | „Casa scanată cu raze X" — radiograful e fotograf cu echipament special care vede prin pereți                           | 📌 Propus          |
| Chemoterapie (FLOT, paclitaxel)            | „Antibiotic pentru celulele rebele" — dezinfectant care oprește celulele care „lucrează prea tare"                      | 📌 Propus          |
| Imunoterapie (PD-L1, checkpoint inhibitor) | „Cum ridici steagul alb al celulelor canceroase" — pacient învață sistemul imun să recunoască inamicul deghizat         | 📌 Propus          |
| Chirurgie esofagiană (esofagectomie)       | „Reconstrucție arhitectonică" — repară un perete deteriorat conectând capete sănătoase                                  | 📌 Propus          |
| Markeri tumorali (HER2, CEA, CA 19-9)      | „Antene de recunoaștere" — semnale chimice pe care celulele tumorale le emit, pe care medicul le poate detecta în sânge | 📌 Propus          |
| Stadializare TNM                           | „Scara cu 4 trepte" — T = mărime ranii pe perete, N = câte încăperi vecine afectate, M = dacă a ajuns în alte case      | 📌 Propus          |

**La dubiu pe metaforă:** întrebi user-ul O SINGURĂ DATĂ cu 2-3 propuneri scurte, apoi aplici.

### 2.2 Acoperire integrală a termenilor (regula #2)

Fiecare termen tehnic medical primește 3 elemente:

1. **Definiție directă scurtă** — ce e termenul, în limba simplă
2. **Etimologie / explicație lingvistică** unde relevant (ex: „hiper" = mult + „emie" = sânge → „pline cu sânge")
3. **Plasare în firul narativ** prin callout `analogy` cu prefix „Pe firul nostru: ..."

**NU** lăsa termeni medicali fără explicație. Validat 2026-04-28: versiunea anterioară a documentului biopsie explica doar concluzia, NU și descrierea microscopică (15+ termeni omise).

### 2.3 Structură secțiune dedicată (regula #3)

Pentru rapoarte medicale lungi (CT, biopsie, examene complexe), creezi secțiune „Anatomia raportului — fiecare mențiune, explicată" cu:

```
Secțiune mare h1: „X. Anatomia raportului — fiecare mențiune, explicată"
├── Sub-secțiune h2: „Firul narativ: <metafora centrală>"
│   └── Callout `analogy` mare — povestea de bază (8-10 rânduri)
├── Sub-secțiune h2 per element major raport (Antet, Macroscopic, Microscopic, Concluzie, ...)
│   ├── Citat textual (callout `info`)
│   ├── Pentru fiecare termen din citat:
│   │   ├── h3: „» <termenul în ghilimele românești>"
│   │   ├── Bullet-uri cu definiție + etimologie (când e cazul)
│   │   └── Callout `analogy` cu „Pe firul nostru: ..."
└── Sub-secțiune finală h2: „Pe scurt — ce înseamnă ÎMPREUNĂ" (sinteza pentru familie)
```

### 2.4 Marcaje certitudine R17 păstrate (regula #4)

Marcajele `[CERT]` / `[PROBABIL]` / `[INCERT]` / `[NEGASIT]` continuă să se aplice la afirmații medicale factuale. Firul narativ NU le înlocuiește — le însoțește.

Exemplu corect: „[CERT] Granulocitele neutrofile sunt globule albe cu nucleu multi-lobat (sursă: histologie standard, Robbins & Cotran 10th ed). Pe firul nostru: sunt 'pompierii' sistemului imun..."

---

## 3. Template structurat document tip

```markdown
# COVER (titlu + dedicare + identificare proba)

# TL;DR — În două rânduri (callout `info` cu concluzie esențializată)

# 1. Citatul textual al raportului (părțile importante, cu indicarea sursei)

# 2. Anatomia raportului — fiecare mențiune, explicată

## 2.1 Firul narativ: <metafora centrală>

<callout analogy mare cu povestea de bază>

## 2.2-N <Element major> (antet / macroscopic / microscopic / etc.)

   <citat exact din raport>
   ### » „Termenul"
      Definiție · etimologie · plasare în fir narativ
   ### » „Următorul termen"
      ...

## 2.X Sinteza descrierii (pentru familie)

<recapitulare în limba simplă>

# 3. Ce NU înseamnă acest rezultat (callouts `warn` cu mituri/false interpretări)

# 4. Ce urmează — opțiuni standard (cu pro/contra în tabele)

# 5. De ce e important (timeline + impact)

# 6. Ce facem concret (acțiuni următoare cu deadline)

# 7. Pe scurt, pentru moral (callouts `ok` + `warn` + mesaj final)

# Footer: surse + R17 atenționare + pacient destinație
```

---

## 4. Reguli tehnice (pentru scripturi Python)

### Paleta de callouts (din `python-docx` cu `set_cell_bg`)

| Tip           | Fill (hex) | Border (hex) | Folosit pentru                              |
| ------------- | ---------- | ------------ | ------------------------------------------- |
| `info`        | D9E2F3     | 2E75B6       | Citate textuale, definiții, contextualizare |
| `warn`        | FCE4D6     | C05504       | Limitări, ce NU înseamnă, atenționări       |
| `ok`          | E2EFDA     | 38761D       | Lucruri favorabile, recomandări pozitive    |
| `urgent`      | FADBD8     | C00000       | Întrebări prioritare, decizii critice       |
| **`analogy`** | **F2F2F2** | **595959**   | **„Pe firul nostru" — toate analogiile**    |

### Convenții ortografice

- Ghilimele românești tipografice: `„...”` (U+201E + U+201D)
- NU folosi ghilimele drepte ASCII `"..."` (U+0022) în textul afișat user-ului — vezi [feedback_u0022-recurring-romanian-quotes.md](memory)
- Em dash românesc: `—` (U+2014)
- Funcția helper `q(text)` în scripturi: returnează `„text"` cu ghilimele tipografice

### Pattern Python pentru callout analogy

```python
add_callout(
    doc,
    "Pe firul nostru:",
    "Imaginează-ți că <metafora aplicată> ...",
    kind="analogy",
)
```

### Estimare lungime

- Document tip: 50-90 KB (220-300 paragrafe + 35-50 callouts/tabele)
- Pagini: 18-25 (mai mult la rapoarte cu mulți termeni microscopici)

---

## 5. Exemple validate

### 5.1 EXPLICATIE_REZULTAT_BIOPSIE_2026-04-28.docx ✅

- **Generator:** `scripts/generate_explicatie_biopsie.py`
- **Dimensiune:** 52 KB
- **Structură:** 231 paragrafe, 41 callouts
- **Fir narativ:** „casa cu o pată suspectă pe perete"
- **Termeni acoperiți:** antet (9 elemente) + cod diagnostic + examen histopatologic + diagnostic clinic + piesa A + 4 termeni macroscopici + 13 termeni microscopici + concluzie (4 sub-părți) + nota laboratorului + 2 medici semnatari
- **Validat de user:** 2026-04-28 (varianta finală cu fir narativ unic + acoperire integrală)

---

## 6. Versionare și update

La modificare a stilului:

1. Backup R10 acest fișier în `Dosar_Medical/arhiva/context_medical_versiuni/`
2. Update versiune + data în antet
3. Log în `CHANGELOG.md` + `SESSION_LOG.md`
4. Update memoria `feedback_explicatii_familie_fir_narativ.md` în paralel
5. Update R17 (REGULI_CLAUDE_CODE.md) dacă schimbarea afectează triggerul

---

## 7. Atenționare obligatorie (R17)

Documentele generate cu acest stil NU înlocuiesc consultul medical. Stilul are scop EDUCATIV pentru familie. Diagnosticul, tratamentul și deciziile clinice aparțin EXCLUSIV medicilor curanți.

Toate documentele generate cu acest stil includ obligatoriu o secțiune „Atenționare" la final (callout `warn`) cu mesajul standard.
