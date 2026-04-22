# CONTEXT_MEDICAL.md — Starea medicală actuală

**Fișier central de stare.** Se actualizează la fiecare informație medicală nouă. Ultima modificare trebuie reflectată în antetul de mai jos și în `CHANGELOG.md`.

---

**Ultima actualizare:** 22 aprilie 2026 16:00 (rezultat CT stadializare integrat + clarificare leziune esofag „circumferențial nedepășibil endoscopic" confirmată de user)
**Responsabil dosar:** Roland Petrilă (fiul pacientului)
**Versiune structură:** 1.2 (post-CT, reconciliere Claude_Opus_4.7)
**Versiune anterioară arhivată:** `Dosar_Medical/arhiva/context_medical_versiuni/CONTEXT_MEDICAL_pre-CT-stadializare_2026-04-22_1600.md` (v1.1 pre-CT) + `Dosar_Medical/arhiva/context_medical_versiuni/CONTEXT_MEDICAL_v1_2026-04-17.md`

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

**Context:** Leziune identificată la endoscopie digestivă superioară (17.04.2026, Dr. Noufal Abdul Vahab, Genesis Medical Clinic Arad). Biopsie prelevată — rezultat histopatologic încă în lucru la Bioclinica Arad (monitor automat activ, estimat 24.04–01.05.2026). CT TAP N+SDC de stadializare efectuat luni **20.04.2026 ora 17:00** la Genesis Medical Clinic Micălaca, raport semnat de Dr. Buie Florian-Laurențiu + Dr. Candea Florin-Vasile (ambii medici primari radiologie).

**Stadializare imagistică preliminară (CT 20.04.2026) — estimativă, necesită corelare cu biopsie:**

| Element       | Estimare CT           | Note                                                                                                                     |
| ------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **T** (tumor) | T3–T4                 | Proces expansiv infiltrativ circumferențial cu extensie loco-regională, densificarea grăsimii peritumorale               |
| **N** (nodes) | N0–N1                 | Limfonoduli loco-regionali max 7.5 mm (sub pragul standard <10 mm, dar în context neoplazic pot fi relevanți)            |
| **M** (meta)  | **M0 probabil**       | Fără metastaze hepatice, pulmonare, osoase, ganglionare distale vizibile                                                 |
| **Siewert**   | II probabil           | Joncțiune eso-gastrică propriu-zisă, centrată pe cardia cu extensie eso-distală și fundică                               |
| **ATENȚIE**   | **Ascită de evaluat** | Colecție fluidă perihepatică 15 mm + intrapelvină 28 mm → de exclus CARCINOMATOZĂ PERITONEALĂ (ar echivala cu stadiu IV) |

**Natura histologică a leziunii:** neclarificată. Biopsia în lucru la Bioclinica Arad va preciza tipul exact (adenocarcinom vs. carcinom scuamocelular, grad de diferențiere). Localizarea distală + extensia fundică sugerează **adenocarcinom** (pattern tipic Siewert II), dar confirmarea aparține histopatologului.

**Descoperiri colaterale la CT (care necesită urmărire):**

- **Glandă suprarenală stângă hipertrofă, heterogenă, fără leziuni focale** — „de monitorizat" per radiolog. Necesită evaluare endocrinologică (hormoni bazali + follow-up imagistic).
- **Colecție fluidă pulmonar bazal LID** — 9.3 mm, de urmărit evolutiv
- **Leziune chistică subcutan perete toracic posterior cXI-cXII** — 22/47.4 mm, „a se corela clinic" (probabilă benignă — chist sebaceu / lipom / chist epidermoid, palpare)
- **Cardiomegalie + ateromatoză calcara aorto-coronariană + aortă abdominală + emergențe** — consecvent cu antecedente SCA ST+ 2012 / stent IVA, fără modificare terapeutică imediată necesară

**Acțiuni în curs (22.04.2026):**

- ✅ **CT efectuat 20.04.2026** — raport integrat în dosar (`Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json`)
- 🟡 **Rezultat biopsie esofagiană** — așteptat la Bioclinica Arad, monitor automat activ 24/7 (GitHub Actions)
- 🔴 **Consult oncolog digestiv URGENT** — de programat (stadiul infiltrativ + ascită modifică abordarea terapeutică)
- 🟡 **Evaluare endocrinologică** glanda suprarenală stângă — de programat post-consult oncolog
- 🟡 **Reluare Jamesi** AZI 22.04.2026 (H+48 post-CT, creatinină pre-CT normală)

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

**Buletin endoscopie:** stocat în `documente_sursa/09_endoscopie_2026_04/` (fișier PDF sursă); extras structurat în `Dosar_Medical/2026-04-17_buletin_gastroenterologie.json` (secțiune `examinare_endoscopica` adăugată 22.04.2026).

### 7.3 Colonoscopie (17 aprilie 2026)

Efectuată concomitent cu endoscopia la Genesis Medical Clinic Arad (Dr. Noufal Abdul Vahab).

**Rezultat:**

- **Polip colon descendent** (K63.5) — recomandare: revine pentru polipectomie
- **Boală hemoroidală** — hemoroizi interni grad II (K64.1)

**Sursă:** `Dosar_Medical/2026-04-17_buletin_gastroenterologie.json`.

### 7.4 Biopsie esofagiană (în lucru)

**Status:** la laboratorul de anatomopatologie Bioclinica Arad.
**Timp estimat:** 7-14 zile lucrătoare (estimare 24.04-01.05.2026).
**Monitor automat:** activ (GitHub Actions → ntfy.sh, verificare portal Bioclinica la 30 min, 24/7).
**Importanță:** diagnostic de certitudine (tip histologic — adenocarcinom vs. scuamocelular, grad de diferențiere, markeri moleculari relevanți pentru decizia terapeutică).

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

### 8.2 Reluare Jamesi (H+48 post-CT) — 22.04.2026 AZI

**Status:** **AZI**. Creatinina pre-CT era 0.83 mg/dL (normală). În absența unei deteriorări suspecte a funcției renale post-CT (care necesită test de control), Jamesi se reia conform schemei zilnice (1-0-1, 50/1000 mg).

**De monitorizat:** glicemie de control, orice semn de afectare renală (scădere diureză, edeme, senzație de vertij).

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

| Specialitate                                                   | Medic                                                                                                          | Unitate                                    | Contact              |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | -------------------- |
| Gastroenterologie                                              | Dr. Noufal Abdul Vahab (medic primar)                                                                          | Genesis Medical Clinic Arad                | De completat         |
| **Radiologie și Imagistică (CT 20.04.2026)**                   | **Dr. Buie Florian-Laurențiu (cod A11818)** + **Dr. Candea Florin-Vasile (cod F52510)** — ambii medici primari | **Genesis Medical Clinic Micălaca**        | Prin Genesis         |
| Anatomopatologie (biopsie esofag)                              | De identificat (Bioclinica Arad)                                                                               | Bioclinica Arad                            | `arad@bioclinica.ro` |
| Cardiologie (SCA ST+ 2012)                                     | Echipa Vichy, Franța — de identificat pe PDF                                                                   | Centre Hospitalier de Vichy (de confirmat) | —                    |
| Cardiologie / Medicină internă (prescriere actuală 10.11.2025) | Dr. LAZĂR [nume parțial ilizibil]                                                                              | De identificat                             | —                    |
| Diabetologie / prescriere Jamesi                               | Dr. LAZĂR (probabil, din prescrierea 10.11.2025)                                                               | De identificat                             | —                    |
| Medic de familie                                               | De identificat                                                                                                 | De identificat                             | —                    |
| Chirurgie Generală (hernie 28.11.2025)                         | De identificat din documentul original                                                                         | Secția Chirurgie Generală II               | —                    |
| Urologie / Gastroenterologie (consult 28.10.2025)              | De identificat                                                                                                 | De identificat                             | —                    |
| **Oncologie digestivă** (prioritate URGENT)                    | **De stabilit**                                                                                                | Arad / Timișoara / Cluj / București        | —                    |
| Endocrinologie (glandă suprarenală, follow-up)                 | De stabilit post-consult oncolog                                                                               | —                                          | —                    |

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
3. Biopsia în lucru (Bioclinica, estimat 24.04-01.05); **consult oncolog URGENT** de programat — posibil protocol FLOT; reluare Jamesi AZI 22.04 H+48 post-CT.

---

**Istoric versiuni:** vezi `arhiva/` pentru versiunile anterioare ale acestui fișier.
**Următoarea actualizare planificată:** la primirea rezultatului biopsiei (histologie) SAU la primul consult oncolog digestiv.
