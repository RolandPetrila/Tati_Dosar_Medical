# STATUS SNAPSHOT — Petrilă Viorel-Mihai

**Generat automat:** 2026-04-30 01:12
**Ultim commit git:** `53aa43a` (2026-04-29 23:55:20 +0300)
**Mesaj commit:** [FIX 2026-04-29] Cleanup 6 referințe LIVE rămase la 4.05 / Anater post-reprogramare
**Sursă de adevăr:** fișierele originale din proiect `.Tati`. Acest snapshot e mirror sintetic generat de `scripts/regen_projects_sync.py` pentru chat Claude Projects (web/mobil).

> **Ordine consultare în chat:** STATUS_SNAPSHOT.md (aici) → CONTEXT_MEDICAL.md (detaliu clinic) → TODO.md (calendar) → CONTACTE_MEDICALE.md (medici) → REGULAMENT.md (reguli) → INDEX.json (index documente) → EXPLICATIE_CONSULT_ONCOLOG_SCENARII.md (glosar + scenarii prognostice).

---

## 🧑 Date pacient

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

---

## 🏥 Status clinic curent (sumar TNM)

**Stadializare imagistică preliminară** `[PROBABIL]` — estimativă per radiolog, necesită corelare cu biopsie pentru confirmare histologică:

| Element       | Estimare CT           | Marcaj       | Note                                                                                                                                         |
| ------------- | --------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **T** (tumor) | T3–T4                 | `[PROBABIL]` | Proces expansiv infiltrativ circumferențial cu extensie loco-regională, densificarea grăsimii peritumorale                                   |
| **N** (nodes) | N0–N1                 | `[PROBABIL]` | Limfonoduli loco-regionali max 7.5 mm `[CERT]` (sub pragul standard <10 mm, dar în context neoplazic pot fi relevanți)                       |
| **M** (meta)  | **M0 probabil**       | `[PROBABIL]` | Fără metastaze hepatice, pulmonare, osoase, ganglionare distale vizibile pe CT `[CERT]`                                                      |
| **Siewert**   | II probabil           | `[PROBABIL]` | Joncțiune eso-gastrică propriu-zisă, centrată pe cardia cu extensie eso-distală și fundică                                                   |
| **ATENȚIE**   | **Ascită de evaluat** | `[CERT]`     | Colecție fluidă perihepatică 15 mm + intrapelvină 28 mm `[CERT]` → de exclus CARCINOMATOZĂ PERITONEALĂ `[INCERT]` (ar echivala cu stadiu IV) |

**Natura histologică a leziunii:** `[INCERT]` — neclarificată. Biopsia în lucru la Bioclinica Arad va preciza tipul exact (adenocarcinom vs. carcinom scuamocelular, grad de diferențiere). Localizarea distală + extensia fundică sugerează **adenocarcinom** `[PROBABIL]` (pattern tipic Siewert II per literatura de specialitate), dar confirmarea aparține histopatologului.

> **Detalii complete:** CONTEXT_MEDICAL.md §2 (findings principale + secundare + colaterale + parametri tehnici CT).

---

## 💊 Medicație activă

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

---

## 📅 Calendar — date cheie

| Data                                | Eveniment                                                                                                               | Status                                                                                                                                              |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 17.04.2026                          | Endoscopie + colonoscopie efectuate                                                                                     | ✅ Finalizat                                                                                                                                        |
| 17.04.2026                          | Bilet trimitere CT emis                                                                                                 | ✅ Finalizat                                                                                                                                        |
| **18.04.2026**                      | **STOP Jamesi (H-48 pre-CT)**                                                                                           | ✅ Finalizat                                                                                                                                        |
| ~~19.04.2026 — analize creatinină~~ | ~~de efectuat~~ → ✅ ACOPERIT (buletin Bioclinica 17.04.2026)                                                           | ✅ Finalizat                                                                                                                                        |
| 19.04.2026                          | Hidratare activă (plan confirmat de familie)                                                                            | ✅ Finalizat                                                                                                                                        |
| **20.04.2026 17:00**                | **CT torace + abdomen + pelvis cu contrast (Genesis Micălaca)**                                                         | ✅ **Finalizat** — raport integrat 22.04.2026                                                                                                       |
| **22.04.2026**                      | Reluare Jamesi (H+48 post-CT, creatinină pre-CT normală)                                                                | ✅ **Finalizat** — reluat seara 22.04, fără complicații                                                                                             |
| **25.04.2026 18:00**                | Mail trimis Dr. Anater (programare 30.04 + 5 întrebări organizatorice)                                                  | ✅ Trimis                                                                                                                                           |
| **26.04.2026 10:28**                | Răspuns Dr. Anater — reprogramare 30.04 → 4 mai + clarificări complete                                                  | ✅ Primit · ingest 26.04 19:06                                                                                                                      |
| **27.04.2026**                      | 3 telefoane programări                                                                                                  | ✅ Finalizat — cardiolog 30.04 · analize 29.04 · bilete trimitere obținute                                                                          |
| **28.04.2026** ✅                   | **Rezultat biopsie esofagiană PRIMIT** (Bioclinica SA Timișoara — buletin 26417A0362 / cod T26H06044)                   | ✅ **Primit — INCONCLUZIV** („țesut granulație + ulcerație cronică, doar SUGESTIV carcinom"); monitor ntfy.sh oprit                                 |
| **29.04.2026** ✅                   | Analize sânge — Bioclinica Nădlac (CEA + CA 19-9 + CA 72-4 + HbA1c)                                                     | ✅ **EFECTUAT** — buletin 26429A0020; CEA 0,87 normal · CA 19-9 27,00 borderline · **CA 72-4 18,59 ELEVAT 2,7x** · **HbA1c 7,5% diabet suboptimal** |
| **30.04.2026 ora 08:30**            | Consult cardiologic — ambulator Arad                                                                                    | 🟢 **PROGRAMAT** [confirmat 27.04, ora exactă confirmată user 28.04]                                                                                |
| **30.04.2026 ora 12:00** 🔴         | **Consult oncolog OncoHelp Timișoara cu Dr. Mate Endre** — preluare dosar medical + discuție inițială (consult primary) | 🔴 **PROGRAMAT** — ÎNLOCUIEȘTE consultul 4.05 cu Dr. Anater [decizie user 29.04] · fără tata e OK, doar Roland + Maria + dosarul                    |
| **28-29.04.2026**                   | Pregătire dosar fizic POST-biopsie pentru consult oncolog 30.04                                                         | 🔴 P0 — vezi secțiune dedicată mai jos                                                                                                              |
| ~~4.05.2026~~                       | ~~Consult oncolog digestiv — Dr. Anater OncoHelp Timișoara~~                                                            | ❌ **ANULAT 29.04** (înlocuit de consultul 30.04 ora 12:00 cu Dr. Mate Endre)                                                                       |
| Post-consult oncolog                | Evaluare endocrinologică (glandă suprarenală stângă)                                                                    | 🟡 De programat                                                                                                                                     |

---

## 🔴 Acțiuni P0 active

### [P0] 🟡 27.04.2026 — 3 telefoane (declanșate de mail Anater 26.04)

**Status:** ✅ FINALIZAT 28.04.2026 — cardiolog 30.04 ✅ · analize Bioclinica 29.04 (CEA + CA 19-9 + HbA1c) ✅ · bilete trimitere Dr. Orbán obținute ✅ · CD DICOM la dosar ✅.

**📋 Document operațional pentru Roland:** [`Documente_Informative/GHID_TELEFOANE_27-04.md`](Documente_Informative/GHID_TELEFOANE_27-04.md) — 3 scripturi apel detaliate + checklist pregătire 5 min + obstacole comune + numere backup utile (creat 26.04 19:50). De citit/printat înainte de a forma primul număr.

**1. Medic de familie Dr. Orbán Ecaterina-Maria (Cabinet Medical Individual Nădlac):**

- [x] ✅ Bilet trimitere **oncologie medicală** — obținut [28.04.2026]
- [x] ✅ Bilet trimitere **cardiologie** — obținut [28.04.2026]

**2. Cardiolog Arad — programare consult ambulator:**

- [x] ✅ **PROGRAMAT — 30.04.2026** [confirmat 27.04.2026]
- [ ] La prezentare 30.04: solicitat ECG + ECO + **scrisoare medicală scrisă cu FEVS + aviz perioperator** (de adus fizic la OncoHelp 4.05)
- [ ] **📋 Ghid detaliat:** [`Documente_Informative/GHID_CARDIOLOG_30-04.md`](Documente_Informative/GHID_CARDIOLOG_30-04.md) — ce aduci, ce spui, ce ceri, ce înseamnă FEVS

**3. Analize sânge — Bioclinica Arad:**

- [x] ✅ **EFECTUAT — 29.04.2026** · recoltare à jeun 07:22 Bioclinica Nădlac · buletin 26429A0020
- [x] ✅ **CEA** (antigen carcinoembrionar) — **0,87 ng/mL NORMAL** (<3,80 nefumători)
- [x] ✅ **CA 19-9** — **27,00 U/mL BORDERLINE** (exact pe limita superioară <27,00)
- [x] ✅ **HbA1c** — **7,5% PESTE LIMITĂ** (țintă ADA <7,0% pacient >20 ani; control glicemic suboptimal cu Jamesi)
- [x] ✅ **CA 72-4** (marker tumoral specific gastric, adăugat la recoltare ca extra) — **18,59 U/mL ELEVAT ~2,7x** limita (<6,90); subcontractat Bioclinica Timișoara · medic raportor Dr. Gaiță Pîrvan Corina (D15815)

**Acțiune Roland:** după telefoane, revine cu statusul (programare confirmată / alternativă propusă) — actualizare task corespunzător.

### [P0] 🔴 Consult oncolog digestiv — 30 aprilie 2026 ora 12:00 OncoHelp Timișoara (Dr. Mate Endre)

**Status:** 🔴 **PROGRAMAT 30.04.2026 ora 12:00** [obținut telefonic 28.04 prin Dr. Vornicu Vlad-Norin]. **ÎNLOCUIEȘTE consultul anterior 4.05 cu Dr. Anater** (decizie user 29.04.2026).

**Detalii:**

- **Data:** **30 aprilie 2026 (joi), ora 12:00**
- **Unitate:** **OncoHelp Timișoara** (Str. Ciprian Porumbescu nr. 57-59)
- **Medic oncolog:** **Dr. Mate Endre** — va prelua dosarul medical și va începe discuția în prima fază
- **Format:** consult primar oncolog (luare în evidență la OncoHelp + preluare dosar complet + discuție inițială asupra cazului + decizie pași diagnostici post-biopsie inconcluzivă)
- **Prezență:** Roland + Maria + dosarul fizic (fără tata e OK pentru această fază)

**Motivație clinică (păstrată):** CT 20.04.2026 arată proces expansiv infiltrativ circumferențial la joncțiunea eso-gastrică (Siewert II probabil) + ascită perihepatică 15 mm + intrapelvină 28 mm. Biopsia 17.04 (primită 28.04) inconcluzivă — recomandare anatomopatolog: IHC pe blocul T26H06044 sau rebiopsie. Pași ulteriori (comisie oncologică + chirurg eso + plan FLOT/alternative) → TBD la consultul 30.04 cu Dr. Mate Endre.

**Sub-task-uri rămase:**

- [x] ✅ Programare consult — confirmată telefonic 28.04 prin Vornicu (30.04 ora 12:00)
- [x] ✅ Programări 27-28.04: cardiolog 30.04 + analize Bioclinica 29.04 + bilete trimitere obținute
- [x] ✅ Analize Bioclinica 29.04 efectuate (CEA + CA 19-9 + CA 72-4 + HbA1c)
- [ ] **Pregătire dosar fizic — vezi task P0 dedicat de mai jos** (deadline 28-29.04, finalizare cu buletin analize 29.04)
- [ ] **Printare buletin analize 29.04** (Bioclinica 26429A0020)
- [ ] Recapitulare listă întrebări pregătite (secțiunea „Pentru viitorul oncolog digestiv" mai jos) — adaptată pentru Dr. Mate Endre
- [ ] (Notă istorică) Mail trimis Dr. Anater 28.04 09:37 cu PDF biopsia rămâne ca log; consultul Anater 4.05 ANULAT

### [P0] 🔴 Pregătire dosar fizic POST-biopsie pentru consult oncolog (deadline 28-29.04, consult 30.04 ora 12:00)

**Status:** ACTUALIZAT 29.04.2026 — consultul devine 30.04 ora 12:00 cu Dr. Mate Endre (înlocuiește 4.05 cu Dr. Anater).

**Decizie user (25.04):** dosarul se asamblează **DUPĂ primirea rezultatului histopatologic**, pentru a fi complet la consult.

**Cronologie revizuită:**

1. ✅ **27.04.2026** — programări confirmate: analize Bioclinica 29.04 + cardiolog 30.04
2. ✅ **27-28.04.2026** — bilete trimitere Dr. Orbán obținute (oncologie + cardiologie)
3. ✅ **28.04.2026** — **rezultat biopsie PRIMIT** (Bioclinica 26417A0362 / T26H06044) — INCONCLUZIV, sugestiv carcinom; recomandare anatomopatolog: IHC sau rebiopsie
4. ✅ **29.04.2026** — analize Bioclinica EFECTUATE: CEA 0,87 normal · CA 19-9 27,00 borderline · CA 72-4 18,59 ELEVAT 2,7x · HbA1c 7,5% diabet suboptimal (buletin 26429A0020)
5. 🔜 **29.04.2026 seara** — printare buletin analize 29.04 + finalizare dosar fizic
6. 🔜 **30.04.2026 ora 08:30** — consult cardiologic Arad → scrisoare medicală + ECG + ECO + aviz perioperator
7. 🔴 **30.04.2026 ora 12:00** — consult OncoHelp Timișoara cu Dr. Mate Endre → preluare dosar + decizie pași diagnostici (IHC pe blocul T26H06044 vs rebiopsie țintită) + planificare pași ulteriori (comisie + chirurg eso TBD)

**Componente dosar:**

- [ ] C.I. + card CAS
- [x] ✅ **Bilet trimitere medic familie pentru oncologie medicală** [obținut 27-28.04 · per mail Anater 26.04]
- [ ] Bilet trimitere BCTAP 0631727 (17.04.2026)
- [ ] Buletin endoscopie + colonoscopie 17.04.2026 (de printat din `Dosar_Medical/`)
- [ ] Buletin Bioclinica creatinină + uree 17.04.2026 (de printat)
- [x] ✅ **CD DICOM** de la CT 20.04.2026 (Genesis) — la dosar [confirmat 28.04]
- [ ] **Raport CT 20.04.2026** (printare)
- [x] ✅ **Rezultat biopsie histopatologic** — primit 28.04.2026 (Bioclinica 26417A0362 / T26H06044). **De printat** atât buletinul Bioclinica cât și interpretarea sintetizată (`CONTEXT_MEDICAL.md §7.4`) + documentul `.docx` pentru familie generat 28.04
- [x] ✅ **Markeri tumorali CEA + CA 19-9** — efectuat 29.04 (CEA 0,87 normal · CA 19-9 27,00 borderline)
- [x] ✅ **HbA1c (hemoglobina glicozilată A1c)** — efectuat 29.04 (7,5% — diabet suboptimal vs țintă ADA <7,0%)
- [x] ✅ **CA 72-4** (marker tumoral specific adenocarcinom gastric/eso-gastric) — efectuat 29.04 (18,59 U/mL ELEVAT ~2,7x; relevant Siewert II) [adăugat la recoltare ca extra-marker]
- [ ] **Printare buletin analize 29.04** + adăugare în dosarul fizic pentru consult 30.04 ora 12:00
- [ ] **Consult cardiologic** — 🟢 PROGRAMAT 30.04.2026 ora 08:30 → de adus scrisoare medicală + ECG + ECO fizic la consultul oncolog 30.04 ora 12:00
- [ ] Listă medicație curentă (4 confirmate: Aspenter, Concor, Triplixam, Jamesi) + alergii (fără)
- [ ] **Scrisori medicale + bilete ieșire spital pentru ALTE patologii / intervenții / proceduri** [per mail Anater 26.04 — pentru evaluare comorbidități]:
  - Hernie 28.11.2025 (Dr. Papiu, Spitalul Județean Arad — Chirurgie Generală II)
  - Urologie 28.10.2025 (Dr. Pitea, Complex Medical Pitea & Pitea Arad)
  - Cardiologie 10.11.2025 (Dr. Laza Cristina) + ECO transtoracic
  - UPU 30.05.2024 (gastro Dr. Grada + cardiologie Dr. Post + urgență Dr. Pop Florica)
  - Serologie H. pylori 04.06.2024 + 06.09.2024 (Ultra ClinicaVest Pecica)
  - Stent Vichy 2012 — dacă obținut de la familie până atunci
- [ ] Listă întrebări pregătite pentru oncolog (secțiunea dedicată mai jos)
- [ ] **Notă observație** statină nealuată — pentru discuție la consult (vezi `CONTEXT_MEDICAL.md §4`)
- [ ] (Opțional) `Documente_Informative/EXPLICATIE_CONSULT_ONCOLOG_SCENARII.md` — pentru orientare familie pre-consult

### [P0] 🔴 NOU 28.04 — Decizie IHC pe blocul T26H06044 sau rebiopsie (consult oncolog 30.04 ora 12:00)

**Context:** rezultatul biopsiei 17.04 primit 28.04 este **inconcluziv** — concluzie anatomopatolog: „țesut de granulație + ulcerație cronică, doar SUGESTIV pentru infiltrat carcinomatos". Limitare explicită: **număr mic de celule epiteliale atipice surprinse**. Recomandare laborator: „eventuală evaluare imunohistochimică pentru diagnostic histologic de certitudine și conduită terapeutică".

**Status:** 🔴 P0 — depinde de decizia Dr. Mate Endre la consult 30.04 ora 12:00.

**Trei opțiuni standard pentru diagnostic de certitudine:**

1. **IHC pe blocul existent T26H06044** [recomandat de anatomopatolog] — markeri tipici: pan-CK, CK7/CK20, CDX-2, p53; eventual HER2 / PD-L1 / MSI dacă se confirmă carcinom (relevanță decizie terapeutică). Avantaj: rapid (3-7 zile), fără reintervenție. Dezavantaj: dacă atipia e prea redusă, IHC poate fi tot inconcluziv.
2. **Rebiopsie endoscopică țintită** cu fragmente mai numeroase, mai profunde — eventual ghidată **EUS (ecoendoscopie)** pentru a depăși stratul superficial. Avantaj: randament diagnostic superior. Dezavantaj: necesită reintervenție + timp suplimentar.
3. **Combinare IHC + rebiopsie programată în paralel.**

**Sub-task-uri:**

- [ ] Printare buletin biopsie + interpretare sintetizată + document `.docx` pentru familie (28-29.04, înainte de consult)
- [ ] La consult 30.04 ora 12:00 — întrebare prioritară Dr. Mate Endre (vezi secțiunea „Pentru viitorul oncolog digestiv" mai jos): IHC pe blocul T26H06044 (cu ce markeri) vs rebiopsie țintită vs combinare?
- [ ] La decizia Dr. Mate Endre — solicitare formală la Bioclinica (poate prin oncolog cu trimitere) sau programare rebiopsie la Genesis/IOCN/OncoHelp
- [ ] Update CONTEXT_MEDICAL.md §7.4 cu rezultatul IHC sau rebiopsiei, când vine

**Referințe:** `CONTEXT_MEDICAL.md §7.4` (interpretare completă) · `Dosar_Medical/2026-04-17_biopsie_esofagiana_histopatologic.json` · `Documente_Informative/EXPLICATIE_REZULTAT_BIOPSIE_2026-04-28.docx` (28.04 — pentru familie).

### [P0] 📋 Analiză și prezentare rezultat CT familiei (22.04.2026)

**Status:** NOU deschis.

**Obiectiv:** explicație clară și fără alarmism inutil, cu separarea veștilor bune de cele care necesită atenție.

- [ ] Printare / transmitere raport CT către familie (document oficial Genesis)
- [ ] Discuție 15-30 min: ce înseamnă T3-T4, N0-N1, M0 probabil; de ce ascita e un semnal de urmărit; ce urmează
- [ ] Actualizare DOCX ghid cancer esofagian cu informațiile noi (opțional — sesiune separată)

### [P0] 🔴 Consult oncolog digestiv URGENT

**Detalii:** vezi prima secțiune P0 de mai sus („Consult oncolog digestiv URGENT (post-CT, 22.04.2026)").

### [P0] 📋 Analiză și prezentare rezultat CT familiei

**Detalii:** vezi prima secțiune P0 de mai sus.

---

## 📚 Cum răspunzi (instrucțiuni Claude Projects)

- **Limba:** română strict (excepție: termeni medicali tehnici fără echivalent comun)
- **Marcaje certitudine OBLIGATORII** pe afirmații medicale (R17 — REGULAMENT.md):
  - `[CERT]` — confirmat din sursă primară (JSON canonic, RCP/SmPC, ghid ESMO/NCCN, studiu peer-reviewed)
  - `[PROBABIL]` — susținut de literatura medicală standard
  - `[INCERT]` — conflict surse / extrapolare / lacună
  - `[NEGASIT]` — căutat și neidentificat
- **NU PRESUPUNE** — la neclaritate întreabă explicit (R7); niciodată nu inventa cifre, doze, nume medic, date
- **La conflict între acest snapshot și fișierele originale** → CONTEXT_MEDICAL.md / TODO.md prevalează (autoritate)
- **Detalii operaționale extinse:** PROJECTS_PRIMER.md

---

_Pentru actualizare: editezi fișiere originale pe laptop → rulezi `python scripts/regen_projects_sync.py` → push git → Google Drive sync → Drive Connector re-index Projects ([PROBABIL] 5-30 min)._
