# REGULI_CLAUDE_CODE.md — Reguli specifice Claude Code (6-22)

**Versiune:** 12.0 (arhitectură restructurată din `CLAUDE.md` v11) | **Data:** 2026-04-23

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

## Note generale

- Regulile din acest fișier **extind** (nu înlocuiesc) `REGULAMENT.md` (reguli medicale 1-10) + regulamentul global `~/.claude/CLAUDE.md` + `rules/*.md`.
- La conflict direct pentru `.Tati`: Regulile din acest fișier + `REGULAMENT.md` au prioritate.
- Changelog evoluție reguli v1→v11 (ce s-a schimbat, când, de ce): `Documentatie_Initiala/HISTORY_CLAUDE_MD.md`.
- Pentru reguli care se aplică DOAR în `Dosar_Medical/` (OCR, chain of custody, valabilitate clinică, manuscrise, coordonare Gemini, backup, WEB_QUERIES log): `Dosar_Medical/CLAUDE.md`.
