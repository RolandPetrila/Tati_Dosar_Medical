# WEB_QUERIES.md — Log cercetări web (Regula 15)

**Scop:** pentru fiecare cercetare web care produce conținut introdus în dosar, loghez aici întrebarea exactă, sursele acceptate, sursele respinse, concluzia integrată și data publicării sursei.

**De completat proactiv la fiecare `WebSearch`/`WebFetch`/Firecrawl/Context7/Brave care alimentează fișiere de referință.**

---

## Format standard per intrare

```markdown
## YYYY-MM-DD HH:MM — [slug-subiect]

- **Query exact:** "..."
- **Instrumente folosite:** WebSearch / WebFetch / Firecrawl / Context7 / Brave
- **Surse acceptate:**
  - URL — motiv acceptare (instituție medicală, peer-reviewed, etc.) — data publicării
- **Surse respinse:**
  - URL — motiv respingere (comercial, blog, outdated)
- **Concluzie introdusă în:** `fisier.md` / `fisier.json`, secțiunea X
- **Data publicării materialului sursă:** YYYY-MM-DD
- **Încredere concluzie:** high / medium / low
```

---

## Intrări

## 2026-04-18 09:25-09:30 — ghiduri-internationale-CT-contrast-pacient-pe-metformin-IECA-diuretic

- **Scop:** identificarea gap-urilor in cele 4 rapoarte AI existente despre Jamesi+Triplixam, prin verificarea ghidurilor internationale actuale (ACR 2024, ESUR 2025) — pentru a putea adauga in raportul unificat informatiile lipsa relevante CT-ului din 20.04.2026.
- **Instrumente folosite:** `WebSearch` (4 query-uri).
- **Queries exacte:**
  1. `"ESUR guidelines contrast media 2024 metformin recommendation eGFR"` — WebSearch
  2. `"ACR manual contrast media 2024 metformin discontinuation iodinated contrast"` — WebSearch
  3. `"ACE inhibitor diuretic continue or hold before iodinated contrast CT scan 2024"` — WebSearch
  4. `"post-contrast acute kidney injury PC-AKI prevention 2024 hydration protocol"` — WebSearch
- **Surse acceptate (CERT, sursă primară):**
  - https://www.esur.org/wp-content/uploads/2025/12/Guidelines-2025-ESUR-vf-1.pdf — **ESUR Contrast Media Safety Committee Guidelines 2025**. Motiv: ghidul european oficial al European Society of Urogenital Radiology, versiune cea mai recenta. Data publicarii: decembrie 2025.
  - https://adus-radiologie.ch/files/ESUR_Guidelines_10.0.pdf — **ESUR Guidelines on Contrast Agents v10.0**. Motiv: copie oficiala accesibila a ghidului ESUR v10.0. Data: anterioara versiunii 2025, complementara.
  - https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2024/08/ACR-contrast-2024.pdf — **ACR Manual on Contrast Media versiunea 2024**. Motiv: ghidul american oficial al American College of Radiology, publicat iulie 2024. Cea mai recenta versiune comprehensiva.
  - https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Contrast-Manual — **ACR Manual on Contrast Media (oficial portal)**. Motiv: confirma versiunea curenta.
- **Surse acceptate (CERT, peer-reviewed):**
  - https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1547725/full — **Frontiers in Medicine: Systematic review and meta-analysis of guidelines on metformin + contrast media in diabetic patients**. Motiv: meta-analiza recenta 2025, peer-reviewed open access.
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC3925541 — **PMC: ACE-I/ARB Therapy prior to Contrast Exposure: What Should the Clinician Do?**. Motiv: review clinical relevant.
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC5986837 — **PMC: Post-contrast acute kidney injury Part 2 (ESUR recommendations)**. Motiv: documentul de referinta pentru PC-AKI prevention.
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11229940 — **PMC: Comprehensive overview of CIN prevention 2024**. Motiv: review actual.
  - https://www.jacc.org/doi/10.1016/j.jcin.2023.03.025 — **JACC Cardiovascular Interventions 2023: Simplified Rapid Hydration**. Motiv: studiu randomizat.
  - https://pubmed.ncbi.nlm.nih.gov/22322819/ — **PubMed: ACE inhibitor or ARB use as risk factor for CIN**. Motiv: cross-check evidenta.
- **Surse respinse:**
  - https://www.contrast-connect.com/blog-post/acr-manual-on-contrast-media-2025-guidelines-explained — blog comercial / agregator, nu sursa primara.
  - https://www.scribd.com/... — agregator de PDF-uri.
  - https://emedicine.medscape.com/article/246751-treatment — bibliografie tertiara, doar pentru cross-check informational, nu sursa citabila.
  - https://www.fellahealth.com/... — site comercial.
  - https://www.stroke-manual.com/... — manual specializat stroke, nu pertinent CT general.
- **Concluzii integrate in document:**
  - **Descoperire principala:** ACR 2024 + ESUR 2025 nu mai cer oprirea metforminului la pacient cu eGFR ≥30 si fara AKI. Pacientul are eGFR ~95 (CKD G1, calculat din creatinina 0.83 mg/dL la varsta 66 ani). Conform ghidurilor actuale → oprirea NU ar fi necesara. Documentat in raport ca DISCREPANTA intre RCP Janumet (cere 48h pauza) si ghidurile internationale 2024-2025. Decizia medicului curant (oprire conservatoare) este RESPECTATA si JUSTIFICATA prin combinatia particulara cu Triplixam (indapamida = diuretic care potenteaza nefrotoxicitatea contrastului).
  - **IECA si diuretic pre-CT:** dovezi MIXTE — practica curenta este continuare cu hidratare adecvata. Decizia individuala apartine radiologului. Documentat in raport ca [INCERT] cu intrebare explicita pentru radiolog (Sectiunea V).
  - **PC-AKI prevention 2024:** singura profilaxie dovedita = hidratare. Pacientii cu eGFR ≥30 NU necesita hidratare IV obligatorie. Hidratarea orala (1.5-2 L apa plata) este la fel de eficienta ca cea IV pentru pacientii cu functie renala buna. Pentru pacientul Petrila → hidratarea orala duminica 19.04 este suficienta.
- **Concluzie integrata in:** `Cercetare/2026-04-18_RAPORT_UNIFICAT_Jamesi_Triplixam_pentru_CT.docx` (Partea I.1 Metformin, Partea II.4 Indapamida, Partea III.3 PC-AKI, Partea IV Hidratare).
- **Marcaje certitudine folosite:** [CERT] dominant pentru recomandarile ghidurilor; [INCERT] pentru deciziile individuale (oprire/continuare Triplixam ziua CT, prag exact creatinina reluare metformin).
- **Data publicării materialelor sursă:**
  - ACR Manual: iulie 2024
  - ESUR Guidelines: v10.0 + decembrie 2025
  - Frontiers meta-analiza: 2025
  - PMC reviews: 2014-2024
  - JACC: 2023
- **Încredere concluzie:** high (surse primare ghiduri oficiale + cross-check meta-analize peer-reviewed).
- **Observații:**
  - Niciuna din cele 4 rapoarte AI sursa (Claude, Gemini, ChatGPT, Grok) NU mentiona ACR 2024 sau ESUR 2025. Toate citau SmPC Janumet (varianta clasica cu 48h). Aceasta cercetare web suplimentara a adus o informatie cu impact clinic real (modernizarea ghidurilor face oprirea de 48h o decizie conservatoare, nu o cerinta absoluta).
  - Pacientul are functie renala excelenta (eGFR 95 = CKD G1). Asta inseamna risc PC-AKI MIC. Documentat in raport ca RISC MIC, fara minimizare a precautiei pre-CT (hidratare ramane obligatorie).
  - SmPC-ul Janumet ramane sursa primara pentru pacient — daca prospectul cere 48h, asta urmeaza. Ghidurile internationale sunt informative, nu prescriptive direct catre pacient.

---

## 2026-04-18 03:11-03:28 — reactii-adverse-jamesi-triplixam

- **Scop:** culegere date din RCP/SmPC oficial pentru generarea raportului `2026-04-18_raport_reactii_adverse_jamesi_triplixam.docx`.
- **Instrumente folosite:** `WebSearch`, `WebFetch`, `Read` (PDF cu OCR integrat — pages 1-25).
- **Queries exacte:**
  1. `"Janumet 50/1000 sitagliptin metformin RCP reactii adverse ANMDMR"` — WebSearch
  2. `"Triplixam 10/2.5/5 perindopril indapamida amlodipina RCP reactii adverse ANMDMR"` — WebSearch
  3. `"Triplixam 10/2.5/5 SmPC Servier European Medicines Agency adverse reactions"` — WebSearch
- **Surse acceptate (CERT, sursă primară):**
  - https://www.medicines.org.uk/emc/product/564/smpc — **RCP Janumet 50/1000 — Electronic Medicines Compendium UK**. Motiv: SmPC oficial aliniat la EMA. Data publicării: actualizat 2024 (versiune curentă la 18.04.2026).
  - https://myservier-me.com/wp-content/uploads/2022/09/SmPC_Triplixam_Version-06.2021-Bhn.pdf — **SmPC Triplixam (4 dozaje, inclusiv 10/2.5/5) — Servier**. Motiv: document oficial producător, acoperă toate 4 dozajele. Data versiunii: 06.2021. Limitare: vechi ~5 ani — recomandată verificare versiune curentă ANMDMR.
  - https://rwandafda.gov.rw/wp-content/uploads/2023/07/Triplixam-5mg-1.25mg-5mg-film-coated-tablets_-Perindopril-arginine-5-mg-Indapamide-1.25mg-and-Amlodipine-besilate-5mg-SmPC.pdf — **SmPC Triplixam (Rwanda FDA)**. Motiv: copie oficială a SmPC-ului Servier, descărcabilă și parseabilă; confirmă conținutul versiunii 06.2021. Data: 2023.
- **Surse acceptate (CERT, sursă secundară / confirmare):**
  - https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/022044s042lbl.pdf — FDA label Janumet 2017. Motiv: cross-check SmPC EMA cu FDA.
  - https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d19c7ed0-ad5c-426e-b2df-722508f97d67 — DailyMed Janumet. Motiv: sursă primară NIH.
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC8964631/ — „Perindopril/Indapamide/Amlodipine in Hypertension: A Profile of Its Use" (PMC peer-reviewed review).
  - https://comenzi.farmaciatei.ro/medicamente-cu-reteta/medicamente/triplixam-10mg2-5mg5mg-30-comprimate-filmate-les-laboratoires-servier-p345501 — Farmacia Tei, pagina comercială Triplixam 10/2.5/5 în RO. Motiv: confirmă disponibilitatea în piața RO și trimitere către ANMDMR pentru raportare reacții adverse.
- **Surse respinse:**
  - Reference Medscape (medscape.com/drug/janumet) — nu sursă primară, bibliografie terțiară; folosit doar pentru cross-check informațional, nu ca sursă citabilă.
  - RxList (rxlist.com) — comercial / agregator.
  - Drugs.com — agregator, folosit exclusiv pentru confirmare secundară.
  - Janumetxr.com — site promoțional producător, nu SmPC oficial.
  - PharmEasy (pharmeasy.in) — site comercial India, fără valoare pentru RO.
  - MIMS Philippines/Malaysia — 403 error la fetch (nu s-a folosit).
  - Dr.Max.ro — 403 error la fetch.
- **Concluzie integrată în:** `Dosar_Medical/rapoarte_generate/2026-04-18_raport_reactii_adverse_jamesi_triplixam.docx` (raport pentru familie, Regula 17 aplicată integral).
- **Marcaje certitudine folosite în document:** [CERT] = 75%+, [PROBABIL] = 10%, [INCERT] = 10%, [NEGASIT] = 5%. Secțiunea V a documentului enumeră explicit ce nu s-a găsit.
- **Data publicării materialelor sursă:**
  - Janumet SmPC EMC: actualizat 2024
  - Triplixam SmPC Servier: 06.2021 (semnalată vechimea > 12 luni — verificare versiune curentă recomandată)
  - PMC review: 2022
- **Încredere concluzie:** high (surse primare SmPC + cross-check FDA + peer-reviewed review).
- **Observații:**
  - RCP ANMDMR românesc nu a fost găsit direct online (anm.ro nu a apărut în rezultate); conținutul este echivalent cu SmPC-ul Servier internațional (RO face parte din EMA).
  - SmPC-ul Servier pentru Triplixam acoperă toate 4 dozajele (5/1.25/5, 5/1.25/10, 10/2.5/5, 10/2.5/10) — pacientul primește 10/2.5/5. Profilul de reacții adverse e identic calitativ; doar incidența poate varia ușor cu doza.

---

**Ultima revizuire:** 2026-04-18.
