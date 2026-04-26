# STATUS SNAPSHOT — Petrilă Viorel-Mihai

**Generat automat:** 2026-04-27 01:06
**Ultim commit git:** `9f89809` (2026-04-27 00:43:23 +0300)
**Mesaj commit:** [NEW R30 2026-04-27] Sistem sync Claude Projects: _projects_sync/ + script regen
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

| Medicament                                                     | Indicație                                                | Doză                  | Ritm                  | Note                                                                      |
| -------------------------------------------------------------- | -------------------------------------------------------- | --------------------- | --------------------- | ------------------------------------------------------------------------- |
| **Jamesi** (sitagliptin + clorhidrat de metformin)             | Diabet zaharat tip 2                                     | 50 mg / 1000 mg       | 1-0-1 (dim. și seara) | **CRITIC**: componenta metformin se oprește 48h înainte de CT cu contrast |
| **Aspenter** (acid acetilsalicilic)                            | Antiagregant post-stent coronarian 2012                  | 75 mg                 | 0-1-0 (prânz)         | NU se oprește pentru CT                                                   |
| **Concor** (fumarat de bisoprolol)                             | Beta-blocant (cardioprotecție + HTA + control frecvență) | 5 mg                  | 1-0-0 (dimineața)     | Nu se oprește pentru CT                                                   |
| **Triplixam** (perindopril arginine + indapamidă + amlodipină) | Antihipertensiv combinație triplă                        | 10 mg / 2.5 mg / 5 mg | 1-0-0 (dimineața)     | Nu se oprește pentru CT                                                   |

**Notă:** manuscrisul conținea o a 5-a recomandare tăiată cu marker albastru (anulată).

**Suplimente alimentare:** de verificat cu familia.

**Sursă:** `Dosar_Medical/2025-11-10_schema_medicamente.json` (manuscris parțial + fotografii cutii). Medicamentele, dozele și ritmul de administrare sunt `[CERT]` (fotografii cutii + manuscris lizibil pentru ritm). Medicul prescriptor identificat retroactiv 2026-04-24: **Dr. LAZA CRISTINA (cod parafă C07842)** via cross-reference ECO tipărită aceeași zi.

### Observație clinică — statină nealuată curent (de evaluat la consult oncolog 30.04)

**Context (clarificat de user 2026-04-25):** scrisoarea medicală Dr. LAZA CRISTINA din 10.11.2025 (`2025-11-10_scrisoare_medicala_cardiologie.json`) prescrisese **TORVACARD 10/20 mg 0-0-1 seara**, însă pacientul **NU îl administrează curent** — schema reală în vigoare este cea manuscrisă în aceeași zi (cele 4 medicamente din tabelul de mai sus, fără statină). Documentele sursă confirmă: folder `Dosar_Medical/documente_sursa/08_schema_tratament/` (manuscris talon + foto cutii Aspenter, Concor, Triplixam, Jamesi).

**Relevanță pre-esofagectomie** `[CERT]`:

- Pacient post-stent coronarian 2012 → ghidurile AHA/ESC recomandă statină continuă pentru prevenție CV secundară
- **Lipidogramă 17.06.2025** (`Dosar_Medical/2025-06-17_buletin_analize_sange.json`): colesterol total 189, **LDL 133 mg/dL** — țintă ESC 2019/2021 post-stent: <70 mg/dL → ținta neatinsă
- De ridicat la **consultul oncolog 30.04.2026 OncoHelp Timișoara** + medicul de familie Dr. Orbán: reevaluare prevenție CV secundară pre-chirurgie esofagiană

**Paritate R24:** TORVACARD apare în JSON-ul scrisorii (chain of custody intact — nu se modifică sursa) și este reflectat aici ca observație clinică, nu ca prescripție efectivă.

### Interacțiune medicamentoasă documentată — de urmărit

**Sitagliptin (Jamesi) + Perindopril (Triplixam) → risc crescut de angioedem.** Mecanism: sitagliptinul inhibă DPP-4 (enzima care degradează substanța P); perindoprilul inhibă ECA (care degradează bradikinina); acumularea ambelor substanțe vasoactive crește riscul de umflare bruscă a feței, buzelor, limbii sau căilor respiratorii. **NU e contraindicație** — pacientul poate continua ambele medicamente.

**Urmărire:** la orice umflare bruscă la față/buze/limbă sau dificultate bruscă de respirație → 112 IMEDIAT. Medicul curant să fie informat despre combinația actuală.

**Sursă:** [CERT] SmPC Triplixam v06.2021, secțiunea 4.5 „Gliptins": „Increased risk of angio-oedema, due to dipeptidyl peptidase IV (DPP-IV) decreased activity by the gliptine, in patients co-treated with an ACE inhibitor."

**Detalii complete pentru familie:** `Dosar_Medical/rapoarte_generate/2026-04-18_raport_reactii_adverse_jamesi_triplixam.docx`, Partea III.A.

---

---

## 📅 Calendar — date cheie

| Data                                | Eveniment                                                                                | Status                                                  |
| ----------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| 17.04.2026                          | Endoscopie + colonoscopie efectuate                                                      | ✅ Finalizat                                            |
| 17.04.2026                          | Bilet trimitere CT emis                                                                  | ✅ Finalizat                                            |
| **18.04.2026**                      | **STOP Jamesi (H-48 pre-CT)**                                                            | ✅ Finalizat                                            |
| ~~19.04.2026 — analize creatinină~~ | ~~de efectuat~~ → ✅ ACOPERIT (buletin Bioclinica 17.04.2026)                            | ✅ Finalizat                                            |
| 19.04.2026                          | Hidratare activă (plan confirmat de familie)                                             | ✅ Finalizat                                            |
| **20.04.2026 17:00**                | **CT torace + abdomen + pelvis cu contrast (Genesis Micălaca)**                          | ✅ **Finalizat** — raport integrat 22.04.2026           |
| **22.04.2026**                      | Reluare Jamesi (H+48 post-CT, creatinină pre-CT normală)                                 | ✅ **Finalizat** — reluat seara 22.04, fără complicații |
| **25.04.2026 18:00**                | Mail trimis Dr. Anater (programare 30.04 + 5 întrebări organizatorice)                   | ✅ Trimis                                               |
| **26.04.2026 10:28**                | Răspuns Dr. Anater — reprogramare 30.04 → 4 mai + clarificări complete                   | ✅ Primit · ingest 26.04 19:06                          |
| **27.04.2026 (mâine)**              | **3 telefoane:** medic familie (2 bilete trimitere) + cardiolog + Synevo (CEA + CA 19-9) | 🔴 P0 nou — vezi secțiune dedicată mai jos              |
| **28-29.04.2026** (estimat)         | **Rezultat biopsie esofagiană** (Bioclinica Arad)                                        | 🟢 În așteptare · monitor automat activ 24/7 (ntfy.sh)  |
| **28-30.04.2026**                   | Pregătire dosar fizic POST-biopsie pentru consult oncolog                                | 🔴 P0 — vezi secțiune dedicată mai jos                  |
| ~~30.04.2026~~                      | ~~Consult oncolog digestiv — OncoHelp Timișoara~~                                        | ❌ ANULAT 26.04 (motivat: aglomerație 1 mai)            |
| **4.05.2026 (luni)** 🔴             | **Consult oncolog digestiv — OncoHelp Timișoara** (REPROGRAMAT)                          | 🔴 **PROGRAMAT** [per mail Anater 26.04]                |
| Post-consult oncolog                | Evaluare endocrinologică (glandă suprarenală stângă)                                     | 🟡 De programat                                         |

---

## 🔴 Acțiuni P0 active

### [P0] 🔴 MÂINE 27.04.2026 — 3 telefoane (declanșate de mail Anater 26.04)

**Status:** NOU deschis 26.04.2026 19:06 — declanșat de instrucțiunile Dr. Anater 26.04.

**📋 Document operațional pentru Roland:** [`Documente_Informative/GHID_TELEFOANE_27-04.md`](Documente_Informative/GHID_TELEFOANE_27-04.md) — 3 scripturi apel detaliate + checklist pregătire 5 min + obstacole comune + numere backup utile (creat 26.04 19:50). De citit/printat înainte de a forma primul număr.

**1. Medic de familie Dr. Orbán Ecaterina-Maria (Cabinet Medical Individual Nădlac):**

- [ ] Cerere **bilet de trimitere pentru oncologie medicală** (necesar la primul consult OncoHelp 4.05; ulterior nu mai e necesar) [per mail Anater 26.04]
- [ ] Cerere **bilet de trimitere pentru cardiologie** (consult cardiologic recent, max 6 luni vechime — cerere Anater) [per mail Anater 26.04]
- [ ] Discuție: oportunitatea de a le obține împreună într-o singură vizită
- [ ] Verificare contact telefonic Dr. Orbán (de adăugat în CONTACTE_MEDICALE.md dacă nu e)

**2. Cardiolog Arad — programare consult ambulator:**

- [ ] Identificare cardiolog (Dr. LAZA CRISTINA — consult anterior 10.11.2025 la cabinet Arad — dacă disponibil; alternativ cardiolog ambulator ușor accesibil)
- [ ] Programare consult înainte de 4.05 (tata are deja stent 2012 + post-stent ATC + ECO transtoracic 10.11.2025)
- [ ] Solicitare ECG + ECO + scrisoare medicală scrisă (rezultat fizic adus la consult OncoHelp)

**3. Synevo Arad — programare markeri tumorali (opțional dar recomandat pre-consult):**

- [ ] **CEA** (antigen carcinoembrionar)
- [ ] **CA 19-9** (antigen carbohidrat 19-9)
- [ ] Recoltare a jeun, dimineața (ambele se pot face la aceeași recoltare)
- [ ] Slot dimineață devreme dacă disponibil (tata să nu rabde foame mult)
- [ ] **Verificare locație Synevo Arad** (puncte de recoltare zona Bd. Revoluției / Aurel Vlaicu)
- [ ] Notă: Anater a confirmat „laborator extern la fel de bine" + alternativ se pot face la OncoHelp pe internare (1 decontat + 1 plătit)

**Acțiune Roland:** după telefoane, revine cu statusul (programare confirmată / alternativă propusă) — actualizare task corespunzător.

### [P0] 🔴 Consult oncolog digestiv — REPROGRAMAT 4 mai 2026 OncoHelp Timișoara

**Status:** 🔴 **REPROGRAMAT 30.04 → 4 mai 2026 (luni)** [per mail Dr. Anater 2026-04-26 10:28].

**Motiv reprogramare:** 30.04 era foarte aglomerată din cauza zilei libere de 1 mai; caz nou care necesită mai mult timp pentru constituirea dosarului de comisie oncologică.

**Detalii:**

- **Data:** **4 mai 2026 (luni)**
- **Unitate:** **OncoHelp Timișoara**
- **Medic oncolog:** Dr. Anater Angelo - Christian (consult inițial); va aduce și opinia unui chirurg care operează tumori esofagiene
- **Programul zilei [per mail Anater 26.04]:** consult + comisie oncologică (constituire dosar) + opinie chirurg eso pentru evaluare rezecție + plan tratament. **NU rămâne internat din 4 mai.** Posibilă intervenție laparoscopică ulterior (NU pe 4.05) pentru evaluarea peritoneului.
- **Telefon contact:** va fi furnizat de Dr. Anater la consult [per mail 26.04]

**Motivație clinică (păstrată):** CT-ul din 20.04.2026 arată proces expansiv infiltrativ circumferențial la joncțiunea eso-gastrică (Siewert II probabil) + ascită perihepatică 15 mm + intrapelvină 28 mm. Anater a clarificat în mailul 24.04 că ascita e „cel mai probabil secundară afecțiunii sale cardiace", nu oncologică primă vedere. Decizia terapeutică (FLOT adjuvant + chirurgie vs. chemoterapie paliativă) depinde de biopsie + comisie + chirurg.

**Sub-task-uri rămase:**

- [x] ✅ Programare consult — confirmată Anater 26.04 (4 mai)
- [x] ✅ Mail trimis 25.04 18:00 + răspuns primit 26.04 cu toate clarificările
- [ ] Telefoane mâine 27.04 (vezi task dedicat mai sus)
- [ ] **Pregătire dosar fizic — vezi task P0 dedicat de mai jos** (deadline 28-30.04, post-biopsie)
- [ ] (Opțional) Solicitare recomandare oncolog de la Dr. Noufal Abdul Vahab (Genesis Arad) — pentru continuitate
- [ ] Recapitulare listă întrebări pregătite (secțiunea „Pentru viitorul oncolog digestiv" mai jos)

### [P0] 🔴 Pregătire dosar fizic POST-biopsie pentru consult oncolog (deadline 28-30.04, consult 4.05)

**Status:** ACTUALIZAT 26.04.2026 cu instrucțiuni Anater 26.04 (lista revizuită completă).

**Decizie user (25.04 + clarificare Anater 26.04):** dosarul se asamblează **DUPĂ primirea rezultatului histopatologic**, pentru a fi complet la consult. Nu se pregătește în avans.

**Cronologie revizuită:**

1. **27.04.2026** — telefoane (medic familie, cardiolog, Synevo)
2. **27-30.04.2026** — recoltare markeri Synevo + consult cardiolog + obținere bilete trimitere
3. **28-29.04.2026** — primire rezultat biopsie (notificare automată ntfy.sh)
4. **29-30.04 + 1-3.05** — asamblare dosar fizic complet (printare + organizare)
5. **4.05.2026** — consult OncoHelp Timișoara (comisie oncologică)

**Componente dosar (revizuit 26.04 cu instrucțiuni Anater):**

- [ ] C.I. + card CAS
- [ ] **Bilet de trimitere medic familie pentru oncologie medicală** [per mail Anater 26.04] — necesar la primul consult OncoHelp
- [ ] Bilet trimitere BCTAP 0631727 (17.04.2026)
- [ ] Buletin endoscopie + colonoscopie 17.04.2026 (de printat din `Dosar_Medical/`)
- [ ] Buletin Bioclinica creatinină + uree 17.04.2026 (de printat)
- [ ] **Raport CT 20.04.2026** + CD DICOM (dacă s-a primit la efectuare — verificare familie)
- [ ] **Rezultat biopsie histopatologic** (element-cheie — printat când apare 28-29.04)
- [ ] **Markeri tumorali CEA + CA 19-9** (Synevo Arad sau alt laborator) — dacă recoltați mâine 27-28.04
- [ ] **Consult cardiologic recent (max 6 luni) cu ECG + ECO + scrisoare medicală scrisă** [per mail Anater 26.04]
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
