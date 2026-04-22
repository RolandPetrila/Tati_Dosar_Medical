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

## 2026-04-23 02:05-02:13 — verificare-roluri-interne-OncoHelp-Dr-Sirbu-Dr-Oprean

- **Scop:** verificare independentă pe surse primare/reputabile a rolurilor interne la OncoHelp Timișoara pentru Dr. Sîrbu Daniela (Șef Spitalizare Continuă) și Dr. Oprean Cristina (Șef Spitalizare de Zi) — afirmații marcate `[INCERT]` în `SINTEZA_CLINICI_ONCOLOGIE.md` §4.5 preluate neverificate din sinteza anterioară Gemini (ștearsă). Aplicare Regula 22 nouă (verificare proactivă + decizie explicită păstrez/șterg).
- **Instrumente folosite:** WebFetch × 2, WebSearch × 2.
- **Queries exacte:**
  1. WebFetch `https://oncohelp.ro/echipa-oncohelp/dr-sirbu-daniela-medic-primar-oncolog/` — pagină individuală Dr. Sîrbu (404)
  2. WebFetch `https://oncohelp.ro/echipa-oncohelp/dr-oprean-cristina-medic-primar-oncolog/` — pagină individuală Dr. Oprean (404)
  3. WebSearch `""Daniela Sirbu" OR "Sirbu Daniela" OncoHelp Timisoara "sef sectie" OR "spitalizare continua" coordonator"` — rezultat pozitiv
  4. WebSearch `""Cristina Oprean" OR "Oprean Cristina" OncoHelp Timisoara "farmacologie clinica" OR "spitalizare de zi" sef"` — rezultat pozitiv
- **Surse acceptate (primare/reputabile):**
  - https://timpolis.ro/la-oncohelp-timisoara-functioneaza-cea-mai-mare-sectie-de-paliatie-dintr-un-spital-din-vestul-tarii/ — confirmă Dr. Sîrbu Șef Spitalizare Continuă în Secția Oncologie OncoHelp
  - https://oncohelp.ro/echipa-oncohelp/ — roster oficial cu ambii medici listați
  - https://oncohelp.ro/echipa-oncohelp/dr-cristina-oprean-medic-primar-oncolog-1/ — pagină oficială Dr. Oprean (nume URL diferit de încercarea inițială)
  - https://medical-virtual.ro/speaker/dr-cristina-oprean/ — profil profesional Dr. Oprean (dublă specializare farmacologie clinică + detalii carieră)
  - https://www.medichub.ro/stiri/premiera-la-timisoara-pacientii-cu-cancer-pot-participa-la-studii-clinice-de-faza-1-in-cadrul-centrului-oncohelp-id-9227-cmsid-2 — confirmare OncoHelp primul centru Timișoara cu studii fază 1 (descoperire colaterală)
  - https://renasterea.ro/premiera-intr-un-spital-din-timisoara/ — confirmare secundară studii fază 1 OncoHelp
  - https://oncohelp.ro/asociatia-oncohelp/membri/ — confirmă Dr. Sîrbu vice-președinte Asociație + Dr. Oprean membru fondator
- **Surse respinse:**
  - Forumuri și recenzii pacienți (doctorbun.ro, ghidulmedical.com) — non-primare, doar orientativ
  - Wikipedia — necăutat (regulă Regula 22)
- **Concluzie integrată în:** `Dosar_Medical/cercetari/SINTEZA_CLINICI_ONCOLOGIE.md` §4.5 (upgrade marcaje `[INCERT]` → `[CERT]` + info nouă) + §11.1 (surse noi) + §12.1 (scoase puncte rezolvate)
- **Marcaje certitudine folosite:** `[CERT]` cu surse primare + secundare reputabile
- **Data verificării surselor:** 23.04.2026 02:05-02:13
- **Încredere concluzie:** high (rol Dr. Sîrbu confirmat pe timpolis.ro + roster oficial; rol Dr. Oprean confirmat pe medical-virtual.ro + medichub.ro + pagină profil oncohelp.ro)
- **Observații:**
  - Încercarea inițială de a accesa pagini individuale la `oncohelp.ro/echipa-oncohelp/dr-*-medic-primar-oncolog/` a dat 404 pentru ambele — URL-urile efective pe site nu respectă acest pattern. Dr. Oprean are URL propriu (`dr-cristina-oprean-medic-primar-oncolog-1/`), Dr. Sîrbu nu pare să aibă pagină individuală pe site
  - Descoperire colaterală importantă: OncoHelp primul centru din Timișoara cu studii clinice fază 1. Relevant pentru pacient ca opțiune de rezervă pentru cancer eso-gastric dacă FLOT nu funcționează sau dacă există trial aplicabil
  - Principiul Regula 22 aplicat: 2 afirmații `[INCERT]` → ambele confirmate → upgrade la `[CERT]` + surse. Dacă nu s-ar fi confirmat, ambele ar fi fost șterse

---

## 2026-04-23 01:10-01:40 — audit-clinici-oncologie-multi-regiune

- **Scop:** audit + reverificare din surse primare oficiale a clinicilor oncologice pentru tratamentul pacientului Petrilă Viorel-Mihai (suspiciune adenocarcinom eso-gastric Siewert II). Rezultat integrat în `Dosar_Medical/cercetari/SINTEZA_CLINICI_ONCOLOGIE.md`.
- **Instrumente folosite:** WebSearch × 7, WebFetch × 3.
- **Queries exacte:**
  1. `"OncoHelp Timisoara Centru Oncologie adresa contact 2026"` — WebSearch
  2. `""Serban Negru" OncoHelp Timisoara medic oncolog presedinte"` — WebSearch
  3. `""Dorel Popovici" OncoHelp Timisoara medic oncolog UMF"` — WebSearch
  4. `"Amethyst Radiotherapy Timisoara adresa contact oncologi medici 2026"` — WebSearch
  5. `"Amethyst Radiotherapy Cluj-Napoca medici oncologi "Carmen Bodale" OR "Kacso" contact"` — WebSearch
  6. `"Institutul Oncologic Cluj "Prof Dr Ion Chiricuta" IOCN oncologi digestivi cancer gastric esofagian CNAS 2026"` — WebSearch
  7. `"oncologie medicala Oradea clinici private CNAS "program national oncologie" cancer digestiv"` — WebSearch
  8. `"clinici private oncologie Cluj Timisoara CNAS decontare cancer esofagian adenocarcinom FLOT tratament gratuit"` — WebSearch
  9. `"IOCN Cluj Chiricuta programare pacient nou trimitere procedura adresa telefon contact"` — WebSearch
  10. `"Medisprof Cluj oncologie "program national" CNAS medici specialisti cancer digestiv contact"` — WebSearch
  11. `"chirurgie oncologica digestiva Cluj Timisoara Oradea esofagectomie gastrectomie Siewert medici renumit 2026"` — WebSearch
  12. `https://oncohelp.ro/echipa-oncohelp/` — WebFetch (prompt: echipa completă + specialități)
  13. `https://oncohelp.ro/centrul-de-oncologie/oncologie/` — WebFetch (prompt: servicii + CNAS + markeri moleculari)
  14. `https://amethyst-radiotherapy.ro/en/amethyst-centre-timisoara/` — WebFetch (prompt: contact + echipă + servicii + lipsuri)
  15. `https://amethyst-radiotherapy.ro/en/amethyst-cluj-radiotherapy-centre/` — WebFetch (prompt: contact + echipă + servicii + lipsuri)
- **Surse acceptate (primare, oficiale):**
  - https://oncohelp.ro/contact/ — OncoHelp contact oficial (adresă, telefoane, orar)
  - https://oncohelp.ro/echipa-oncohelp/ — roster complet medici OncoHelp
  - https://oncohelp.ro/centrul-de-oncologie/oncologie/ — servicii OncoHelp + contract CNAS
  - https://iocn.ro/ + https://ms.ro/ro/unitati-sanitare/institutul-oncologic-prof-dr-ion-chiricuta-cluj-napoca/ — IOCN Cluj oficial + MS
  - https://iocn.ro/sectia_chirurgie_oncologica_i/ + https://iocn.ro/sectia-oncologie-medicala/ — secții IOCN relevante
  - https://www.uicc.org/membership/institutul-oncologic-prof-dr-ion-chiricuta-cluj-napoca-iocn — acreditare UICC
  - https://iroca.eu/center/the-oncology-institute-prof-dr-ion-chiricuta-cluj-napoca-iocn/ — acreditare OECI
  - https://www.medicover.ro/spital-cluj/oncologie-medicala/ + https://www.medicover.ro/spital-cluj/chirurgia-oncologica/ + https://programare.medicover.ro/centrul-de-excelenta-chirurgie-robotica-onco-digestiva — Medicover Cluj Chirurgie Robotică
  - https://medisprof.ro/ + https://medisprof.ro/servicii/servicii-decontate-cas/ + https://oncopedia.ro/medisprof-cancer-center-cluj-accesibil-asiguratilor-cnas/ — Medisprof
  - https://www.medeuropa.ro/medeuropa-oradea + https://www.medeuropa.ro/oncologie-medicala — MedEuropa Oradea
  - https://amethyst-radiotherapy.ro/en/amethyst-centre-timisoara/ + https://amethyst-radiotherapy.ro/en/amethyst-cluj-radiotherapy-centre/ — Amethyst TM + CJ
  - https://amethyst-radiotherapy.ro/dr-carmen-bodale-medic-specialist-oncologie-medicala-amethyst/ — profil Dr. Carmen Bodale
  - https://buletindetimisoara.ro/in-cadrul-oncohelp-timisoara-functioneaza-tumor-board-comisia-oncologica-multidisciplinara-care-creste-sansele-de-supravietuire-ale-bolnavilor-de-cancer/ — confirmare Tumor Board zilnic OncoHelp
  - https://spatiulmedical.ro/doctor-serban-negru-presedinte-centru-oncologie-oncohelp-timisoara-program-de-screening/ — profil Șerban Negru
  - https://www.caspa.ro/oncohelp-timisoara-10-000-de-pacienti-ingrijiti-gratuit-anul-trecut-aici-aproape-o-jumatate-cazuri-noi/ — statistici OncoHelp
  - http://www.casan.ro/page/programul-national-de-oncologie.html + http://cas.cnas.ro/cjastm/page/program-national-de-oncologie.html — CNAS oficial
- **Surse respinse:**
  - Wikipedia (sursă terțiară, nu primară) — neutilizat
  - Google reviews / doctorbun.ro / agregatori comerciali — doar citire orientativă, nu citat
  - medscape / rxlist — nu relevante pentru clinici RO
- **Concluzie introdusă în:** `Dosar_Medical/cercetari/SINTEZA_CLINICI_ONCOLOGIE.md` (integrare completă)
- **Marcaje certitudine folosite în document:** `[CERT]` = 70%+, `[PROBABIL]` = 20%, `[INCERT]` = 8%, `[NEGASIT]` = 2% (pentru elemente de contact / costuri / pozițiii interne neclare pe site-uri oficiale)
- **Data verificării surselor:** 23.04.2026 (toate URL-urile consultate în intervalul 01:10-01:40)
- **Încredere concluzie:** high pentru date de contact + echipă + servicii listate oficial; medium pentru roluri interne neconfirmate pe site (Dr. Sîrbu „Șef Spitalizare Continuă" / Dr. Oprean „Șef Spitalizare de Zi") — marcate `[INCERT]` în document; low pentru afirmații reputaționale (timp așteptare Prof. Negru) — marcate `[INCERT]` în document.
- **Observații:**
  - Sinteza anterioară produsă de Gemini (`SINTEZA_ONCOHELP_TIMISOARA.md`) conținea 8 nereguli documentabile (inclusiv afirmații potențial defăimătoare fără sursă). Listate în `CHANGELOG.md` intrarea 2026-04-23 01:45.
  - Identificate 2 clinici complet omise de Gemini: Medicover Cluj (Centru Excelență Chirurgie Robotică Onco-Digestivă) + Medisprof Cluj (privat CNAS).
  - Contact OncoHelp suplimentar identificat: `0752 01 05 08` (programări pacienți noi, recomandat pe site) + email `programari@oncohelp.ro` + orar L-V 08:00-16:00.

---

## 2026-04-18 09:50 — RETRAGERE intrare 09:25-09:30

Intrarea anterioara (cercetare web pe ghiduri ACR 2024 / ESUR 2025) a fost RETRASA la cererea user-ului dupa ce a sters folderul `Cercetare/` (rapoartele AI care au alimentat acea cercetare au halucinat). Cercetarea respectiva nu mai are output activ in proiect — documentul unificat care o folosea a fost si el sters.

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
