# CONTEXT_MEDICAL.md — Starea medicală actuală

**Fișier central de stare.** Se actualizează la fiecare informație medicală nouă. Ultima modificare trebuie reflectată în antetul de mai jos și în `CHANGELOG.md`.

---

**Ultima actualizare:** 18 aprilie 2026 (reconciliere cu JSON-uri Dosar_Medical/)
**Responsabil dosar:** Roland Petrilă (fiul pacientului)
**Versiune structură:** 1.1 (post-reconciliere Claude_Opus_4.7)
**Versiune anterioară arhivată:** `Dosar_Medical/arhiva/context_medical_versiuni/CONTEXT_MEDICAL_v1_2026-04-17.md`

---

## 1. Date pacient

| Câmp                | Valoare                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| Nume complet        | Petrilă Viorel-Mihai                                                                           |
| Data nașterii       | 18 mai 1959                                                                                    |
| Vârsta              | 66 ani (împlinește 67 în mai 2026)                                                             |
| Sex                 | Masculin                                                                                       |
| CNP                 | 1590518024486                                                                                  |
| Serie / Nr. CI      | ZR 089382 (emisă 12.06.2023 de SPCLEP Nădlac, valabilă până la 03.08.2031)                     |
| Locul nașterii      | Sat Igriș (Com. Sânpetru Mare), Jud. Timiș                                                     |
| Domiciliu actual    | Str. Vasile Goldiș nr. 42, oraș Nădlac, jud. Arad                                              |
| Categorie asigurare | Pensionar — CJP Arad (CJP 021), dosar pensie 42/355336, total drepturi 3166 lei/lună (11/2025) |
| Grupa sanguină      | De completat                                                                                   |
| Greutate            | De completat                                                                                   |
| Înălțime            | De completat                                                                                   |

**Sursa datelor administrative:** `Dosar_Medical/2023-06-12_carte_identitate.json` + `Dosar_Medical/2025-11-01_talon_pensie_asigurare.json`.

---

## 2. Status clinic curent

**Suspiciune clinică principală:** Proces proliferativ esofagian (cod 95, bilet BCTAP 0631727 din 17.04.2026).

**Context:** Leziune esofagiană identificată la endoscopie digestivă superioară efectuată la Genesis Medical Clinic Arad, de Dr. Noufal Abdul Vahab (medic primar gastroenterologie). S-a prelevat biopsie. Medicul curant a emis bilet de trimitere către CT de stadializare (torace + abdomen + pelvis cu substanță de contrast), cu prioritate URGENȚĂ.

**Natura leziunii:** neclarificată. Rezultatul biopsiei va preciza dacă leziunea este benignă, premalignă sau malignă.

**Extensia bolii:** neclarificată. Rezultatul CT va preciza dimensiunea, invazia locală, implicarea ganglionilor, eventualele metastaze.

**Acțiuni în curs:**

- Programare și efectuare CT la Genesis Medical Clinic Micălaca (urgent)
- Așteptarea rezultatului biopsiei (estimat 7–14 zile lucrătoare)
- Consult oncolog digestiv după primirea ambelor rezultate

---

## 3. Antecedente medicale personale

### Boală cardiacă ischemică cu stent (februarie 2012)

**Status clinic:** Sindrom coronarian acut ST+ (STEMI) antero-septo-apical pe stenoză a arterei interventriculare anterioare proximale și mijlocii.

**Tratament efectuat:**

- Fibrinoliză cu tenecteplază (metaliză)
- Tratament adjuvant: PLAVIX (clopidogrel) + ASPEGIC (aspirină) + LOVENOX (enoxaparină)
- Coronarografie + angioplastie cu **stent RX VISION 3.5 × 28 mm pe IVA** (19.02.2012)

**Spital:** Vichy, Franța (denumire exactă de confirmat din documentul original).

**Consecință practică:** necesită antiagregare plachetară pe termen lung (Aspenter 75 mg, confirmat prin schema din 10.11.2025).

**Date de completat:**

- Tipul exact al stentului (activ medicamentos DES vs. pasiv metalic BMS) — nu este explicit în extrasul Gemini
- Cardiolog curant din România după repatriere, ultimul control
- Date CEH (consult coronarografic) repetat, dacă există

**Sursă:** `Dosar_Medical/2012-02-17_cardiologie_vichy_stent.json` (în așteptarea scanului PDF original).

### Infecție cu Helicobacter pylori (30 mai 2024)

Episod acut cu simptome digestive, internare pentru investigații. Diagnosticat cu infecție H. pylori. Tratament cu antibiotice și inhibitor de pompă de protoni efectuat cu succes. Fără recidivă simptomatică până la momentul actual.

**Serologie de control (06.09.2024):** Anti-H. pylori IgG **>100 U/mL** (referință 0-20 U/mL) — semnifică expunere anterioară confirmată.

**Important:** Serologia IgG **nu diferențiază** infecție activă de antecedentă (anticorpii persistă luni/ani post-eradicare). Pentru a valida eradicarea ar trebui efectuat: (a) antigen fecal H. pylori SAU (b) test respirator cu uree C13. Nu este clar dacă un astfel de test a fost făcut. De clarificat cu medicul de familie sau gastroenterologul.

**Date de completat:**

- Spitalul unde a fost internat (mai 2024)
- Schema exactă de tratament administrată (antibioticele + IPP)
- Test de control post-eradicare (antigen fecal sau UBT) — NU serologie

**Sursă:** `Dosar_Medical/2024-09-06_anti_helicobacter_pylori_igg.json` + CONTEXT_MEDICAL v1 (raportat verbal de Roland pentru episodul din mai).

### Hernie operată (28 noiembrie 2025)

**Tip hernie:** **inghinală dreaptă** (K40.90) + **aderențe peritoneale** (K66.0). Confirmat prin scrisoarea preoperatorie din 28.10.2025 și biletul de externare din 28.11.2025.

**NU a fost hernie hiatală** — nu există legătură anatomică directă cu patologia esofagiană actuală.

**Secția:** Chirurgie Generală II (unitate neidentificată explicit în extrasul digitizat).

**Tip intervenție:** cură chirurgicală cu grefon (plasă sintetică), conform procedurii PO nr. 1476 din 26.11.2025.

**Anestezie:** rahidiană (bupivacaină spinal heavy 5 mg/mL) + sedare (midazolam + propofol).

**Antibioprofilaxie:** Zolinef (cefazolin) 1 g. **Profilaxie trombotică:** Clexane (enoxaparină) 60 mg s.c.

**Indicații asociate preoperator (28.10.2025) — de confirmat dacă s-au efectuat concomitent:**

- Cură chirurgicală hidrocel drept (N43.3)
- Excizie chiste epididimare bilaterale (N50.89)

**Analize preop relevante (28.11.2025):** glicemie 129 mg/dL (↑), creatinină 0.66 mg/dL (normală — OK pentru CT cu contrast), eozinofile 7.5% (↑), radiografie toracică PA/Cord fără leziuni active.

**Sursă:** `Dosar_Medical/2025-11-28_externare_chirurgie_hernie.json` (fuziune 3 JSON-uri Gemini v1) + `Dosar_Medical/2025-10-28_scrisoare_urologie_gastroenterologie.json`.

### Hernie operată anterior (dată neclarificată)

A mai avut o intervenție pentru hernie în trecut, cu dată necunoscută momentan. De identificat din documente.

### Diabet zaharat tip 2 (tratat cu Jamesi)

Diabet zaharat confirmat, tratament actual: **Jamesi 50 mg / 1000 mg** (sitagliptin + metformin), 1-0-1 (dimineața și seara). Schema curentă datată 10.11.2025.

**Monitorizare glicemică:**

- 2025-06-17: glicemie à jeun 136.1 mg/dL (↑, ref 70-115)
- 2025-11-28: glicemie 129 mg/dL (↑) — internare chirurgicală

**Ambele valori peste 115 mg/dL** — compatibile cu diabet cunoscut. Controlul ar necesita HbA1c recent.

**Date de completat:**

- Anul diagnosticării inițiale
- Valoarea HbA1c recentă (nu există în dosarul digitizat)
- Evaluare complicații (fund de ochi — retinopatie; fibră neurologică — neuropatie; albumină urinară — nefropatie)

**CRITIC pre-CT cu contrast:** componenta metformin din Jamesi se oprește 48h înainte, pentru prevenirea acidozei lactice.

### Hipertensiune arterială

Confirmat prin tratament antihipertensiv triplu:

- **Triplixam 10/2.5/5 mg** (perindopril + indapamidă + amlodipină), 1-0-0 dimineața
- **Concor 5 mg** (fumarat de bisoprolol), 1-0-0 dimineața — beta-blocant cu dublu rol (cardioprotecție post-stent + control frecvență)

**Status:** controlat medicamentos. Valori TA uzuale — de documentat cu jurnal simptome.

**Sursă:** `Dosar_Medical/2025-11-10_schema_medicamente.json`.

---

## 4. Medicație zilnică

Schema datată **10 noiembrie 2025**, prescrisă de Dr. LAZĂR [nume parțial ilizibil pe manuscris — de identificat].

| Medicament                                                     | Indicație                                                | Doză                  | Ritm                  | Note                                                                      |
| -------------------------------------------------------------- | -------------------------------------------------------- | --------------------- | --------------------- | ------------------------------------------------------------------------- |
| **Jamesi** (sitagliptin + clorhidrat de metformin)             | Diabet zaharat tip 2                                     | 50 mg / 1000 mg       | 1-0-1 (dim. și seara) | **CRITIC**: componenta metformin se oprește 48h înainte de CT cu contrast |
| **Aspenter** (acid acetilsalicilic)                            | Antiagregant post-stent coronarian 2012                  | 75 mg                 | 0-1-0 (prânz)         | NU se oprește pentru CT                                                   |
| **Concor** (fumarat de bisoprolol)                             | Beta-blocant (cardioprotecție + HTA + control frecvență) | 5 mg                  | 1-0-0 (dimineața)     | Nu se oprește pentru CT                                                   |
| **Triplixam** (perindopril arginine + indapamidă + amlodipină) | Antihipertensiv combinație triplă                        | 10 mg / 2.5 mg / 5 mg | 1-0-0 (dimineața)     | Nu se oprește pentru CT                                                   |

**Notă:** manuscrisul conținea o a 5-a recomandare tăiată cu marker albastru (anulată).

**Suplimente alimentare:** de verificat cu familia.

**Sursă:** `Dosar_Medical/2025-11-10_schema_medicamente.json` (manuscris + fotografii cutii).

---

## 5. Stil de viață și factori de risc

| Factor                           | Valoare                                                                          | Relevanță                                                   |
| -------------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Fumat                            | Fost fumător (1977 – 2012), aproximativ 35 de ani de fumat, 14 ani de abstinență | Factor de risc persistent pentru carcinom scuamos esofagian |
| Alcool                           | Rar, ocazional, cantități mici                                                   | Risc scăzut                                                 |
| Activitate fizică uzuală         | Persoană activă, energică (în mod obișnuit)                                      | Stare generală bună până la debutul simptomelor actuale     |
| Antecedente oncologice familiale | Niciunul raportat                                                                | —                                                           |

---

## 6. Simptomatologie curentă

### Simptome prezente (apărute în ultimele 2-3 săptămâni — atipice pentru pacient)

| Simptom                  | Detalii                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Oboseală marcată         | Scădere evidentă a energiei, stări prelungite de odihnă în pat                                                |
| Somnolență crescută      | Dorința de a dormi mai mult decât normal                                                                      |
| Scăderea apetitului      | Apetit diminuat, fără aversiune specifică raportată                                                           |
| Senzație de „nod în gât” | Intermitent, după mese, fără durere la înghițire și fără necesitatea de a bea apă pentru a împinge alimentele |
| Reflux / arsuri          | Recent reapărute (după perioada de remisiune post-tratament H. pylori din 2024)                               |

### Simptome ABSENTE (element clinic pozitiv)

- Scădere ponderală — greutatea este stabilă în ultimul an
- Disfagie progresivă clasică (solide → lichide)
- Regurgitații cu alimente nedigerate
- Hematemeză (vărsături cu sânge)
- Melenă (scaune negre ca smoala)
- Răgușeală persistentă
- Tuse la înghițirea lichidelor
- Noduli palpabili la gât sau supraclavicular
- Durere toracică persistentă

---

## 7. Investigații efectuate

### 7.1 Ecografie abdominală (14 aprilie 2026)

**Rezultat:** fără modificări vizibile.
**Notă:** ecografia nu vizualizează bine esofagul (aerul blochează ultrasunetele) — rezultat normal nu exclude patologie esofagiană.

### 7.2 Endoscopie digestivă superioară (17 aprilie 2026)

**Unitate:** Genesis Medical Clinic Arad
**Medic:** Dr. Noufal Abdul Vahab, medic primar gastroenterologie
**Rezultat principal:** leziune la nivelul esofagului, descrisă în bilet drept „proces proliferativ esofagian”.
**Acțiune:** biopsie prelevată, trimisă la anatomopatologie.
**Buletin endoscopie:** de obținut și arhivat în `documente_sursa/05_endoscopie_aprilie_2026/`.

### 7.3 Colonoscopie (17 aprilie 2026)

Efectuată concomitent cu endoscopia la Genesis Medical Clinic Arad (Dr. Noufal Abdul Vahab).

**Rezultat:**

- **Polip colon descendent** (K63.5) — recomandare: revine pentru polipectomie
- **Boală hemoroidală** — hemoroizi interni grad II (K64.1)

**Sursă:** `Dosar_Medical/2026-04-17_buletin_gastroenterologie.json`.

### 7.4 Biopsie esofagiană (în lucru)

**Status:** la laboratorul de anatomopatologie.
**Timp estimat:** 7-14 zile lucrătoare.
**Importanță:** diagnostic de certitudine.

---

## 8. Investigații programate / în așteptare

### 8.1 CT torace + abdomen + pelvis cu contrast (urgent)

**Bilet trimitere:** BCTAP nr. 0631727 (17.04.2026)
**Unitate:** Genesis Medical Clinic Micălaca
**Prioritate:** URGENȚĂ
**Diagnostic trimitere:** Proces proliferativ esofagian (cod 95)
**Medic trimițător:** Dr. Noufal Abdul Vahab
**Status programare:** ✅ **PROGRAMAT LUNI 20.04.2026, ORA 17:00** (confirmat 18.04.2026)

**Cronologie pregătire (deadline-uri exacte):**

| Data/ora                       | Acțiune                                                               |
| ------------------------------ | --------------------------------------------------------------------- |
| **Sâmbătă 18.04.2026, 17:00**  | STOP Jamesi (H-48 înainte de CT)                                      |
| Duminică 19.04.2026            | Hidratare activă cu apă plată (1.5-2 L/zi dacă tolerat cardiologic)   |
| Duminică 19.04.2026, ~20:00    | Cină ușoară — ultima masă mai consistentă                             |
| Luni 20.04.2026, ~11:00        | Gustare ușoară — ultima masă înainte de CT                            |
| Luni 20.04.2026, dimineața     | Aspenter + Concor + Triplixam — DA (normal)                           |
| Luni 20.04.2026, 17:00         | **CT**                                                                |
| Luni 20.04.2026, seara         | Glicemie de control; NU relua Jamesi încă                             |
| **Miercuri 22.04.2026, 17:00** | Reluare Jamesi (H+48 după CT) DOAR după confirmare creatinină normală |

**⚠️ Pregătire critică:**

- **Oprire Jamesi (sitagliptin + metformin) cu 48h înainte** — sâmbătă 18.04 ora 17:00 (componenta metformin → risc acidoză lactică cu contrast iodat)
- ✅ **Funcție renală recent verificată** — buletin Bioclinica 17.04.2026: creatinină 0.83 mg/dL (ref 0.67-1.17, NORMALĂ), uree 33.4 mg/dL (NORMALĂ). eGFR ~95 mL/min/1.73m² (stadiu G1). **Nu necesită repetare.**
- **Confirmare absență alergii la iod / fructe de mare / contrast anterior** — **STATUS: neconfirmat, P0 critic**
- **Triplixam** (indapamidă diuretic + perindopril IECA) — de întrebat radiologul la confirmare dacă păstrez integral
- Hidratare activă duminică 19.04: 1.5-2 L apă plată (atent la tolerabilitatea cardiacă)

**Istoric creatinină (funcție renală în timp):**

| Data | Valoare | Interval ref | Sursă |
|---|---|---|---|
| 2025-06-17 | 0.95 mg/dL | 0.8-1.3 | Buletin analize complet |
| 2025-11-28 | 0.66 mg/dL | — | Analize preop chirurgie (Spital) |
| **2026-04-17** | **0.83 mg/dL** | 0.67-1.17 | ✅ **Buletin Bioclinica (VALID pentru CT 20.04)** |

**Sursă curentă:** `Dosar_Medical/2026-04-17_buletin_bioclinica_uree_creatinina.json` (buletin nr. 26417A0362, Dr. Statnic Maria Luminița, Bioclinica Arad).

**Observație-cheie pentru urmărire biopsie:** același buletin Bioclinica menționează „Examen histopatologic în curs de execuție" → **biopsia esofagiană se procesează la Bioclinica Arad** (nu la Genesis, cum s-ar presupune). Contact urmărire rezultat: `arad@bioclinica.ro`.

---

## 9. Echipă medicală

| Specialitate                                                   | Medic                                            | Unitate                                    | Contact      |
| -------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------ | ------------ |
| Gastroenterologie                                              | Dr. Noufal Abdul Vahab (medic primar)            | Genesis Medical Clinic Arad                | De completat |
| Cardiologie (SCA ST+ 2012)                                     | Echipa Vichy, Franța — de identificat pe PDF     | Centre Hospitalier de Vichy (de confirmat) | —            |
| Cardiologie / Medicină internă (prescriere actuală 10.11.2025) | Dr. LAZĂR [nume parțial ilizibil]                | De identificat                             | —            |
| Diabetologie / prescriere Jamesi                               | Dr. LAZĂR (probabil, din prescrierea 10.11.2025) | De identificat                             | —            |
| Medic de familie                                               | De identificat                                   | De identificat                             | —            |
| Chirurgie Generală (hernie 28.11.2025)                         | De identificat din documentul original           | Secția Chirurgie Generală II               | —            |
| Urologie / Gastroenterologie (consult 28.10.2025)              | De identificat                                   | De identificat                             | —            |
| Oncologie digestivă (viitor)                                   | De stabilit                                      | —                                          | —            |

---

## 10. Evaluare preliminară

Pe baza informațiilor disponibile la data actualizării acestui fișier:

**Elemente care susțin suspiciunea de leziune semnificativă:**

- Limbajul biletului („proces proliferativ”) + nivel URGENȚĂ
- Decizia medicului primar de a cere direct CT de stadializare
- Vârsta + istoricul de fumat prelungit (factori de risc)
- Simptome sistemice apărute recent

**Elemente care sugerează că boala NU este în stadiu avansat:**

- Absența disfagiei progresive clasice
- Absența scăderii ponderale
- Absența sângerărilor digestive
- Absența semnelor de extensie locală (răgușeală, tuse la lichide, noduli)
- Absența durerii toracice persistente

**Ipoteze diagnostice — prioritizare estimată (NU diagnostic, doar orientare):**

1. Tumoră malignă esofagiană în stadiu localizat (neavansat) — probabilitate medie-mare
2. Leziune premalignă (displazie pe Barrett) — probabilitate medie
3. Leziune benignă cu aspect pseudotumoral (ulcer cronic, leiomiom, esofagită severă) — probabilitate mică-medie
4. Tumoră malignă în stadiu avansat — probabilitate mică (pe baza absenței semnelor clasice)

**Decizia finală se bazează EXCLUSIV pe:**

- Rezultatul histopatologic al biopsiei
- Raportul imagistic al CT-ului de stadializare
- Evaluarea de către medicul oncolog digestiv

---

## 11. Alergii cunoscute

**Status:** de verificat cu familia.

| Categoria                                         | Alergie      | Reacție |
| ------------------------------------------------- | ------------ | ------- |
| Medicamente                                       | De verificat | —       |
| Alimente (iod, fructe de mare — CRITIC pentru CT) | De verificat | —       |
| Alte                                              | De verificat | —       |

---

## 12. Rezumat în 3 linii (pentru preluare rapidă)

1. Pacient masculin, 66 ani, diabetic, post-stent cardiac 2012, ex-fumător 35 ani.
2. Leziune esofagiană descoperită la endoscopie (17.04.2026), biopsie trimisă, CT de stadializare programat.
3. În așteptarea rezultatelor; consult oncologic planificat imediat ce ambele rezultate sunt disponibile.

---

**Istoric versiuni:** vezi `arhiva/` pentru versiunile anterioare ale acestui fișier.
**Următoarea actualizare planificată:** la primirea rezultatului CT sau biopsiei.
