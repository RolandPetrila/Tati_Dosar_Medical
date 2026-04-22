# TODO.md — Acțiuni curente

**Fișier de evidență a tuturor acțiunilor de făcut. Se actualizează continuu — la adăugarea și completarea fiecărei acțiuni.**

**Ultima actualizare:** 22 aprilie 2026 16:00 (rezultat CT integrat + clarificare „nedepășibil endoscopic").

---

## Calendar — date cheie

| Data                                | Eveniment                                                       | Status                                          |
| ----------------------------------- | --------------------------------------------------------------- | ----------------------------------------------- |
| 17.04.2026                          | Endoscopie + colonoscopie efectuate                             | ✅ Finalizat                                    |
| 17.04.2026                          | Bilet trimitere CT emis                                         | ✅ Finalizat                                    |
| **18.04.2026**                      | **STOP Jamesi (H-48 pre-CT)**                                   | ✅ Finalizat                                    |
| ~~19.04.2026 — analize creatinină~~ | ~~de efectuat~~ → ✅ ACOPERIT (buletin Bioclinica 17.04.2026)   | ✅ Finalizat                                    |
| 19.04.2026                          | Hidratare activă (plan confirmat de familie)                    | ✅ Finalizat                                    |
| **20.04.2026 17:00**                | **CT torace + abdomen + pelvis cu contrast (Genesis Micălaca)** | ✅ **Finalizat** — raport integrat 22.04.2026   |
| **22.04.2026 (AZI)**                | Reluare Jamesi (H+48 post-CT, creatinină pre-CT normală)        | 🟡 **AZI** — reluare conform schemei            |
| {17.04.2026 + 7-14 zile}            | Rezultat biopsie (estimat 24.04-01.05)                          | 🟡 În așteptare · monitor automat activ ↓       |
| **Post-CT, URGENT**                 | **Consult oncolog digestiv** (nu se așteaptă biopsia)           | 🔴 **De programat URGENT** (ascită de elucidat) |
| Post-consult oncolog                | Evaluare endocrinologică (glandă suprarenală stângă)            | 🟡 De programat                                 |

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

### [P0] 🔴 Consult oncolog digestiv URGENT (post-CT, 22.04.2026)

**Status:** NOU deschis. **Prioritate maximă** — nu se așteaptă biopsia.

**Motivație accelerare:** CT-ul din 20.04.2026 arată proces expansiv infiltrativ circumferențial la joncțiunea eso-gastrică (Siewert II probabil) + **ascită perihepatică 15 mm + intrapelvină 28 mm**. Ascita în context neoplazic esofagian avansat poate indica **carcinomatoză peritoneală** (stadiu IV). Decizia terapeutică se schimbă esențial: FLOT adjuvant + chirurgie vs. chemoterapie paliativă.

**Sub-task-uri:**

- [ ] Solicitare recomandare oncolog de la Dr. Noufal Abdul Vahab (Genesis Arad)
- [ ] Comparare opțiuni: Arad / Timișoara (IOCN, OncoHelp, SCJU) / Cluj (IOC Chiricuță) / București (Fundeni, SanaDor, Monza)
- [ ] Programare preventivă cât mai curând, chiar înainte de rezultatul biopsiei
- [ ] Pregătire dosar fizic pentru consult: CI, card CAS, bilet BCTAP, buletin endoscopie 17.04, buletin Bioclinica creatinină 17.04, **raport CT 20.04 (imprimare + CD DICOM dacă s-a primit)**
- [ ] Listă întrebări actualizată (secțiunea „Întrebări pentru viitorul oncolog digestiv" mai jos)

### [P0] 📋 Analiză și prezentare rezultat CT familiei (22.04.2026)

**Status:** NOU deschis.

**Obiectiv:** explicație clară și fără alarmism inutil, cu separarea veștilor bune de cele care necesită atenție.

- [ ] Printare / transmitere raport CT către familie (document oficial Genesis)
- [ ] Discuție 15-30 min: ce înseamnă T3-T4, N0-N1, M0 probabil; de ce ascita e un semnal de urmărit; ce urmează
- [ ] Actualizare DOCX ghid cancer esofagian cu informațiile noi (opțional — sesiune separată)

### [P0] 🟡 Reluare Jamesi AZI 22.04.2026 (H+48 post-CT)

**Status:** schema standard se reia AZI (1-0-1, 50/1000 mg). Creatinina pre-CT (17.04.2026) a fost 0.83 mg/dL (normală).

- [x] ✅ Pauză 48h finalizată (18.04 → 22.04)
- [ ] Reluare normală: doză dimineață + doză seară
- [ ] Glicemie de control
- [ ] Dacă apar simptome renale post-CT (scădere urinat, edeme, vertij, gust metalic) → STOP imediat + consult

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

### [P1] Identificare conținut PDF-uri nedigitizate

**Context:** 6 PDF-uri `2026-04-17_doc_neidentificat_{2-7}.pdf` în `Dosar_Medical/documente_sursa/99_altele/` fără conținut cartografiat.

- [ ] Deschidere fiecare PDF
- [ ] Anunț Claude Code: `proces [nume_fisier], corelează cu JSON-ul v2 corespunzător`
- [ ] Actualizare `.meta.json` corespunzător

### [P1] Digitizare documente lipsă

- [ ] PDF original cardiologie Vichy 2012 (pentru tipul exact al stent-ului DES vs. BMS)
- [ ] Document externare episod H. pylori 30.05.2024
- [ ] Buletin ecografie abdominală 14.04.2026

### [P1] Identificare Dr. LAZĂR (prescriere 10.11.2025)

**Context:** nume medic parțial ilizibil pe manuscris.

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
