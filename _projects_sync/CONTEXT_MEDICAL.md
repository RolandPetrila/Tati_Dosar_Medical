# CONTEXT_MEDICAL.md — Starea medicală actuală

**Fișier central de stare.** Se actualizează la fiecare informație medicală nouă. Ultima modificare trebuie reflectată în antetul de mai jos și în `CHANGELOG.md`.

---

**Ultima actualizare:** 29 aprilie 2026 19:24 (multi-eveniment: **(1) REPROGRAMARE 30.04 ÎNLOCUIEȘTE 4.05** — consultul cu Dr. Anater 4.05 anulat; consultul oncolog primary devine 30.04.2026 ora 12:00 OncoHelp Timișoara cu Dr. Mate Endre care va prelua dosarul medical și va începe discuția în prima fază; **(2) ANALIZE 29.04 EFECTUATE** — buletin Bioclinica 26429A0020: CEA 0,87 normal · CA 19-9 27,00 borderline · CA 72-4 18,59 ELEVAT 2,7x · HbA1c 7,5% diabet suboptimal; **(3) REZULTAT BIOPSIE 17.04 PRIMIT 28.04** — INCONCLUZIV; **(4) PDF VICHY 2012 PROCESAT INTEGRAL** — stent confirmat **BMS** (NU DES) → schimbă substanțial calculul perioperator pentru chirurgia esofagiană; **(5) Cardiolog 30.04 ora 08:30** confirmat — secvență coerentă: cardio Arad dimineață → Timișoara prânz consult oncolog.)
**Responsabil dosar:** Roland Petrilă (fiul pacientului)
**Versiune structură:** 1.8 (integrare PDF Vichy complet — BMS confirmat, echipă franceză identificată; programare nouă 30.04 Mate Endre OncoHelp; reconfirmare cardiolog 30.04 ora 08:30; flow OncoHelp clarificat per documente oficiale)
**Versiune anterioară arhivată:** `Dosar_Medical/arhiva/context_medical_versiuni/CONTEXT_MEDICAL_pre-vichy-stent-bms_2026-04-28_1045.md` + `CONTEXT_MEDICAL_pre-biopsie-rezultat_2026-04-28_0845.md` + versiunile anterioare (vezi arhiva).

---

### Convenție marcaje certitudine (R17 + R22 — aplicare în acest fișier)

Acest fișier este **state file intern** (sursă pentru documentele de ieșire), nu document final trimis medicilor. Aplicarea R17 (marcaje obligatorii pe `output docs`) + R22 (zero afirmații fără sursă în fișiere de referință) se face astfel:

- **`[CERT]`** — afirmație factuală confirmată din sursă primară (JSON canonic din `Dosar_Medical/`, RCP/SmPC oficial, ghid ESMO/NCCN/AJCC, studiu peer-reviewed). Sursa citată în ultima linie a secțiunii relevante.
- **`[PROBABIL]`** — susținut de literatura medicală standard, estimare clinică a unui medic, sau inferare rezonabilă; nu sursă primară directă.
- **`[INCERT]`** — conflict între surse, extrapolare de la alt context, lacună date care necesită clarificare.
- **`[NEGASIT]`** — căutat explicit în surse și neidentificat; listăm unde s-a căutat.

**Valori default fără marcaj explicit** = `[CERT]` cu sursă în JSON-ul sursă menționat în referința secțiunii (`Sursă:` la finalul secțiunii). Afirmațiile care NU sunt factuale (concluzii clinice preliminare, opțiuni terapeutice, întrebări deschise) NU necesită marcaj — dar secțiunea menționează explicit natura lor în titlu (ex: „§10 Evaluare preliminară").

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

**Status histologic la 28.04.2026:** Biopsia 17.04 prelevată endoscopic = **INCONCLUZIVĂ** — „țesut de granulație pe fond de ulcerație cronică, doar SUGESTIV pentru infiltrat carcinomatos" `[CERT]`. NU confirmă, NU infirmă carcinomul. Suspiciunea clinico-imagistică (CT + endoscopie + simptome) **persistă**, dar diagnosticul histologic de certitudine necesită **imunohistochimie (IHC) pe blocul existent T26H06044** sau **rebiopsie țintită** (decizie la consult 30.04 ora 12:00 OncoHelp Timișoara cu Dr. Mate Endre). Vezi §7.4.

**Context:** Leziune identificată la endoscopie digestivă superioară (17.04.2026, Dr. Noufal Abdul Vahab, Genesis Medical Clinic Arad). Biopsie prelevată — **rezultat histopatologic primit 28.04.2026 (Bioclinica SA Timișoara, semnat Dr. Glăja Romanița), inconcluziv (vezi §7.4)**. CT TAP N+SDC de stadializare efectuat luni **20.04.2026 ora 17:00** la Genesis Medical Clinic Micălaca, raport semnat de Dr. Buie Florian-Laurențiu (cod parafă A11818) + Dr. Candea Florin-Vasile (cod parafă F52510), ambii medici primari radiologie.

> **Restructurare R24 aplicată 2026-04-24** (post-audit `AUDIT_EXTRAGERE_2026-04-24.md` Batch A): secțiunea 2 reorganizată în 5 sub-secțiuni (Findings principale / secundare / colaterale / parametri tehnici / referință sursă) pentru paritate completă cu `Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json`. Backup pre-restructurare: `Dosar_Medical/arhiva/context_medical_versiuni/CONTEXT_MEDICAL_pre-batchA-r24-CT_2026-04-24_0230.md`.

### 2.1 Findings principale CT 20.04.2026 (impact decizional direct)

**Stadializare imagistică preliminară** `[PROBABIL]` — estimativă per radiolog, necesită corelare cu biopsie pentru confirmare histologică:

| Element       | Estimare CT           | Marcaj       | Note                                                                                                                                         |
| ------------- | --------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **T** (tumor) | T3–T4                 | `[PROBABIL]` | Proces expansiv infiltrativ circumferențial cu extensie loco-regională, densificarea grăsimii peritumorale                                   |
| **N** (nodes) | N0–N1                 | `[PROBABIL]` | Limfonoduli loco-regionali max 7.5 mm `[CERT]` (sub pragul standard <10 mm, dar în context neoplazic pot fi relevanți)                       |
| **M** (meta)  | **M0 probabil**       | `[PROBABIL]` | Fără metastaze hepatice, pulmonare, osoase, ganglionare distale vizibile pe CT `[CERT]`                                                      |
| **Siewert**   | II probabil           | `[PROBABIL]` | Joncțiune eso-gastrică propriu-zisă, centrată pe cardia cu extensie eso-distală și fundică                                                   |
| **ATENȚIE**   | **Ascită de evaluat** | `[CERT]`     | Colecție fluidă perihepatică 15 mm + intrapelvină 28 mm `[CERT]` → de exclus CARCINOMATOZĂ PERITONEALĂ `[INCERT]` (ar echivala cu stadiu IV) |

**Natura histologică a leziunii:** `[INCERT]` — neclarificată. Biopsia în lucru la Bioclinica Arad va preciza tipul exact (adenocarcinom vs. carcinom scuamocelular, grad de diferențiere). Localizarea distală + extensia fundică sugerează **adenocarcinom** `[PROBABIL]` (pattern tipic Siewert II per literatura de specialitate), dar confirmarea aparține histopatologului.

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
- **PDF sursă:** `Dosar_Medical/documente_sursa/11_CT_stadializare_2026/2026-04-20_ct_torace_abdomen_pelvis.pdf` (mutat de user 2026-04-24 din `99_altele/` în folder dedicat; redenumit 2026-04-28 din `CT - Genesys.pdf` conform R26)
- **Data extragere JSON:** 2026-04-22
- **Data audit R24 + restructurare:** 2026-04-24
- **Marcaj `.meta.json`:** `"completeness_verified": "2026-04-24"`, `"coverage": "100%"` (post-audit Batch A)
- **Confidence overall:** high (PDF digital nativ, text extractabil, fără OCR)

### 2.6 Acțiuni în curs (status la 2026-04-28 10:50 — post programare 30.04 + PDF Vichy procesat)

**🔴 SECVENȚĂ ZILEI 30.04.2026 (CRITICĂ — 3 evenimente într-o zi):**

1. **08:30 Arad — consult cardiologic ambulator** (programare confirmată 27.04). Solicită: ECG + ECO + scrisoare medicală cu FEVS + aviz perioperator. ⚠ **Adăugat 28.04 după PDF Vichy:** menționează cardiologului că stent-ul implantat 2012 este **BMS (Bare Metal Stent)** — nu DES — relevant pentru evaluarea DAPT și pauzei pre-chirurgie.
2. **~10:00 Plecare Arad → Timișoara** (~50 km, ~1h cu mașina; rezervă suficientă)
3. **12:00 Timișoara — consult oncolog OncoHelp cu Dr. Mate Endre** (Str. Ciprian Porumbescu nr. 57-59) — programare obținută telefonic 28.04 prin Dr. Vornicu Vlad-Norin. **Scop:** consult primar oncolog — Dr. Mate Endre va prelua dosarul medical și va începe discuția în prima fază (luare în evidență + decizie pași diagnostici post-biopsie inconcluzivă). **Acest consult ÎNLOCUIEȘTE programarea anterioară din 4 mai cu Dr. Anater** (decizie user 29.04). **Tata este OPȚIONAL** — pot veni doar Roland + Maria cu documentația.

- ✅ **CT efectuat 20.04.2026** — raport integrat în dosar
- ✅ **Rezultat biopsie esofagiană PRIMIT 28.04.2026** (Bioclinica SA Timișoara, buletin 26417A0362 / cod T26H06044, semnat Dr. Glăja Romanița 27.04). **CONCLUZIE: inconcluzivă — „țesut de granulație + ulcerație cronică, doar SUGESTIV pentru infiltrat carcinomatos"** `[CERT]`. Limitare explicită: număr mic celule epiteliale atipice. **Recomandare laborator: IHC pe blocul T26H06044** pentru diagnostic de certitudine. Vezi §7.4.
- ✅ **Markeri tumorali + HbA1c — efectuate 29.04.2026** (Bioclinica Nădlac, buletin 26429A0020): CEA 0,87 normal · CA 19-9 27,00 borderline · CA 72-4 18,59 ELEVAT 2,7x · HbA1c 7,5% diabet suboptimal. Vezi §7.6.
- 🔴 **DECIZIE PENDENTĂ ONCOLOG 30.04** — opțiuni pentru diagnostic histologic de certitudine: **(a) IHC pe blocul existent T26H06044** (rapid, fără reintervenție; recomandat de anatomopatolog), **(b) rebiopsie țintită endoscopică ± EUS**, **(c) combinare**. Decident: Dr. Mate Endre la consult OncoHelp.
- 🔴 **Monitor automat ntfy.sh** → **DEZACTIVARE necesară** (rezultat primit; flag .DETECTED activat).
- 🟡 **Pași ulteriori (TBD la consultul 30.04)**: comisie oncologică OncoHelp + opinie chirurg eso pentru posibilitate rezecție + plan terapeutic FLOT vs alternative. Posibilă intervenție laparoscopică ulterioară pentru evaluarea peritoneului (excludere carcinomatoză).
- 🟡 **Evaluare endocrinologică** glanda suprarenală stângă — de programat post-consult oncolog
- ✅ **Jamesi reluat** 22.04.2026 seara, conform schemei standard (1-0-1, 50/1000 mg), **fără complicații** — pauza H-48h → H+48h a funcționat corect, fără simptome renale post-contrast raportate de familie
- 🟡 **Spirometrie + anamneză pulmonară pre-esofagectomie** (post audit Batch A 2026-04-24) — de discutat cu chirurgul oncolog: tulburările ventilație posterobazal LID+LIS + nodulii apicali sechelari LSD necesită evaluare pulmonară pre-operator (spirometrie + DLCO + posibil consult pneumolog)
- ✅ **Programări 27.04 confirmate:** analize Bioclinica 29.04 (CEA + CA 19-9 + HbA1c) · cardiolog 30.04 · bilete trimitere Dr. Orbán obținute (oncologie + cardiologie) · CD DICOM la dosar

---

## 3. Antecedente medicale personale

### Boală cardiacă ischemică cu stent (februarie 2012)

**Status clinic:** Sindrom coronarian acut ST+ (STEMI) antero-septo-apical pe stenoză a arterei interventriculare anterioare (IVA) — proximală 70-90% + mijlocie subocluzivă 90-99% `[CERT]` (per coronarografie 17.02.2012).

#### Eveniment acut + intervenție (cronologie completă)

- **13.02.2012** (estimat — «în urmă cu trei zile»): primă durere toracică la efort, ~10 minute, în timpul ridicării de greutăți
- **16.02.2012 noaptea:** recidivă durere toracică nocturnă, durată scurtă
- **17.02.2012 ~04:00:** durere toracică continuă → preluare SAMU pentru SCA
- **17.02.2012 07:45:** fibrinoliză cu **tenecteplază (Metaliză)** — succes (flux TIMI 3 restabilit, durere dispărută)
- **17.02.2012 09:54-10:37:** coronarografie de control la Vichy (Procedura nr. **11829**, Dr. Pierre LAVAUD) — confirmă stenozele IVA + circumflexa cu leziune sub 50% pe marginală, coronara dreaptă fără leziuni
- **17.02.2012:** decizie temporizare angioplastie (TIMI 3 obținut)
- **19.02.2012 16:05:** coronarografie + **angioplastie cu implantare stent** la Centrul de Cardiologie de Intervenție din Allier (Moulins-Yzeure) — Procedura nr. **11836**, operator Dr. Xavier MARCAGGI + Dr. Gabriel BITAR (A.OP); cale: artera radială dreaptă, 6 French
- **21.02.2012:** asimptomatic, transfer la cardiologie (mobilizare)
- **23.02.2012:** examen clinic fără insuficiență cardiacă, fără durere toracică, fără anomalii repolarizare ECG (persistă supradenivelare ST V2V3)
- **24.02.2012** (estimat): întoarcere în România cu mașina, împreună cu soția

#### Detalii stent — CRITIC pentru evaluare pre-chirurgie esofagiană

| Element                     | Valoare                                                                                 | Marcaj                                                              |
| --------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Tip stent**               | **BMS (Bare Metal Stent / „stent gol")** — RX VISION 3.5 × 28 mm Abbott Nr. **1110341** | `[CERT]` (confirmat dublu în doc: text Marcaggi + concluzie raport) |
| **Locație**                 | IVA proximală (după predilatare cu balon Apex 2.5 × 20 Boston Scientific)               | `[CERT]`                                                            |
| **Material complet**        | Sondă LAUNCHER EBU 3.5 6F 100 cm Medtronic + ghid TERUMO J + ghidaj BMW Abbott          | `[CERT]`                                                            |
| **Rezultat final**          | Succes primar — fără leziune semnificativă reziduală, flux TIMI 3 normal                | `[CERT]`                                                            |
| **Complicații procedurale** | niciuna                                                                                 | `[CERT]`                                                            |

**Implicație clinică pentru consult oncolog 30.04 + planificare chirurg eso ulterior `[PROBABIL]` (per ghiduri ESC 2017 + ACC/AHA):**

- BMS la 14 ani vechime → endotelizare completă cu mult timp în urmă; risc tromboză in-stent **<1%** la pauza temporară de aspirină
- DAPT (dual antiplatelet therapy) standard BMS = **1 lună post-stent** (vs 6-12 luni pentru DES) — pacientul a continuat doar Aspenter (monoterapie)
- Pentru chirurgie majoră non-cardiacă: pauza Aspenter **5-7 zile pre-op** este în general sigură pentru BMS >12 luni
- **Schimbă substanțial calculul perioperator** vs. ipoteza inițială (DES nedocumentat) — risc cardiovascular mai mic decât presupus, esofagectomie devine mai accesibilă

#### Tratament în acut (2012)

- Fibrinoliza primară pre-spital: **tenecteplază (Metaliză)** la 07:45
- Adjuvant la internare: **PLAVIX** (clopidogrel) + **ASPEGIC** (acid acetilsalicilic) + **LOVENOX** (enoxaparină s.c.)
- Vârf troponină: 150 (unitate neclarificată în traducere) cu descreștere documentată

#### Antecedente declarate la momentul 2012 (per documentul Vichy)

- **Tabagism activ** `[CERT]` (a renunțat la fumat post-eveniment cardiac, conform §5)
- **Obezitate** `[CERT]` (greutate 85 kg la 2012; 79 kg actual 2026 — scădere 6 kg în 14 ani)
- DZ tip 2 `[NEGASIT]` în acest document — probabil dezvoltat ulterior 2012
- HTA `[NEGASIT]` în acest document — confirmat ulterior

⚠ **Anomalie de transcriere în PDF:** înălțime declarată 178 cm (coronarografie 17.02) vs 168 cm (angioplastie 19.02) — discrepanță 10 cm. Per IMC + diagnostic „Obezitate", **168 cm e mai probabil corect** (IMC 30.1 = obezitate clasa I). De clarificat cu user la oportunitate.

**Spital:** Centrul Spitalicesc **Jacques Lacarin Vichy** (Bulevardul Denière, 03207 Vichy Cedex) + Centrul Spitalicesc Moulins Yzeure — Centrul de Cardiologie de Intervenție din Allier (unde s-a făcut angioplastia).

**Echipa franceză 2012** (cf. §9 — istoric extern):

- **Coordonator:** Dr. Xavier MARCAGGI (operator angioplastie 19.02)
- **Șefii secției:** Dr. Eddie PIERRE-JUSTIN + Dr. Georges AMAT
- **Operator coronarografie 17.02:** Dr. Pierre LAVAUD (medic atașat Vichy)
- **A.OP angioplastie:** Dr. Gabriel BITAR (Vichy)
- **Medici generaliști în echipă:** Dr. Jean Jacques CLOIX (Moulins) + Dr. Raphael RODRIGUEZ (Moulins)
- **Interni implicați:** Djamel ADJTOUTAH (raport spitalizare) + Xavier CHABIN + Armel NANA

**Continuitate medic familie:** la 19.02.2012 echipa Vichy a luat contact cu **Dr. Orbán Ecaterina, Nădlac** (telefon 0040 723 560 193, per documentul francez). Aceeași persoană este medicul de familie actual în 2026 (Dr. Orbán Ecaterina-Maria, cod parafă 718705) — **continuitate de 14 ani** `[CERT]`.

**Consecință practică:** necesită antiagregare plachetară pe termen lung (Aspenter 75 mg, confirmat prin schema din 10.11.2025); LDL actual 133 mg/dL (țintă ESC <70 mg/dL post-stent — neatinsă, statină prescrisă dar nealuată — vezi §4).

**Date încă de completat:**

- Cardiolog curant din România după repatriere 2012 → 2024 (Dr. Post Mihaela 2024 UPU + Dr. LAZA Cristina 2025 ambulator confirmate)
- Eventuale controale coronarografice ulterioare 2012 — `[NEGASIT]` în dosar

**Sursă:** `Dosar_Medical/2012-02-17_cardiologie_vichy_stent.json` (v2 — Claude Opus 4.7, 2026-04-28, extragere completă din PDF) + `documente_sursa/02_cardiologie_2012/2012-02-17_cardiologie_vichy_stent.pdf` (10 pagini, traducere autorizată Blidar Ioana, autorizație 705/2002 Ministerul Justiției; redenumit 2026-04-28 din `Document_Cardiologie_Vichy_2012.pdf` conform R26) + `2012-02-17_cardiologie_vichy_stent_extragere.md` (MD strict-extractive paralel cu JSON canonic).

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

| Medicament                                                     | Indicație                                                | Doză                  | Ritm                  | Note                                                                                                                                                       |
| -------------------------------------------------------------- | -------------------------------------------------------- | --------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Jamesi** (sitagliptin + clorhidrat de metformin)             | Diabet zaharat tip 2                                     | 50 mg / 1000 mg       | 1-0-1 (dim. și seara) | **CRITIC**: componenta metformin se oprește 48h înainte de CT cu contrast. **HbA1c 7,5% (29.04.2026) → control suboptimal** vs țintă ADA <7,0% (vezi §7.6) |
| **Aspenter** (acid acetilsalicilic)                            | Antiagregant post-stent coronarian 2012                  | 75 mg                 | 0-1-0 (prânz)         | NU se oprește pentru CT                                                                                                                                    |
| **Concor** (fumarat de bisoprolol)                             | Beta-blocant (cardioprotecție + HTA + control frecvență) | 5 mg                  | 1-0-0 (dimineața)     | Nu se oprește pentru CT                                                                                                                                    |
| **Triplixam** (perindopril arginine + indapamidă + amlodipină) | Antihipertensiv combinație triplă                        | 10 mg / 2.5 mg / 5 mg | 1-0-0 (dimineața)     | Nu se oprește pentru CT                                                                                                                                    |

**Notă:** manuscrisul conținea o a 5-a recomandare tăiată cu marker albastru (anulată).

**Suplimente alimentare:** de verificat cu familia.

**Sursă:** `Dosar_Medical/2025-11-10_schema_medicamente.json` (manuscris parțial + fotografii cutii). Medicamentele, dozele și ritmul de administrare sunt `[CERT]` (fotografii cutii + manuscris lizibil pentru ritm). Medicul prescriptor identificat retroactiv 2026-04-24: **Dr. LAZA CRISTINA (cod parafă C07842)** via cross-reference ECO tipărită aceeași zi.

### Observație clinică — statină nealuată curent (de evaluat la consult oncolog 4.05)

**Context (clarificat de user 2026-04-25):** scrisoarea medicală Dr. LAZA CRISTINA din 10.11.2025 (`2025-11-10_scrisoare_medicala_cardiologie.json`) prescrisese **TORVACARD 10/20 mg 0-0-1 seara**, însă pacientul **NU îl administrează curent** — schema reală în vigoare este cea manuscrisă în aceeași zi (cele 4 medicamente din tabelul de mai sus, fără statină). Documentele sursă confirmă: folder `Dosar_Medical/documente_sursa/08_schema_tratament/` (manuscris talon + foto cutii Aspenter, Concor, Triplixam, Jamesi).

**Relevanță pre-esofagectomie** `[CERT]`:

- Pacient post-stent coronarian 2012 → ghidurile AHA/ESC recomandă statină continuă pentru prevenție CV secundară
- **Lipidogramă 17.06.2025** (`Dosar_Medical/2025-06-17_buletin_analize_sange.json`): colesterol total 189, **LDL 133 mg/dL** — țintă ESC 2019/2021 post-stent: <70 mg/dL → ținta neatinsă
- De ridicat la **consultul oncolog 30.04.2026 ora 12:00 OncoHelp Timișoara — Dr. Mate Endre** + medicul de familie Dr. Orbán: reevaluare prevenție CV secundară pre-chirurgie esofagiană

**Paritate R24:** TORVACARD apare în JSON-ul scrisorii (chain of custody intact — nu se modifică sursa) și este reflectat aici ca observație clinică, nu ca prescripție efectivă.

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
**Medic:** Dr. Noufal Abdul Vahab, medic primar gastroenterologie · telefon **0735 447 449**

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

### 7.4 Rezultat biopsie esofagiană 17.04.2026 — PRIMIT 28.04.2026 (INCONCLUZIV)

**Status:** ✅ rezultat primit; monitor automat dezactivat.

**Buletin:** Bioclinica SA, nr. **26417A0362**, cod diagnostic lab **T26H06044**.
**Recoltat:** 17.04.2026 14:21 (Bioclinica Vlaicu Arad — la endoscopia Genesis, Dr. Noufal).
**Lucrat:** Bioclinica SA, CAL Torontalului 1, Timișoara.
**Raport semnat:** 27.04.2026 — Dr. Glăja Romanița (medic primar anatomopatolog, cod parafă **367427**).
**Macroscopie:** Dr. Teoran Samy Ștefan (medic specialist, cod parafă **G70575**).
**PDF generat:** 28.04.2026 06:46.

#### Findings

**Macroscopic** `[CERT]`: 2 piese biopsice 0,2 / 0,1 / 0,1 cm — sub-milimetrice, aspect neregulat, cafenii, elastice; 1 bloc parafină procesat, orientare totală fără secționare (block T26H06044-A1).

**Microscopic — componenta dominantă** `[CERT]`: numeroase structuri vasculare cu endoteliu tumefiat, hiperemiate, cu marginație leucocitară + manșon leucocitar; suprafață acoperită parțial de **detritus și necroză fibrinoidă**; elemente celulare inflamatorii mononucleate. Pattern compatibil cu **țesut de granulație** pe ulcerație cronică.

**Microscopic — componenta atipică minoritară** `[INCERT]`: aparent celule epitelioide de talie medie, cu **nucleu nucleolat, nucleol eozinofil**, citoplasmă moderată palid colorată / slab eozinofilă, singulare/grupate. Caracteristici nucleare compatibile cu adenocarcinom moderat diferențiat `[PROBABIL]`, dar **insuficiente cantitativ** pentru diagnostic de certitudine.

**Fragment secundar** `[CERT]`: epiteliu stratificat scuamos nekeratinizat (mucoasă esofagiană normală) cu exocitoză neutrofilă + extravazate hematice — fără valoare diagnostică tumorală.

#### Concluzia raportului `[CERT]` (text original)

> „Ansamblul histologic, pe secțiuni seriate și în colorația uzuală, **pledează pentru țesut de granulație pe fond de ulcerație cronică, fiind doar sugestiv pentru infiltrat carcinomatos.**"

#### Nota laboratorului `[CERT]` (text original)

> „De corelat cu datele endoscopice/imagistice (**diagnostic histologic tumoral mult limitat de numărul mic al celulelor epiteliale atipice**); eventuală evaluare imunohistochimică pentru diagnostic histologic de certitudine și conduită terapeutică."

#### Interpretare clinică sintetizată

| Element                                          | Verdict                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Confirmare histologică de cancer                 | **Niciuna** `[CERT]` — sugestiv ≠ confirmat                                                                                                                                                                                                                                                |
| Infirmare carcinom                               | **Nu** `[CERT]` — celule atipice prezente; absența confirmării e _tehnică_ (cantitate de țesut), nu definitivă                                                                                                                                                                             |
| Suspiciune clinico-imagistică                    | **Persistă ridicată** `[PROBABIL]` (CT T3-T4, stenoză circumferențială, ascită, simptome — neschimbate)                                                                                                                                                                                    |
| Tip tumoral                                      | **Nedeterminat** `[INCERT]` — celulele atipice par epitelioide/glandulare → compatibil adenocarcinom, dar fără IHC nu se poate confirma                                                                                                                                                    |
| Stadializare imagistică                          | **Neschimbată** `[CERT]` — rămâne T3-T4 / N0-N1 / M0 probabil per CT 20.04 până la confirmare histologică                                                                                                                                                                                  |
| Cauză probabilă a inconcluzivității `[PROBABIL]` | Pattern clasic la biopsii prelevate de pe leziuni stenozante/ulcerate: prelevarea conține în principal _crusta inflamatorie superficială_ (granulație + necroză + detritus) și prea puține celule din _stratul tumoral profund_; consistent cu CT „infiltrativ" + endoscopie „nedepășibil" |

#### Pași următori — opțiuni standard pentru diagnostic de certitudine

1. **IHC pe blocul existent T26H06044** `[PROBABIL — recomandat de anatomopatolog]` — markeri propuși clinic: pan-CK (citokeratine), CK7/CK20, CDX-2, p53; eventual HER2 / PD-L1 / MSI dacă se confirmă carcinom (relevanță decizie terapeutică). **Avantaj:** rapid (3-7 zile), fără reintervenție. **Dezavantaj:** dacă celulele atipice sunt prea puține, IHC poate fi tot inconcluziv.
2. **Rebiopsie endoscopică țintită** cu fragmente mai numeroase, mai profunde — eventual sub ghidaj **EUS (ecoendoscopie)** pentru biopsie din strat profund. **Avantaj:** randament diagnostic superior. **Dezavantaj:** necesită reintervenție + timp suplimentar.
3. **Combinare IHC + rebiopsie programată în paralel** — variantă mixtă, decisă de oncolog/comisie tumor board.

**Decident:** Dr. Mate Endre, consult **30.04.2026 ora 12:00 OncoHelp Timișoara** (consult primar cu preluare dosar medical complet).

**Sursă document:** `Dosar_Medical/2026-04-17_biopsie_esofagiana_histopatologic.json` + `documente_sursa/12_biopsie_2026/2026-04-17_biopsie_esofagiana_histopatologic.{pdf,md,pdf.meta.json}` (PDF oficial Bioclinica descărcat de user 28.04 09:09; JPEG intermediar șters R-MINIMAL).

**Trimis Dr. Anater + OncoHelp:** mailul cu PDF atașat trimis de user pe 28.04.2026 09:37 ora României (mesaj `19dd2ce9816692eb` în thread `19dbe7d30cfacbb3`); destinatari: `angelo.anater@oncohelp.ro` + `angelo.anater95@yahoo.com` + `programari@oncohelp.ro` + `office@oncohelp.ro`. Vezi `Dosar_Medical/corespondenta/2026-04-24_re-solicitare-consult-anater.md` (cronologie extinsă) — așteptăm răspuns Anater.

### 7.5 Bilet trimitere CT (17 aprilie 2026) — document administrativ declanșator

**Serie/Număr:** **BCTAP 0631727**.
**Emitent:** Dr. Noufal Abdul Vahab (cod parafă C 11074), Genesis Medical Clinic Arad (CUI R20295098, Bd. Revoluției nr. 3).
**Casa asigurări:** CAS AR, nr. contract/convenție 1148.
**Nivel prioritate:** Ambulator Specialitate (bifat).
**Cod diagnostic (intern CAS):** 95 — „PROCES PROLIFERATIV ESOFAGIAN".
**Investigații recomandate:** CT TORACE (SDC) + CT ABDOMEN (SDC) + CT PELVIS (SDC) — toate cu substanță de contrast.

**A declanșat:** CT efectuat 20.04.2026 la Genesis Medical Clinic Micălaca (vezi §2).

**Sursă:** `documente_sursa/11_CT_stadializare_2026/2026-04-17_bilet_trimitere_CT_BCTAP_0631727.jpeg` + `Dosar_Medical/2026-04-17_bilet_trimitere_CT.json`.

### 7.6 Markeri tumorali + HbA1c (29 aprilie 2026, Bioclinica Nădlac) — pre-consult oncolog 30.04

**Status:** ✅ **EFECTUAT 29.04.2026** — recoltare matinală à jeun (07:22), buletin generat aceeași zi 18:08.

**Buletin:** Bioclinica SRL Arad, nr. **26429A0020**, punct recoltare 00036 Bioclinica Nădlac.
**Validator final:** Dr. Luminița Statnic (medic primar medicină de laborator, cod **A08064**).
**Trimitere:** Dr. Orbán Ecaterina-Maria (medic familie Nădlac).
**Scop:** pregătire consult oncolog 30.04.2026 ora 12:00 OncoHelp Timișoara cu Dr. Mate Endre.

#### Rezultate

| Analiză                                | Rezultat       | Interval normal             | Flag         | Metodă                            | Acreditare   |
| -------------------------------------- | -------------- | --------------------------- | ------------ | --------------------------------- | ------------ |
| **Antigen carcino embrionar (CEA)**    | **0,87 ng/mL** | < 3,80 (nefumători)         | normal       | ser, ECLIA                        | RENAR        |
| **CA 19-9**                            | **27,00 U/mL** | < 27,00                     | borderline   | ser, ECLIA                        | RENAR        |
| **Hemoglobină glicozilată (HbA1c)**    | **7,5 %**      | 4,0 - 5,6 (țintă ADA <7,0%) | peste limită | sânge integral EDTA, Ion-ex. HPLC | RENAR        |
| **CA 72-4ˢ** (subcontractat Timișoara) | **18,59 U/mL** | < 6,90                      | peste limită | ser, ECLIA                        | NU subcontr. |

**Subcontractor CA 72-4:** Bioclinica Timișoara (cod laborator **26429T2632**, BLD Cetății 53B, Bioclinica SA), medic raportor Dr. Gaiță Pîrvan Corina (cod parafă **D15815**). Per nota explicativă a buletinului: analizele subcontractate (marcaj `s`) NU sunt acoperite de acreditarea RENAR pentru subcontractor.

**Medic raportor HbA1c:** Dr. Vorindan Anca Laura (cod parafă **A07744**).

#### Interpretare clinică sintetizată

| Element                                                                     | Verdict                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CEA — pattern cancer eso-gastric                                            | **Normal** `[CERT]` — sub limita nefumători (pacient cu 14 ani de abstinență tabagică). CEA poate fi normal în adenocarcinoame gastrice până la 30-50% din cazuri, mai ales în stadii localizate; nu exclude diagnosticul.                                                                                                                                     |
| CA 19-9                                                                     | **La limita superioară** `[CERT]` — exact la 27,00 U/mL. CA 19-9 = marker asociat cu adenocarcinom pancreatic, biliar, gastric, esofagian; valori la limită necesită monitorizare evolutivă comparativă.                                                                                                                                                       |
| **CA 72-4 — marker specific gastric**                                       | **Elevat ~2,7x limită** `[CERT]` (18,59 vs <6,90). CA 72-4 are specificitate ridicată pentru adenocarcinom gastric / gastro-esofagian (ovarian secundar). Sensibilitate 30-50%, **specificitate superioară CA 19-9** pentru patologia gastrică. Adăugat la recoltare ca marker suplimentar specific Siewert II suspect (CT 20.04.2026).                        |
| Implicații clinice combinate (CEA normal + CA 19-9 limită + CA 72-4 elevat) | **Pattern compatibil cu adenocarcinom gastric / joncțional cu producție selectivă de mucină** `[PROBABIL]`. Markerii nu confirmă diagnosticul (rezervat IHC/biopsie), dar **întăresc suspiciunea clinico-imagistică** a CT-ului 20.04 + biopsiei 17.04. **NU înlocuiesc consultul medical** — interpretarea finală aparține Dr. Mate Endre (30.04 ora 12:00).  |
| HbA1c — control glicemic                                                    | **Diabet zaharat confirmat** `[CERT]` (≥6,5% per ADA). **Control suboptimal** `[CERT]` cu schema actuală — depășește ținta ADA <7,0% pentru pacient >20 ani. Glicemia medie estimată ultimele 2-3 luni: ~169 mg/dL. **Implicații pre-tratament oncologic:** controlul glicemic suboptimal afectează vindecare anastomotică și risc complicații post-chirurgie. |

#### Markeri tumorali — **NU se folosesc pentru diagnostic primar**

Markerii tumorali serici sunt instrumente complementare, NU substitut pentru diagnosticul histologic. Rolul lor principal:

1. **Baseline pre-tratament** — referință pentru monitorizarea evoluției sub chimioterapie / post-chirurgie.
2. **Monitorizare răspuns terapeutic** — scădere = răspuns probabil; creștere persistentă = progresie/recidivă.
3. **Sugestie suplimentară** la datele clinico-imagistice deja prezente.

**Decizie finală conduită terapeutică:** la consultul Dr. Mate Endre 30.04 ora 12:00 + comisia oncologică OncoHelp (pași ulteriori), după rezultatele IHC pe blocul T26H06044 sau rebiopsie țintită (vezi §7.4).

#### Sursă document

`Dosar_Medical/2026-04-29_buletin_bioclinica_markeri_tumorali_hba1c.json` + `documente_sursa/16_analize_markeri_2026_04/2026-04-29_buletin_bioclinica_markeri_tumorali_hba1c.{pdf,pdf.meta.json}` + extragere strict-extractivă `2026-04-29_buletin_bioclinica_markeri_tumorali_hba1c_extragere.md`.

---

## 8. Investigații programate / în așteptare

### 8.1 Consult oncolog digestiv — 🔴 30 aprilie 2026 ora 12:00 OncoHelp Timișoara (Dr. Mate Endre)

**Status:** 🔴 **PROGRAMAT 30.04.2026 ora 12:00** [obținut telefonic 28.04 prin Dr. Vornicu Vlad]. **Acest consult ÎNLOCUIEȘTE programarea anterioară din 4 mai cu Dr. Anater** (decizie user 29.04.2026).

**Detalii programare:**

- **Data:** **30 aprilie 2026 (joi), ora 12:00**
- **Unitate:** **OncoHelp Timișoara**
- **Medic oncolog:** **Dr. Mate Endre** — va prelua dosarul medical și cu el va începe discuția în prima fază
- **Format:** consult primar — luare în evidență la OncoHelp + preluare dosar medical complet + discuție inițială asupra cazului
- **Prezență:** Roland + Maria + dosarul fizic (fără tata e OK pentru această fază)

**Anularea consultului 4.05 cu Dr. Anater:**

> **Decizie user 29.04.2026:** consultul cu Dr. Anater Angelo-Christian programat pentru 4 mai 2026 ESTE ÎNLOCUIT de consultul cu Dr. Mate Endre din 30 aprilie 2026 ora 12:00. Mailul trimis lui Dr. Anater pe 28.04.2026 09:37 cu PDF biopsia rămâne ca log istoric (`Dosar_Medical/corespondenta/2026-04-24_re-solicitare-consult-anater.md`). Comisia oncologică / opinia chirurgului eso / planul terapeutic vor fi discutate cu Dr. Mate Endre la consultul 30.04 (pași ulteriori — TBD).

**Motivație clinică (păstrată pentru context):** stadiul infiltrativ + ascită + extensia la joncțiunea eso-gastrică → protocolul terapeutic se schimbă față de un cancer esofagian distal simplu (probabil **FLOT** în loc de **CROSS**, având componenta gastrică). Decizia finală aparține Dr. Mate Endre + comisia oncologică OncoHelp.

**Pregătirea dosarului fizic — finalizare POST-biopsie (28-29.04):**

> **Important:** dosarul fizic se asamblează **DUPĂ primirea rezultatului histopatologic** (primit 28.04, inconcluziv) și **DUPĂ analizele 29.04** (CEA + CA 19-9 + CA 72-4 + HbA1c), pentru a fi **complet** la consultul din 30 aprilie ora 12:00.

Componente prevăzute:

- C.I. + card CAS
- **Bilet de trimitere medic familie pentru oncologie medicală** [obținut 28.04 de la Dr. Orbán]
- Bilet trimitere BCTAP 0631727 (17.04.2026)
- Buletin endoscopie + colonoscopie 17.04.2026 (Genesis Arad)
- Buletin Bioclinica creatinină + uree 17.04.2026
- **Raport CT 20.04.2026** + CD DICOM
- **Rezultat biopsie histopatologic** (Bioclinica 26417A0362, primit 28.04, INCONCLUZIV — element-cheie; recomandare anatomopatolog: IHC pe blocul T26H06044)
- **Markeri tumorali + HbA1c — buletin Bioclinica 26429A0020 (29.04)**: CEA 0,87 normal · CA 19-9 27,00 borderline · CA 72-4 18,59 ELEVAT 2,7x · HbA1c 7,5% diabet suboptimal
- **Consult cardiologic recent** — programat 30.04.2026 ora 08:30 ambulator Arad (max 4h înainte de consultul oncolog 12:00, scrisoare medicală cu FEVS + ECG + ECO + aviz perioperator de adus fizic)
- Listă medicație curentă (4 medicamente confirmate: Aspenter, Concor, Triplixam, Jamesi) + alergii (fără alergii relevante)
- **Scrisori medicale + bilete ieșire spital pentru ALTE patologii / intervenții / proceduri** (pentru evaluare comorbidități): hernie 28.11.2025 (Dr. Papiu), urologie 28.10.2025 (Dr. Pitea), cardiologie 10.11.2025 (Dr. Laza Cristina) + ECO transtoracică, UPU 30.05.2024 (gastro Dr. Grada + cardiologie Dr. Post), serologie H. pylori 2024, stent Vichy 2012 (BMS confirmat — traducere autorizată Vichy procesată 28.04)
- Listă întrebări pregătite (vezi `TODO.md` secțiunea „Pentru viitorul oncolog digestiv")
- **Notă observație:** statină indicată dar nealuată — de discutat la consult (vezi §4)

**Cronologie 30.04.2026:**

1. **Ora 08:30** — consult cardiologic ambulator Arad (FEVS + ECG + ECO + aviz perioperator)
2. **Deplasare** Arad → Timișoara (~1h drum)
3. **Ora 12:00** — consult OncoHelp Timișoara cu Dr. Mate Endre (preluare dosar + discuție inițială)

**Task tracking:** `TODO.md` secțiunea P0 „Pregătire dosar fizic POST-biopsie".

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

| Specialitate                                                                                       | Medic                                                                                                                                                                                                                                                                                                                                                                     | Unitate                                                                                                                                                                    | Contact                                             |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **Medic de familie**                                                                               | **Dr. ORBÁN ECATERINA-MARIA** (medic specialist medicină generală-pediatrie, cod parafă **718705**, CUI **20263730**)                                                                                                                                                                                                                                                     | **Cabinet Medical Individual, Nădlac**                                                                                                                                     | De completat                                        |
| Gastroenterologie (endoscopie 17.04.2026)                                                          | Dr. Noufal Abdul Vahab (medic primar, cod parafă **C 11074**)                                                                                                                                                                                                                                                                                                             | Genesis Medical Clinic Arad                                                                                                                                                | **0735 447 449**                                    |
| **Radiologie și Imagistică (CT 20.04.2026)**                                                       | **Dr. Buie Florian-Laurențiu (cod A11818)** + **Dr. Candea Florin-Vasile (cod F52510)** — ambii medici primari                                                                                                                                                                                                                                                            | **Genesis Medical Clinic Micălaca**                                                                                                                                        | Prin Genesis                                        |
| **Anatomopatologie (biopsie esofag 17.04.2026)**                                                   | **Dr. Glăja Romanița** (medic primar anatomopatolog, cod parafă **367427**) — semnatar raport histopatologic 27.04.2026 + **Dr. Teoran Samy Ștefan** (medic specialist, cod parafă **G70575**) — evaluare macroscopică                                                                                                                                                    | **Bioclinica SA** — laborator anatomopatologie CAL Torontalului 1, Timișoara (recoltare Bioclinica Vlaicu Arad)                                                            | `arad@bioclinica.ro`                                |
| Laborator clinic (pre-CT 17.04.2026)                                                               | Dr. Statnic Maria Luminița (medic primar medicina de laborator, cod **A08064**)                                                                                                                                                                                                                                                                                           | Bioclinica SRL Arad, punct recoltare Vlaicu                                                                                                                                | `arad@bioclinica.ro`                                |
| **Cardiologie ambulator (consult pre-chirurgie 10.11.2025)**                                       | **Dr. LAZA CRISTINA** (medic primar cardiolog, cod parafă **C07842**) — prescriptor schemă medicație actuală                                                                                                                                                                                                                                                              | Arad (cabinet de identificat)                                                                                                                                              | —                                                   |
| **Cardiologie (SCA ST+ 2012, PDF integral procesat 28.04.2026)**                                   | **Echipa identificată complet:** **Dr. Xavier MARCAGGI** (coordonator + operator angioplastie 19.02 cu BMS RX VISION 3.5×28 mm Abbott) + **Dr. Pierre LAVAUD** (operator coronarografie 17.02) + **Dr. Gabriel BITAR** (A.OP) + Dr. Eddie PIERRE-JUSTIN + Dr. Georges AMAT (șefii secției) + Dr. Cloix + Dr. Rodriguez (medici Moulins) + interni Adjtoutah, Chabin, Nana | **Centrul Spitalicesc Jacques Lacarin Vichy** (Bd. Denière, 03207 Vichy Cedex) + **Centrul Spitalicesc Moulins-Yzeure** (Centrul de Cardiologie de Intervenție din Allier) | Vichy: 04.70.97.33.48; Moulins: 04.70.35.77.95      |
| Cardiologie (episod UPU 30.05.2024)                                                                | Dr. Post Mihaela (medic specialist cardiologie, cod **A13550** / **A14555** — 2 coduri pe 2 ștampile diferite)                                                                                                                                                                                                                                                            | Spitalul Clinic Județean de Urgență Arad + ambulator                                                                                                                       | —                                                   |
| Gastroenterologie (episod UPU 30.05.2024)                                                          | Dr. Grada Sebastian (medic specialist gastroenterologie, cod **G15512**)                                                                                                                                                                                                                                                                                                  | Spitalul Clinic Județean de Urgență Arad                                                                                                                                   | —                                                   |
| Medicină de urgență (UPU 30.05.2024)                                                               | Dr. Pop Florica (medic primar medicină de urgență, cod **C79981**)                                                                                                                                                                                                                                                                                                        | Spitalul Clinic Județean de Urgență Arad — UPU Adulți                                                                                                                      | —                                                   |
| **Chirurgie Generală (hernie 28.11.2025)**                                                         | **Dr. Papiu Horațiu-Sabin (medic primar chirurgie, cod parafă 775468)**                                                                                                                                                                                                                                                                                                   | Spitalul Clinic Județean de Urgență Arad — Chirurgie Generală II                                                                                                           | —                                                   |
| **Urologie (consult 28.10.2025)**                                                                  | **Dr. PITEA ALEXANDRU (medic primar urologie, cod A13044)**                                                                                                                                                                                                                                                                                                               | Complex Medical Pitea & Pitea SRL, Arad, Revoluției 45                                                                                                                     | **0749111455**                                      |
| Laborator clinic (serologie HP + analize 2025)                                                     | Dr. Cret Anamaria (medic primar laborator, cod A 0769)                                                                                                                                                                                                                                                                                                                    | SC Ultra ClinicaVest SRL Pecica                                                                                                                                            | `laborator@ultraclinicavest.ro`                     |
| Laborator clinic (UPU 30.05.2024)                                                                  | Dr. Igas Angelica (cod 119856) + Dr. Avram Cecilia — ambii medici primari medicina de laborator                                                                                                                                                                                                                                                                           | Spitalul Clinic Județean de Urgență Arad — Laborator Central                                                                                                               | —                                                   |
| **Oncologie digestivă** (consult 🔴 30.04.2026 ora 12:00)                                          | **Dr. Mate Endre** — medic oncolog OncoHelp Timișoara, programare obținută telefonic 28.04 prin Dr. Vornicu Vlad-Norin · va prelua dosarul medical · vezi `Dosar_Medical/CONTACTE_MEDICALE.md`. **Istoric:** consultul anterior 4.05 cu Dr. Anater Angelo-Christian (`angelo.anater@oncohelp.ro`) ANULAT 29.04 — înlocuit de consultul Mate Endre 30.04.                  | **OncoHelp Timișoara** (Str. C. Porumbescu 57-59, 300239)                                                                                                                  | centrală OncoHelp 0256 495403                       |
| **Oncologie consult inițial OncoHelp** (🔴 30.04.2026 ora 12:00)                                   | **Dr. Mate Endre** (Medic Rezident Oncologie Medicală per oncohelp.ro/echipa-oncohelp/, training UMF Victor Babeș Timișoara + Aix-Marseille Université + Hôpital Saint-Louis AP-HP Paris, focus declarat imunoterapie) — case manager / înregistrare pacient                                                                                                              | **OncoHelp Timișoara** (Str. C. Porumbescu 57-59) — programare prin Dr. Vornicu telefonic 28.04                                                                            | (telefon contact la consult)                        |
| Oncologie (contact direct furnizat user 25.04, telefonic 28.04 → recomandare Dr. Mate Endre 30.04) | **Dr. Vornicu Vlad-Norin** (Medic Specialist Oncolog, Asistent Univ PhD UMFT, focus oncologie pulmonară) — opțiune second opinion / specialist complementar                                                                                                                                                                                                               | OncoHelp Timișoara                                                                                                                                                         | `0762 120 428` · `vornicuvlad91@gmail.com`          |
| Oncologie second opinion (IOCN Cluj — răspuns 24.04)                                               | **Șef Lucrări Dr. Andra Meșter** (Medic Specialist Oncologie Medicală)                                                                                                                                                                                                                                                                                                    | Institutul Oncologic „Prof. Dr. Ion Chiricuță", Cluj-Napoca                                                                                                                | `drmester.iocn@gmail.com` · `0264 598 362 int. 347` |
| Endocrinologie (glandă suprarenală, follow-up)                                                     | De stabilit post-consult oncolog                                                                                                                                                                                                                                                                                                                                          | —                                                                                                                                                                          | —                                                   |

> **Corespondență oncologică completă** (toate threadurile email cu medici și clinici): vezi `Dosar_Medical/corespondenta/INDEX.md` (R27 — primul ingest Gmail full-history 2026-04-25). Conține 5 fișiere thread (Anater, Mester, broadcast 5 clinici, OncoHelp inițial, Cip adjuvant).

---

## 10. Evaluare preliminară (actualizată post-CT, 22.04.2026)

> **Marcaj secțiune:** această secțiune conține **concluzii preliminare interpretative** care NU sunt afirmații factuale directe — sunt sinteze bazate pe datele din §2 și §7. Deciziile clinice finale aparțin medicilor curanți (Dr. Noufal gastro + viitor oncolog digestiv). Marcajele individuale aplicate la ipoteze și probabilități.

**Context actualizat:** CT-ul de stadializare (20.04.2026) a clarificat semnificativ imaginea — leziune infiltrativă circumferențială la joncțiunea eso-gastrică cu extensie fundică, fără metastaze la distanță vizibile `[CERT]`, dar cu ascită de etiologie de elucidat `[INCERT]`.

**Elemente care susțin neoplazie avansată (post-CT):**

- Stenoza completă „nedepășibilă endoscopic" (17.04.2026) = masă obstructivă `[CERT]`
- Proces expansiv infiltrativ circumferențial + densificarea grăsimii loco-regionale (CT 20.04) `[CERT]`
- Extensie la joncțiunea eso-gastrică + cadru gastric fundic (Siewert II probabil) `[PROBABIL]`
- Stadiu imagistic estimativ **T3–T4** `[PROBABIL]`
- **Ascita** perihepatică + intrapelvină `[CERT]` (risc carcinomatoză peritoneală de exclus `[INCERT]`)
- Simptome sistemice (oboseală, apetit diminuat, senzație „nod în gât" postprandial) `[CERT]` declarativ familie
- Vârsta + istoric fumat 35 ani + reflux recent reapărut `[CERT]` factori de risc cumulați

**Elemente favorabile (aspecte pozitive la CT):**

- **M0 probabil** `[PROBABIL]` — fără metastaze hepatice, pulmonare, osoase sau ganglionare distale vizibile
- Limfonoduli loco-regionali sub pragul patologic standard (max 7.5 mm vs. <10 mm criteriu) `[CERT]`
- Fără adenopatii mediastinale / hilare / axilare / abdomino-pelvine `[CERT]`
- Funcție renală normală (creatinină 0.83 mg/dL) `[CERT]`
- Status cardiac stabil (post-stent 2012, controlat farmacologic) `[PROBABIL]` (baseline 10.11.2025 ECO — FE 55% `[CERT]`)
- Absența disfagiei progresive clasice `[CERT]` declarativ familie (deși stenoza e aproape completă, pacientul se alimentează încă rezonabil)
- Scădere ponderală absentă până acum `[CERT]` declarativ familie

**Ipoteze diagnostice revizuite** `[PROBABIL]` **(NU diagnostic — doar orientare pre-biopsie):**

1. **Adenocarcinom de joncțiune eso-gastrică Siewert II** `[PROBABIL]` — probabilitate ridicată (localizare distală + extensie fundică + circumferențial; pattern tipic per literatura ESMO/NCCN)
2. Carcinom scuamocelular cu extensie distală `[PROBABIL]` — probabilitate mai mică (localizarea atipică pentru scuamos)
3. Alte tumori rare (GIST, limfoame esofagiene, sarcoame) `[PROBABIL]` — probabilitate foarte mică

**Stadializare clinică probabilă (pre-biopsie)** `[PROBABIL]`:

- **Dacă M0 confirmat (fără carcinomatoză):** Stadiu III (T3-T4, N0-N1, M0) → candidat pentru protocol **FLOT** (chemoterapie perioperatorie) + chirurgie `[PROBABIL]` (sursă: ghid ESMO 2022 + NCCN V1.2025)
- **Dacă M1 (carcinomatoză peritoneală confirmată):** Stadiu IV → protocol paliativ / chemoterapie sistemică (FLOT sau FOLFOX, +/- imunoterapie dacă markeri PD-L1+ / HER2+) `[PROBABIL]`

**Decizia finală se bazează EXCLUSIV pe:**

- **Rezultatul histopatologic al biopsiei — primit 28.04.2026, INCONCLUZIV** `[CERT]` (vezi §7.4): ține pasul „diagnostic de certitudine" deschis până la **IHC pe blocul T26H06044** sau **rebiopsie țintită** (decizie consult 4.05). Fără diagnostic histologic ferm, alegerea protocolului (FLOT / CROSS / paliativ) **NU poate fi finalizată**.
- Clarificarea etiologiei ascitei (reactivă vs. carcinomatoză — poate necesita paracenteză + citologie sau laparoscopie)
- Evaluarea de către medicul oncolog digestiv
- Eventual PET-CT pentru activitate metabolică și confirmare M0 cu sensibilitate superioară CT-ului

**Recalibrare 28.04.2026 post-biopsie:** Inconcluzivitatea biopsiei NU schimbă suspiciunea clinico-imagistică `[CERT]` — toate elementele care susțin neoplazia avansată (stenoză „nedepășibilă", proces infiltrativ T3-T4, ascită) rămân valide. Modifică doar _ritmul deciziei terapeutice_: pasul histologic de certitudine necesită IHC sau rebiopsie înainte de inițierea unui protocol oncologic. Probabilitatea ca leziunea să fie **non-tumorală** (ulcerație cronică pură, esofagită severă, etc.) rămâne **mică** `[PROBABIL]` dar NU zero — diagnostic diferențial care va fi clarificat prin IHC/rebiopsie.

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

## 12. Rezumat în 3 linii (pentru preluare rapidă — actualizat 28.04.2026)

1. Pacient masculin, 66 ani, diabetic, post-stent cardiac 2012, ex-fumător 35 ani. CNP 1590518024486.
2. Proces proliferativ **circumferențial nedepășibil endoscopic** la joncțiunea eso-gastrică (Siewert II probabil); CT 20.04.2026 arată **T3-T4, N0-N1, M0 probabil**, cu ASCITĂ probabil cardiacă per Anater (de elucidat eventual cu laparoscopie ulterior).
3. **Biopsie 17.04 primită 28.04 — INCONCLUZIVĂ** („țesut de granulație + ulcerație cronică, doar SUGESTIV pentru carcinom"; cod T26H06044, Dr. Glăja Romanița 27.04); recomandare anatomopatolog: **IHC pe blocul T26H06044** sau rebiopsie. Suspiciunea clinico-imagistică persistă. **Consult oncolog 30.04.2026 ora 12:00 OncoHelp Timișoara — Dr. Mate Endre** (înlocuiește consultul anterior 4.05 cu Dr. Anater) → preluare dosar + decizie IHC vs rebiopsie + pași ulteriori (comisie + chirurg eso TBD).

---

**Istoric versiuni:** vezi `arhiva/` pentru versiunile anterioare ale acestui fișier.
**Următoarea actualizare planificată:** la consultul oncolog 30.04.2026 ora 12:00 cu Dr. Mate Endre (decizie IHC/rebiopsie + pași ulteriori) sau la primirea rezultatului IHC (dacă se inițiază înainte de 30.04).
