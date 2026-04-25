# TODO.md — Acțiuni curente

**Fișier de evidență a tuturor acțiunilor de făcut. Se actualizează continuu — la adăugarea și completarea fiecărei acțiuni.**

**Ultima actualizare:** 25 aprilie 2026 03:00 (clarificare TORVACARD: NU se administrează — schema reală este cea manuscrisă; consult oncolog ✅ programat 30.04 OncoHelp Timișoara; rezultat biopsie estimat 28-29.04; dosar fizic POST-biopsie; ALIMENTATIE.md sincronizat cu ghid nutrițional ESPEN/IDDSI/FLOT).

---

## Calendar — date cheie

| Data                                | Eveniment                                                       | Status                                                  |
| ----------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------- |
| 17.04.2026                          | Endoscopie + colonoscopie efectuate                             | ✅ Finalizat                                            |
| 17.04.2026                          | Bilet trimitere CT emis                                         | ✅ Finalizat                                            |
| **18.04.2026**                      | **STOP Jamesi (H-48 pre-CT)**                                   | ✅ Finalizat                                            |
| ~~19.04.2026 — analize creatinină~~ | ~~de efectuat~~ → ✅ ACOPERIT (buletin Bioclinica 17.04.2026)   | ✅ Finalizat                                            |
| 19.04.2026                          | Hidratare activă (plan confirmat de familie)                    | ✅ Finalizat                                            |
| **20.04.2026 17:00**                | **CT torace + abdomen + pelvis cu contrast (Genesis Micălaca)** | ✅ **Finalizat** — raport integrat 22.04.2026           |
| **22.04.2026**                      | Reluare Jamesi (H+48 post-CT, creatinină pre-CT normală)        | ✅ **Finalizat** — reluat seara 22.04, fără complicații |
| **28-29.04.2026** (estimat)         | **Rezultat biopsie esofagiană** (Bioclinica Arad)               | 🟢 În așteptare · monitor automat activ 24/7 (ntfy.sh)  |
| **29-30.04.2026**                   | Pregătire dosar fizic POST-biopsie pentru consult oncolog       | 🔴 P0 nou — vezi secțiune dedicată mai jos              |
| **30.04.2026** ✅                   | **Consult oncolog digestiv — OncoHelp Timișoara**               | ✅ **PROGRAMAT** (confirmat user 25.04)                 |
| Post-consult oncolog                | Evaluare endocrinologică (glandă suprarenală stângă)            | 🟡 De programat                                         |

---

## 🔔 Monitor automat rezultat biopsie — ACTIV

**Sistem independent** care verifică automat portalul Bioclinica la fiecare 30 min, 24/7, și notifică instant pe telefonul Roland (ntfy.sh, prioritate urgentă) când apare rezultatul histopatologic. **Nu depinde de laptop pornit** — rulează pe GitHub Actions.

- **Repo privat:** `RolandPetrila/Sistem_Notificari` (nu e parte din dosarul `.Tati`, e hub separat pentru notificări reutilizabile)
- **Folder local:** `C:\Users\ALIENWARE\Desktop\Roly\Sistem_Notificari_Telefon\`
- **Mecanism:** Playwright headless → login Bioclinica (credențialele — cod buletin, cod acces, CNP — stocate ca GitHub Secrets în repo-ul privat, **nu** în acest dosar) → detecție text „histopatologic" în afara secțiunii „în curs de execuție" → ntfy.sh priority 5 → se oprește automat după prima notificare (flag `.DETECTED`)
- **Abonament telefon ntfy:** topicul folosit de monitor trăiește doar în Secrets privat + aplicația ntfy pe telefon (nu e scris aici în dosarul public)
- **Activat:** 2026-04-19 02:27 (commit `cf675ec`)

**Acțiune așteptată:** niciuna din partea ta; primești notificare pe telefon când e cazul.

---

## P0 — Critic, de efectuat IMEDIAT

### [P0] ✅ Consult oncolog digestiv — PROGRAMAT 30.04.2026 OncoHelp Timișoara

**Status:** ✅ **PROGRAMAT** — confirmat de user 25.04.2026.

**Detalii:**

- **Data:** 30 aprilie 2026
- **Unitate:** **OncoHelp Timișoara**
- **Context așteptat:** rezultat biopsie estimat 28-29.04 → consultul are toate elementele decizionale

**Motivație (păstrată pentru context):** CT-ul din 20.04.2026 arată proces expansiv infiltrativ circumferențial la joncțiunea eso-gastrică (Siewert II probabil) + **ascită perihepatică 15 mm + intrapelvină 28 mm**. Ascita în context neoplazic esofagian avansat poate indica **carcinomatoză peritoneală** (stadiu IV). Decizia terapeutică se schimbă esențial: FLOT adjuvant + chirurgie vs. chemoterapie paliativă.

**Sub-task-uri rămase:**

- [x] ✅ Programare consult — confirmată user 25.04
- [ ] (Opțional) Solicitare recomandare oncolog de la Dr. Noufal Abdul Vahab (Genesis Arad) — pentru continuitate
- [ ] **Pregătire dosar fizic — vezi task P0 dedicat de mai jos** (deadline 29-30.04, post-biopsie)
- [ ] Recapitulare listă întrebări pregătite (secțiunea „Pentru viitorul oncolog digestiv" mai jos)

### [P0] 🔴 Pregătire dosar fizic POST-biopsie pentru consult oncolog (deadline 29-30.04)

**Status:** NOU deschis 25.04.2026.

**Decizie user (25.04):** dosarul se asamblează **DUPĂ primirea rezultatului histopatologic**, pentru a fi complet la consult. Nu se pregătește în avans.

**Cronologie:**

1. **28-29.04.2026** — primire rezultat biopsie (notificare automată ntfy.sh pe telefon)
2. **29-30.04.2026** — asamblare dosar fizic (printare + organizare)
3. **30.04.2026** — consult OncoHelp Timișoara

**Componente dosar:**

- [ ] C.I. + card CAS
- [ ] Bilet trimitere BCTAP 0631727 (17.04.2026)
- [ ] Buletin endoscopie + colonoscopie 17.04.2026 (de printat din `Dosar_Medical/`)
- [ ] Buletin Bioclinica creatinină + uree 17.04.2026 (de printat)
- [ ] **Raport CT 20.04.2026** + CD DICOM (dacă s-a primit la efectuare — verificare familie)
- [ ] **Rezultat biopsie histopatologic** (element-cheie — printat când apare 28-29.04)
- [ ] Listă medicație curentă (4 confirmate: Aspenter, Concor, Triplixam, Jamesi) + alergii (fără)
- [ ] Listă întrebări pregătite pentru oncolog (secțiunea dedicată mai jos)
- [ ] **Notă observație** statină nealuată — pentru discuție la consult (vezi `CONTEXT_MEDICAL.md §4`)
- [ ] (Opțional) `Documente_Informative/EXPLICATIE_CONSULT_ONCOLOG_SCENARII.md` — pentru orientare familie pre-consult

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

### [P2] Identificare și contactare oncolog digestiv

**Context:** Pentru a avea un consult pregătit imediat ce primim rezultatele biopsiei și CT.
**Sub-task-uri:**

- [ ] Evaluare opțiuni: Arad, Timișoara, Cluj (conform `CONTEXT_MEDICAL.md`)
- [ ] Recomandare de la Dr. Noufal Abdul Vahab (dacă e posibil)
- [ ] Verificare disponibilitate, costuri, timp de așteptare
- [ ] Programare preventivă (dacă permit, se pot anula dacă nu e cazul)

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

### Pentru viitorul oncolog digestiv (URGENT — post-CT)

**Despre stadializare:**

- Stadiul TNM exact (după biopsie): T, N, M — și criteriul aplicat?
- **Cum interpretați ascita observată la CT?** Reactivă vs. carcinomatoză peritoneală?
- Avem nevoie de **paracenteză diagnostică** pentru citologie peritoneală?
- Avem nevoie de **laparoscopie diagnostică** pentru excluderea carcinomatozei?
- **PET-CT** recomandat pentru sensibilitate superioară CT-ului standard?

**Despre tipul tumoral și protocol:**

- Tipul histologic (adenocarcinom vs. scuamocelular) și grad de diferențiere?
- Clasificare Siewert I/II/III confirmată? (CT sugerează II)
- Opțiuni de tratament — ordonate după eficacitate pentru stadiul nostru?
- Protocol **FLOT** (perioperator) vs. **CROSS** (neoadjuvant chimio-radioterapie)? — decizie bazată pe componenta gastrică?
- Imunoterapie (pembrolizumab, nivolumab) — indicată dacă PD-L1+ sau MSI-H?
- Trastuzumab/zolbetuximab — dacă HER2+ sau claudin-18.2+?

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
