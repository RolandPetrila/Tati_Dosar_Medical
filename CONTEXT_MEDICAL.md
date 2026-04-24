# CONTEXT_MEDICAL.md — Starea medicală actuală

**Fișier central de stare.** Se actualizează la fiecare informație medicală nouă. Ultima modificare trebuie reflectată în antetul de mai jos și în `CHANGELOG.md`.

---

**Ultima actualizare:** 24 aprilie 2026 18:30 (integrare completă Arhiva_Generala + Boala_Actuala: cardiologie ambulator 10.11.2025, UPU 30.05.2024, medic familie identificat, separare gastroscopie/colonoscopie, bilet trimitere CT ca document propriu)
**Responsabil dosar:** Roland Petrilă (fiul pacientului)
**Versiune structură:** 1.3 (integrare masivă extrageri strict-extractive + 12 JSON-uri noi canonice + MANIFEST v2.0)
**Versiune anterioară arhivată:** `Dosar_Medical/arhiva/context_medical_versiuni/CONTEXT_MEDICAL_pre-status-jamesi-reluat_2026-04-22_1658.md` + `Dosar_Medical/arhiva/context_medical_versiuni/CONTEXT_MEDICAL_pre-CT-stadializare_2026-04-22_1600.md` (v1.1 pre-CT) + `Dosar_Medical/arhiva/context_medical_versiuni/CONTEXT_MEDICAL_v1_2026-04-17.md`

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
| Greutate            | ~79 kg (aproximativ, declarat de familie 2026-04-18 — reper pentru monitorizare scădere)       |
| Înălțime            | De completat                                                                                   |

**Sursa datelor administrative:** `Dosar_Medical/2023-06-12_carte_identitate.json` + `Dosar_Medical/2025-11-01_talon_pensie_asigurare.json`.

---

## 2. Status clinic curent

**Suspiciune clinică principală:** Proces proliferativ **circumferențial nedepășibil endoscopic** la nivelul 2/3 inferioare a esofagului, cu **extensie la joncțiunea eso-gastrică (orificiul cardia + cadru gastric fundic)** — probabil **Siewert II** (de confirmat cu oncolog). Cod 95, bilet BCTAP 0631727 din 17.04.2026.

**Context:** Leziune identificată la endoscopie digestivă superioară (17.04.2026, Dr. Noufal Abdul Vahab, Genesis Medical Clinic Arad). Biopsie prelevată — rezultat histopatologic încă în lucru la Bioclinica Arad (monitor automat activ, estimat 24.04–01.05.2026). CT TAP N+SDC de stadializare efectuat luni **20.04.2026 ora 17:00** la Genesis Medical Clinic Micălaca, raport semnat de Dr. Buie Florian-Laurențiu (cod parafă A11818) + Dr. Candea Florin-Vasile (cod parafă F52510), ambii medici primari radiologie.

> **Restructurare R24 aplicată 2026-04-24** (post-audit `AUDIT_EXTRAGERE_2026-04-24.md` Batch A): secțiunea 2 reorganizată în 5 sub-secțiuni (Findings principale / secundare / colaterale / parametri tehnici / referință sursă) pentru paritate completă cu `Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json`. Backup pre-restructurare: `Dosar_Medical/arhiva/context_medical_versiuni/CONTEXT_MEDICAL_pre-batchA-r24-CT_2026-04-24_0230.md`.

### 2.1 Findings principale CT 20.04.2026 (impact decizional direct)

**Stadializare imagistică preliminară — estimativă, necesită corelare cu biopsie:**

| Element       | Estimare CT           | Note                                                                                                                     |
| ------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **T** (tumor) | T3–T4                 | Proces expansiv infiltrativ circumferențial cu extensie loco-regională, densificarea grăsimii peritumorale               |
| **N** (nodes) | N0–N1                 | Limfonoduli loco-regionali max 7.5 mm (sub pragul standard <10 mm, dar în context neoplazic pot fi relevanți)            |
| **M** (meta)  | **M0 probabil**       | Fără metastaze hepatice, pulmonare, osoase, ganglionare distale vizibile                                                 |
| **Siewert**   | II probabil           | Joncțiune eso-gastrică propriu-zisă, centrată pe cardia cu extensie eso-distală și fundică                               |
| **ATENȚIE**   | **Ascită de evaluat** | Colecție fluidă perihepatică 15 mm + intrapelvină 28 mm → de exclus CARCINOMATOZĂ PERITONEALĂ (ar echivala cu stadiu IV) |

**Natura histologică a leziunii:** neclarificată. Biopsia în lucru la Bioclinica Arad va preciza tipul exact (adenocarcinom vs. carcinom scuamocelular, grad de diferențiere). Localizarea distală + extensia fundică sugerează **adenocarcinom** (pattern tipic Siewert II), dar confirmarea aparține histopatologului.

### 2.2 Findings secundare CT 20.04.2026 (monitorizare / urmărire)

- **Glandă suprarenală stângă hipertrofă, heterogenă, fără leziuni focale** — „de monitorizat" per radiolog. Necesită evaluare endocrinologică (hormoni bazali: cortizol 8AM, aldosteron/renină, metanefrine plasmatice + follow-up imagistic).
- **Colecție fluidă pulmonar bazal LID** — 9.3 mm, de urmărit evolutiv.
- **Leziune chistică subcutan perete toracic posterior cXI-cXII** — 22/47.4 mm, „a se corela clinic" (probabilă benignă — chist sebaceu / lipom / chist epidermoid; palpare la următorul consult).
- **Cardiomegalie + ateromatoză calcara aorto-coronariană + aortă abdominală + emergențe** — consecvent cu antecedente SCA ST+ 2012 / stent IVA, fără modificare terapeutică imediată necesară.

### 2.3 Findings colaterale CT 20.04.2026 (R24 — listare integrală post-audit 2026-04-24)

**Pulmonar (relevant pre-esofagectomie):**

- **Tulburări de ventilație posterobazal LID + LIS** — relevant pentru pregătirea pre-chirurgie esofagiană (necesită spirometrie + kinetoterapie respiratorie pre-operatorie + anamneză pulmonară detaliată).
- **Leziuni micronodulare calcare sechelare apical LSD, diametru maxim 6.8 mm** — sugestiv pentru sechele TBC vechi (de confirmat anamneza); follow-up imagistic la control oncologic.
- Trahee și bronșii principale: permeabile.
- Parenchim pulmonar: condensări absente, procese expansive absente, fibroză absentă, emfizem absent.

**Adenopatii (toate categoriile evaluate explicit — confirmare M0):**

- Mediastinale: absente.
- Hilare: absente.
- Axilare: absente.
- Abdomino-pelvine: absente.

**Aspecte normale organe (R24 — listare explicită, NU se prezumă din absența mențiunii):**

- **Tiroidă:** aspect normal dimensional, omogen captantă de SDC.
- **Cord și vase mari:** artera pulmonară permeabilă (calibru normal); aorta toracală permeabilă (calibru normal); colecții intrapericardice absente.
- **Ficat:** dimensiuni și contur normale, fără prize patologice de SDC.
- **Căi biliare:** colecist fără îngroșări parietale, fără calculi evidențiabili CT; intra/extrahepatice fără dilatări.
- **Pancreas:** aspect normal.
- **Splină:** aspect normal.
- **Glandă suprarenală dreaptă:** aspect normal (vs. stânga hipertrofă — vezi findings secundare).
- **Rinichi:** bilateral dimensiuni și IP normale, funcționali, secreție și excreție prezentă, fără calculi radioopaci, fără dilatații pielo-caliceale.
- **Vezică urinară:** fără modificări parietale sau intracavitare.
- **Prostată:** aspect normal CT.
- **Vase abdominale:** ax spleno-portal celiaco-mezenteric permeabil; aorta abdominală + VCI calibru normal, permeabile.
- **Modificări osoase suspecte malignitate:** absente.

**Coloană vertebrală:**

- **Modificări degenerative disco-vertebrale prezente supraetajat toraco-lombar** (context musculoscheletic — relevant pentru poziționare intraoperatorie + recuperare post-chirurgie).

### 2.4 Parametri tehnici CT 20.04.2026 (R24 — listare obligatorie)

- **Protocol:** TAP nativ + substanță de contrast iodat (N+SDC).
- **Regiuni scanate:** torace + abdomen + pelvis.
- **Doza radiație:** **DLP = 2474 mGy·cm²** (parametru tehnic obligatoriu pentru evaluare expunere cumulativă la radiații).
- **Numărul înregistrare examinare:** 284.
- **Bilet trimitere CT:** BCTAP 0631727 (cod diagnostic 95).
- **Medic ordonator:** Dr. Noufal Abdul Vahab (gastroenterologie Genesis Arad).
- **Medici examinatori:** Dr. Buie Florian-Laurențiu (parafă A11818) + Dr. Candea Florin-Vasile (parafă F52510), ambii medici primari radiologie.
- **Unitate:** Genesis Medical Clinic Micălaca (denumire în document „Genesys").

### 2.5 Referință sursă

- **JSON canonic:** `Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json`
- **PDF sursă:** `Dosar_Medical/documente_sursa/11_CT_stadializare_2026/CT - Genesys.pdf` (mutat de user 2026-04-24 din `99_altele/` în folder dedicat)
- **Data extragere JSON:** 2026-04-22
- **Data audit R24 + restructurare:** 2026-04-24
- **Marcaj `.meta.json`:** `"completeness_verified": "2026-04-24"`, `"coverage": "100%"` (post-audit Batch A)
- **Confidence overall:** high (PDF digital nativ, text extractabil, fără OCR)

### 2.6 Acțiuni în curs (status la 2026-04-24)

- ✅ **CT efectuat 20.04.2026** — raport integrat în dosar
- 🟡 **Rezultat biopsie esofagiană** — așteptat la Bioclinica Arad, monitor automat activ 24/7 (GitHub Actions)
- 🔴 **Consult oncolog digestiv URGENT** — de programat (stadiul infiltrativ + ascită modifică abordarea terapeutică)
- 🟡 **Evaluare endocrinologică** glanda suprarenală stângă — de programat post-consult oncolog
- ✅ **Jamesi reluat** 22.04.2026 seara, conform schemei standard (1-0-1, 50/1000 mg), **fără complicații** — pauza H-48h → H+48h a funcționat corect, fără simptome renale post-contrast raportate de familie
- 🟡 **Spirometrie + anamneză pulmonară pre-esofagectomie** (post audit Batch A 2026-04-24) — de discutat cu chirurgul oncolog: tulburările ventilație posterobazal LID+LIS + nodulii apicali sechelari LSD necesită evaluare pulmonară pre-operator (spirometrie + DLCO + posibil consult pneumolog)

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

### Episod UPU 30 mai 2024 (criza HTA + hiperglicemie + troponină dinamică)

**Prezentare UPU Arad 17:30:** grețuri + vărsături (după consum sarmale) + vertij. Trimis de medic de familie Dr. Orbán Ecaterina (Cabinet Medical Individual Nădlac) pentru „criza HTA 200/100 mmHg, SaO2 91%, glicemie 177 mg%, DZ tip II dezechilibrat".

**La UPU (Dr. Pop Florica, medic primar medicină de urgență):**

- TA 145/70 mmHg, AV 55 bpm, SaO2 97%
- Stare generală conștient, cooperant; MV prezent bilateral, fără raluri
- Biologic CRITIC: **hs-cTnI dinamic 4.24 → 4.59 ng/L** (trending UP între 2 măsurători succesive — relevant cardiologic)
- Glicemie serică **180.48 mg/dL** (↑↑), glucozurie (+), corpi cetonici (+) — decompensare metabolică DZ
- EKG auto Glasgow: „Sinus bradycardia HR 55, **Anteroseptal infarct - age undetermined**, Lateral T wave abnormality, **Markedly Abnormal ECG**"
- Lymphopenie 15.4% (↓), creatinină 0.66 (↓ ușor)

**Consult gastroenterologie (Dr. Grada Sebastian, cod G15512):** ecografie abdominală — ficat cu suprafață micronodulară moderat, colecist cu sediment, pancreas hiperecogen, splină 12 cm, anse intestinale ușor dilatate flanc stâng. **Diagnostic: sindrom dispeptic**. Recomandare: Controloc 20 mg 1-0-0 + Debridat 3×1/zi + reevaluare ambulator gastro.

**Consult cardiologie (Dr. Post Mihaela, cod parafă A13550 UPU / A14555 ambulator):** sindrom coronarian cronic, IM vechi (2011), HTAE gradul I stadiul 3, DZ tip II non-insulino-necesitant, IM + IT ușoare. Scrisoare medicală nr 0003622 cu recomandare: PRESTARIUM 10 mg 1-0-0 ×2 + ASPENTER 75 0-1-0 + SORTIS 80 0-0-1 + CONCOR 5 1-0-0 + NORVASC 5 0-1-0.

**NU există documentație serologie H. pylori în acest episod** — serologia IgG a fost efectuată ulterior (04.06.2024 + 06.09.2024) la Ultra ClinicaVest Pecica.

**Medic de familie identificat prin acest episod:** **Dr. ORBÁN ECATERINA-MARIA** — Cabinet Medical Individual Nădlac, CUI 20263730, cod parafă 718705, medic specialist medicină generală-pediatrie.

**Relevanță pre-oncologică:** EKG automat „Markedly Abnormal ECG" + troponina dinamică în creștere + criza HTA cu glicemie 200 mg% documentează un pacient cardiovascular instabil la distanță. Necesar pentru evaluarea riscului anestezic preoperator.

**Sursă:** `Dosar_Medical/2024-05-30_upu_consult_gastro_cardio.json` + `2024-05-30_analize_upu_sange_1517243.json` + `2024-05-30_analize_upu_urina_1517290.json` (documente sursă în `documente_sursa/14_UPU_2024_05_30/`).

### Infecție cu Helicobacter pylori (serologie 2024)

**Serologie IgG pozitivă consistentă în timp:**

- **04.06.2024 buletin 77449** — Anti-H. pylori IgG **>100 U/mL** (referință 0-20)
- **06.09.2024 buletin 79765** — Anti-H. pylori IgG **>100 U/mL** (aceeași valoare la ~3 luni distanță)

Ambele recoltate la SC Ultra ClinicaVest SRL Pecica (metoda CLIA), solicitate de Dr. Orbán Ecaterina (medic familie).

**Interpretare:** rezultatul masiv pozitiv confirmă expunere anterioară. Serologia IgG **NU distinge** infecție activă de antecedentă (anticorpii IgG persistă luni/ani post-eradicare). Pentru validarea eradicării ar trebui efectuat: (a) antigen fecal H. pylori SAU (b) test respirator cu uree C13 — **niciun astfel de test documentat în dosar**.

**Date de completat:**

- Tratament antibiotic + IPP specific — nu există documentare explicită (probabil efectuat ambulator post-episod UPU)
- Test de control post-eradicare (antigen fecal sau UBT) — NU serologie

**Sursă:** `Dosar_Medical/2024-06-04_anti_helicobacter_pylori_igg_77449.json` + `2024-09-06_anti_helicobacter_pylori_igg_79765.json`.

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

Schema datată **10 noiembrie 2025**. Medic prescriptor **IDENTIFICAT (2026-04-24): Dr. LAZA CRISTINA** (medic primar cardiolog, cod parafă **C07842**) — cross-reference cu ecografia transtoracică efectuată în aceeași zi (sursă tipărită, cod parafă clar vizibil). Consult pre-chirurgie hernie.

| Medicament                                                     | Indicație                                                | Doză                  | Ritm                  | Note                                                                      |
| -------------------------------------------------------------- | -------------------------------------------------------- | --------------------- | --------------------- | ------------------------------------------------------------------------- |
| **Jamesi** (sitagliptin + clorhidrat de metformin)             | Diabet zaharat tip 2                                     | 50 mg / 1000 mg       | 1-0-1 (dim. și seara) | **CRITIC**: componenta metformin se oprește 48h înainte de CT cu contrast |
| **Aspenter** (acid acetilsalicilic)                            | Antiagregant post-stent coronarian 2012                  | 75 mg                 | 0-1-0 (prânz)         | NU se oprește pentru CT                                                   |
| **Concor** (fumarat de bisoprolol)                             | Beta-blocant (cardioprotecție + HTA + control frecvență) | 5 mg                  | 1-0-0 (dimineața)     | Nu se oprește pentru CT                                                   |
| **Triplixam** (perindopril arginine + indapamidă + amlodipină) | Antihipertensiv combinație triplă                        | 10 mg / 2.5 mg / 5 mg | 1-0-0 (dimineața)     | Nu se oprește pentru CT                                                   |

**Notă:** manuscrisul conținea o a 5-a recomandare tăiată cu marker albastru (anulată).

**Suplimente alimentare:** de verificat cu familia.

**Sursă:** `Dosar_Medical/2025-11-10_schema_medicamente.json` (manuscris parțial + fotografii cutii). Medicamentele, dozele și ritmul de administrare sunt `[CERT]` (fotografii cutii + manuscris lizibil pentru ritm). Numele medicului prescriptor NU e integrat conform Regula 25 (manuscris parțial ilizibil — tracking în `Dosar_Medical/EXTRAGERI_INCOMPLETE.md`).

### Interacțiune medicamentoasă documentată — de urmărit

**Sitagliptin (Jamesi) + Perindopril (Triplixam) → risc crescut de angioedem.** Mecanism: sitagliptinul inhibă DPP-4 (enzima care degradează substanța P); perindoprilul inhibă ECA (care degradează bradikinina); acumularea ambelor substanțe vasoactive crește riscul de umflare bruscă a feței, buzelor, limbii sau căilor respiratorii. **NU e contraindicație** — pacientul poate continua ambele medicamente.

**Urmărire:** la orice umflare bruscă la față/buze/limbă sau dificultate bruscă de respirație → 112 IMEDIAT. Medicul curant să fie informat despre combinația actuală.

**Sursă:** [CERT] SmPC Triplixam v06.2021, secțiunea 4.5 „Gliptins": „Increased risk of angio-oedema, due to dipeptidyl peptidase IV (DPP-IV) decreased activity by the gliptine, in patients co-treated with an ACE inhibitor."

**Detalii complete pentru familie:** `Dosar_Medical/rapoarte_generate/2026-04-18_raport_reactii_adverse_jamesi_triplixam.docx`, Partea III.A.

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

**Rezultat principal — findings detaliate:**

| Element                        | Valoare                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------- |
| **Localizare**                 | **2/3 inferioară a esofagului**                                                                           |
| **Aspect**                     | **Proces proliferativ circumferențial**                                                                   |
| **Depășibilitate endoscopică** | **NU — nedepășibil** (stenoză aproape completă, endoscopul nu a trecut dincolo de leziune)                |
| **Biopsie**                    | Prelevată, trimisă la Bioclinica Arad                                                                     |
| **Text original document**     | „La 2/3 inferioara esofagului prezinta proces proliferativ circumferentialne depasibila endoscopica(Bio)" |

**Clarificare 2026-04-22 (confirmată de user Roland):** textul contopit din PDF „circumferentialne depasibila" se interpretează ca „**circumferențial nedepășibilă**" (adjectiv feminin + formulă standard rapoarte gastro RO). Interpretarea este confirmată suplimentar de raportul CT din 20.04.2026 care descrie procesul ca „infiltrativ" și „dificil de caracterizat dimensional" (compatibil cu stenoză completă care împiedică trecerea endoscopului).

**Impact clinic al „nedepășibilității":**

- Stenoză strânsă — esofagul nu mai are lumen liber pentru endoscop (diametru normal ~25 mm, aici mult mai îngust)
- Explică parțial simptomatologia atipică („nod în gât" intermitent după mese, chiar fără disfagie progresivă clasică)
- Argument suplimentar pentru stadiul avansat (T3-T4 coroborat cu CT)
- Implicație practică: posibilă necesitate de stent esofagian preoperator sau jejunostomă nutrițională dacă disfagia se agravează înainte de tratament

**Buletin gastroscopie:** JPEG sursă `documente_sursa/09_endoscopie_2026_04/2026-04-17_examen_gastroscopic.jpeg`; extragere MD strict-extractivă alături; JSON canonic dedicat `Dosar_Medical/2026-04-17_examen_gastroscopic.json` (separat 2026-04-24 din fostul JSON unificat).

### 7.3 Colonoscopie (17 aprilie 2026)

Efectuată concomitent cu endoscopia la Genesis Medical Clinic Arad (Dr. Noufal Abdul Vahab).

**Examinare detaliată pe segmente (R23 — aspecte normale listate explicit):**

| Segment        | Aspect                                          | Calitate pregătire    |
| -------------- | ----------------------------------------------- | --------------------- |
| Rect           | fără modificări                                 | bună                  |
| Sigmoid        | porțiune vizibilă fără modificări               | resturi fecale solide |
| **Descendent** | **polip sesil 8 mm** — recomandare polipectomie | bună                  |
| Transvers      | porțiune vizibilă fără modificări               | resturi fecale solide |
| Ascendent      | porțiune vizibilă fără modificări               | resturi fecale solide |
| Cec            | fără modificări                                 | bună                  |

**Mențiune inițială:** hemoroizi interni grad II (K64.1).

**Concluzii:**

- **Polip colon descendent** (K63.5) — sesil 8 mm — recomandare: revine pentru polipectomie
- **Boală hemoroidală** (K64) — hemoroizi interni grad II (K64.1)

**Observație pregătire colon:** reziduuri fecale solide în 3 segmente (sigmoid, transvers, ascendent) au limitat vizualizarea completă — pregătire colon optimizată recomandată pentru următoarea colonoscopie.

**Buletin colonoscopie:** JPEG sursă `documente_sursa/09_endoscopie_2026_04/2026-04-17_examen_colonoscopic.jpeg`; JSON canonic `Dosar_Medical/2026-04-17_examen_colonoscopic.json`.

### 7.4 Biopsie esofagiană (în lucru)

**Status:** la laboratorul de anatomopatologie Bioclinica Arad.
**Timp estimat:** 7-14 zile lucrătoare (estimare 24.04-01.05.2026).
**Monitor automat:** activ (GitHub Actions → ntfy.sh, verificare portal Bioclinica la 30 min, 24/7).
**Importanță:** diagnostic de certitudine (tip histologic — adenocarcinom vs. scuamocelular, grad de diferențiere, markeri moleculari relevanți pentru decizia terapeutică).

### 7.5 Bilet trimitere CT (17 aprilie 2026) — document administrativ declanșator

**Serie/Număr:** **BCTAP 0631727**.
**Emitent:** Dr. Noufal Abdul Vahab (cod parafă C 11074), Genesis Medical Clinic Arad (CUI R20295098, Bd. Revoluției nr. 3).
**Casa asigurări:** CAS AR, nr. contract/convenție 1148.
**Nivel prioritate:** Ambulator Specialitate (bifat).
**Cod diagnostic (intern CAS):** 95 — „PROCES PROLIFERATIV ESOFAGIAN".
**Investigații recomandate:** CT TORACE (SDC) + CT ABDOMEN (SDC) + CT PELVIS (SDC) — toate cu substanță de contrast.

**A declanșat:** CT efectuat 20.04.2026 la Genesis Medical Clinic Micălaca (vezi §2).

**Sursă:** `documente_sursa/11_CT_stadializare_2026/2026-04-17_bilet_trimitere_CT_BCTAP_0631727.jpeg` + `Dosar_Medical/2026-04-17_bilet_trimitere_CT.json`.

---

## 8. Investigații programate / în așteptare

### 8.1 Consult oncolog digestiv (URGENT)

**Status:** de programat imediat după primirea rezultatului biopsiei (sau înaintea lui dacă se poate — discuție preliminară pe baza CT).
**Motivație accelerare:** stadiul infiltrativ + ascită + extensia la joncțiunea eso-gastrică → protocolul terapeutic se schimbă față de un cancer esofagian distal simplu (probabil **FLOT** în loc de **CROSS**, având componenta gastrică).

**Centre recomandate (opțiuni):**

- **Arad** — apropiere geografică, continuitate cu Genesis
- **Timișoara** — Institutul Regional / OncoHelp / SCJU
- **Cluj** — Institutul Oncologic Prof. Dr. Ion Chiricuță
- **București** — pentru second opinion sau cazuri complexe (Institutul Fundeni, SanaDor, Monza)

**Decizie:** la familie + recomandare Dr. Noufal Abdul Vahab (de solicitat).

### 8.2 Reluare Jamesi (H+48 post-CT) — 22.04.2026 ✅ FINALIZAT

**Status:** ✅ **FINALIZAT seara 22.04.2026.** Jamesi reluat conform schemei standard (1-0-1, 50/1000 mg), **fără complicații** raportate de familie. Pauza H-48h → H+48h a fost respectată corect; creatinina pre-CT era 0.83 mg/dL (normală), iar pacientul a tolerat contrastul iodat fără reacție alergică sau simptome renale post-CT.

**Continuă monitorizare (de rutină):** glicemie de control în zilele următoare, vigilență pentru semne de afectare renală (scădere diureză, edeme, senzație de vertij, gust metalic) — la orice apariție → STOP medicament + consult medic familie.

### 8.3 Evaluare endocrinologică (glanda suprarenală stângă)

**Status:** de programat post-consult oncolog (prioritate secundară — cancerul esofagian primar este urgența).

**Analize minime:** cortizol bazal 8AM, raport aldosteron/renină, metanefrine plasmatice (+/- urinare 24h).
**Follow-up imagistic:** interval 3-6 luni (corelat cu controlul oncologic, evitare iradiere suplimentară).

**Istoric creatinină (funcție renală în timp):**

| Data           | Valoare        | Interval ref | Sursă                                     |
| -------------- | -------------- | ------------ | ----------------------------------------- |
| 2025-06-17     | 0.95 mg/dL     | 0.8-1.3      | Buletin analize complet                   |
| 2025-11-28     | 0.66 mg/dL     | —            | Analize preop chirurgie (Spital)          |
| **2026-04-17** | **0.83 mg/dL** | 0.67-1.17    | ✅ **Buletin Bioclinica (pre-CT validă)** |

**Sursă curentă:** `Dosar_Medical/2026-04-17_buletin_bioclinica_uree_creatinina.json` (buletin nr. 26417A0362, Dr. Statnic Maria Luminița, Bioclinica Arad).

**Observație-cheie pentru urmărire biopsie:** același buletin Bioclinica menționează „Examen histopatologic în curs de execuție" → **biopsia esofagiană se procesează la Bioclinica Arad** (nu la Genesis, cum s-ar presupune). Contact urmărire rezultat: `arad@bioclinica.ro`.

---

## 9. Echipă medicală

| Specialitate                                                 | Medic                                                                                                                 | Unitate                                                          | Contact                         |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------- |
| **Medic de familie**                                         | **Dr. ORBÁN ECATERINA-MARIA** (medic specialist medicină generală-pediatrie, cod parafă **718705**, CUI **20263730**) | **Cabinet Medical Individual, Nădlac**                           | De completat                    |
| Gastroenterologie (endoscopie 17.04.2026)                    | Dr. Noufal Abdul Vahab (medic primar, cod parafă **C 11074**)                                                         | Genesis Medical Clinic Arad                                      | De completat                    |
| **Radiologie și Imagistică (CT 20.04.2026)**                 | **Dr. Buie Florian-Laurențiu (cod A11818)** + **Dr. Candea Florin-Vasile (cod F52510)** — ambii medici primari        | **Genesis Medical Clinic Micălaca**                              | Prin Genesis                    |
| Anatomopatologie (biopsie esofag)                            | De identificat (Bioclinica Arad)                                                                                      | Bioclinica Arad                                                  | `arad@bioclinica.ro`            |
| Laborator clinic (pre-CT 17.04.2026)                         | Dr. Statnic Maria Luminița (medic primar medicina de laborator, cod **A08064**)                                       | Bioclinica SRL Arad, punct recoltare Vlaicu                      | `arad@bioclinica.ro`            |
| **Cardiologie ambulator (consult pre-chirurgie 10.11.2025)** | **Dr. LAZA CRISTINA** (medic primar cardiolog, cod parafă **C07842**) — prescriptor schemă medicație actuală          | Arad (cabinet de identificat)                                    | —                               |
| Cardiologie (SCA ST+ 2012)                                   | Echipa Vichy, Franța — de identificat pe PDF                                                                          | Centre Hospitalier de Vichy (de confirmat)                       | —                               |
| Cardiologie (episod UPU 30.05.2024)                          | Dr. Post Mihaela (medic specialist cardiologie, cod **A13550** / **A14555** — 2 coduri pe 2 ștampile diferite)        | Spitalul Clinic Județean de Urgență Arad + ambulator             | —                               |
| Gastroenterologie (episod UPU 30.05.2024)                    | Dr. Grada Sebastian (medic specialist gastroenterologie, cod **G15512**)                                              | Spitalul Clinic Județean de Urgență Arad                         | —                               |
| Medicină de urgență (UPU 30.05.2024)                         | Dr. Pop Florica (medic primar medicină de urgență, cod **C79981**)                                                    | Spitalul Clinic Județean de Urgență Arad — UPU Adulți            | —                               |
| **Chirurgie Generală (hernie 28.11.2025)**                   | **Dr. Papiu Horațiu-Sabin (medic primar chirurgie, cod parafă 775468)**                                               | Spitalul Clinic Județean de Urgență Arad — Chirurgie Generală II | —                               |
| **Urologie (consult 28.10.2025)**                            | **Dr. PITEA ALEXANDRU (medic primar urologie, cod A13044)**                                                           | Complex Medical Pitea & Pitea SRL, Arad, Revoluției 45           | **0749111455**                  |
| Laborator clinic (serologie HP + analize 2025)               | Dr. Cret Anamaria (medic primar laborator, cod A 0769)                                                                | SC Ultra ClinicaVest SRL Pecica                                  | `laborator@ultraclinicavest.ro` |
| Laborator clinic (UPU 30.05.2024)                            | Dr. Igas Angelica (cod 119856) + Dr. Avram Cecilia — ambii medici primari medicina de laborator                       | Spitalul Clinic Județean de Urgență Arad — Laborator Central     | —                               |
| **Oncologie digestivă** (prioritate URGENT)                  | **De stabilit**                                                                                                       | Arad / Timișoara / Cluj / București                              | —                               |
| Endocrinologie (glandă suprarenală, follow-up)               | De stabilit post-consult oncolog                                                                                      | —                                                                | —                               |

---

## 10. Evaluare preliminară (actualizată post-CT, 22.04.2026)

**Context actualizat:** CT-ul de stadializare (20.04.2026) a clarificat semnificativ imaginea — leziune infiltrativă circumferențială la joncțiunea eso-gastrică cu extensie fundică, fără metastaze la distanță vizibile, dar cu ascită de etiologie de elucidat.

**Elemente care susțin neoplazie avansată (post-CT):**

- Stenoza completă „nedepășibilă endoscopic" (17.04.2026) = masă obstructivă
- Proces expansiv infiltrativ circumferențial + densificarea grăsimii loco-regionale (CT 20.04)
- Extensie la joncțiunea eso-gastrică + cadru gastric fundic (Siewert II probabil)
- Stadiu imagistic estimativ **T3–T4**
- **Ascita** perihepatică + intrapelvină (risc carcinomatoză peritoneală de exclus)
- Simptome sistemice (oboseală, apetit diminuat, senzație „nod în gât" postprandial)
- Vârsta + istoric fumat 35 ani + reflux recent reapărut

**Elemente favorabile (aspecte pozitive la CT):**

- **M0 probabil** — fără metastaze hepatice, pulmonare, osoase sau ganglionare distale vizibile
- Limfonoduli loco-regionali sub pragul patologic standard (max 7.5 mm vs. <10 mm criteriu)
- Fără adenopatii mediastinale / hilare / axilare / abdomino-pelvine
- Funcție renală normală (creatinină 0.83 mg/dL)
- Status cardiac stabil (post-stent 2012, controlat farmacologic)
- Absența disfagiei progresive clasice (deși stenoza e aproape completă, pacientul se alimentează încă rezonabil)
- Scădere ponderală absentă până acum

**Ipoteze diagnostice revizuite (NU diagnostic, doar orientare):**

1. **Adenocarcinom de joncțiune eso-gastrică Siewert II** — probabilitate ridicată (localizare distală + extensie fundică + circumferențial)
2. Carcinom scuamocelular cu extensie distală — probabilitate mai mică (localizarea atipică pentru scuamos)
3. Alte tumori rare (GIST, limfoame esofagiene, sarcoame) — probabilitate foarte mică

**Stadializare clinică probabilă (pre-biopsie):**

- **Dacă M0 confirmat (fără carcinomatoză):** Stadiu III (T3-T4, N0-N1, M0) → candidat pentru protocol **FLOT** (chemoterapie perioperatorie) + chirurgie
- **Dacă M1 (carcinomatoză peritoneală confirmată):** Stadiu IV → protocol paliativ / chemoterapie sistemică (FLOT sau FOLFOX, +/- imunoterapie dacă markeri PD-L1+ / HER2+)

**Decizia finală se bazează EXCLUSIV pe:**

- Rezultatul histopatologic al biopsiei (tip celular, grad de diferențiere, markeri moleculari HER2, PD-L1, MSI)
- Clarificarea etiologiei ascitei (reactivă vs. carcinomatoză — poate necesita paracenteză + citologie sau laparoscopie)
- Evaluarea de către medicul oncolog digestiv
- Eventual PET-CT pentru activitate metabolică și confirmare M0 cu sensibilitate superioară CT-ului

---

## 11. Alergii cunoscute

**Status:** fără alergii cunoscute relevante pentru CT cu contrast iodat (confirmat de familie 18.04.2026 13:28, sursă: Roland Petrilă).

| Categoria                               | Alergie                           | Reacție |
| --------------------------------------- | --------------------------------- | ------- |
| Medicamente                             | Niciuna declarată                 | —       |
| Iod (contrast iodat) — CRITIC pentru CT | **Fără alergie** (confirmat)      | —       |
| Fructe de mare — CRITIC pentru CT       | **Fără alergie** (confirmat)      | —       |
| Contrast iodat anterior                 | Fără reacții anterioare raportate | —       |
| Alte                                    | Niciuna declarată                 | —       |

**Notă:** confirmarea este declarație familie (nu document medical). Rămâne valabil să i se confirme din nou verbal la radiolog înainte de injectarea contrastului.

---

## 12. Rezumat în 3 linii (pentru preluare rapidă — actualizat 22.04.2026)

1. Pacient masculin, 66 ani, diabetic, post-stent cardiac 2012, ex-fumător 35 ani. CNP 1590518024486.
2. Proces proliferativ **circumferențial nedepășibil endoscopic** la joncțiunea eso-gastrică (Siewert II probabil); CT 20.04.2026 arată **T3-T4, N0-N1, M0 probabil**, cu ASCITĂ de elucidat (posibilă carcinomatoză peritoneală).
3. Biopsia în lucru (Bioclinica, estimat 24.04-01.05); **consult oncolog URGENT** de programat — posibil protocol FLOT; Jamesi reluat seara 22.04 post-CT fără complicații.

---

**Istoric versiuni:** vezi `arhiva/` pentru versiunile anterioare ale acestui fișier.
**Următoarea actualizare planificată:** la primirea rezultatului biopsiei (histologie) SAU la primul consult oncolog digestiv.
