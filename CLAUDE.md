# CLAUDE.md — Reguli proiect `.Tati`

**Acest fișier conține reguli suplimentare pentru orice sesiune deschisă în folderul `G:\My Drive\Roly\.Tati`. Are prioritate față de regulamentul global la conflict direct.**

**Ultima revizuire:** 18 aprilie 2026 (v6).
**Context proiect:** dosar medical real pentru pacient Petrilă Viorel-Mihai (n. 18.05.1959), suspiciune proces proliferativ esofagian identificat la endoscopie pe 17.04.2026.

**Relație cu alte regulamente:**

- Extinde `C:\Users\ALIENWARE\.claude\CLAUDE.md` (regulament global)
- Preia regulile medicale critice din `C:\Users\ALIENWARE\Desktop\Roly\.Tati_Dosar_Medical\REGULAMENT.md` (dosar paralel — sursă originală)
- Coexistă cu `GEMINI.md` din același folder (vezi Regula 9)

---

## Regula 6 — Confirmare fișiere la final de mesaj (scoped)

La finalul oricărui mesaj în care ai modificat sau creat **fișiere de referință**, listezi explicit ce s-a modificat.

**Format standard:**

```
**Fișiere actualizate în acest mesaj:**
- `cale/fisier.md` — descriere scurtă a modificării
```

**Fișiere de referință** (declanșează lista obligatoriu):

- `CONTEXT_MEDICAL.md`, `CHANGELOG.md`, `GLOSAR.md`, `TODO.md`, `REGULAMENT.md`, `CLAUDE.md`, `SESSION_LOG.md`, `WEB_QUERIES.md`
- Orice `.json` din `Dosar_Medical/` (date structurate extrase)
- Documente generate pentru medici sau familie
- Fișiere în `documente_sursa/` sau `arhiva/`

**NU se aplică la:** scratch files, debug logs, simple lecturi (`Read`, `Grep`, `Glob`).

**Why:** transparență strictă pe modificările datelor medicale; minim necesar pentru trasabilitate. Aplicarea la tot (inclusiv scratch) creează zgomot și tocește atenția.

**How to apply:** după `Write`/`Edit` pe fișier de referință → lista obligatorie; pentru fișiere auxiliare → judecată.

---

## Regula 7 — `AskUserQuestion` pentru decizii care ating date medicale

Folosești `AskUserQuestion` înainte de orice decizie cu incertitudine **care atinge date medicale, structura dosarului, sau documente destinate medicilor**.

**Obligatoriu întrebare explicită la:**

- Două valori care se contrazic (doze, date, rezultate laborator, denumiri medicamente)
- Informație medicală lipsă pe care ai putea-o presupune
- Interpretarea unui text medical ambiguu
- Conținutul unui document pentru medic / familie
- Denumirea unui fișier de referință
- Structurarea unei secțiuni noi în `CONTEXT_MEDICAL.md`

**Judecată profesională (fără întrebare):**

- Formatare markdown, indentare, whitespace
- Denumirea unor fișiere auxiliare non-referință
- Decizii pur procedurale (ce skill să folosești, ordinea operațiilor)

**Why:** presupunerile implicite pe date medicale pot avea consecințe clinice; presupunerile pe formatare nu. Regula originală („orice neclaritate, oricât de mică") era prea absolută și bloca progresul.

**How to apply:** dubiu factual medical → oprește, întreabă cu variante A/B/C. Dubiu procedural → decizi tu, menționezi alegerea în răspuns.

---

## Regula 8 — Protecție anti-halucinație OCR

La text provenit din OCR (PDF scanat, fotografie document), niciodată nu completezi zone ilizibile din context.

**Protocol:**

1. Text corupt / caractere lipsă → marchează `[ILIZIBIL]` sau `[INCERT]` la transcriere
2. Existența unui `Eroare_Format_*.txt` pentru un document = semnal că OCR-ul a eșuat → tratează originalul ca sursă primară, cere re-scanare / transcriere manuală
3. NU inventa valori care „par logice în context"
4. Cifre din analize / doze cu incertitudine OCR → `[CIFRĂ INCERTĂ: X sau Y]` + escaladare

**Why:** în `Dosar_Medical/` există deja `Eroare_Format_*.txt` — dovadă că digitizarea e imperfectă. O cifră halucinată într-o analiză = risc clinic direct.

**How to apply:** la fiecare procesare de PDF scanat sau fotografie document medical.

---

## Regula 9 — Coordonare Claude ↔ Gemini

În acest folder există `GEMINI.md` cu reguli diferite (permite modificare directă în orice subfolder). Pentru a evita conflicte silent:

**Protocol:**

1. La deschidere sesiune: verifică timestamp-ul ultimelor modificări în `CHANGELOG.md` și în fișierele de referință
2. La modificări majore în fișiere de referință: adaugă linie în `SESSION_LOG.md` (creează dacă nu există):
   ```
   [YYYY-MM-DD HH:MM] [Claude|Gemini] [slug-operație] [lista-fișiere]
   ```
3. Înainte de a suprascrie conținut modificat recent (< 1 oră) de celălalt agent → STOP, cere confirmare user
4. NU presupune că celălalt agent a greșit; poate fi lucru deliberat

**Why:** doi agenți pe același dosar fără coordonare = conflicte silent, pierdere de informație. GEMINI.md permite modificări libere, deci Claude trebuie să fie cel defensiv.

**How to apply:** la orice sesiune care modifică fișiere de referință, verifică `SESSION_LOG.md` și loghează propria intenție.

---

## Regula 10 — Backup înainte de modificări majore

Înainte de orice modificare structurală la un fișier de referință, creezi backup explicit în `arhiva/`.

**„Modificare majoră" =**

- Rescriere de secțiune întreagă
- Ștergere sau mutare de conținut
- Schimbare format / structură
- Update la date medicale deja înregistrate

**Format backup:**

```
arhiva/[nume_fisier]_pre-[slug-operatie]_YYYY-MM-DD_HHMM.ext
```

Exemplu: `arhiva/CONTEXT_MEDICAL_pre-adaugare-CT-toracic_2026-04-17_2345.md`

**Why:** Google Drive nu are git; singurul mecanism real de rollback = copia explicită. Regula existentă „nu ștergi" e incompletă fără „salvezi înainte de a modifica structural".

**How to apply:** backup = PRIMUL pas într-o secvență de modificare majoră, apoi modifici.

---

## Regula 11 — Marcaj valabilitate clinică

Orice dată medicală temporală se marchează cu vechimea la citare.

**Praguri:**
| Tip informație | < 3 luni | 3-6 luni | 6-12 luni | > 12 luni |
|---|---|---|---|---|
| Analiză laborator | validă fără avertisment | `[de reverificat dacă decizia o cere]` | `[POTENȚIAL STALE]` + reverificare | repetare obligatorie |
| Imagistică (CT/RMN/ECO) | validă | validă cu mențiunea datei | reverificare | repetare obligatorie |
| Ghiduri terapeutice (ESMO/NCCN) | validă | validă | verifică ediția curentă | ediția e obsolete |

**Why:** o cifră corectă acum 8 luni poate fi irelevantă clinic astăzi. Prezentare fără context temporal = informație înșelătoare.

**How to apply:** la orice citare de valoare numerică din dosar, include data sursei.

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

**Orientare implicită (NU decizie):**

- România → ESMO preferat (standard european)
- Stadializare → AJCC/UICC (ediția curentă)
- Protocoale chirurgicale → NCCN tinde să fie mai explicit

**Why:** AI-ul care alege silent între două ghiduri autoritare face medicină fără autoritate clinică.

**How to apply:** la orice protocol / stadializare / decizie de tratament cu > 1 sursă autoritară.

---

## Regula 13 — Transcriere documente scrise de mână

Pentru text manuscris (scrisori medicale, bilete de trimitere, rețete):

**Protocol:**

1. Transcriere cu marcaj confidence: `[TRANSCRIERE confidence ~60%: „text aproximativ"]`
2. Cuvânt ambiguu → variante: `[„aspirin" | „aspirină" | „aspirat"]`
3. Nume proprii (medic, spital, medicament) → confidence obligatoriu
4. Cifre (doze, date) → confidence obligatoriu; la <80% confidence → cere confirmare user

**Why:** manuscrisul medical e notoriu dificil de descifrat; interpretare greșită a unei doze = risc.

**How to apply:** la fiecare scanare de document manuscris, înainte de integrare în `CONTEXT_MEDICAL.md`.

---

## Regula 14 — Chain of custody documente sursă

Pentru fiecare document nou adăugat în `Dosar_Medical/`, creezi fișier însoțitor metadata.

**`[nume_document].meta.json`:**

```json
{
  "source_document": "nume_fisier.pdf",
  "received_date": "YYYY-MM-DD",
  "received_from": "spital X / cabinet Y / pacient / familie",
  "digitized_by": "scanner / foto / email / portal online",
  "digitized_date": "YYYY-MM-DD",
  "transcriber": "Claude / Gemini / Roland manual",
  "ocr_quality": "good / partial / failed",
  "chain_notes": "orice informație relevantă"
}
```

**Why:** la consult secundar sau litigiu, proveniența unui document e parte din valoarea lui clinică și legală.

**How to apply:** la adăugarea oricărui document nou în `Dosar_Medical/`, creezi `.meta.json` corespunzător.

---

## Regula 15 — Log cercetări web

Pentru fiecare cercetare web care produce conținut introdus în dosar, log în `WEB_QUERIES.md`:

**Format:**

```markdown
## YYYY-MM-DD HH:MM — [slug-subiect]

- **Query:** "...exact ce ai căutat..."
- **Surse acceptate:** [URL-uri + motiv acceptare]
- **Surse respinse:** [URL-uri + motiv respingere: comercial / blog / outdated / nu peer-reviewed]
- **Concluzie introdusă în:** [fișier + secțiune]
- **Data publicării materialului:** [când a fost publicat / ultima actualizare]
```

**Why:** la verificare ulterioară, user sau medicul trebuie să poată reconstitui de unde vine o afirmație.

**How to apply:** după fiecare cercetare web care generează conținut factual introdus într-un fișier de referință.

---

## Regula 16 — Git auto-commit + push la finalul fiecărei sesiuni

**Context:** proiectul este versionat pe GitHub în repo-ul privat `RolandPetrila/Tati_Dosar_Medical` (creat 2026-04-18, sincronizat cu `origin/main`). User a pre-autorizat Claude să facă `git add + commit + push` automat fără confirmare individuală pe sesiune.

**Protocol obligatoriu:**

1. La finalul oricărei sesiuni care a modificat fișiere de referință (`CONTEXT_MEDICAL.md`, JSON-uri din `Dosar_Medical/`, documente configurare, `.meta.json`-uri, documente sursă adăugate), execuți secvența:

   ```bash
   cd "C:\Users\ALIENWARE\Desktop\Roly\.Tati"
   git status --short         # verificare ce e modificat
   git add .                  # stage toate modificările
   git commit -m "<mesaj>"    # mesaj descriptiv
   git push                   # către origin/main
   ```

2. **Mesajul de commit** urmează convenția din `CHANGELOG.md`:
   - Prima linie (max 72 caractere): rezumat acțiune principală (ex. `"Adaugare rezultat biopsie esofagiana + reconciliere CONTEXT_MEDICAL"`)
   - Corp: bullet-uri cu modificările concrete
   - Footer: `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>`

3. **Actualizare obligatorie înainte de commit:**
   - `CHANGELOG.md` — intrare nouă cu modificările sesiunii
   - `SESSION_LOG.md` — linie nouă conform Regulii 9

4. **Verificări obligatorii înainte de push:**
   - `git status` confirmă că niciun fișier secret (`.env`, `*.key`, credențiale) nu e staged
   - Repo rămâne **privat** (nu modifici visibility)
   - Nu faci `--force` push fără confirmare explicită user
   - Nu faci `--amend` pe commit-uri deja push-uite

5. **Dacă push eșuează:**
   - `fetch-and-merge` conflicte simple → rezolvare locală + retry push
   - Conflicte complexe → STOP, raportare la user, nu `--force`
   - Permisiune refuzată → verifică `gh auth status`, raportează

6. **Raportare la final:** ultima linie a răspunsului confirmă hash-ul commit-ului și status-ul push-ului.

   Format: `✅ Commit <hash> pushed → origin/main (N files changed)`

7. **Timestamp-uri narative — OBLIGATORIU `date` înainte de scriere** (incident 2026-04-18 02:51; clarificări 2026-04-18 03:10):

   Înainte de a scrie orice timestamp într-un `SESSION_LOG.md`, `CHANGELOG.md`, `CONTEXT_MEDICAL.md`, câmpul `_metadata.data_procesare` din JSON-urile `Dosar_Medical/` sau alt fișier narativ de referință, **rulează `date` în Bash** pentru a obține ora exactă a sistemului.

   ```bash
   date +"%Y-%m-%d %H:%M:%S %z"    # ex: 2026-04-18 14:32:17 +0300
   ```

   **NU presupune ora din context.** Sistemul îți dă data (`Today's date is YYYY-MM-DD`), dar NU ora. Fără verificare, tendința modelului e să invente timestamp-uri „plauzibile" (ex: 15:00, 17:30) → halucinație directă, violare R3 + Regula 8 + Regula 11.

   **Frecvență rulare `date`:** o dată la începutul sesiunii + **refresh per bloc de modificări cu durată estimată >15 min**. O sesiune lungă poate acumula 30-60 min între prima și ultima scriere → un singur timestamp inițial devine stale. La serii rapide de scrieri în <15 min, o singură rulare e suficientă.

   **Format timestamp per fișier (convenție proiect):**
   - `SESSION_LOG.md` — trunchiat la `YYYY-MM-DD HH:MM` (fără secunde, fără `+0300`); timezone implicit = ora locală România (EET/EEST)
   - `CHANGELOG.md` — `YYYY-MM-DD HH:MM` (același format ca SESSION_LOG)
   - `CONTEXT_MEDICAL.md` — data simplă `YYYY-MM-DD` sau text narativ (ex: „17 aprilie 2026")
   - `_metadata.data_procesare` din JSON-uri — format ISO 8601 complet `YYYY-MM-DDTHH:MM:SS+03:00`

   **Excepție:** commit-urile git au timestamp propriu automat (`git log --format=%ai`). Nu trebuie inclus manual în mesajul de commit — e deja în metadata git.

   **Cross-check:** dacă în sesiune apar ore intermediare (ex: user menționează „acum e 14:00"), verifică și cu `date` — sistemul e sursa de adevăr, nu afirmația din context.

   **Dacă observi discrepanță între un timestamp deja scris și `date` real → oprește și corectează imediat** (audit trail transparent în `CHANGELOG.md`, ca în erata din 02:51).

**Excepții (NU commit automat):**

- Sesiuni pur de citire/audit fără modificări
- Când există conflicte nerezolvate în working tree
- Când user solicită explicit "nu face push" / "doar local"
- Când working tree conține artefacte temporare (fișiere `.tmp`, `.bak`, experimente) — atunci faci commit selectiv (nu `git add .`)

**Why:** proiectul are două sisteme de backup paralele — Google Drive (sync continuu al folderului) și Git (snapshot-uri discrete cu istoric). Git oferă rollback granular, diff între versiuni, colaborare structurată cu medicii / alte instanțe AI. Pierderea unui snapshot la o sesiune importantă = pierdere de istoric trasabil pentru un dosar medical cu relevanță legală.

**How to apply:** după ultima operație de scriere din sesiune, înainte de raportul final către user, rulează secvența de commit + push. Nu aștepta ca user-ul să ceară explicit.

---

## Regula 17 — Marcaj certitudine pentru informații medicale în documente generate

Pentru orice **document de ieșire** (raport, rezumat, interpretare, traducere prospect, comunicare pentru medici/familie, document destinat pacientului) care conține afirmații medicale factuale, **TOATE afirmațiile trebuie marcate cu nivel de certitudine**.

**Cele 4 marcaje obligatorii:**

| Marcaj         | Când se aplică                                                                                                                                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **[CERT]**     | Confirmat din sursă primară autoritară: RCP ANMDMR / SmPC EMA, ghid clinic major (ESMO, NCCN, AJCC, AHA/ESC), studiu peer-reviewed major cu citare. Fiecare [CERT] are obligatoriu sursa identificată. |
| **[PROBABIL]** | Susținut de literatura medicală generală (review articles, UpToDate, farmacologie standard), dar **nu explicit** în sursa primară relevantă. Se declară motivul.                                       |
| **[INCERT]**   | Date conflictuale între surse, mecanism ipotezat, extrapolare de la studii pe populație diferită, sau lipsă de date specifice. Se declară ce anume e incert.                                           |
| **[NEGASIT]**  | Am căutat în surse autoritare (cel puțin 2) și **nu am găsit** informația. Se declară **unde** s-a căutat.                                                                                             |

**Reguli operaționale:**

1. **Cifre, procente, frecvențe → [CERT] obligatoriu + sursă citată cu URL/referință + data versiunii documentului.** Fără sursă → nu se citează cifra.
2. **Nume proprii de medicamente, doze exacte, intervale de referință → [CERT] obligatoriu.**
3. **Mecanisme de acțiune și explicații farmacologice generale → [PROBABIL] acceptabil** dacă sunt din cunoașterea medicală standard.
4. **La [PROBABIL] și [INCERT]:** declară motivul — ce anume lipsește sau ce anume e incert.
5. **La [NEGASIT]:** declară **ce** surse ai consultat (ex: „verificat SmPC Servier 06.2021 + RCP ANMDMR + literatura EMA — fără rezultate").
6. **Secțiune obligatorie „Surse citate"** la finalul fiecărui document medical, cu URL + data accesării + versiunea sursei.
7. **Secțiune obligatorie „Ce NU am găsit" (transparență)** — listează întrebările pe care documentul nu le acoperă și ar trebui puse medicului curant.
8. **Atenționare finală obligatorie** pentru documente destinate pacienților/familiei: „NU înlocuiește consultul medical."
9. **Limită temporală (coroborează cu Regula 11):** SmPC / ghid clinic / studiu cu vechime > 12 luni → marchează „verificare versiune curentă recomandată" lângă sursă.
10. **Sursă primară > sursă secundară.** Dacă Wikipedia / site comercial / blog / AI tool (inclusiv alt Claude / ChatGPT / Gemini) contrazic o sursă primară (SmPC / ghid), **sursa primară câștigă**. Nu se citează AI-ul ca sursă.

**Bonus — format intern în document:**

- Marcajele se scriu **la începutul paragrafului sau al afirmației** (nu la sfârșit).
- Un paragraf care combină afirmații de certitudini diferite → se împarte în sub-paragrafe, fiecare cu propriul marcaj.
- În tabele → coloană dedicată „Sursă" sau „Certitudine" dacă sunt multe rânduri.

**Why:** o afirmație medicală incorectă într-un document destinat familiei poate influența o decizie clinică (ex: „nu-i mai dăm medicamentul, am citit că e periculos") fără validare medicală. Marcajul explicit forțează atât autorul (Claude/Gemini) cât și cititorul (familie/medic) să distingă fapte verificate de ipoteze / extrapolări. Regula supremă R3 a regulamentului global acoperă principiul general de „nu inventezi"; Regula 17 îl **operaționalizează** specific pentru outputul medical al acestui dosar.

**How to apply:** la fiecare afirmație factuală dintr-un document medical de ieșire, rulează mental întrebarea: „Am sursă primară citabilă pentru asta?". Dacă da → [CERT] + citare. Dacă nu → [PROBABIL] / [INCERT] / [NEGASIT]. Niciodată nu lăsa afirmația neadnotată.

**Exemplu corect:**

> [CERT] Metforminul trebuie oprit cu 48h înainte de CT cu contrast iodat (RCP Janumet, secțiunea 4.4, Electronic Medicines Compendium UK, consultat 18.04.2026).
>
> [PROBABIL] La pacienții vârstnici cu funcție renală la limită, pauza poate fi prelungită la 72h, deși RCP nu specifică explicit — convenție clinică.
>
> [NEGASIT] Rata exactă a acidozei lactice la pacienții care au ignorat pauza de 48h — verificat SmPC + FDA label + nu există date consolidate dincolo de case reports.

**Exemplu GREȘIT (nu se face):**

> Metforminul se oprește 48h înainte. (fără marcaj, fără sursă)
>
> Metforminul cauzează acidoza lactică la aproximativ 5% din pacienți. (cifră fără [CERT] + sursă — dacă nu e în RCP, cifra nu se folosește)

---

## Regula 18 — Sincronizare `DASHBOARD.html` la actualizări medicale

**Context:** `DASHBOARD.html` (la rădăcina proiectului) este vizualizarea rapidă a dosarului pentru familie — status pacient, medicație, alergii, analize, calendar CT, acțiuni deschise. Fiind HTML static (fără backend), sincronizarea cu fișierele de referință se face manual de către agentul AI la fiecare sesiune care modifică conținutul medical.

**Declanșatori — OBLIGATORIU regenerare la sfârșit de sesiune:**

1. Analiză nouă (laborator, imagistică, biopsie, histopatologie) adăugată în dosar
2. Medicație modificată — doză nouă, medicament nou, oprire, reluare, schimbare
3. Alergie nouă documentată sau invalidată
4. Investigație nouă — programată, efectuată sau cu rezultat primit
5. Antecedent medical nou adăugat (consult, spitalizare, diagnostic)
6. Document medical sursă nou procesat în `Dosar_Medical/` (PDF / foto / manuscris)
7. Modificare status acțiuni **P0** în `TODO.md` (critice pentru pacient)
8. Schimbare simptomatologie sau status clinic relevant
9. Modificare `ALIMENTATIE.md` → regenerare **parțială** a dashboardului: actualizează **DOAR** blocul `<script type="text/markdown" id="md-alimentatie">…</script>` + variabila `lastRegen` din JS (tab-ul Alimentație). Nu necesită regenerare integrală — doar sincronizare embed pentru browser-ele care blochează `fetch()` pe `file://`. Timing: la finalul sesiunii, înainte de commit.

**NU declanșează regenerare:**

- Corectare typo în fișiere de referință fără modificare de conținut medical
- Update la `SESSION_LOG.md` / `CHANGELOG.md` (log-uri de proces)
- Reorganizare secțiuni, formatare markdown, whitespace
- Modificări la `TODO.md` pe P1/P2/P3 (non-critic pentru pacient)
- Update la `.meta.json`-uri (chain-of-custody)

**Timing:** o singură regenerare per sesiune, la final, imediat **ÎNAINTE** de `git add + commit + push` din Regula 16. Dashboardul intră în commit împreună cu modificările care l-au declanșat.

**Ce trebuie să conțină dashboardul (secțiuni obligatorii):**

1. **Header** — nume pacient, vârstă, data ultimei actualizări a dashboardului
2. **Countdown CT** / următorul eveniment medical major (JavaScript live)
3. **Status clinic curent** — suspiciune + faza investigațiilor
4. **Medicație activă** — tabel cu schema zilnică + marcaje STOP temporar / pauză
5. **Alergii** — verde dacă free, roșu dacă confirmate
6. **Analize recente** — valori + unități + interval referință + trend + flag normal/anormal
7. **Timeline antecedente** — cronologic, din 2012 până azi
8. **Echipă medicală** — specialitate, nume, unitate, contact
9. **Acțiuni deschise** — P0 (roșu), P1 (galben), P2/P3 (verde)
10. **Întrebări pregătite pentru consulturi** — grupate pe specialist
11. **Footer** — sursă date (link la `CONTEXT_MEDICAL.md`), atenționare „nu înlocuiește consultul medical"

**Reguli de conținut (coroborate cu Regulile 11 + 17):**

- Orice cifră din dashboard citează data sursei (data analizei, nu data dashboardului)
- Afirmațiile medicale factuale din dashboard respectă marcajul de certitudine (Regula 17) — atunci când nu e evident, indicație textuală scurtă
- Datele volatile (analize > 6 luni) primesc marcaj `[POTENȚIAL STALE]` conform Regulei 11
- NU se inventează valori lipsă — câmpurile goale se marchează „De completat"

**Reguli tehnice:**

- CSS inline în `<style>`, **fără dependențe externe** (offline-first, funcționează direct din Google Drive)
- Limbă: română, ton profesional dar accesibil familiei
- Palette culoare: albastru medical + verde OK + galben atenție + roșu critic
- Font: system fonts (Segoe UI / -apple-system / sans-serif) — fără web fonts
- Responsiv pentru desktop + imprimare A4 (`@media print`)
- Encoding UTF-8, declarat explicit în `<head>`

**La fiecare regenerare:**

1. Citește `CONTEXT_MEDICAL.md` + `TODO.md` + JSON-urile relevante din `Dosar_Medical/`
2. Suprascrie complet `DASHBOARD.html` (nu patch parțial)
3. Actualizează câmpul „Ultima generare" din header cu timestamp-ul obținut via `date` (Regula 16.7)
4. Logează generarea în `CHANGELOG.md` + `SESSION_LOG.md`
5. Include în commit-ul final al sesiunii

**Why:** familia vrea o vizualizare rapidă fără să navigheze prin 370 de rânduri de markdown. Un dashboard HTML static offline e formatul cel mai accesibil (click în Google Drive → deschide în browser, fără instalare). Fiind manual sincronizat, singura garanție că nu devine obsolet este regula explicită de regenerare la fiecare adăugare relevantă. Fără regulă, dashboardul devine o sursă paralelă de adevăr care diverge de documentație — anti-pattern.

**How to apply:** la finalul oricărei sesiuni cu un declanșator din lista de mai sus, regenerezi integral `DASHBOARD.html` înainte de commit. Excepție: declanșatorul #9 (modificare `ALIMENTATIE.md`) cere doar regenerare parțială a blocului embedded, nu a întregului dashboard. Dacă sesiunea nu are niciun declanșator (doar citire / audit / log-uri), nu regenerezi.

**Tab-uri dashboard:** începând cu v6, dashboardul are 2 tab-uri — `medical` (default, conținutul clinic) și `alimentatie` (ghidul culinar). Tab-ul Alimentație folosește strategie hibridă: încearcă `fetch('ALIMENTATIE.md')` la încărcare (vizualizare live pe browserele care permit) + fallback pe conținutul embedded în `<script type="text/markdown" id="md-alimentatie">` (pentru Chrome/Edge care blochează `fetch()` pe `file://`). Parser Markdown minimal inline, fără dependențe externe.

---

## Relația cu celelalte regulamente

Regulile de aici **extind** (nu înlocuiesc):

- Regulamentul global `C:\Users\ALIENWARE\.claude\CLAUDE.md`
- Regulile din `C:\Users\ALIENWARE\.claude\rules\` (01–05)
- Regulile medicale critice din `C:\Users\ALIENWARE\Desktop\Roly\.Tati_Dosar_Medical\REGULAMENT.md`

La conflict direct pentru lucrul în `G:\My Drive\Roly\.Tati`, regulile din acest fișier au prioritate.

---

## Changelog

- **2026-04-18 v6:** extinsă Regula 18 — adăugat declanșator #9 (modificare `ALIMENTATIE.md` → regenerare parțială tab Alimentație din dashboard). Clarificată strategia hibridă fetch+embed a tab-urilor. Trigger: user a cerut tab dedicat Alimentație în dashboard cu auto-update la modificarea `ALIMENTATIE.md`.
- **2026-04-18 v5:** adăugată Regula 18 (sincronizare `DASHBOARD.html` la fiecare actualizare medicală relevantă). Trigger: user a solicitat vizualizare rapidă HTML a dosarului + regulă explicită pentru a preveni divergența dashboard vs. documentație sursă.
- **2026-04-18 v4:** adăugată Regula 17 (marcaj certitudine [CERT]/[PROBABIL]/[INCERT]/[NEGASIT] pentru informații medicale în documente generate). Trigger: user a cerut un raport despre reacții adverse Jamesi + Triplixam și a solicitat explicit ca informațiile nesigure să fie marcate ca atare; Regula 17 operaționalizează R3 global pentru outputul medical al dosarului.
- **2026-04-18 v3.1:** clarificări Regula 16 sub-clauza 7 (timestamp narativ): adăugat câmp `_metadata.data_procesare` în lista fișierelor afectate; fix typo „intermediar" → „intermediare"; specificat frecvența rulării `date` (refresh >15 min); tabel format per fișier (SESSION_LOG/CHANGELOG trunchiat la `HH:MM`, JSON ISO 8601 complet). Trigger: audit utilizator care a detectat ambiguitățile și commit-ul 478048f nelogat în SESSION_LOG/CHANGELOG (remediat simultan).
- **2026-04-18 v3:** adăugată Regula 16 (git auto-commit + push la finalul fiecărei sesiuni, după crearea repo-ului privat `RolandPetrila/Tati_Dosar_Medical`).
- **2026-04-17 v2:** adăugate regulile 8-15 (OCR anti-halucinație, coordonare Gemini, backup pre-modificare, valabilitate clinică, conflict surse, manuscrise, chain of custody, web queries log); scoped regulile 6-7 pentru a elimina overhead pe decizii triviale.
- **2026-04-17 v1:** prima versiune — regulile 6 și 7 preluate din `REGULAMENT.md` al dosarului paralel.
