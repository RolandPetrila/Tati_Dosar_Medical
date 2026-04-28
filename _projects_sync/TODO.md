# TODO.md — Acțiuni curente

**Fișier de evidență a tuturor acțiunilor de făcut. Se actualizează continuu — la adăugarea și completarea fiecărei acțiuni.**

**Ultima actualizare:** 28 aprilie 2026 08:45 (**REZULTAT BIOPSIE 17.04 PRIMIT 28.04 — INCONCLUZIV**: „țesut de granulație + ulcerație cronică, doar SUGESTIV pentru carcinom"; recomandare anatomopatolog: IHC pe blocul T26H06044 sau rebiopsie; monitor ntfy.sh dezactivat; întrebări oncolog 4.05 reprioritizate).

---

## Calendar — date cheie

| Data                                | Eveniment                                                                                             | Status                                                                                                              |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 17.04.2026                          | Endoscopie + colonoscopie efectuate                                                                   | ✅ Finalizat                                                                                                        |
| 17.04.2026                          | Bilet trimitere CT emis                                                                               | ✅ Finalizat                                                                                                        |
| **18.04.2026**                      | **STOP Jamesi (H-48 pre-CT)**                                                                         | ✅ Finalizat                                                                                                        |
| ~~19.04.2026 — analize creatinină~~ | ~~de efectuat~~ → ✅ ACOPERIT (buletin Bioclinica 17.04.2026)                                         | ✅ Finalizat                                                                                                        |
| 19.04.2026                          | Hidratare activă (plan confirmat de familie)                                                          | ✅ Finalizat                                                                                                        |
| **20.04.2026 17:00**                | **CT torace + abdomen + pelvis cu contrast (Genesis Micălaca)**                                       | ✅ **Finalizat** — raport integrat 22.04.2026                                                                       |
| **22.04.2026**                      | Reluare Jamesi (H+48 post-CT, creatinină pre-CT normală)                                              | ✅ **Finalizat** — reluat seara 22.04, fără complicații                                                             |
| **25.04.2026 18:00**                | Mail trimis Dr. Anater (programare 30.04 + 5 întrebări organizatorice)                                | ✅ Trimis                                                                                                           |
| **26.04.2026 10:28**                | Răspuns Dr. Anater — reprogramare 30.04 → 4 mai + clarificări complete                                | ✅ Primit · ingest 26.04 19:06                                                                                      |
| **27.04.2026**                      | 3 telefoane programări                                                                                | ✅ Finalizat — cardiolog 30.04 · analize 29.04 · bilete trimitere obținute                                          |
| **28.04.2026** ✅                   | **Rezultat biopsie esofagiană PRIMIT** (Bioclinica SA Timișoara — buletin 26417A0362 / cod T26H06044) | ✅ **Primit — INCONCLUZIV** („țesut granulație + ulcerație cronică, doar SUGESTIV carcinom"); monitor ntfy.sh oprit |
| **29.04.2026**                      | Analize sânge — Bioclinica Arad                                                                       | 🟢 **PROGRAMAT** [confirmat 27.04]                                                                                  |
| **30.04.2026**                      | Consult cardiologic — ambulator Arad                                                                  | 🟢 **PROGRAMAT** [confirmat 27.04]                                                                                  |
| **28-30.04.2026**                   | Pregătire dosar fizic POST-biopsie pentru consult oncolog                                             | 🔴 P0 — vezi secțiune dedicată mai jos                                                                              |
| ~~30.04.2026~~                      | ~~Consult oncolog digestiv — OncoHelp Timișoara~~                                                     | ❌ ANULAT 26.04 (motivat: aglomerație 1 mai)                                                                        |
| **4.05.2026 (luni)** 🔴             | **Consult oncolog digestiv — OncoHelp Timișoara** (REPROGRAMAT)                                       | 🔴 **PROGRAMAT** [per mail Anater 26.04]                                                                            |
| Post-consult oncolog                | Evaluare endocrinologică (glandă suprarenală stângă)                                                  | 🟡 De programat                                                                                                     |

---

## 🔔 Monitor automat rezultat biopsie — ✅ FINALIZAT 28.04.2026

**Sistemul a notificat user-ul de apariția rezultatului** pe portalul Bioclinica. Flag `.DETECTED` activat conform protocol; monitor oprit automat.

- **Rezultat primit:** 28.04.2026 dimineața (PDF generat 06:46) — buletin **26417A0362**, cod **T26H06044**, semnat 27.04 de Dr. Glăja Romanița (Bioclinica SA Timișoara)
- **Concluzie:** INCONCLUZIVĂ — vezi `CONTEXT_MEDICAL.md §7.4` pentru interpretare clinică completă
- **Acțiune rămasă pe Sistem_Notificari (separat de `.Tati`):** confirmare workflow disabled / repo arhivat după consultul 4.05 (când ne asigurăm că nu mai apare un rezultat IHC/rebiopsie de monitorizat)

**Detalii istorice (păstrat pentru referință):**

- Repo privat: `RolandPetrila/Sistem_Notificari` (separat de `.Tati`, hub notificări reutilizabile)
- Folder local: `C:\Users\ALIENWARE\Desktop\Roly\Sistem_Notificari_Telefon\`
- Mecanism: Playwright headless → portal Bioclinica → detecție text „histopatologic" în afara „în curs" → ntfy.sh priority 5
- Activat: 2026-04-19 02:27 (commit `cf675ec`); dezactivat: 2026-04-28 (rezultat detectat)

---

## P0 — Critic, de efectuat IMEDIAT

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

- [x] ✅ **PROGRAMAT — 29.04.2026** · recoltare a jeun, dimineața
- [x] ✅ **CEA** (antigen carcinoembrionar) — inclus [confirmat 28.04]
- [x] ✅ **CA 19-9** (antigen carbohidrat 19-9) — inclus [confirmat 28.04]
- [x] ✅ **HbA1c** (hemoglobina glicozilată A1c) — adăugat [28.04] · arată controlul glicemic pe 2-3 luni · relevant pre-chimio/chirurgie

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
- [x] ✅ Programări 27.04: cardiolog 30.04 + analize Bioclinica 29.04 — bilete trimitere ❓
- [ ] **Pregătire dosar fizic — vezi task P0 dedicat de mai jos** (deadline 28-30.04, post-biopsie)
- [ ] (Opțional) Solicitare recomandare oncolog de la Dr. Noufal Abdul Vahab (Genesis Arad) — pentru continuitate
- [ ] Recapitulare listă întrebări pregătite (secțiunea „Pentru viitorul oncolog digestiv" mai jos)

### [P0] 🔴 Pregătire dosar fizic POST-biopsie pentru consult oncolog (deadline 28-30.04, consult 4.05)

**Status:** ACTUALIZAT 26.04.2026 cu instrucțiuni Anater 26.04 (lista revizuită completă).

**Decizie user (25.04 + clarificare Anater 26.04):** dosarul se asamblează **DUPĂ primirea rezultatului histopatologic**, pentru a fi complet la consult. Nu se pregătește în avans.

**Cronologie revizuită:**

1. ✅ **27.04.2026** — programări confirmate: analize Bioclinica 29.04 + cardiolog 30.04
2. ✅ **27-28.04.2026** — bilete trimitere Dr. Orbán obținute (oncologie + cardiologie)
3. ✅ **28.04.2026** — **rezultat biopsie PRIMIT** (Bioclinica 26417A0362 / T26H06044) — INCONCLUZIV, sugestiv carcinom; recomandare anatomopatolog: IHC sau rebiopsie
4. 🔜 **29.04.2026** — analize Bioclinica: CEA + CA 19-9 + **HbA1c** (hemoglobina glicozilată) + altele
5. 🔜 **30.04.2026** — consult cardiologic → scrisoare medicală + ECG + ECO
6. 🔜 **30.04 + 1-3.05** — asamblare dosar fizic complet (printare + organizare) + printare buletin biopsie + interpretare scrisă
7. 🔴 **4.05.2026** — consult OncoHelp Timișoara (comisie oncologică) → **decizie urgentă: IHC pe blocul T26H06044 sau rebiopsie țintită**

**Componente dosar (revizuit 26.04 cu instrucțiuni Anater):**

- [ ] C.I. + card CAS
- [x] ✅ **Bilet trimitere medic familie pentru oncologie medicală** [obținut 27-28.04 · per mail Anater 26.04]
- [ ] Bilet trimitere BCTAP 0631727 (17.04.2026)
- [ ] Buletin endoscopie + colonoscopie 17.04.2026 (de printat din `Dosar_Medical/`)
- [ ] Buletin Bioclinica creatinină + uree 17.04.2026 (de printat)
- [x] ✅ **CD DICOM** de la CT 20.04.2026 (Genesis) — la dosar [confirmat 28.04]
- [ ] **Raport CT 20.04.2026** (printare)
- [x] ✅ **Rezultat biopsie histopatologic** — primit 28.04.2026 (Bioclinica 26417A0362 / T26H06044). **De printat** atât buletinul Bioclinica cât și interpretarea sintetizată (`CONTEXT_MEDICAL.md §7.4`) + documentul `.docx` pentru familie generat 28.04
- [x] ✅ **Markeri tumorali CEA + CA 19-9** — confirmat în analizele Bioclinica 29.04 [confirmat 28.04]
- [x] ✅ **HbA1c (hemoglobina glicozilată A1c)** — adăugat în analizele Bioclinica 29.04 [28.04] — arată controlul glicemic pe 2-3 luni; relevant pre-chimio/chirurgie
- [ ] **Consult cardiologic** — 🟢 PROGRAMAT 30.04.2026 → de adus scrisoare medicală + ECG + ECO fizic la 04.05
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

### [P0] 🔴 NOU 28.04 — Decizie IHC pe blocul T26H06044 sau rebiopsie (consult oncolog 4.05)

**Context:** rezultatul biopsiei 17.04 primit 28.04 este **inconcluziv** — concluzie anatomopatolog: „țesut de granulație + ulcerație cronică, doar SUGESTIV pentru infiltrat carcinomatos". Limitare explicită: **număr mic de celule epiteliale atipice surprinse**. Recomandare laborator: „eventuală evaluare imunohistochimică pentru diagnostic histologic de certitudine și conduită terapeutică".

**Status:** 🔴 P0 — depinde de decizia Dr. Anater la consult 4.05.

**Trei opțiuni standard pentru diagnostic de certitudine:**

1. **IHC pe blocul existent T26H06044** [recomandat de anatomopatolog] — markeri tipici: pan-CK, CK7/CK20, CDX-2, p53; eventual HER2 / PD-L1 / MSI dacă se confirmă carcinom (relevanță decizie terapeutică). Avantaj: rapid (3-7 zile), fără reintervenție. Dezavantaj: dacă atipia e prea redusă, IHC poate fi tot inconcluziv.
2. **Rebiopsie endoscopică țintită** cu fragmente mai numeroase, mai profunde — eventual ghidată **EUS (ecoendoscopie)** pentru a depăși stratul superficial. Avantaj: randament diagnostic superior. Dezavantaj: necesită reintervenție + timp suplimentar.
3. **Combinare IHC + rebiopsie programată în paralel.**

**Sub-task-uri:**

- [ ] Printare buletin biopsie + interpretare sintetizată + document `.docx` pentru familie (28-30.04, înainte de consult)
- [ ] La consult 4.05 — întrebare prioritară Dr. Anater (vezi secțiunea „Pentru viitorul oncolog digestiv" mai jos): IHC pe blocul T26H06044 (cu ce markeri) vs rebiopsie țintită vs combinare?
- [ ] La decizia Dr. Anater — solicitare formală la Bioclinica (poate prin oncolog cu trimitere) sau programare rebiopsie la Genesis/IOCN/OncoHelp
- [ ] Update CONTEXT_MEDICAL.md §7.4 cu rezultatul IHC sau rebiopsiei, când vine

**Referințe:** `CONTEXT_MEDICAL.md §7.4` (interpretare completă) · `Dosar_Medical/2026-04-17_biopsie_esofagiana_histopatologic.json` · `Documente_Informative/EXPLICATIE_REZULTAT_BIOPSIE_2026-04-28.docx` (28.04 — pentru familie).

### [P0] 📋 Analiză și prezentare rezultat CT familiei (22.04.2026)

**Status:** NOU deschis.

**Obiectiv:** explicație clară și fără alarmism inutil, cu separarea veștilor bune de cele care necesită atenție.

- [ ] Printare / transmitere raport CT către familie (document oficial Genesis)
- [ ] Discuție 15-30 min: ce înseamnă T3-T4, N0-N1, M0 probabil; de ce ascita e un semnal de urmărit; ce urmează
- [ ] Actualizare DOCX ghid cancer esofagian cu informațiile noi (opțional — sesiune separată)

### [P0] ✅ Reluare Jamesi 22.04.2026 (H+48 post-CT) — COMPLET

**Status (22.04.2026 seara):** ✅ Jamesi reluat conform schemei (1-0-1, 50/1000 mg). **Fără complicații** post-CT (toleranță bună contrast, fără simptome renale raportate).

- [x] ✅ Pauză 48h finalizată (18.04 → 22.04)
- [x] ✅ Reluare seara 22.04 confirmată de familie
- [ ] Glicemie de control (în zilele următoare, de rutină)
- [ ] Semnale de urmărit (pentru familie): scădere diureză, edeme, senzație vertij, gust metalic → STOP imediat + consult medic familie

### [P0] ✅ Programare CT de stadializare — COMPLET

**Status:** ✅ **EFECTUAT luni 20.04.2026 ora 17:00** la Genesis Medical Clinic Micălaca. Raport integrat 22.04.2026.

- [x] Sunat pentru programare
- [x] Rezervare confirmată 20.04.2026 17:00
- [x] **CT efectuat** (Dr. Buie Florian-Laurențiu + Dr. Candea Florin-Vasile)
- [x] Raport primit și integrat în `Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json`

**Notă:** verificare primire CD cu imagini DICOM pentru consult oncolog.

### [P0] ✅ Pregătire pacient pentru CT luni 20.04.2026 — COMPLET

**Status (22.04.2026):** ✅ toate sub-task-urile executate, CT efectuat cu succes.

- [x] ✅ STOP Jamesi 18.04.2026 (H-48 pre-CT)
- [x] ✅ Analize creatinină + uree normale
- [x] ✅ Plan hidratare duminică 19.04.2026
- [x] ✅ Confirmare absență alergii
- [x] ✅ Documente pregătite
- [x] ✅ CT efectuat 20.04.2026 17:00

### [P0] ✅ Analize prealabile pentru CT — COMPLET pentru funcția renală

**Status (18.04.2026):** Buletin Bioclinica nr. 26417A0362 din 17.04.2026 integrat în dosar.

- [x] **Creatinină serică:** 0.83 mg/dL (normală, eGFR ~95) ✅
- [x] **Uree serică:** 33.4 mg/dL (normală) ✅
- [ ] Hemoleucogramă completă — opțional, ultima e din 28.11.2025; nu e blocant
- [ ] Glicemie à jeun — opțional, ultima 136 mg/dL (17.06.2025); nu e blocant

**Sursă:** `Dosar_Medical/2026-04-17_buletin_bioclinica_uree_creatinina.json`
**Data închiderii:** 18.04.2026

---

## P1 — Important, de efectuat în câteva zile

### [P1] Colectare informații medicale suplimentare de la familie

**Context:** Multe detalii importante lipsesc (lista exactă de medicamente, alergii, grupa sanguină, istoric detaliat).
**Sub-task-uri:** vezi `fisa_colectare_informatii_petrila.docx` (din rapoarte_generate/)

- [ ] Lista completă de medicamente (denumiri comerciale, doze, orar)
- [ ] Alergii confirmate (medicamente, alimente, contrast iodat anterior)
- [ ] Grupa sanguină și Rh
- [ ] Greutatea și înălțimea actuală
- [ ] HbA1c recent — pentru control diabet
- [ ] Tensiunea arterială uzuală

**Data creării:** 17.04.2026

### [P1] Obținere și scanare documente istorice

**Sub-task-uri:**

- [ ] Bilet externare 2012 (stent coronarian)
- [ ] Bilet externare 30.05.2024 (H. pylori)
- [ ] Documente hernie noiembrie 2025 (raport operator, bilet externare)
- [ ] Documente hernie anterioară (data de identificat)
- [ ] Analize recente dacă există
- [ ] Buletin endoscopie 17.04.2026 (de obținut de la Genesis Arad)
- [ ] Buletin colonoscopie 17.04.2026

**Destinație:** `documente_sursa/` conform `STRUCTURA_PROIECT.md`

**Data creării:** 17.04.2026

### [P1] Clarificare tip hernie noiembrie 2025

**Context:** Dacă a fost hernie hiatală, este direct relevantă pentru patologia esofagiană actuală.
**Sub-task-uri:**

- [ ] Întrebat pacientul / familia despre tipul exact al herniei
- [ ] Obținut raport operator
- [ ] Integrare informație în `CONTEXT_MEDICAL.md`

**Data creării:** 17.04.2026

---

## P2 — Util, de efectuat în săptămânile următoare

### [P2] ✅ Identificare și contactare oncolog digestiv — REZOLVAT 2026-04-25

**Status:** ✅ **REZOLVAT 2026-04-25** — oncolog identificat (**Dr. Anater Angelo - Christian, OncoHelp Timișoara**) și programat (**4.05.2026 luni**, REPROGRAMAT din 30.04 per mail Anater 26.04). Vezi task **[P0] Consult oncolog digestiv — REPROGRAMAT 4 mai 2026** mai sus pentru detalii complete + `Dosar_Medical/CONTACTE_MEDICALE.md`.

- [x] Evaluare opțiuni: OncoHelp Timișoara selectat (Anater + Vornicu disponibili în echipă)
- [x] Recomandare oncolog identificat: Dr. Anater (medic curant) + Dr. Vornicu Vlad (specialist senior, contact furnizat user 25.04)
- [x] Verificare disponibilitate: confirmată 4.05.2026 (program: consult + comisie oncologică + opinie chirurg eso)
- [x] Programare confirmată: 4.05.2026 OncoHelp Timișoara via thread Gmail Anater (vezi `corespondenta/2026-04-24_re-solicitare-consult-anater.md`)

### [P2] Jurnal simptome — început de la data startului

**Context:** Util pentru consultul oncolog și monitorizare evoluție.
**Sub-task-uri:**

- [ ] Creare template în `interpretari/jurnal_simptome/`
- [ ] Rugat pacientul / familia să noteze zilnic

### [P2] Verificare status asigurare CAS

**Sub-task-uri:**

- [ ] Confirmare status pensionar → asigurat automat
- [ ] Card CAS valabil
- [ ] Card European de Sănătate (opțional)

### [P2] Completare antecedente familiale detaliate

**Sub-task-uri:**

- [ ] Afecțiuni parinti (cauze deces, vârsta)
- [ ] Afecțiuni frați / surori
- [ ] Cancere în familie extinsă
- [ ] Alte boli cu componentă ereditară

---

## P3 — Util pe termen mediu

### [P3] 🔧 Pre-commit hook pentru lint JSON (escaladare audit 2026-04-26)

**Context:** auditul `AUDIT_EXTRAGERE_2026-04-26.md` a descoperit 3 JSON-uri cu ghilimele drepte `"` (U+0022) neescapate care au închis string-uri prematur, sărite silent de `generate_index.py` (`documente_canonice` 18 în loc de 21). Fix-ul a fost aplicat în commit `cec37bb`. Pentru a preveni recidiva, auditorul a recomandat ca **P2** un pre-commit hook care rulează `python -c "import json; json.load(open(f))"` pe orice `*.json` modificat. Auditorul a escaladat decizia la user (impact pe workflow git, scop mai larg decât remediere — depășește un fix punctual).

**Decizie cerută user:**

- [ ] Aplic hook (modificare `.git/hooks/pre-commit` SAU `pre-commit` framework dacă va fi adoptat)
- [ ] Refuz hook (aleg lint manual ad-hoc)
- [ ] Amânat — re-discutat la următoarea sesiune

**Note:**

- Hook-ul ar bloca commit-ul DOAR la JSON-uri syntactic invalide; nu validează schema (mai relax decât JSON Schema validation)
- Funcționează cross-platform (Windows + Linux + Mac)
- Latență adăugată ~0.1-0.5s per commit (pe ~60 JSON-uri actuale)
- Notă: scriptul `system_health_check.py` (R28) NU validează JSON syntactic — e un alt scop (KB warning)

### [P3] Documentare istoric de fumat detaliat

Pentru evaluare mai precisă a expunerii (calculul „pachete-an”).

- [ ] Numărul de țigări/zi în medie
- [ ] Perioade de consum variat
- [ ] Tip de tutun

### [P3] Documentare expuneri profesionale

- [ ] Istoric ocupațional
- [ ] Expuneri posibile (pesticide, azbest, solvenți)

### [P3] Backup și organizare dosar

- [x] Sincronizare cu Google Drive (folder privat) — ✅ proiectul rulează din Google Drive (sync continuu)
- [ ] Backup pe disk extern
- [x] Configurare Git pentru versionare automată — ✅ repo GitHub + auto-commit Regula 16 (2026-04-18)

---

## Întrebări pregătite pentru consulturi viitoare

### Pentru Dr. Noufal Abdul Vahab (gastroenterolog)

- ~~În ce segment al esofagului este leziunea?~~ ✅ clarificat: 2/3 inferioară, circumferențial, nedepășibil
- Confirmare interpretare: leziunea e „circumferențial nedepășibilă" (nu „depășibilă")?
- Dimensiunea aproximativă (longitudinală) a leziunii — la ce cm de arcada dentară începe și se termină?
- Aspect (ulcerativ, vegetant, stenozant)?
- A fost observat esofag Barrett proximal de leziune?
- A putut fi prelevată biopsie suficientă pentru analiza markerilor moleculari (HER2, PD-L1, MSI)?
- Când sunt gata rezultatele biopsiei?
- Ne recomandă un oncolog anume (din Arad / Timișoara / Cluj / București)?
- Avem nevoie de endoscopie cu eco-endoscopie (EUS) pentru stadializarea locală mai precisă?

### Pentru viitorul oncolog digestiv (URGENT — post-CT + post-biopsie inconcluzivă)

**🔴 PRIORITATE 1 — Diagnostic histologic (biopsie 17.04 inconcluzivă, primită 28.04):**

- **Care e următorul pas pentru diagnostic de certitudine: IHC pe blocul T26H06044 (recomandat de anatomopatolog Dr. Glăja) sau rebiopsie țintită endoscopică?**
- Dacă IHC: cu ce **panel de markeri** — pan-CK / CK7 / CK20 / CDX-2 / p53 + HER2 / PD-L1 / MSI dacă se confirmă carcinom?
- Dacă rebiopsie: la ce centru o programați și cu ce ghidaj (EUS pentru strat profund)? Cât timp adaugă în plan?
- Aveți acces direct la blocul T26H06044 la Bioclinica SA Timișoara pentru a demara IHC fără reintervenție?
- Cât timp adaugă fiecare opțiune în plan-ul terapeutic — cu impact asupra deciziei de începere a tratamentului?

**Despre stadializare:**

- Stadiul TNM exact (post-IHC sau post-rebiopsie): T, N, M — și criteriul aplicat?
- **Cum interpretați ascita observată la CT?** Reactivă (cardiacă, per Anater 24.04) vs. carcinomatoză peritoneală?
- Avem nevoie de **paracenteză diagnostică** pentru citologie peritoneală — acum sau după clarificare histologică?
- Avem nevoie de **laparoscopie diagnostică** pentru excluderea carcinomatozei?
- **PET-CT** recomandat pentru sensibilitate superioară CT-ului standard?

**Despre tipul tumoral și protocol (după confirmarea histologică):**

- Tipul histologic (adenocarcinom vs. scuamocelular) și grad de diferențiere?
- Clasificare Siewert I/II/III confirmată? (CT sugerează II)
- Opțiuni de tratament — ordonate după eficacitate pentru stadiul nostru?
- Protocol **FLOT** (perioperator) vs. **CROSS** (neoadjuvant chimio-radioterapie)? — decizie bazată pe componenta gastrică?
- Imunoterapie (pembrolizumab, nivolumab) — indicată dacă PD-L1+ sau MSI-H?
- Trastuzumab/zolbetuximab — dacă HER2+ sau claudin-18.2+?
- **Plan provizoriu pentru ambele scenarii** (IHC confirmă carcinom vs IHC negativ și rebiopsie necesară) — cum diferă pașii imediați?

**Despre chirurgie:**

- Dacă răspundem la chemoterapie, chirurgie fezabilă? Ezofagogastrectomie totală vs. parțială?
- **RAMIE** (robot-assisted) disponibil — e mai potrivit pentru pacient cardiac post-stent?
- Risc chirurgical la un pacient cardiac post-stent 2012 + hernie operată 2025?

**Despre comorbidități:**

- Gestionarea diabetului (Jamesi) în timpul chemoterapiei / chirurgiei?
- Gestionarea antiagregantei (Aspenter) preoperator — pauză, LMWH bridge?
- Nutriție preoperatorie (prehabilitare) — necesar jejunostomă / stent dacă disfagia se agravează?
- Gestionarea glandei suprarenale stângi hipertrofe post-consult endocrinolog?

**Despre prognostic:**

- Prognostic realist pentru stadiul nostru (supraviețuire mediană, 5-year OS)?
- Trialuri clinice disponibile la centru / în România (recruiting în 2026)?
- Second opinion internațional util (Germania, Austria, prin Card European)?

### Pentru endocrinolog (după consult oncolog)

- Interpretare glandă suprarenală stângă hipertrofă heterogenă din CT 20.04.2026?
- Necesită analize hormonale funcționale (cortizol, aldosteron, metanefrine)?
- Care e intervalul optim pentru follow-up imagistic (3 luni? 6 luni?) — corelat cu oncologia?

---

## Acțiuni finalizate (arhivă recentă)

- ✅ **22.04.2026 18:30**: Extins masiv `EXPLICATIE_CONSULT_ONCOLOG_SCENARII.md` de la 5500 la ~15000 cuvinte cu 10 secțiuni noi: secțiunea ascită detaliat cu 4 cauze analogice (conductă picură, filtre înfundate, drenaj blocat, mucegai invizibil); investigații posibile (paracenteza, laparoscopia, PET-CT „dronă termică", EUS „urechea interioară"); markeri moleculari (HER2 „antenă multiplicare", PD-L1 „steagul alb", MSI „fotocopiator stricat", Claudin-18.2); protocol FLOT detaliat (4 medicamente cu analogii, calendar 2 săpt per ciclu, efecte secundare tabelate + gestionare); imunoterapie (pembrolizumab, trastuzumab, zolbetuximab, accesibilitate PNO 2026); nutriție (alimente recomandate/evitate, suplimente ESPEN, monitorizare greutate); semnale de alarmă (112 vs contact oncolog 24h vs rutină); FAQ familie 10 întrebări (cât timp trăiește, va suferi, ne mutăm, îngrijire acasă, părul, rolul rudelor, mâncare post-tratament, ereditate, biopsie negativă, ce nu-i spunem); timeline vizual aprilie 2026 — mai 2027; glossar 39 termeni. Surse: FLOT4, Keynote-590/811, SPOTLIGHT, ESPEN, NCCN V1.2025, ESMO 2022.
- ✅ **22.04.2026 18:30**: Generat `Dosar_Medical/rapoarte_generate/2026-04-22_explicatie_consult_oncolog_scenarii.docx` (64 KB, ~35 pagini estimat) cu script Python `generate_explicatie_scenarii.py` (script-as-source-of-truth): design profesional cu cover page, cuprins, paletă culori medical (albastru/verde/portocaliu/roșu), callouts colorate pentru analogii/URGENT/OK/warning, tabele cu zebra stripes + header albastru, quotes cu border lateral pentru analogii, 16 secțiuni complete + surse + disclaimer. Include `.meta.json` cu chain-of-custody Regula 14.
- ✅ **22.04.2026 18:09**: Creat `Documente_Informative/EXPLICATIE_CONSULT_ONCOLOG_SCENARII.md` — document explicativ extins (poveste casă/arhitect + răspunsuri la 4 întrebări Roland: trebuie merge la oncolog acum, apa poate fi cancerigenă indiferent de origine, ce poate oncolog fără analize, e obligatoriu analize suplimentare) + **4 scenarii combinatorii** biopsie/ascită cu plan tratament detaliat pentru fiecare (Scenariu A: malign + benignă = stadiu III FLOT curativ ~60-70% prob.; B: malign + malign = stadiu IV chimio + imunoterapie paliativ ~15-25%; C: benignă + benignă = non-oncologic ~5-10%; D: benignă + malign = rebiopsie + căutare tumoră primară ~1-3%). Surse: studii FLOT4, Keynote-590/811, SPOTLIGHT. Marcaje certitudine R17 aplicate.
- ✅ **22.04.2026 17:41**: Restructurare organizare proiect — creat folder `Documente_Informative/` pentru documente informative/ghiduri, mutat `GHID_CONSULT_ONCOLOG.md` în acesta (locație nouă: `Documente_Informative/GHID_CONSULT_ONCOLOG.md`), șters `GHID_PREZENTARE_CT_FAMILIE.md` (la cererea user). Adăugată Regula 19 în `CLAUDE.md` (v8): documente informative NU la rădăcina proiectului, ci în folderul dedicat. `STRUCTURA_PROIECT.md` + `DASHBOARD.html` actualizate cu noua locație.
- ✅ **22.04.2026 17:00**: Jamesi reluat seara conform schemei standard (1-0-1, 50/1000 mg), fără complicații post-CT — pauza H-48h → H+48h respectată corect, creatinină pre-CT normală (0.83 mg/dL).
- ✅ **22.04.2026 17:00**: Creat `GHID_PREZENTARE_CT_FAMILIE.md` — document operațional pentru Roland cu structură detaliată de prezentare rezultat CT familiei (4 blocuri, scripturi sugerate, Q&A, materiale printat, semnale escaladare).
- ✅ **22.04.2026 17:00**: Creat `GHID_CONSULT_ONCOLOG.md` — checklist acțiune concret pentru programare consult oncolog URGENT (recomandare Dr. Noufal, centre oncologice Arad/Timișoara/Cluj/București cu telefoane și informații, dosar fizic, 22 întrebări pregătite, costuri estimative, timeline realist, checklist 3-zile + ziua consultului + post-consult).
- ✅ **22.04.2026 16:00**: Rezultat CT 20.04.2026 integrat în dosar (JSON structurat + .meta.json + actualizare CONTEXT_MEDICAL.md + DASHBOARD.html). Clarificare interpretare endoscopie confirmată de user: „circumferențial nedepășibil endoscopic". Stadializare imagistică preliminară T3-T4, N0-N1, M0 probabil, Siewert II probabil. Ascită perihepatică + intrapelvină de evaluat cu oncolog.
- ✅ **20.04.2026 17:00**: CT torace + abdomen + pelvis efectuat la Genesis Medical Clinic Micălaca (Dr. Buie Florian-Laurențiu + Dr. Candea Florin-Vasile, medici primari radiologie).
- ✅ **18.04.2026 21:04**: GitHub Pages configurat pentru distribuție live-sync `DASHBOARD.html`. URL: https://rolandpetrila.github.io/Tati_Dosar_Medical/ — auto-deploy la fiecare `git push`. Repo mutat public intenționat. `index.html` redirect adăugat la rădăcina repo-ului.
- ✅ **18.04.2026 03:31**: Raport reacții adverse Jamesi + Triplixam generat în format `.docx` — `Dosar_Medical/rapoarte_generate/2026-04-18_raport_reactii_adverse_jamesi_triplixam.docx` (47 KB, ~30 pagini). Marcaj certitudine conform Regula 17 nouă. Observație clinică documentată: combinație sitagliptin + perindopril → risc crescut angioedem (RCP Triplixam 4.5). De prezentat familiei + medicului curant.
- ✅ **18.04.2026 03:10**: Remediere audit Regula 16 sub-clauza 7 (clarificări + logare retroactivă commit `478048f`). Detalii în `CHANGELOG.md`.
- ✅ **18.04.2026**: Audit complet Dosar_Medical — migrare JSON la schema v2.0, corecturi date (CNP talon, data nașterii urologie, nume manuscris, unități lab), dedup chirurgie 3→1, creare JSON identitate, `.meta.json`-uri chain-of-custody, reorganizare subfoldere tematice, reconciliere CONTEXT_MEDICAL.md. Detalii în `CHANGELOG.md`.
- ✅ 17.04.2026: Endoscopie digestivă superioară efectuată
- ✅ 17.04.2026: Colonoscopie efectuată
- ✅ 17.04.2026: Biopsie esofagiană prelevată
- ✅ 17.04.2026: Bilet trimitere CT emis
- ✅ 14.04.2026: Ecografie abdominală efectuată
- ✅ 30.05.2024: Tratament H. pylori efectuat cu succes

---

## Acțiuni noi deschise de audit (18.04.2026)

### [P0] ✅ Confirmare status alergii pacient (pre-CT) — FINALIZAT

**Rezultat (18.04.2026 13:28):** Pacientul NU are alergii la iod, fructe de mare sau contrast iodat anterior. Fără alergii medicamentoase cunoscute. Confirmat de Roland Petrilă (familie).

- [x] Interogare directă pacient + familia: alergii la medicamente, iod, fructe de mare → negative
- [x] Notare în `CONTEXT_MEDICAL.md`, secțiunea 11

**Notă:** confirmarea rămâne valabil să fie repetată verbal la radiolog înainte de injectarea contrastului.

### [P1] ✅ Identificare conținut PDF-uri nedigitizate — REZOLVAT 2026-04-24

**Rezolvat:** toate 6 PDF-uri `doc_neidentificat_{2-7}.pdf` din `99_altele/` au fost identificate prin match exact de dimensiune cu fișierele din workspace-ul extern `Arhiva_Generala`:

- `_2` (1.52 MB) = `Hernie municipal.pdf`
- `_3` (1.75 MB) = `Cardiologie.pdf`
- `_4` (2.40 MB) = `Urologie 2025.pdf`
- `_5` (1.39 MB) = `Analize_2025.pdf`
- `_6` (898 KB) = `Heliobacter.pdf`
- `_7` (12 MB) ≈ `2024 - complet analize.pdf`

**Operații efectuate 2026-04-24:**

- [x] Identificate ca duplicate (match dimensiune)
- [x] Conținutul real copiat din `Arhiva_Generala` în folderele dedicate (`04_helicobacter_2024/`, `05_analize_laborator/`, `06_urologie_gastro_2025/`, `07_hernie_2025_11/`, `13_cardiologie_ambulator_2025/`, `14_UPU_2024_05_30/`)
- [x] JSON-uri canonice create din extrageri strict-extractive (12 noi)
- [x] Folderul `99_altele/` **ȘTERS** integral (nu arhivat — conform cererii user)

### [P1] Digitizare documente lipsă

- [ ] PDF original cardiologie Vichy 2012 (pentru tipul exact al stent-ului DES vs. BMS)
- [x] ✅ Document externare episod H. pylori 30.05.2024 — **REZOLVAT 2026-04-24** prin integrarea `2024_Gastro_Complet` (10 pagini UPU + consulturi + analize) → JSON-uri: `2024-05-30_upu_consult_gastro_cardio.json` + `2024-05-30_analize_upu_sange_1517243.json` + `2024-05-30_analize_upu_urina_1517290.json`
- [ ] Buletin ecografie abdominală 14.04.2026

### [P1] ✅ Identificare medic prescriptor schema 10.11.2025 — REZOLVAT 2026-04-24

**Rezolvat:** **Dr. LAZA CRISTINA** (medic primar cardiolog, cod parafă **C07842**) — identificat prin cross-reference cu ecografia transtoracică efectuată în aceeași zi (10.11.2025), text tipărit cu cod parafă clar vizibil pe ștampilă. Consult pre-chirurgie hernie.

- [x] Identificare prin cross-reference ECO aceeași zi (10.11.2025)
- [x] Update `CONTEXT_MEDICAL.md` §4 Medicație + §9 Echipă medicală
- [x] Update `Dosar_Medical/2025-11-10_schema_medicamente.json`
- [ ] Clarificare cabinet/unitate Dr. LAZA CRISTINA (probabil cabinet cardiologie ambulator Arad — de confirmat cu familia)

### [P1] ✅ Clarificare TORVACARD — REZOLVAT 2026-04-25

**Status:** ✅ **REZOLVAT 2026-04-25** — clarificat de user. Schema reală în vigoare este cea manuscrisă din `Dosar_Medical/documente_sursa/08_schema_tratament/` (4 medicamente: Aspenter, Concor, Triplixam, Jamesi). **Pacientul NU administrează TORVACARD.**

- [x] Clarificare status real — user a confirmat 25.04 că schema reală e cea manuscrisă, fără statină
- [x] Update `CONTEXT_MEDICAL.md §4` — sub-secțiunea de discrepanță înlocuită cu observație clinică scurtă (LDL 133 + lipsă statină pre-esofagectomie → de discutat la consult oncolog 30.04)
- [x] `Dosar_Medical/2025-11-10_schema_medicamente.json` — reflectă deja schema reală, nu necesită modificare
- [x] `DASHBOARD.html` — alert TORVACARD eliminat la regenerarea 2026-04-25
- [ ] **Acțiune rămasă:** discuție cu oncologul (30.04 OncoHelp) + medic familie (Dr. Orbán) despre reevaluare prevenție CV secundară (LDL 133 mg/dL pre-esofagectomie) — listat în task P0 „Pregătire dosar fizic"

### [P1] 🟢 NOU — Test confirmare eradicare H. pylori (UBT sau antigen fecal)

**Context:** Serologia Anti-H. pylori IgG era pozitivă **>100 U/mL** în 04.06.2024 + 06.09.2024 (Ultra ClinicaVest Pecica). Serologia IgG NU distinge infecție activă de antecedentă (anticorpii persistă luni/ani post-eradicare). Tratamentul antibiotic + IPP probabil a fost efectuat ambulator post-episod UPU 30.05.2024 (NU documentat explicit). **Niciun test de control post-eradicare** efectuat (UBT sau antigen fecal).

**De ce e important pre-esofagectomie:**

- HP activ persistent în context tumoral eso-gastric → factor de risc inflamator + posibil impact pe vindecare anastomotică
- Eradicarea HP înainte de chirurgie e standard ESMO/NCCN dacă se confirmă activ

**Sub-task-uri:**

- [ ] **Decizie test:** UBT (urea breath test, mai sensibil) sau antigen fecal HP (alternativă acceptabilă)
- [ ] Programare test la laborator (Ultra ClinicaVest Pecica / Bioclinica Arad / alt laborator)
- [ ] Întrebare pentru oncolog 30.04: este necesar testul pre-FLOT/chirurgie sau se poate face concomitent?
- [ ] Dacă pozitiv → re-tratament eradicare conform ghid Maastricht VI
- [ ] Integrare rezultat în `Dosar_Medical/` (JSON canonic + .meta.json + propagare CONTEXT_MEDICAL.md)

**Data deschiderii:** 2026-04-25.

### [P2] ✅ Rafinare R28 System Health Monitor — metric `auto_loaded_md_kb` — FINALIZAT 2026-04-26

**Status:** ✅ **FINALIZAT 2026-04-26 19:30** (sesiunea declanșată de WARNING fals-pozitiv la 61.4% după ingest mail Anater).

**Implementat:**

- [x] Metric nou `auto_loaded_md_kb` în `scripts/system_health_check.py` cu prag **150 KB** (calibrat pragmatic: 5 fișiere × ~40 KB oficial CLAUDE.md = ~200 KB teoretic; 150 KB lasă ~50% headroom; la 150 KB ≈ 50K tokens = 25% Sonnet / 5% Opus 1M). Listă fișiere monitorizate:
  - `CLAUDE.md` (root) — always-on
  - `REGULAMENT.md` — citit la prima interacțiune (per ordine din `CLAUDE.md` root)
  - `REGULI_CLAUDE_CODE.md` — citit la prima interacțiune
  - `Dosar_Medical/CLAUDE.md` — nested contextual
  - `Documente_Informative/CLAUDE.md` — nested contextual
- [x] `total_md_root_kb` **demote la metric informativ** (NU mai declanșează WARNING/ALERT/CRITICAL — rămâne în output pentru igienă proiect, dar nu contribuie la overall status).
- [x] Update `REGULI_CLAUDE_CODE.md §Regula 28` cu metricul nou + istoric rafinări (2 rafinări documentate: 2026-04-25 ridicare prag temporar + 2026-04-26 rafinare arhitecturală).
- [x] Backup R10: `Dosar_Medical/arhiva/context_medical_versiuni/system_health_check_pre-rafinare-r28_2026-04-26_1930.py` + `REGULI_CLAUDE_CODE_pre-rafinare-r28_2026-04-26_1930.md`.

**Rezultat:** WARNING pe `total_md_root_kb` eliminat definitiv. Sistemul alertează acum pe risc REAL (auto-loaded files > 100 KB), nu pe igienă cumulativă a logurilor istorice (CHANGELOG, SESSION_LOG).

**Data deschiderii:** 2026-04-25 · **Data finalizării:** 2026-04-26.

### [P2] HbA1c recent

**Context:** monitorizare control diabet cu Jamesi; ultima HbA1c necunoscută.

### [P2] Prezentare raport reacții adverse familiei + medic

**Context:** raport generat 18.04.2026 — `Dosar_Medical/rapoarte_generate/2026-04-18_raport_reactii_adverse_jamesi_triplixam.docx`.

- [ ] Printare/trimitere familie (pregătire înainte de CT)
- [ ] Atenționare către medicul curant despre interacțiunea sitagliptin + perindopril (risc angioedem) — de întrebat dacă e utilă monitorizare adițională sau dacă combinația trebuie reevaluată post-CT

### [P2] Verificare versiune curentă SmPC Triplixam pe ANMDMR

**Context:** SmPC-ul Servier folosit pentru raport e versiunea 06.2021 (vechime ~5 ani). Pentru decizii terapeutice majore, se verifică versiunea curentă pe anm.ro.

- [ ] Căutare „Triplixam 10/2.5/5" pe nomenclator.anm.ro
- [ ] Comparare cu conținutul raportului — actualizare dacă există diferențe semnificative

### [P2] ✅ Clarificare conținut arhivă `2025-11-01_talon_pensie_asigurare.zip` — FINALIZAT

**Decizie (18.04.2026 13:28):** ȘTERS la cererea user-ului. JSON-urile canonice sunt în `Dosar_Medical/`, iar git-ul păstrează istoricul complet — backup-ul zip era redundant.

### [P2] Clarificare rezolvare simultană hidrocel + chiste epididimare

**Context:** scrisoarea din 28.10.2025 indica ambele intervenții în plus față de hernie; biletul de externare 28.11.2025 menționează doar hernia + aderențe.

---

## Acțiuni noi deschise de rezultat CT 20.04.2026 (22.04.2026)

### [P0] 🔴 Consult oncolog digestiv URGENT

**Detalii:** vezi prima secțiune P0 de mai sus („Consult oncolog digestiv URGENT (post-CT, 22.04.2026)").

### [P0] 📋 Analiză și prezentare rezultat CT familiei

**Detalii:** vezi prima secțiune P0 de mai sus.

### [P1] Verificare CD cu imagini DICOM de la CT Genesis Micălaca

**Context:** pentru consultul oncologic, CD-ul cu imagini DICOM e util pentru ca oncologul să vadă direct imaginile (nu doar raportul narativ).

- [ ] Confirmare familie: s-a primit CD la efectuarea CT?
- [ ] Dacă nu, solicitare retrospectivă la Genesis Micălaca

### [P1] Evaluare endocrinologică glanda suprarenală stângă

**Context:** CT 20.04.2026 descrie glanda suprarenală stângă „hipertrofă, heterogenă, fără leziuni focale, de monitorizat". Diagnostic diferențial: incidentaloma benignă / adenom nefuncțional / hiperplazie reactivă / metastază (mai puțin probabilă).

- [ ] Programare consult endocrinologic (poate aștepta post-consult oncolog)
- [ ] Analize bazale: cortizol 8AM, aldosteron/renină, metanefrine plasmatice (+/- urinare 24h)
- [ ] Follow-up imagistic la 3-6 luni (corelat cu controlul oncologic)

### [P2] Corelare clinică leziune chistică subcutan perete toracic posterior

**Context:** CT 20.04.2026 descrie „leziune chistică rotund-ovalară încapsulată, 22/47.4 mm, subcutan perete toracic posterior cXI-cXII, a se corela clinic". Probabil benignă (chist sebaceu, lipom, chist epidermoid).

- [ ] Palpare clinică la următorul consult (oncolog sau medic familie)
- [ ] Eventual ecografie superficială dacă e semnificativă

### [P2] Monitorizare colecție fluidă pulmonar bazal LID (9.3 mm)

**Context:** CT 20.04.2026 descrie colecție fluidă mică, nesemnificativă clinic singură, dar de urmărit evolutiv.

---

## Note

- Acțiunile cu deadline strict sunt marcate clar.
- Când o acțiune este finalizată, se mută în secțiunea „Acțiuni finalizate” cu data completării.
- Acțiunile noi care apar se adaugă la nivelul de prioritate corespunzător.
- La fiecare sesiune, Claude Code verifică statusul acțiunilor deschise și raportează.

---

**Ultima revizuire:** 17 aprilie 2026.
