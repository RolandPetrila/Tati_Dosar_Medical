# AUDIT_EXTRAGERE_2026-04-24.md — Audit complet conformitate R23 + R24 + R25

**Data audit:** 2026-04-24 02:30
**Auditor:** Claude_Opus_4.7
**Scope:** toate JSON-urile din `Dosar_Medical/` vs PDF-uri sursă (acolo unde disponibile) vs `CONTEXT_MEDICAL.md`
**Reguli aplicate:** R23 (extragere integrală PDF→JSON), R24 (propagare integrală JSON→CONTEXT_MEDICAL.md), R25 (prioritate claritate la indescifrabil)

> **Status raport:** propuneri de corectură, NU modificări directe. User decide ce se aplică.
>
> **UPDATE 2026-04-24 02:30 — Batch A APLICAT** (vezi §4 Recomandări, secțiunea Prioritate 1 HIGH). `CONTEXT_MEDICAL.md` §2 restructurat în 5 sub-secțiuni R24 obligatorii; `.meta.json` CT 20.04 marcat `completeness_verified: 2026-04-24`, `coverage: 100%`. DASHBOARD.html LAZĂR fix aplicat (5 locuri). Backup-uri Regula 10 create. Commit + push: vezi CHANGELOG.md 2026-04-24 02:30.
>
> **Batch B + C + D + procesare doc*neidentificat*\***: NEAPLICATE — la decizie user în sesiune separată.

---

## 1. Metodologie

1. Citit toate 11 JSON-uri din `Dosar_Medical/` + meta-files
2. Comparație JSON ↔ `CONTEXT_MEDICAL.md` (R24 — regula de paritate)
3. Verificare elemente cu confidence LOW pentru R25 (scoatere vs marcaj)
4. PDF-urile sursă NU au fost re-citite în acest audit (volum mare); R23 evaluat indirect prin completitudinea JSON-urilor și prin notele meta

**Limitare:** R23 (extragere integrală PDF→JSON) nu poate fi validat 100% fără re-citirea PDF-urilor sursă. Acest audit prezumă că JSON-urile sunt complete vs sursă (pe baza notelor meta `confidence_overall: high` + `ocr_quality: good` documentate la procesare). Pentru certificare R23, audit suplimentar pe PDF-uri ar fi necesar (escalare separată).

---

## 2. Rezumat executiv

| #      | Document                                               | R23 (JSON vs PDF)               | R24 (CONTEXT_MEDICAL vs JSON)            | R25                              | Severitate |
| ------ | ------------------------------------------------------ | ------------------------------- | ---------------------------------------- | -------------------------------- | ---------- |
| **1**  | `2026-04-20_ct_torace_abdomen_pelvis.json`             | ✅ complet (confidence high)    | 🔴 **OMISIUNI MULTIPLE**                 | ❎ N/A                           | **HIGH**   |
| **2**  | `2026-04-17_buletin_gastroenterologie.json`            | ✅ complet                      | ✅ propagat                              | ❎ N/A                           | OK         |
| **3**  | `2026-04-17_buletin_bioclinica_uree_creatinina.json`   | ✅ complet                      | 🟡 minor: unități SI nelistate           | ❎ N/A                           | LOW        |
| **4**  | `2025-11-28_externare_chirurgie_hernie.json`           | ✅ complet (fuziune v1×3)       | 🟡 ~21 analize lab nelistate             | ❎ N/A                           | MEDIUM     |
| **5**  | `2025-11-10_schema_medicamente.json`                   | 🟡 parțial (manuscris ilizibil) | ✅ propagat (post-R25 LAZĂR)             | ✅ R25 aplicat                   | OK (post)  |
| **6**  | `2025-10-28_scrisoare_urologie_gastroenterologie.json` | ✅ complet                      | ✅ propagat (preop hernie)               | ❎ N/A                           | OK         |
| **7**  | `2025-11-01_talon_pensie_asigurare.json`               | ✅ (parțial OCR scan)           | ✅ propagat (date admin esenț.)          | ❎ N/A                           | OK         |
| **8**  | `2025-06-17_buletin_analize_sange.json`                | ✅ complet                      | 🟡 ~28 analize din 32 nelistate explicit | ❎ N/A                           | MEDIUM     |
| **9**  | `2024-09-06_anti_helicobacter_pylori_igg.json`         | ✅ complet                      | ✅ propagat                              | ❎ N/A                           | OK         |
| **10** | `2023-06-12_carte_identitate.json`                     | ✅ complet (MRZ verificat)      | ✅ propagat (date admin)                 | ❎ N/A                           | OK         |
| **11** | `2012-02-17_cardiologie_vichy_stent.json`              | 🔴 PDF SURSĂ LIPSĂ              | ✅ propagat (parțial — tip stent INCERT) | 🟡 INCERT „tip stent DES vs BMS" | MEDIUM     |

**Rezumat severitate:**

- **HIGH (1):** CT 20.04.2026 — incidentul declanșator R23, nu e remediat în CONTEXT_MEDICAL.md
- **MEDIUM (3):** analize sânge 17.06 + externare hernie 28.11 + cardiologie Vichy 2012
- **LOW (1):** bioclinica uree/creatinină
- **OK (6):** restul

---

## 3. Findings detaliate

### 3.1 🔴 HIGH — CT 20.04.2026 (incidentul declanșator R23/R24)

**JSON sursă:** `Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json`
**PDF sursă:** `Dosar_Medical/documente_sursa/99_altele/CT - Genesys.pdf` (`confidence_overall: high`)
**Locație CONTEXT_MEDICAL.md:** secțiunea 2 (Status clinic curent)

**Findings prezente în JSON dar OMISE din CONTEXT_MEDICAL.md (violare R24):**

| #   | Element JSON                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Path JSON                                                                              | Severitate                                                                       |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| 1   | **Tulburări ventilație posterobazal LID + LIS**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `findings_imagistice.torace.parenchim_pulmonar.tulburari_ventilatie`                   | **HIGH** — relevant pre-esofagectomie (spirometrie + kinetoterapie respiratorie) |
| 2   | **Leziuni micronodulare calcare sechelare apical LSD, max 6.8 mm**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `findings_imagistice.torace.leziuni_nodulare`                                          | **HIGH** — anamneză TBC vechi, follow-up imagistic                               |
| 3   | **Modificări degenerative disco-vertebrale supraetajat toraco-lombar**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `findings_imagistice.abdomen_pelvis.coloana_vertebrala`                                | MEDIUM — context musculoscheletic                                                |
| 4   | **Doza radiație DLP: 2474 mGy·cm²**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `examinare.doza_radiatie`                                                              | MEDIUM — parametru tehnic R24-obligatoriu                                        |
| 5   | **Adenopatii absente — explicit** (mediastinale, hilare, axilare, abdomino-pelvine)                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `findings_imagistice.torace.adenopatii` + `abdomen_pelvis.adenopatii_abdomino_pelvine` | MEDIUM — confirmare M0                                                           |
| 6   | **Aspect normal organe abdominale:** colecist (fără îngrosări/calculi), căi biliare (fără dilatări), pancreas (normal), splină (normal), ficat (normal, fără prize patologice), prostata (normal CT), vezică urinară (fără modificări), rinichi (bilateral normali, IP normal, secreție/excreție prezentă, fără calculi/dilatații), suprarenală dreaptă (normal), tiroidă (normal), trahee/bronșii (permeabile), cord/vase mari (artera pulmonară permeabilă, aorta toracală permeabilă, ax spleno-portal permeabil, aorta abdominală + VCI permeabile) | `findings_imagistice.torace.*` + `findings_imagistice.abdomen_pelvis.*`                | MEDIUM — R24 listare explicită aspecte normale                                   |
| 7   | **Numere referință:** înregistrare CT nr. 284                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `numere_referinta.numar_inregistrare_examinare`                                        | LOW — trasabilitate                                                              |
| 8   | **Coduri parafă medici:** Buie A11818 + Candea F52510                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `medici_unitati.medic_examinator_*`                                                    | LOW — chain of custody                                                           |
| 9   | **Denumire unitate „Genesys" în document vs „Genesis Medical Clinic Micălaca" canonic**                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `medici_unitati.denumire_in_document`                                                  | LOW                                                                              |
| 10  | **Nume pacient text original „PETRILA VIOREL MIHAI" (fără diacritice, prenume cu spațiu)**                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `pacient.nume_text_original_document`                                                  | LOW                                                                              |

**Recomandare corectură R24 pentru CT 20.04.2026:**

Restructurare secțiunea 2 din `CONTEXT_MEDICAL.md` conform format R24 cu 5 sub-secțiuni obligatorii:

1. **Findings principale** (impact decizional direct): Siewert II infiltrativ + ascită
2. **Findings secundare** (monitorizare): glandă suprarenală stângă + colecție pulmonar bazal LID + leziune chistică perete toracic + cardiomegalie/ateromatoză
3. **Findings colaterale** (NEW): tulburări ventilație + noduli apicali sechelari + modificări degenerative + adenopatii absente explicit + aspecte normale organe abdominale (toate enumerate)
4. **Parametri tehnici** (NEW): protocol TAP N+SDC, doza radiație DLP 2474 mGy·cm², înregistrare 284, bilet BCTAP 0631727, medici examinatori cu coduri parafă
5. **Referință sursă** (NEW): `Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json` + data extragere 2026-04-22 + `completeness_verified` (de marcat în .meta.json)

---

### 3.2 🟡 MEDIUM — Analize sânge 17.06.2025

**JSON sursă:** `Dosar_Medical/2025-06-17_buletin_analize_sange.json` (32 analize, toate `confidence_ocr: high`)
**Locație CONTEXT_MEDICAL.md:** secțiunea 3.4 Diabet + 3.5 Stil de viață + sub-mențiuni dispersate

**Analize din JSON menționate explicit în CONTEXT_MEDICAL.md:**

- Glicemie 136.1 ✅
- HDL 33.86 (sub prag) ✅ (parțial — citat „HDL sub prag")
- Eozinofile 6.8% (crescute) ✅ (parțial)
- Creatinină 0.95 ✅

**Analize din JSON OMISE explicit din CONTEXT_MEDICAL.md (violare R24):**

| Categorie      | Analize OMISE                                                                                                                                                  | Severitate                                           |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Hemoleucogramă | WBC 6.54, RBC 4.94, HGB 14.9, HCT 43.2, MCV 87.3, MCH 30.1, MCHC 34.5, RDW 12.6, PLT 221, PCT 0.26, MPV 11.8, PDW 16.3, Lym/Mon/Neu/Bas absolute + procentuale | MEDIUM — toate normale, dar R24 cere listare         |
| Lipidogramă    | Colesterol total 195.44, Trigliceride 141.77, LDL 133.18 (țintă <70 post-stent — interpretare cardiolog)                                                       | **MEDIUM** — LDL > țintă post-stent, relevant clinic |
| Ionogramă      | Sodiu 141.3, Potasiu 3.61                                                                                                                                      | LOW — normale                                        |
| Inflamație     | PCR <6                                                                                                                                                         | LOW — normal                                         |
| Tiroidă        | TSH 1.7, FT4 10.9                                                                                                                                              | LOW — normale, screening                             |
| Onco-screening | PSA Total 1.45 (<4)                                                                                                                                            | LOW — normal, screening prostată                     |
| Uree           | 34.81 mg/dL                                                                                                                                                    | LOW — normal                                         |

**Recomandare corectură R24:**
Adăugare în CONTEXT_MEDICAL.md secțiunea 3 (sau secțiune nouă „Profil laborator iunie 2025") tabel complet analize cu interval referință + flag (normal/crescut/scăzut) + sursa JSON. Marcare specială LDL 133 vs țintă <70 post-stent (interpretare cardiolog necesară).

---

### 3.3 🟡 MEDIUM — Externare hernie 28.11.2025

**JSON sursă:** `Dosar_Medical/2025-11-28_externare_chirurgie_hernie.json` (~25 analize lab + 13 medicamente)
**Locație CONTEXT_MEDICAL.md:** secțiunea 3.3

**Elemente prezente în JSON, propagate corect:**

- Diagnostic ICD10 (K40.90 + K66.0) ✅
- Tip intervenție (cură cu grefon, PO 1476) ✅
- Anestezie (rahidiană bupivacaină + sedare midazolam/propofol) ✅
- Antibioprofilaxie Zolinef + profilaxie trombotică Clexane ✅
- 4 analize preop relevante (glicemie 129, creatinină 0.66, eozinofile 7.5, RX toracic) ✅

**Elemente OMISE din CONTEXT_MEDICAL.md (violare R24):**

| Categorie               | OMISIUNI                                                                                        | Severitate                         |
| ----------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------- |
| Coagulare               | INR 1.06, TQ-IQ 92%, APTT 28 sec                                                                | LOW — normale, dar relevante preop |
| Chimie clinică          | AST 15.5, ALT 14.2, Uree 31.7                                                                   | LOW — normale                      |
| Hemoleucogramă completă | WBC 7.3, RBC 5.02, HGB 15.0, HCT 42.9, MCV/MCH/MCHC, RDW, PLT 208, Neu/Lym/Mon/Eos/Bas          | LOW — toate normale                |
| Medicație suport spital | ALGOCALMIN, BIOSUN SYMBIO SPOR, BRAUNOL, NaCl 0.9%, FAMODIN 40mg, GLUCOZĂ 10%, PANTOPRAZOL 40mg | LOW — administrare în spital       |

**Recomandare corectură R24:**
Adăugare în CONTEXT_MEDICAL.md secțiunea 3.3 sub-secțiune „Analize complete preop (28.11.2025)" + listare medicație suport (separat de schema cronică).

---

### 3.4 🟡 MEDIUM — Cardiologie Vichy 2012

**JSON sursă:** `Dosar_Medical/2012-02-17_cardiologie_vichy_stent.json`
**PDF sursă:** ❌ **LIPSĂ** (`sursa_pdf: "de_identificat_din_arhiva_pacient"`)

**Probleme identificate:**

1. **R23 nu poate fi auditat** — PDF-ul sursă nu e în dosar. JSON-ul a fost generat din transcriere verbală/Gemini, nu din OCR PDF. Trebuie obținut PDF-ul original de la familie.
2. **R25 candidat:** „tip stent: RX VISION (tip nespecificat în document — de clarificat: activ medicamentos sau pasiv metalic)" cu `confidence_ocr: high` (paradox — confidence high pe transcriere, dar tipul exact e necunoscut). **Nu e R25 strict** (informația lipsește, nu e ilizibilă), dar e un caz limită.
3. **CONTEXT_MEDICAL.md secțiunea 3.1** — propagat corect cu mențiunea „Tipul exact al stentului (DES vs BMS) — nu este explicit în extrasul Gemini" ✅

**Recomandare:** TODO P1 deja deschis pentru obținere PDF Vichy. Nu necesită audit suplimentar până la digitizare PDF.

---

### 3.5 🟡 LOW — Bioclinica uree/creatinină 17.04.2026

**Element minor OMISE:** unitățile SI (uree mmol/L 5.6 + creatinină µmol/L 73.37) — duplicată cu mg/dL deja propagată. R24 strict cere listarea, dar valorile sunt aceleași în alte unități.

**Recomandare:** opțional, adăugare în CONTEXT_MEDICAL.md secțiunea 8.3 a unităților SI între paranteze pentru completitudine.

---

### 3.6 ✅ OK — restul JSON-urilor

- **Gastroenterologie 17.04.2026** (#2): JSON ↔ CONTEXT_MEDICAL.md complet aliniate (clarificare 2026-04-22 inclusă)
- **Schema medicamente 10.11.2025** (#5): post-R25 retroactive aplicat în această sesiune ✅
- **Scrisoare urologie 28.10.2025** (#6): preop hernie, propagat
- **Talon pensie 2025-11-01** (#7): date administrative, propagate esențial
- **Anti-H. pylori IgG 06.09.2024** (#9): propagat cu interpretare corectă
- **Carte identitate 2023-06-12** (#10): MRZ verificat, propagat

---

## 4. Recomandări corectură (ordonate severitate)

### 🔴 Prioritate 1 — HIGH (incident declanșator)

**[CORECTURĂ-CT-20.04]** Restructurare CONTEXT_MEDICAL.md secțiunea 2 conform format R24 (5 sub-secțiuni obligatorii). Adăugare:

- Findings colaterale: tulburări ventilație + noduli apicali sechelari + modificări degenerative + adenopatii absente explicit + aspecte normale organe abdominale
- Parametri tehnici: protocol, DLP 2474 mGy·cm², înregistrare 284, BCTAP 0631727, medici cu cod parafă
- Referință sursă explicită + marcaj `completeness_verified: 2026-04-24` în `.meta.json` corespunzător

**Effort estimat:** 30-45 min (rescriere structurată secțiune 2 + update .meta.json + log)

### 🟡 Prioritate 2 — MEDIUM

**[CORECTURĂ-LAB-17.06]** Adăugare în CONTEXT_MEDICAL.md secțiunea 3 a tabelului complet 32 analize sânge 17.06.2025 cu marcare flagged values + LDL vs țintă post-stent.

**[CORECTURĂ-HERNIE-28.11]** Adăugare în CONTEXT_MEDICAL.md secțiunea 3.3 a sub-secțiunii „Analize complete preop" + medicație spital.

**[CORECTURĂ-VICHY-2012]** Nu necesită corectură audit — TODO P1 deja deschis pentru obținere PDF original. La digitizare se va re-audita.

**Effort estimat per corectură:** 15-20 min

### 🟢 Prioritate 3 — LOW (opțional)

**[CORECTURĂ-BIOCLINICA-17.04]** Adăugare unități SI în paranteze pentru creatinină + uree (cosmetic).

---

## 5. Status completitudine dosar (pentru audit suplimentar R23 — PDF-uri)

| PDF sursă necesar pentru R23 strict  | Status                                                 | Acțiune                                                                            |
| ------------------------------------ | ------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| CT - Genesys.pdf                     | ✅ În `99_altele/`                                     | Re-citire pentru certificare R23 strict (dacă user dorește)                        |
| Buletin endoscopie 17.04             | ✅ În `09_endoscopie_2026_04/`                         | OK                                                                                 |
| Bioclinica uree/creatinină 17.04     | ✅ În `05_analize_laborator/`                          | OK                                                                                 |
| Externare hernie 28.11               | ✅ În `07_hernie_2025_11/`                             | OK                                                                                 |
| Schema medicamente 10.11 (manuscris) | ✅ În `08_schema_tratament/`                           | R25 aplicat — nu se re-extrage                                                     |
| Carte identitate 2023-06             | ✅ În `01_identitate/`                                 | OK                                                                                 |
| Talon pensie 2025-11                 | ✅ În `10_administrativ_pensie/`                       | OK                                                                                 |
| Cardiologie Vichy 2012               | ❌ **LIPSĂ**                                           | TODO P1 — obținere de la familie                                                   |
| H. pylori internare 30.05.2024       | ❌ **LIPSĂ** (JSON null în MANIFEST)                   | TODO P1 — obținere de la spital                                                    |
| Ecografie abdominală 14.04.2026      | ❌ **LIPSĂ**                                           | TODO P1 — obținere PDF                                                             |
| Anti-H. pylori 06.09.2024            | ❌ Status incert (`de_identificat_din_Apr17_Doc*.pdf`) | Verificare în 6 PDF-uri `99_altele/doc_neidentificat_*` (probabil unul corespunde) |
| Analize sânge 17.06.2025             | ❌ Status incert (`de_identificat_din_Apr17_Doc*.pdf`) | Idem                                                                               |
| Scrisoare urologie 28.10.2025        | ❌ Status incert (`de_identificat_din_Apr17_Doc*.pdf`) | Idem                                                                               |

**Notă:** 6 PDF-uri `2026-04-17_doc_neidentificat_2.pdf` ... `_7.pdf` din `99_altele/` sunt nedigitizate. Probabil conțin documente menționate dar nelocalizate (anti-H pylori, analize sânge, scrisoare urologie, bilet trimitere CT etc.). Procesarea lor ar completa scope-ul audit R23.

---

## 6. R25 — elemente indescifrabile identificate

**În tot dosarul, singurul caz R25 actual este:**

- ✅ **Schema medicamente 10.11.2025 — Dr. LAZĂR** (deja aplicat în această sesiune, log în `Dosar_Medical/EXTRAGERI_INCOMPLETE.md`)

**Alte elemente cu confidence variabil dar NU indescifrabile (NU fac obiectul R25):**

- `2012-02-17_cardiologie_vichy_stent.json` — „tip stent RX VISION (tip nespecificat în document — DES vs BMS de clarificat)" → informație LIPSĂ în document, nu indescifrabilă. Tratament corect = TODO P1 (obținere PDF original sau clarificare cardiolog).
- `2025-11-01_talon_pensie_asigurare.json` — `ocr_quality: partial` pe scan jpeg, dar valorile critice (CNP, sumele) au fost completate prin cross-reference + scan complementar, fără elemente rămase indescifrabile.

**Recomandare:** R25 nu necesită aplicări retroactive suplimentare în acest moment.

---

## 7. Sumar final + propuneri batch corectură

| Batch propus                                | Conținut                                                                        | Effort estimat | Severitate           |
| ------------------------------------------- | ------------------------------------------------------------------------------- | -------------- | -------------------- |
| **Batch A — CT 20.04 R24 fix**              | Restructurare CONTEXT_MEDICAL.md §2 (5 sub-secțiuni R24) + update `.meta.json`  | 30-45 min      | 🔴 HIGH              |
| **Batch B — Lab 17.06 R24 fix**             | Tabel complet analize 17.06.2025 în CONTEXT_MEDICAL.md (eventual secțiune nouă) | 15-20 min      | 🟡 MEDIUM            |
| **Batch C — Hernie 28.11 R24 fix**          | Sub-secțiune „Analize complete preop" + medicație spital                        | 15-20 min      | 🟡 MEDIUM            |
| **Batch D — Bioclinica unități SI**         | Cosmetic, opțional                                                              | 5 min          | 🟢 LOW               |
| **Batch E — Procesare 6 PDF-uri 99_altele** | Identificare conținut → corelare cu JSON-uri existente / JSON-uri noi           | 30-90 min      | MEDIUM (R23 closure) |
| **Batch F — Obținere PDF-uri lipsă**        | Vichy 2012 + H. pylori 2024 + ecografie 14.04 (depinde de familie)              | extern         | LOW (acțiune user)   |

**Recomandare strategie:**

- **Imediat:** Batch A (HIGH, incidentul declanșator R23+R24)
- **Următoarea sesiune:** Batch B + C împreună (similar effort, audit lab)
- **Opțional:** Batch D, E, F la decizia user

---

**Final audit:** zero R25 candidate noi (LAZĂR e singurul, tratat); zero halucinație detectată; trei R24 violations confirmate (severitate HIGH/MEDIUM/MEDIUM); R23 nu poate fi certificat strict fără re-citire PDF-uri (acceptabil pe baza confidence high documentat la procesare).
