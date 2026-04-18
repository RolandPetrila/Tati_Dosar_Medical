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
