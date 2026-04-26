# REGULI_CLAUDE_CODE.md — Reguli specifice Claude Code (6-30)

**Versiune:** 12.5 (adăugare R30 sistem sync Claude Projects pentru chat web/mobil) | **Data:** 2026-04-27

> **Citire obligatorie la prima interacțiune** — după `REGULAMENT.md` (reguli medicale fundamentale 1-10), înainte de `CONTEXT_MEDICAL.md`.
>
> **Acest fișier conține Regulile 6-22 specifice Claude Code, în formă compactă (rule + Why + How).**
>
> Regulile 8, 9, 10, 11, 13, 14, 15 (specifice lucrului cu documente medicale) sunt în `Dosar_Medical/CLAUDE.md` — încărcate contextual.
>
> Exemple extinse, matrice și protocoale detaliate: `Documentatie_Initiala/REGULI_DETALIATE.md` (citit on-demand).
>
> Istoricul evoluției regulilor v1→v11: `Documentatie_Initiala/HISTORY_CLAUDE_MD.md`.

---

## Regula 6 — Confirmare fișiere la final de mesaj (scoped)

La finalul oricărui mesaj în care ai modificat sau creat **fișiere de referință**, listezi explicit ce s-a modificat.

**Format:**

```
**Fișiere actualizate în acest mesaj:**
- `cale/fisier.md` — descriere scurtă a modificării
```

**Fișiere de referință** (declanșează lista obligatoriu): `CONTEXT_MEDICAL.md`, `CHANGELOG.md`, `GLOSAR.md`, `TODO.md`, `REGULAMENT.md`, `CLAUDE.md`, `REGULI_CLAUDE_CODE.md`, `SESSION_LOG.md`, `WEB_QUERIES.md`; orice `.json` din `Dosar_Medical/`; documente generate pentru medici sau familie; fișiere în `documente_sursa/` sau `arhiva/`.

**NU se aplică la:** scratch files, debug logs, simple lecturi (`Read`, `Grep`, `Glob`).

**Why:** transparență strictă pe modificările datelor medicale; minim necesar pentru trasabilitate. Aplicarea la tot creează zgomot și tocește atenția.

**How to apply:** după `Write`/`Edit` pe fișier de referință → lista obligatorie; fișiere auxiliare → judecată.

---

## Regula 7 — AskUserQuestion pentru decizii care ating date medicale

Folosești `AskUserQuestion` înainte de orice decizie cu incertitudine **care atinge date medicale, structura dosarului, sau documente destinate medicilor**.

**Obligatoriu întrebare explicită la:**

- Două valori care se contrazic (doze, date, rezultate laborator, denumiri medicamente)
- Informație medicală lipsă pe care ai putea-o presupune
- Interpretarea unui text medical ambiguu
- Conținutul unui document pentru medic / familie
- Denumirea unui fișier de referință
- Structurarea unei secțiuni noi în `CONTEXT_MEDICAL.md`

**Judecată profesională (fără întrebare):** formatare markdown, indentare, whitespace; denumirea unor fișiere auxiliare non-referință; decizii pur procedurale (ce skill să folosești, ordinea operațiilor).

**Why:** presupunerile implicite pe date medicale pot avea consecințe clinice; presupunerile pe formatare nu.

**How to apply:** dubiu factual medical → oprește, întreabă cu variante A/B/C. Dubiu procedural → decizi tu, menționezi alegerea în răspuns.

---

## Regula 12 — Procedură conflict surse autoritare

Când două surse autoritare (ESMO vs NCCN vs AJCC) recomandă diferit:

**Format obligatoriu de prezentare:**

```
**Opțiunea A — [sursă, ediție, an]:** [recomandare]
**Opțiunea B — [sursă, ediție, an]:** [recomandare]

Diferență-cheie: [ce le separă]
Context aplicabilitate: [Europa vs SUA, instituții diferite, etc.]
Recomandare: consult medical oncolog pentru decizie — NU aleg eu între opțiuni.
```

**Orientare implicită (NU decizie):** România → ESMO preferat; stadializare → AJCC/UICC (ediția curentă); protocoale chirurgicale → NCCN tinde să fie mai explicit.

**Why:** AI-ul care alege silent între două ghiduri autoritare face medicină fără autoritate clinică.

**How to apply:** la orice protocol / stadializare / decizie de tratament cu > 1 sursă autoritară.

---

## Regula 16 — Git auto-commit + push la finalul fiecărei sesiuni

**Context:** proiect versionat pe GitHub public `RolandPetrila/Tati_Dosar_Medical` (creat 2026-04-18). User a pre-autorizat Claude să facă `git add + commit + push` automat fără confirmare individuală pe sesiune.

**Protocol obligatoriu la finalul sesiunii:**

1. Dacă s-au modificat fișiere de referință (`CONTEXT_MEDICAL.md`, JSON-uri `Dosar_Medical/`, `.meta.json`-uri, documente sursă, documente generate) → execuți secvența:

   ```bash
   cd "C:\Users\ALIENWARE\Desktop\Roly\.Tati"
   git status --short
   git add .
   git commit -m "<mesaj descriptiv>"
   git push
   ```

2. **Actualizare obligatorie înainte de commit:** `CHANGELOG.md` (intrare nouă) + `SESSION_LOG.md` (Regula 9).

3. **Verificări pre-push:** niciun fișier secret (`.env`, `*.key`, credențiale) staged; repo este **public** (nu modifica visibility); fără `--force` push; fără `--amend` pe commit-uri push-uite.

4. **Mesaj commit:** prima linie max 72 char (rezumat acțiune principală); corp cu bullet-uri; footer `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>`.

5. **Timestamp narative — OBLIGATORIU `date` înainte de scriere.** Sistem îți dă data, NU ora. Fără verificare → tendința de a inventa timestamp-uri → halucinație (violare R3 + Regula 8 + Regula 11).

   ```bash
   date +"%Y-%m-%d %H:%M:%S %z"
   ```

   Frecvență: o dată la start + refresh per bloc >15 min.

6. **Raportare final:** ultima linie confirmă hash commit + status push. Format: `✅ Commit <hash> pushed → origin/main (N files changed)`.

**Excepții (NU commit automat):** sesiuni pur audit fără modificări; conflicte nerezolvate; user cere explicit „doar local"; artefacte temporare (`.tmp`, `.bak`).

**Protocol extins (format timestamp per fișier, edge cases):** `Documentatie_Initiala/REGULI_DETALIATE.md` §R16.

**Why:** Google Drive sync + Git snapshot discret oferă rollback granular pe dosar medical cu relevanță legală.

**How to apply:** după ultima operație de scriere, înainte de raportul final către user. Nu aștepta ca user-ul să ceară.

---

## Regula 17 — Marcaj certitudine pentru informații medicale în documente generate

Pentru orice **document de ieșire** (raport, rezumat, interpretare, traducere prospect, comunicare medici/familie, document pacient) care conține afirmații medicale factuale, **TOATE afirmațiile trebuie marcate cu nivel de certitudine**.

**Cele 4 marcaje obligatorii:**

| Marcaj         | Când se aplică                                                                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **[CERT]**     | Confirmat din sursă primară autoritară: RCP ANMDMR/SmPC EMA, ghid clinic major (ESMO, NCCN, AJCC, AHA/ESC), studiu peer-reviewed cu citare. Sursa identificată explicit. |
| **[PROBABIL]** | Susținut de literatura medicală generală (review, UpToDate, farmacologie standard), dar nu explicit în sursa primară. Se declară motivul.                                |
| **[INCERT]**   | Date conflictuale, mecanism ipotezat, extrapolare de la populație diferită, lipsă date specifice. Se declară ce anume e incert.                                          |
| **[NEGASIT]**  | Căutat în ≥2 surse autoritare, fără rezultat. Se declară **unde** s-a căutat.                                                                                            |

**Reguli operaționale compacte:**

1. Cifre / procente / frecvențe → `[CERT]` obligatoriu + sursă citată URL + data versiunii.
2. Nume medicamente, doze exacte, intervale de referință → `[CERT]` obligatoriu.
3. Mecanisme acțiune + farmacologie standard → `[PROBABIL]` acceptabil.
4. Secțiune obligatorie „Surse citate" la finalul documentului.
5. Secțiune obligatorie „Ce NU am găsit" (transparență).
6. Atenționare finală: „NU înlocuiește consultul medical."
7. SmPC/ghid/studiu > 12 luni → „verificare versiune curentă recomandată" (Regula 11).
8. Sursă primară > sursă secundară. NU se citează AI (Gemini/ChatGPT/Claude) ca sursă.

**Exemple complete + format corect/greșit:** `Documentatie_Initiala/REGULI_DETALIATE.md` §R17.

**Why:** o afirmație medicală incorectă într-un document destinat familiei poate influența o decizie clinică fără validare. Marcajul forțează distincția fapte verificate vs ipoteze.

**How to apply:** la fiecare afirmație factuală, întrebare mentală: „Am sursă primară citabilă?". Da → `[CERT]` + citare. Nu → `[PROBABIL]`/`[INCERT]`/`[NEGASIT]`. Niciodată neadnotată.

---

## Regula 18 — Sincronizare `DASHBOARD.html` la actualizări medicale

**Context:** `DASHBOARD.html` = vizualizare rapidă pentru familie (medicație, alergii, analize, calendar, acțiuni). Distribuit live pe **https://rolandpetrila.github.io/Tati_Dosar_Medical/** (GitHub Pages, auto-deploy la push). Sincronizare manuală de AI, fără backend.

**Declanșatori regenerare integrală la final sesiune:**

1. Analiză nouă (laborator, imagistică, biopsie, histopatologie)
2. Medicație modificată (doză, nou, oprire, reluare, schimbare)
3. Alergie nouă documentată sau invalidată
4. Investigație nouă (programată, efectuată, rezultat)
5. Antecedent medical nou (consult, spitalizare, diagnostic)
6. Document sursă nou procesat în `Dosar_Medical/`
7. Modificare status acțiuni **P0** în `TODO.md` (critice)
8. Schimbare simptomatologie sau status clinic
9. Modificare `ALIMENTATIE.md` → regenerare **PARȚIALĂ** (doar blocul `<script type="text/markdown" id="md-alimentatie">` + `lastRegen`)

**NU declanșează:** corectare typo; update log-uri proces (SESSION_LOG, CHANGELOG); reorganizare markdown; P1/P2/P3 în TODO; `.meta.json`-uri.

**Timing:** o singură regenerare per sesiune, la final, ÎNAINTE de `git commit + push` (Regula 16).

**Secțiuni obligatorii dashboard + reguli tehnice + exemple:** `Documentatie_Initiala/REGULI_DETALIATE.md` §R18.

**Why:** familia vrea vizualizare rapidă fără navigare prin 370 rânduri markdown. Fără regenerare explicită, dashboardul devine sursă paralelă divergentă — anti-pattern.

**How to apply:** la finalul sesiunii cu ≥1 declanșator → regenerare integrală + commit. Declanșator #9 singur → regenerare parțială.

---

## Regula 19 — Documente informative în `Documente_Informative/` (shortcut)

Documentele informative/operaționale (ghiduri, explicații, materiale familie/consulturi) se plasează în `Documente_Informative/`, NU la rădăcina proiectului.

**Detalii complete (format nume, tip conținut destinat, excepții):** `Documente_Informative/CLAUDE.md`.

---

## Regula 20 — Mod de lucru: cercetare → status → AskUserQuestion → confirmare → execuție

**Protocol în 5 pași pentru orice sarcină care implică cercetare, audit sau integrare informații noi:**

1. **Cercetare/audit** — execuți verificările (WebSearch, WebFetch, Read, cross-referencing surse primare) și compilezi rezultatele.
2. **Semnalare proactivă nereguli** — sesizezi erori factuale/omisiuni/contradicții în sursele existente, cu: identificarea (citat exact) + documentarea (sursă contrazicătoare) + sugestia concretă de corecție + marcaj R17.
3. **Status raport** — prezinți user-ului: ce s-a verificat, tablou comparativ, nereguli semnalate, recomandare preliminară, puncte nesoluționate.
4. **AskUserQuestion (meniu interactiv)** — pentru toate deciziile deschise, variante A/B/C/D clar formulate. NU text liber.
5. **Confirmare → execuție** — nu începi nicio modificare scrisă (Write/Edit/move/delete/commit) pe fișiere de referință până user-ul nu răspunde în meniul interactiv. După confirmare, execuți fix ce s-a confirmat, raportezi, dacă apar sub-decizii repeți ciclul.

**Excepții — nu necesită AskUserQuestion:** lecturi/audit pure; backup-uri automate (Regula 10); fix-uri erori evidente (typo) cerute explicit cu context complet; log-uri auxiliare (SESSION_LOG, CHANGELOG, WEB_QUERIES, MEMORY).

**Stop-and-ask în execuție:** dacă descoperi neregulă suplimentară sau conflict nedecis în meniul inițial → **STOP**, raportezi, deschizi nou `AskUserQuestion`. NU iei decizia singur.

**Why:** user controlează fiecare decizie care atinge documentația medicală; Google Drive fără istoric fin + relevanță legală = presupunerile costă.

**How to apply:** la fiecare rundă majoră, opresc la decizii deschise și întreb cu variante.

---

## Regula 21 — Curățenie fluidă folder. Zero ciorne.

**Principii:**

1. **O singură sursă de adevăr per subiect** — un subiect = un fișier validat.
2. **Zero fișiere-ciornă** — ciornele se procesează în conversație, nu pe disc.
3. **Audit + extracție + ștergere** — orice fișier extra (alt AI, raport neverificat, încercare intermediară) se auditează → se extrag informațiile utile → se șterge. Fără arhivare „ca să avem" (git păstrează istoric).
4. **Nume descriptiv și corect** — dacă conținutul s-a extins, fișierul se redenumește.

**Protocol pentru fișier extra:**

1. Identifică rolul (ciornă / backup / raport intermediar / document dubios)
2. Audit conținut (verificat / halucinat / util)
3. Integrează info utilă într-un document validat existent sau nou
4. După confirmare user, șterge sursa (fără arhivare în `arhiva/`)
5. Log în `CHANGELOG.md` + `SESSION_LOG.md`

**Excepție pentru arhivare (Regula 10 rămâne validă):** versiuni anterioare fișiere de referință modificate structural; versiuni CLAUDE.md modificate major; rapoarte DOCX cu valoare istorică. **NU se arhivează** ciorne, sinteze parțial halucinate, încercări.

**Why:** dosar medical consultat la momente critice; confuzie cauzată de fișier învechit poate întârzia o decizie clinică.

**How to apply:** la fiecare sesiune, verifici colaterale care pot fi curățate. La fișier nou propus, întreabă-te „există deja un document unde acest conținut poate fi integrat?" înainte de creare.

---

## Regula 22 — Verificare proactivă + eliminare informații neverificate (tot proiectul)

**Principii:**

1. **Zero afirmații fără sursă validă** în fișierele de referință. Orice afirmație factuală are una dintre:
   - `[CERT]` + sursă primară citată
   - `[PROBABIL]` + justificare
   - `[INCERT]` + destinație verificare
   - `[NEGASIT]` + surse consultate
2. **Afirmațiile `[INCERT]` NU sunt stare de repaus** — sunt task-uri de verificare.
3. **Verificare obligatorie la audit / review / integrare** — fiecare `[INCERT]` / `[PROBABIL]` se verifică activ.
4. **Decizie explicită după verificare:**
   - Confirmat → upgrade `[CERT]` + sursă + data
   - Infirmat → șterge afirmația + log `CHANGELOG.md`
   - Imposibil → lași `[INCERT]` cu surse consultate declarate

**Ierarhie surse acceptabile:** oficial primar (site instituțional, registru, SmPC/RCP, ghid peer-reviewed) > secundar reputabil (PubMed, CASPA, MS România) > media medicală recunoscută (cu cross-reference). **NU acceptabile:** Wikipedia, forumuri, blog-uri, site-uri comerciale, alt AI ca sursă primară.

**Propagare:** dacă găsești că un `[CERT]` existent conținea date incorecte → corectezi imediat + log `CHANGELOG.md` cu tag `corectie-retroactiva`.

**Excepții (nu re-verificare fiecare sesiune):** date statice confirmate (CNP, nume, naștere) — până user semnalează schimbare; OCR marcat `[ILIZIBIL]` (Regula 8); citate din ghiduri cu ediția marcată (Regula 11).

**Protocol concret + exemple:** `Documentatie_Initiala/REGULI_DETALIATE.md` §R22.

**Why:** un dosar medical nu tolerează info vagi permanent marcate „incert" — ori e adevărat (demonstrează), ori e fals (scoate). `[INCERT]` stagnant devine dezinformare cu impact clinic potențial.

**How to apply:** la orice citire a unui fișier de referință, observi `[INCERT]`/`[PROBABIL]` ca obligații deschise. Nu propaga info neverificată între documente.

---

## Regula 24 — Propagare integrală JSON → `CONTEXT_MEDICAL.md`

Orice element prezent într-un JSON medical trebuie să aibă reflexie în `CONTEXT_MEDICAL.md` — fie în secțiunea principală (impact direct), fie într-o secțiune dedicată descoperirilor colaterale (aspect normal / fără impact imediat dar documentat).

**Structură obligatorie per investigație integrată în `CONTEXT_MEDICAL.md`:**

1. **Findings principale** (impact decizional direct — orientează tratamentul)
2. **Findings secundare** (monitorizare / urmărire — necesită follow-up, dar nu schimbă decizia acum)
3. **Findings colaterale** (aspecte normale, sechele vechi, leziuni benigne incidentale — documentate complet)
4. **Parametri tehnici** (doză radiație, aparat, substanță contrast, numere buletin)
5. **Referință sursă**: path JSON + data extragere + `completeness_verified`

**Interzis:**

- Rezumate selective care pierd elemente din JSON
- Clasificarea unui element drept „nerelevant" pentru a-l omite (decide medicul, nu AI)
- „Aspect normal" nelistat explicit (absența e ambiguă — listare explicită = confirmare că a fost examinat)

**Regula de paritate:** dacă JSON-ul are 15 findings, `CONTEXT_MEDICAL.md` listează 15. Verificare obligatorie la finalul fiecărei propagări — se numără elementele din JSON și se confirmă numărul în `CONTEXT_MEDICAL.md`.

**Why:** incidentul 2026-04-23 a arătat că propagarea selectivă JSON → `CONTEXT_MEDICAL.md` pierde elemente cu relevanță clinică reală (tulburări ventilație pre-esofagectomie). Separarea „principal / secundar / colateral" păstrează lizibilitatea fără a sacrifica completitudinea. R24 este corolarul R23 (din `Dosar_Medical/CLAUDE.md`): R23 garantează că JSON-ul e complet, R24 garantează că `CONTEXT_MEDICAL.md` reflectă JSON-ul.

**How to apply:** la orice `Edit`/`Write` pe `CONTEXT_MEDICAL.md` care integrează date dintr-un JSON nou, numeri elementele din JSON și confirmă numărul în `CONTEXT_MEDICAL.md`. La audit periodic: compari cele două fișiere element cu element. Secțiunile 3 și 4 (colaterale + tehnici) sunt obligatorii chiar dacă par „fără impact decizional" (incidentul 2026-04-23 a arătat că tocmai aceste elemente pot deveni relevante la reevaluare).

---

## Regula 27 — Ingest Gmail pentru context dosar medical

Mailurile primite/trimise în legătură cu tata constituie sursă autoritară pentru programări, recomandări medicale, contacte noi. Ele trebuie integrate sistematic în dosar — fără pierderi, fără citate selective.

**Comenzi standard** (declanșabile oricând în chat):

| Comandă user                      | Acțiune                                                                                                                                    |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `verifică gmail oncohelp`         | Scan threaduri cu „oncohelp", „Anater", „Vornicu", „Mester" + alți medici OncoHelp/IOCN                                                    |
| `verifică gmail tata` (full scan) | Larg: „Petrila Viorel", „biopsie", „endoscopie", „colonoscopie", „CT", „Bioclinica", „Genesis", „cardiologie", „Nădlac", „Triplixam", etc. |
| `verifică gmail [keyword]`        | Specific pe termen indicat de user                                                                                                         |
| `verifică gmail nou`              | Tot ce e nou față de ultimul scan (nu limitat la zile — limita = ultimul thread_id procesat în `corespondenta/INDEX.md`)                   |

**Locație fișiere:** `Dosar_Medical/corespondenta/`

```
Dosar_Medical/corespondenta/
├── INDEX.md                                    ← index master cu toate threadurile
├── YYYY-MM-DD_slug-thread.md                   ← un fișier per thread (markdown + YAML frontmatter)
└── atasamente/                                 ← listate (NU descărcate); URL deep-link Gmail păstrat
```

**Format fișier per thread:** Markdown cu YAML frontmatter conținând `thread_id`, `subject`, `participanti`, `data_start`, `data_ultim`, `status`, `tags`. Corpul conține sinteză automată + mesaje cronologic + cross-references.

**Auto-propagare obligatorie după ingest:**

1. `Dosar_Medical/CONTACTE_MEDICALE.md` — emailuri/telefoane noi (dar NUMAI medici OncoHelp activi; nu istoric extern)
2. `CONTEXT_MEDICAL.md` — instrucțiuni medicale primite, cu marcaj sursă `[per mail Dr. X 2026-MM-DD]`
3. `TODO.md` — programări/termene noi
4. `SESSION_LOG.md` + `CHANGELOG.md` — log scan
5. `DASHBOARD.html` — tab Echipă medicală + bannere relevante
6. `INDEX.json` (rădăcină) — regenerat
7. Backup R10 + commit + push

**Atașamente — politică:** listate cu nume + tip + dimensiune + URL deep-link Gmail + extras textual (dacă PDF/DOCX) salvat în `INDEX.json#atasamente_index`. **NU se descarcă** automat. La cerere user („găsește atașamentul X") returnez instant numele + URL + sumar din extras.

**Auto-scan**:

- **Hook SessionStart** rulează `verifică gmail nou` ca primă acțiune
- **Cron Windows zilnic 22:00** rulează același scan independent

**Ce NU fac:** scan fără comandă user, modificare/trimitere/ștergere mailuri, expunere conținut integral mailuri pe DASHBOARD-ul public fără confirmare explicită.

**Why:** mailurile cu medicii sunt momente decizionale. Sesiunea 2026-04-25 a arătat că o reportare incorectă (lactate restricționate de gastroenterolog) propagată în documente fără sursă scrisă duce la decizii nutriționale eronate. Sistemul Gmail-ingest cu cross-reference la mail-sursă elimină acest risc.

**How to apply:** la orice frază de tipul „medicul a zis că..." sau „e programat la...", verifică întâi în `corespondenta/INDEX.md` dacă există sursa scrisă. Dacă da → citează thread-ul. Dacă nu → `[per user — neconfirmat în corespondență]` + propune scan dacă posibil să existe mail.

---

## Regula 28 — System Health Monitor (limite native Claude Code)

Dosarul `.Tati` se va încărca progresiv (corespondență, meta.json-uri, JSON-uri canonice, planuri). Fără monitorizare → risc real de depășire context window, CLAUDE.md prea mare, MEMORY.md trunchiat → erori de execuție și pierdere informație.

**Limite monitorizate** (`Dosar_Medical/SYSTEM_HEALTH.json` auto-generat):

| Metrică                                   | Limită                | Status                                    |
| ----------------------------------------- | --------------------- | ----------------------------------------- |
| Context tokens estimat la pornire sesiune | 200k Sonnet / 1M Opus | 🟢 <60% / 🟡 60-80% / 🟠 80-95% / 🔴 >95% |
| `CLAUDE.md` size (root proiect)           | 40KB warning oficial  | 🟢 / 🟡 / 🔴                              |
| `MEMORY.md` linii                         | 200 (truncat automat) | 🟢 <120 / 🟡 120-180 / 🔴 >180            |
| **`auto_loaded_md_kb`** (NOU 2026-04-26)  | **150KB**             | 🟢 / 🟡 / 🔴                              |
| Fișier individual                         | 200KB sau 5000 linii  | 🟢 / 🟡 / 🔴                              |
| `INDEX.json` size                         | 1MB                   | 🟢 / 🟡 / 🔴                              |
| Total `.md` root size                     | informativ            | _no status_ (vezi note)                   |

**Fișiere auto-loaded urmărite în `auto_loaded_md_kb`:**

- `CLAUDE.md` (root) — always-on
- `REGULAMENT.md` — citit la prima interacțiune (per ordine din `CLAUDE.md` root)
- `REGULI_CLAUDE_CODE.md` — citit la prima interacțiune
- `Dosar_Medical/CLAUDE.md` — nested contextual (subfolder)
- `Documente_Informative/CLAUDE.md` — nested contextual (subfolder)

> **Istoric rafinări:**
>
> - **2026-04-25 (rafinare 1):** `total_md_root_kb` 500 → 1024 KB. Justificare: suma brută `.md` la rădăcină e influențată de logs istorice (CHANGELOG.md, SESSION_LOG.md cresc liniar cu activitatea), care NU sunt auto-loaded. Pragul inițial 500 KB declanșa fals-pozitive predictibile. Limită temporară.
> - **2026-04-26 (rafinare 2 — ticket P2 închis):** introdus metric nou **`auto_loaded_md_kb`** (suma fișierelor REALMENTE auto-loaded la sesiune, prag **150 KB**) ca alertă REALĂ pentru risc context window. Justificare prag: 5 fișiere × ~40 KB oficial CLAUDE.md = ~200 KB teoretic; 150 KB lasă ~50% headroom pentru creștere naturală (reguli noi, update-uri nested) fără fals-pozitive. La 150 KB ≈ 50K tokens = 25% Sonnet 200k / 5% Opus 1M (sub critic). **`total_md_root_kb` demote** la metric **informativ** (NU declanșează status — rămâne pentru igienă proiect, dar nu provoacă WARNING/ALERT/CRITICAL). Plus: aliniere `context_tokens_estimate` cu lista AUTO_LOADED_FILES (5 fișiere) pentru consistency.

**Acțiuni automate la depășire:**

| Status              | Comportament Claude                                                                                                                |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 🟢 OK               | nimic                                                                                                                              |
| 🟡 WARNING (60-80%) | 1-line warning + propunere proactivă restructurare la final răspuns                                                                |
| 🟠 ALERT (80-95%)   | Refuz operații care încarcă suplimentar (scrieri masive, ingest gmail full). Cer confirmare explicită + propun plan restructurare. |
| 🔴 CRITICAL (>95%)  | STOP scrieri. Doar citire. Plan restructurare urgent. Refuz pornire ingest gmail full / adăugare fișiere.                          |

**Strategii preventive standard:**

1. **Lazy-load** — `CONTEXT_MEDICAL.md`, `ALIMENTATIE.md`, `corespondenta/*` NU se citesc la fiecare sesiune; doar la cerere
2. **INDEX.json first** — pentru orice search/query, citesc întâi `INDEX.json` (mic), apoi citesc fișiere specifice
3. **Sharding pe an** corespondență când va fi cazul (`corespondenta/2026/`, `2027/`)
4. **Arhivare proactivă** — corespondență finalizată >6 luni → `corespondenta/arhiva/YYYY/` cu doar sinteze
5. **Versioning** fișiere catalog (CONTACTE_MEDICALE.md cu `version: X.Y` în frontmatter)

**Hook SessionStart:** rulează `scripts/system_health_check.py` → afișează 1-line status în primul răspuns al sesiunii.

**Why:** prevenire pierderi informație și erori execuție. CLAUDE.md depășise 43KB la v11 (re-restructurat la 7KB v12). MEMORY.md poate trunchia silent. Fără monitorizare proactivă, sistemul degradează silent.

**How to apply:** la fiecare scriere semnificativă (>50 linii noi într-un fișier de referință), verific SYSTEM_HEALTH înainte. La 🟠/🔴 propun arhivare/sharding înainte de a continua.

---

## Regula 29 — Plan-Audit cross-terminal pentru task-uri complexe

Când un task depășește 5 sub-operații **sau** traversează mai multe sesiuni **sau** are risc real de rupere parțială, se aplică protocolul Plan-Audit cu **două terminale Claude Code**:

- **Terminal A (Auditor)** — sesiunea care planifică. Creează `PLAN_<nume>_<YYYY-MM-DD>.md` la rădăcina proiectului. Nu execută. Auditează după fiecare commit incremental.
- **Terminal B (Executor)** — sesiunea care execută strict planul. Marchează progresul în plan. Face commit incremental după fiecare task validat.

**Protocol obligatoriu:**

1. **Auditor (terminal A) creează planul** cu:
   - Header: versiune, status (`🔴 PENDING` / `🟡 IN_PROGRESS` / `🟢 COMPLETED`), auditor, executor, durată estimată
   - Context complet (decizii luate în sesiunea anterioară)
   - Reguli protocol (ordine, dependențe, backup R10, commit-uri incrementale)
   - Per task: pre-requisite, pași concreti (cu cod/comenzi/conținut paste-ready), verificare, status checkbox `- [ ]`, commit message planificat
   - Validări finale (ce trebuie să existe la final)
   - Handoff (instrucțiuni pentru terminalul B)

2. **Executor (terminal B), la deschidere:**
   - Citește `MEMORY.md` (vede checkpoint cu pointer la plan)
   - Citește `PLAN_*.md` la rădăcină cu status `🔴 PENDING` sau `🟡 IN_PROGRESS`
   - Confirmă cu user-ul că pornește execuția
   - Execută strict pas cu pas — nu abate, nu refactorează, nu adaugă lucruri ne-cerute
   - La fiecare task completat: marchează `[x]`, face commit incremental, update status plan
   - La eroare: STOP, raport în chat, NU continuă

3. **Auditor (terminal A) verifică** după fiecare commit incremental:
   - `git log` + `git diff` pentru a vedea ce s-a făcut
   - Validează că modificarea respectă planul
   - Semnalează discrepanțe în chat

4. **La final:** executor marchează status `🟢 COMPLETED` în plan + face commit final + audit final.

**Detect plan activ:** `CLAUDE.md` proiect conține instrucțiunea „dacă există `PLAN_*.md` la rădăcină cu status `🔴 PENDING` sau `🟡 IN_PROGRESS` în antet, citește-l ÎNAINTE de orice altceva și urmează instrucțiunile lui strict".

**Convenții bifare:**

- `- [ ]` task pending
- `- [x]` task completed (cu data + commit hash în paranteză)
- `- [⚠]` task blocat (cu motiv)
- `- [~]` task skipped (cu justificare)

**Backup R10 obligatoriu** pentru orice modificare la fișiere de referință medicală listate în plan.

**Commit-uri incrementale obligatorii** — un commit per task major (NU un commit final unic), cu mesaj `[PLAN <nume>] task #X — <subiect>`. Așa, întreruperea sesiunii nu pierde lucrul deja făcut.

**Why:** sesiunea 2026-04-25 a inițiat un task cu 9 sub-operații (R27 + R28 + CONTACTE + ingest Gmail + INDEX + DASHBOARD tab + commit). Sesiunea de planificare deja consumase context substanțial cu cercetarea Gmail + audit. Cumulul plan + execuție într-o singură sesiune ar fi atins limita de context. Decuplarea elimină acest risc + permite audit independent al execuției.

**How to apply:** orice cerere user care presupune `>5` modificări concrete și non-triviale → propune protocolul Plan-Audit. Creează `PLAN_*.md` cu detalierea de mai sus. NU începe execuția în terminalul curent; aștepți terminal nou (executor) și auditezi din terminalul curent.

---

## Regula 30 — Sistem sync Claude Projects (chat web/mobil)

**Pentru acces medical de pe mobil când Roland nu e la laptop**, există un mirror sincronizat al fișierelor critice în `_projects_sync/`, alimentat automat de pre-commit hook + script Python `scripts/regen_projects_sync.py`.

**Componente:**

1. **Folder `_projects_sync/`** la rădăcina proiectului (8 fișiere, ~257 KB total):
   - `STATUS_SNAPSHOT.md` (auto-generat: agregat one-page cu date pacient + status TNM + medicație + calendar + P0 active + git hash)
   - `PROJECTS_PRIMER.md` (manual, instrucțiuni operaționale Claude Projects: ordine consultare, marcaje R17, refuz presupunere R7, conflicte, limite)
   - Mirror al 6 fișiere sursă: `CONTEXT_MEDICAL.md`, `TODO.md`, `REGULAMENT.md`, `INDEX.json`, `Dosar_Medical/CONTACTE_MEDICALE.md`, `Documente_Informative/EXPLICATIE_CONSULT_ONCOLOG_SCENARII.md`

2. **Script `scripts/regen_projects_sync.py`** — copiază cele 6 sursă + generează `STATUS_SNAPSHOT.md` prin extragere regex secțiuni cheie din CONTEXT_MEDICAL §1/§2.1/§4 + TODO calendar + P0 active + git log HEAD.

3. **Pre-commit hook `.git/hooks/pre-commit`** (sincronizat Desktop ↔ Drive prin Drive client desktop):
   - Detectează staged changes pe cele 6 fișiere sursă
   - Dacă DA → rulează scriptul + `git add _projects_sync/`
   - Commit-ul include automat sync-ul (un singur commit, no infinite loop)
   - Dacă scriptul eșuează → abort commit (exit 1)

**Workflow user:**

```
Roland editează fișier sursă local
  → git commit (hook auto-regen _projects_sync/)
  → git push (GitHub + Drive sync auto)
═══════ RUPTURĂ MANUALĂ ═══════
  → Pentru chat Projects: Roland manual remove + drag&drop fișiere modificate
    în Project knowledge (~30s, doar la modificări medicale majore)
```

**Limitare cunoscută [CERT]:** Drive Connector în Project knowledge pe planul Max acceptă DOAR Google Docs nativ (verificat docs Anthropic 2026-04-27). Cataloging RAG cu re-index automat = Enterprise-only. Pe Max → drag&drop static, înghețat la momentul drop-ului.

**Why:** consult oncolog 4.05.2026 OncoHelp Timișoara apropiat; deciziile critice se iau în week-end / deplasări când Roland nu e la laptop. Claude Projects pe mobil cu fișiere sync-uite oferă context medical complet pentru întrebări rapide. Setup-ul auto-mirror local elimină munca manuală de regenerare; doar drag&drop final rămâne user-side.

**How to apply:**

- La adăugare fișier nou care merită sync mobil → update `FILES_TO_COPY` în `scripts/regen_projects_sync.py` + regen
- La modificare medicală majoră anticipată să fie consultată mobil → user re-uploadează cele 8 fișiere în Project knowledge după push
- La conflict raportat de user între chat Projects și fișier original → instruiește verificare data din `STATUS_SNAPSHOT.md` antet + reupload manual
- NU edita direct fișiere în `_projects_sync/` — sunt mirror, suprascrise la următorul commit cu fișier sursă; modificările se fac în originalele

---

## Note generale

- Regulile din acest fișier **extind** (nu înlocuiesc) `REGULAMENT.md` (reguli medicale 1-10) + regulamentul global `~/.claude/CLAUDE.md` + `rules/*.md`.
- La conflict direct pentru `.Tati`: Regulile din acest fișier + `REGULAMENT.md` au prioritate.
- Changelog evoluție reguli v1→v11 (ce s-a schimbat, când, de ce): `Documentatie_Initiala/HISTORY_CLAUDE_MD.md`.
- Pentru reguli care se aplică DOAR în `Dosar_Medical/` (OCR, chain of custody, valabilitate clinică, manuscrise, coordonare Gemini, backup, WEB_QUERIES log): `Dosar_Medical/CLAUDE.md`.
