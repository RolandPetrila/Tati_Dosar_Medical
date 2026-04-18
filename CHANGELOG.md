# CHANGELOG.md — Istoricul modificărilor

**Jurnal cronologic al tuturor modificărilor din dosar. Intrările cele mai recente sunt sus.**

---

## 2026-04-18 14:01 — Generare DASHBOARD.html + Regula 18 (sincronizare dashboard)

**Tip:** CREARE (DASHBOARD.html) + MODIFICARE REGULAMENT (CLAUDE.md — Regula 18)

**Fișiere afectate:**

- `DASHBOARD.html` — **NOU** — vizualizare HTML single-page a dosarului medical (identitate pacient, status clinic, medicație, alergii, analize, timeline antecedente, echipă medicală, factori risc, calendar CT, acțiuni deschise P0/P1/P2, întrebări consulturi). CSS inline, offline-first, countdown live JavaScript la CT 20.04.2026, responsive + print-friendly.
- `CLAUDE.md` — **Regula 18 adăugată** (sincronizare DASHBOARD.html la actualizări medicale relevante); antet actualizat la v5; changelog intern actualizat.
- `Dosar_Medical/arhiva/versiuni_config/CLAUDE_pre-regula-18-dashboard_2026-04-18_1401.md` — backup CLAUDE.md pre-modificare (Regula 10).

**Descriere:**

- User a solicitat un dashboard HTML pentru vizualizare rapidă a dosarului (decizie finală variantă A din propunere) + regulă explicită de sincronizare
- Regula 18 definește declanșatorii obligatorii de regenerare (analize noi, medicație modificată, alergii, investigații, antecedente, documente sursă procesate, modificări P0 TODO, schimbare simptomatologie) și excepțiile (typo-uri, log-uri proces, meta-uri, P1/P2/P3)
- Timing: o singură regenerare per sesiune, înainte de commit-ul final (integrat cu Regula 16)
- Dashboardul respectă regulile de conținut (Regula 11 vechime analize + Regula 17 marcaj certitudine)
- CSS: palette medical profesional (albastru + verde OK + galben atenție + roșu critic), fără dependențe externe, UTF-8

**Sursă informație:** `CONTEXT_MEDICAL.md` (v1.1 post-reconciliere), `TODO.md`, JSON-urile canonice din `Dosar_Medical/` (schemă v2.0).

**Făcut de:** Claude Code (Opus 4.7, 1M context).

---

## 2026-04-18 13:28 — Confirmare pregătire CT 20.04: alergii + STOP Jamesi + hidratare

**Tip:** MODIFICARE (actualizare status pregătire CT)

**Fișiere afectate:**

- `CONTEXT_MEDICAL.md` — secțiunea 8 (pregătire critică) actualizată cu status executat; secțiunea 11 (alergii) populată — fără alergii la iod / fructe de mare / contrast anterior
- `TODO.md` — Calendar + P0 pregătire pacient: 3 sub-task-uri marcate finalizate (STOP Jamesi, confirmare alergii, plan hidratare)
- `Dosar_Medical/2025-11-01_talon_pensie_asigurare.zip` — ȘTERS (backup redundant; JSON-urile canonice sunt în dosar, istoricul în git)

**Descriere:**

- Familia a confirmat: pacientul NU are alergii la iod, fructe de mare sau contrast iodat anterior → cale liberă pentru CT cu substanță de contrast
- Jamesi oprit conform protocolului H-48 pre-CT (18.04.2026), reluare programată 22.04.2026 după verificarea creatininei post-CT
- Plan hidratare duminică 19.04 confirmat (1.5-2 L apă plată)

**Sursă informație:** declarație familie — Roland Petrilă (fiu), 18.04.2026 13:28 (conversație chat).

**Marcaj certitudine (Regula 17):** informații [CERT] pentru status acțiune (confirmat de responsabilul dosar) cu sursă declarație familie citată; NU document medical — rămâne valabil să se confirme verbal la radiolog înainte de injectare contrast.

**Făcut de:** Claude Code (Opus 4.7, 1M context).

---

## 2026-04-18 09:50 — REVERT: stergere folder Cercetare/ + retragere intrari log

**Tip:** STERGERE FISIERE + REVERT INTRARI LOG (la cererea explicita a user-ului)

**Fișiere afectate:**

- `Cercetare/` (folder) — STERS de user; commit reflectat: 5 fisiere D (4 rapoarte AI sursa + raportul unificat generat la 09:37)
- `CHANGELOG.md`, `SESSION_LOG.md`, `WEB_QUERIES.md` — sterse intrarile asociate sesiunii 09:20-09:37

**Declanșator:** user — `am sters folderul cu acele cercetari. am observat ca ai-urile au halucinat si au adaugat detalii pe care eu nu le-am mentionat. sterge din documentatie, ultimele actualizari pe care le-ai adaugat referitor la acele cercetari.`

**Motiv:** cele 4 rapoarte AI din `Cercetare/` (Claude/Gemini/ChatGPT/Grok) au inclus detalii halucinate / neverificate. Documentul unificat generat la 09:37 s-a bazat partial pe acele surse. User a decis sa renunte complet la materialul respectiv.

**NU s-a sters:** raportul `Dosar_Medical/rapoarte_generate/2026-04-18_raport_reactii_adverse_jamesi_triplixam.docx` (sesiunea 03:11-03:31) — acela e generat direct din surse primare RCP/SmPC, NU se baza pe cele 4 rapoarte AI halucinate. Daca user va cere si stergerea acelui raport — operatie separata.

**Făcut de:** Claude Code (Opus 4.7, 1M context).

---

## 2026-04-18 03:31 — Raport reacții adverse Jamesi + Triplixam + Regula 17 (marcaj certitudine info medicală)

**Tip:** ADAUGARE DOCUMENT NOU + MODIFICARE REGULAMENT

**Fișiere afectate:**

- `CLAUDE.md` — adăugată **Regula 17** (marcaj certitudine [CERT]/[PROBABIL]/[INCERT]/[NEGASIT] obligatoriu pentru outputul medical) + changelog intern `v4`
- `WEB_QUERIES.md` — prima intrare reală: cercetare reacții adverse (Regula 15 aplicată integral)
- `Dosar_Medical/rapoarte_generate/generate_reactii_adverse_docx.py` (nou) — generator Python-docx, ~700 linii
- `Dosar_Medical/rapoarte_generate/2026-04-18_raport_reactii_adverse_jamesi_triplixam.docx` (nou) — raport final 47 KB, ~30 pagini
- `Dosar_Medical/arhiva/versiuni_config/CLAUDE_pre-regula17_2026-04-18_0328.md` (nou) — backup Regula 10
- `SESSION_LOG.md` + `CHANGELOG.md`

**Declanșator:** utilizator a cerut raport detaliat despre reacțiile adverse la Jamesi și Triplixam, livrat în `.docx`, pentru un cititor fără pregătire medicală, cu exemple clare. A cerut explicit să fie marcate informațiile nesigure și să fie adăugată o regulă dedicată în regulament pentru acest aspect.

**Operații aplicate:**

1. **Cercetare web** (Regula 15) — 3 WebSearch + 3 WebFetch + citire PDF SmPC cu 25 pagini. Surse primare: SmPC Janumet 50/1000 (Electronic Medicines Compendium UK, 2024), SmPC Triplixam (Servier, versiunea 06.2021, plus copia Rwanda FDA 2023). Surse secundare de cross-check: FDA label Janumet 2017, DailyMed, PMC peer-reviewed review pe perindopril/indapamidă/amlodipină.
2. **Observație clinică identificată:** interacțiune gliptin + IECA → risc angioedem crescut. Documentată explicit în RCP Triplixam secțiunea 4.5. Evidențiată la Partea III.A a raportului ca punct critic de urmărit de familie — fără recomandare de oprire (nu e contraindicație).
3. **Generare `.docx`** — script Python autoexecutabil (`generate_reactii_adverse_docx.py`) folosind `python-docx 1.1.2`. Rulare reușită → 47 KB, ~30 pagini. Structură: copertă, rezumat 5 puncte, Partea I (Jamesi detaliat), Partea II (Triplixam detaliat), Partea III (interacțiuni specifice pacientului), Partea IV (checklist familie + când sună 112), Partea V (transparență: ce nu s-a găsit), Partea VI (surse citate cu URL + data accesării).
4. **Regula 17 adăugată în `CLAUDE.md`:**
   - 4 marcaje obligatorii ([CERT], [PROBABIL], [INCERT], [NEGASIT]) cu definiții precise
   - 10 reguli operaționale (cifre obligatoriu [CERT] + sursă, secțiune „Ce NU am găsit", limită temporală > 12 luni, atenționare „nu înlocuiește consult medical", etc.)
   - Exemple corect/greșit concrete
   - Operaționalizează R3 din regulamentul global („nu inventezi nimic") specific pentru outputul medical
5. **Backup pre-modificare** `CLAUDE.md` (Regula 10).
6. **Logare în `WEB_QUERIES.md`** (Regula 15 — prima utilizare reală de la creare).

**Marcaje certitudine în raport:**

- [CERT]: ~75% din afirmații (citate direct din SmPC)
- [PROBABIL]: ~10% "farmacologie standard nemensionată în SmPC"
- [INCERT]: ~10% "ex: riscul cardiovascular al sitagliptin vs. saxagliptin — date mixte între TECOS și SAVOR-TIMI"
- [NEGASIT]: ~5% "ex: rata numerică exactă a angioedemului la combinația sitagliptin + perindopril — semnalat ca întrebare pentru medicul curant"

**Motiv generare documentului:** pacient + familie au nevoie de informații medicale înainte de CT luni 20.04 și înainte de eventual tratament post-biopsie; raportul îi ajută să recunoască simptomele care necesită intervenție (inclusiv urgențe 112) și reduce confuzia când medicul menționează termeni tehnici.

**Atenționări incluse în raport:** secțiunea finală explicit „NU înlocuiește consultul medical"; fiecare pagină relevantă are callout colorat cu avertizare.

**Sursă informație:** utilizator a cerut cercetarea; conținutul factual vine exclusiv din surse primare autoritare (SmPC Janumet + SmPC Triplixam + FDA + DailyMed + PMC).

**Făcut de:** Claude Code (Opus 4.7, 1M context).

---

## 2026-04-18 03:10 — Clarificări Regula 16 sub-clauza 7 + logare retroactivă commit 478048f

**Tip:** CORECTIE + MODIFICARE

**Fișiere afectate:** `CLAUDE.md`, `SESSION_LOG.md`, `CHANGELOG.md` (acest fișier).

**Declanșator:** utilizator a rulat audit paralel (`info_tati.txt`) care a găsit două probleme:

1. Commit-ul `478048f` (02:54:47, „Extinde Regula 16 cu sub-clauza 7…") nu era logat în SESSION_LOG.md / CHANGELOG.md — violare directă Regula 16 pct. 3 („actualizare obligatorie înainte de commit").
2. Sub-clauza 7 avea 4 ambiguități minore: (a) neclaritate pe ce alte fișiere narative intră în scope, (b) typo „intermediar", (c) frecvența rulării `date` neprecizată, (d) format timestamp per fișier nespecificat.

**Operații aplicate (în ordine):**

1. **Backup pre-modificare** `CLAUDE.md` → `Dosar_Medical/arhiva/versiuni_config/CLAUDE_pre-clarificare-subclauza7_2026-04-18_0310.md` (Regula 10).
2. **Modificare `CLAUDE.md`** — sub-clauza 7 extinsă cu toate 4 clarificările:
   - Adăugat `_metadata.data_procesare` din JSON-urile `Dosar_Medical/` la lista fișierelor care necesită `date` înainte de scriere
   - Fix typo: „ore intermediar" → „ore intermediare"
   - Specificată frecvența: refresh per bloc de modificări >15 min (o rulare inițială insuficientă la sesiuni lungi)
   - Tabel format per fișier: `SESSION_LOG.md` + `CHANGELOG.md` trunchiat la `YYYY-MM-DD HH:MM` fără timezone (timezone implicit = ora locală România); `CONTEXT_MEDICAL.md` text narativ; JSON-uri `_metadata.data_procesare` format ISO 8601 complet cu `+03:00`
   - Notă în antet: „clarificări 2026-04-18 03:10"
3. **Changelog intern `CLAUDE.md`** — intrare nouă `v3.1` cu rezumatul clarificărilor.
4. **Logare retroactivă `SESSION_LOG.md`** — adăugată intrare pentru commit `478048f` la timestamp-ul real git `2026-04-18 02:53-02:54`, cu marcajul `[RETROACTIV — logat 03:10]`.
5. **Logare sesiune curentă** — această intrare + intrare corespunzătoare în `SESSION_LOG.md`.

**Verificare cronologie (git vs log):**

| Intrare                            | Git timestamp    | SESSION_LOG status      |
| ---------------------------------- | ---------------- | ----------------------- |
| Audit + migrare v2                 | 02:23:36         | ✅ logat                |
| Git init + Regula 16               | 02:35:12         | ✅ logat                |
| CT 20.04                           | 02:43:31         | ✅ logat                |
| Bioclinica                         | 02:50:01         | ✅ logat                |
| ERATĂ timestamp                    | 02:52:53         | ✅ logat                |
| Sub-clauza 7 (commit `478048f`)    | 02:54:47         | ✅ **logat retroactiv** |
| Remediere audit (sesiunea curentă) | ~03:15 (estimat) | ✅ logat                |

**Consecință operațională:** toate commit-urile din 2026-04-18 au acum corespondent în SESSION_LOG.md și CHANGELOG.md. Regula 16 pct. 3 e satisfăcută.

**Fără modificări la date medicale.** Regulile procedurale clarificate nu schimbă starea dosarului. Pregătirea pacientului pentru CT (sâmbătă 17:00 STOP Jamesi → luni 17:00 CT) rămâne neafectată.

**Sursă:** audit extern user (`info_tati.txt`), 2026-04-18 ~03:00.

**Făcut de:** Claude Code (Opus 4.7, 1M context).

---

## 2026-04-18 02:54 — [RETROACTIV] Extindere Regula 16 cu sub-clauza 7 (timestamp narativ)

> **[LOGAT RETROACTIV 2026-04-18 03:10]** — intrare absentă la momentul commit-ului; adăugată ulterior în urma auditului user care a comparat `git log --format=%ai` cu jurnalele narative. Commit-ul real `478048f` confirmat la timestamp-ul `2026-04-18 02:54:47 +0300`.

**Tip:** MODIFICARE (regulament)

**Fișiere afectate:** `CLAUDE.md` (+16 linii, -0).

**Context:** la 02:51 aceeași sesiune, Claude corectase timestamp-uri halucinate din SESSION_LOG/CHANGELOG (ERATĂ). Imediat după, a adăugat o sub-clauză preventivă la Regula 16 pentru a forța rularea `date` în Bash înainte de scrierea oricărui timestamp narativ, ca să nu se mai repete incidentul.

**Descriere modificare:**

- Adăugat punctul 7 la „Protocol obligatoriu" al Regula 16 — bloc de ~16 linii cu: comandă exactă (`date +"%Y-%m-%d %H:%M:%S %z"`), lista fișierelor afectate (SESSION_LOG, CHANGELOG, CONTEXT_MEDICAL), excepție pentru commit-urile git (au timestamp automat), cross-check (dacă user menționează ora, verifică cu `date`), protocol corectare la discrepanță.

**Motiv:** prevenire repetare halucinație timestamp. Sistemul dă data în context (`Today's date is…`), dar nu ora; modelul are tendință să inventeze ore „plauzibile".

**Commit:** `478048f` (push direct pe `origin/main`).

**Observație:** această intrare a lipsit inițial din CHANGELOG + SESSION_LOG, ceea ce a constituit însuși o încălcare a Regula 16 pct. 3 (ironie). Remediat 2026-04-18 03:10 — vezi intrarea de mai sus.

**Făcut de:** Claude Code (Opus 4.7, 1M context).

---

## 2026-04-18 02:51 — [ERATĂ] Corectură timestamp halucinate în sesiunea anterioară

**Tip:** CORECTIE

**Fișiere afectate:** `SESSION_LOG.md`, `CHANGELOG.md`.

**Problema identificată de utilizator (sesiune `/onboard` paralelă):**

În sesiunea Claude_Opus_4.7 anterioară (aceeași zi, 18.04.2026), au fost scrise timestamp-uri INVENTATE:

- `SESSION_LOG.md`: „2026-04-18 15:00", „17:30", „~18:00", „~18:30"
- `CHANGELOG.md`: „sesiunea a durat de la ~15:00 la ~17:00"

**Realitatea (confirmată prin `git log --format=%ai`):**

| Etapă sesiune                             | Timestamp real (git) | Ce scrisese Claude (halucinat) |
| ----------------------------------------- | -------------------- | ------------------------------ |
| Audit + migrare v2 (prim commit)          | **02:23:36**         | `15:00`                        |
| Regula 16 (al doilea commit)              | **02:35:12**         | `17:30`                        |
| Confirmare CT 20.04 (al treilea commit)   | **02:43:31**         | `~18:00`                       |
| Integrare Bioclinica (al patrulea commit) | **02:50:01**         | `~18:30`                       |

**Cauza [PROBABIL]:** Claude-ul sesiunii anterioare nu avea ora curentă în system context (doar data — `Today's date is 2026-04-18`), și a inventat ore „plauzibile" în loc să ruleze `date` și să verifice. Violare directă:

- R3 (reguli globale) — „Nu inventezi nimic"
- Regula 8 (proiect) — protecție anti-halucinație
- Regula 11 (proiect) — marcaj valabilitate clinică (trasabilitatea temporală e critică într-un dosar medical)

**Corecturi aplicate (2026-04-18 02:51):**

- Toate intrările `SESSION_LOG.md` aduse la timestamp-urile reale din git
- Notă `[TIMESTAMP CORECTAT]` inserată sub fiecare intrare afectată (audit trail)
- Fraza din `CHANGELOG.md` entry-ul audit inițial corectată cu referință la erată
- Backup pre-corectură în `Dosar_Medical/arhiva/versiuni_config/{SESSION_LOG,CHANGELOG}_pre-corectare-timestamp_2026-04-18_0251.md`

**Lecție operațională:** înainte de a scrie timestamp-uri în log-uri, rulez `date` (sau echivalent) pentru a avea ora sistemului, nu o presupun. Relevant pentru Regula 16 (git auto-commit) — commit message-urile vor avea timestamp-ul automat de git, dar log-urile narative (SESSION_LOG, CHANGELOG) trebuie să corespundă.

**Sursă corectare:** utilizator a rulat `/onboard` în terminal paralel, a observat discrepanța („acum e 02:40 noaptea, nu 18:00"), a forțat verificarea.

**Făcut de:** Claude Code (Opus 4.7) — corectură aplicată la cererea explicită a utilizatorului.

---

## 2026-04-18 (sesiune Claude_Opus_4.7, continuare 3) — Integrare buletin Bioclinica 17.04

**Tip:** ADAUGARE DOCUMENT NOU + ACTUALIZARE

**Fișiere afectate:**

- `Dosar_Medical/2026-04-17_buletin_bioclinica_uree_creatinina.json` (nou, schema v2.0)
- `Dosar_Medical/documente_sursa/05_analize_laborator/2026-04-17_buletin_bioclinica_uree_creatinina.jpeg` (nou — scan original)
- `Dosar_Medical/documente_sursa/05_analize_laborator/2026-04-17_buletin_bioclinica_uree_creatinina.jpeg.meta.json` (nou — chain of custody)
- `CONTEXT_MEDICAL.md` — tabel creatinină actualizat + notă despre localizarea biopsiei
- `TODO.md` — `[P0] Analize prealabile CT` marcat COMPLET
- `CHANGELOG.md` + `SESSION_LOG.md`

**Descriere:**

Integrat buletinul Bioclinica nr. 26417A0362 din 17.04.2026 (recoltat 14:21, emis 17:07, medic primar Dr. Statnic Maria Luminița). Conține uree (33.4 mg/dL, normal) + creatinină (0.83 mg/dL, normal; eGFR CKD-EPI ~95 → stadiu G1).

**Consecințe pentru CT 20.04.2026:**

- Funcție renală confirmată NORMALĂ cu valoare recentă (3 zile vechime)
- Nu se impune repetarea analizelor înainte de CT
- Protocol contrast standard — fără prehidratare IV sau ajustări
- Risc nefropatie post-contrast — scăzut

**Consecință suplimentară (observație critică):**

Pe buletin apare mențiunea „Examen histopatologic în curs de execuție" → **biopsia esofagiană este procesată la Bioclinica Arad** (nu la Genesis, cum se presupunea inițial). Contact urmărire: arad@bioclinica.ro.

**Sursă informație:** utilizator (Roland Petrilă) — a trimis scanul buletinului.

**Făcut de:** Claude Code (Opus 4.7, 1M context).

---

## 2026-04-18 (sesiune Claude_Opus_4.7, continuare 2) — Confirmare CT 20.04 + plan pregătire

**Tip:** ACTUALIZARE DATE MEDICALE

**Fișiere afectate:** `CONTEXT_MEDICAL.md`, `TODO.md`.

**Descriere:**

- Confirmată programarea CT torace+abdomen+pelvis cu contrast pentru **LUNI 20.04.2026 ora 17:00** la Genesis Medical Clinic Micălaca.
- Recalculate deadline-urile pentru pregătirea medicației: STOP Jamesi sâmbătă 18.04 ora 17:00 (H-48); reluare miercuri 22.04 ora 17:00 (H+48) după creatinină normală.
- Adăugat plan alimentație pre-CT (cină duminică 20:00, gustare luni 11:00, doar apă până la CT).
- Semnalat STALE al creatininei (ultima 28.11.2025 — 5 luni vechime) — necesare analize actualizate.
- Atenționare Triplixam (indapamidă diuretic + perindopril IECA) — de clarificat cu radiologul la confirmare telefonică.
- Confirmare absență alergii — P0 critic, încă neconfirmat.

**Sursă informație:** utilizator (Roland Petrilă) — a confirmat programarea CT.

**Făcut de:** Claude Code (Opus 4.7, 1M context).

---

## 2026-04-18 (sesiune Claude_Opus_4.7, continuare) — Git init + push + Regula 16

**Tip:** ADAUGARE + MODIFICARE

**Fișiere afectate:** `CLAUDE.md` (proiect), `REGULAMENT.md`, `.gitignore` (nou), `CHANGELOG.md`, `SESSION_LOG.md`.

**Descriere:**

- Inițializat Git local (`git init -b main`)
- Creat `.gitignore` minimal (OS artifacts + safety net secrete)
- Primul commit `ee642d2`: 81 fișiere, +10.207 linii
- Creat repo privat `RolandPetrila/Tati_Dosar_Medical` pe GitHub (de către user manual)
- Remote `origin` configurat + `main` pushed cu tracking
- **Regula 16** adăugată în `CLAUDE.md` (proiect): git auto-commit + push la finalul fiecărei sesiuni cu modificări de referință
- Cross-reference Regula 16 adăugat în `REGULAMENT.md` secțiunea 4.5

**Motiv:** versionare structurată, rollback granular, backup paralel cu Google Drive, trasabilitate pe istoric dosar medical.

**Făcut de:** Claude Code (Opus 4.7, 1M context).

---

## 2026-04-18 (sesiune Claude_Opus_4.7) — Audit + migrare v2 + reorganizare structurală

**Tip:** MIGRARE_MAJORĂ

**Declanșator:** audit cerut de Roland Petrilă; aprobare execuție completă primită.

### Date corectate (erori în JSON-urile Gemini v1)

- **CNP** în `Talon_Pensie_Asigurare_2025.json`: `1590518244861` → `1590518024486` (ancora: C.I. + 6 alte documente).
- **Data nașterii** în `Dosar_Urologie_Gastroenterologie_2025.json`: `28-10-1959` → `1959-05-18`.
- **Nume pacient** în `Schema_Medicamente_10_11_2025.json`: `PETRICA` → `PETRILĂ` (medicul scrisese eronat pe manuscris).
- **Unitate WBC** în `Buletin_Analize_Sange_17_06_2025.json`: `µg/dl` (imposibil medical) → `x10^3/µL`.
- **Coduri ICD-10** în `Dosar_Urologie_Gastroenterologie_2025.json`: eliminat prefixul intern spital (ex. `702-N43.3` → `N43.3`, cod intern separat).
- **Unități lab** în `Iesire_Din_Spital_Chirurgie_28_11_2025.json`: completate din fișierul paralel `Bilet_Iesire_`.

### Dedup

- 3 JSON-uri chirurgie 28.11.2025 → 1 canonic `2025-11-28_externare_chirurgie_hernie.json`. Originalele arhivate în `Dosar_Medical/arhiva/duplicate_chirurgie_28_11_2025/`.

### Fișiere create (Dosar_Medical/)

- 9 JSON-uri canonice la schema v2.0 (vezi MANIFEST.json pentru listă)
- `PLAN_audit_remediere_v2_2026-04-18.md` — planul sesiunii
- `SCHEMA_JSON_v2.md` — specificația structurii canonice
- `MANIFEST.json` — index cronologic al întregului dosar
- 11 fișiere `.meta.json` (chain of custody — Regula 14)

### Fișiere create (rădăcina proiectului .Tati/)

- `SESSION_LOG.md` — log sesiuni Claude/Gemini (Regula 9)
- `WEB_QUERIES.md` — log cercetări web (Regula 15)
- `CONTEXT_MEDICAL.md` — copiat din `Documentatie_Initiala/` + reconciliat cu JSON-uri (v1.1)
- `CHANGELOG.md` (acest fișier)
- `README.md`, `START.md`, `REGULAMENT.md`, `WORKFLOW.md`, `STRUCTURA_PROIECT.md`, `BAZA_CUNOSTINTE.md`, `TEMPLATES.md`, `SURSE_MEDICALE.md`, `GLOSAR.md`, `TODO.md` — copiate din `Documentatie_Initiala/` la rădăcina proiectului (conform STRUCTURA_PROIECT.md)

### Fișiere modificate

- `REGULAMENT.md`: adăugat preambul de cross-reference către `CLAUDE.md` proiect v2 (Regulile 6-15)
- `Documentatie_Initiala/INSTALARE.md`: path real adăugat (canonical `C:\Users\ALIENWARE\Desktop\Roly\.Tati\`, sync target `G:\My Drive\Roly\.Tati\`)
- `CONTEXT_MEDICAL.md`: reconciliere extensivă cu date confirmate din JSON-uri (secțiuni 1 date pacient, 3 antecedente, 4 medicație, 7.3 colonoscopie, 8 pregătire CT, 9 echipă medicală)

### Structura de foldere creată (în Dosar_Medical/)

- `documente_sursa/01_identitate`…`99_altele` (13 subfoldere)
- `interpretari/jurnal_simptome/`, `interpretari/cronologic/`
- `rapoarte_generate/versiuni_anterioare/`
- `cercetari/`, `comunicare_medici/`
- `arhiva/backup_pre-migrare_v2_2026-04-18/`, `arhiva/duplicate_chirurgie_28_11_2025/`, `arhiva/context_medical_versiuni/`, `arhiva/versiuni_config/`

### Scanuri mutate + redenumite la format ISO (YYYY-MM-DD_slug.ext)

| Vechi                             | Nou                                                                                    |
| --------------------------------- | -------------------------------------------------------------------------------------- |
| `C.I. - Petrila Viorel.pdf`       | `documente_sursa/01_identitate/2023-06-12_carte_identitate.pdf`                        |
| `Gastroscopic_Colonoscopic.pdf`   | `documente_sursa/09_endoscopie_2026_04/2026-04-17_buletin_endoscopie_colonoscopie.pdf` |
| `Ieșire din spital.pdf`           | `documente_sursa/07_hernie_2025_11/2025-11-28_externare_chirurgie_hernie.pdf`          |
| `Schema_Medicamente.jpeg`         | `documente_sursa/08_schema_tratament/2025-11-10_schema_medicamente_manuscris.jpeg`     |
| `Casa_judeteana_de_pensii.jpeg`   | `documente_sursa/10_administrativ_pensie/2025-11-01_talon_pensie_scan.jpeg`            |
| `Apr 17, Doc 2-7.pdf` (6 fișiere) | `documente_sursa/99_altele/2026-04-17_doc_neidentificat_{2-7}.pdf`                     |

### Fișiere șterse (backup-urile rămân în `arhiva/`)

- 10 JSON-uri Gemini v1 din rădăcina `Dosar_Medical/` (identice ca conținut cu cele din `arhiva/backup_pre-migrare_v2_2026-04-18/`)

### Validare finală

- ✅ 21 JSON-uri (9 canonice + 1 MANIFEST + 11 .meta.json) — toate parse OK
- ✅ CONTEXT_MEDICAL.md v1 arhivat în `Dosar_Medical/arhiva/context_medical_versiuni/CONTEXT_MEDICAL_v1_2026-04-17.md`
- ✅ Scanurile originale intacte (doar redenumite și mutate; conținutul binar neschimbat)

### Nerezolvat / rămas pentru sesiuni viitoare

- 6 PDF-uri `2026-04-17_doc_neidentificat_{2-7}.pdf` — de deschis și identificat conținutul
- Schema_Medicamente: numele exact al Dr. LAZĂR de identificat
- Unitatea/secția exactă pentru chirurgia 28.11.2025 (JSON are `de identificat`)
- Status alergii pacient — P0, CRITIC pentru CT cu contrast
- HbA1c recent — P1, relevant pentru monitorizare diabet

**Făcut de:** Claude Code (Opus 4.7, 1M context) — sesiunea audit a durat ~02:00–02:23 pe 2026-04-18 (corectat 2026-04-18 02:51; timestamp-ul original „~15:00 la ~17:00" era halucinație — vezi erata de mai sus).

---

## 2026-04-17/18 — Inițializare dosar + procesare Gemini (retroactiv)

**Tip:** CREARE

**Descriere:** Inițializare kit documentație (Claude.ai) și procesare inițială a PDF-urilor medicale de către Gemini în JSON-uri v1. Detalii în `SESSION_LOG.md`.

**Făcut de:** Claude.ai (web) + Gemini.

---

## Formatul intrărilor viitoare

Fiecare modificare nouă se adaugă la începutul acestui fișier, deasupra intrării precedente, în formatul:

```markdown
## YYYY-MM-DD (HH:MM opțional) — [Titlu scurt]

**Tip:** [CREARE / MODIFICARE / CORECTIE / ARHIVARE / ADAUGARE / MIGRARE]
**Fișier(e) afectat(e):** `fisier1`, `fisier2`
**Descriere:** Ce s-a modificat, concret.
**Motiv:** De ce s-a făcut modificarea.
**Sursă informație (dacă aplicabil):** document / consult / cercetare
**Făcut de:** utilizator / Claude Code / Gemini
```
