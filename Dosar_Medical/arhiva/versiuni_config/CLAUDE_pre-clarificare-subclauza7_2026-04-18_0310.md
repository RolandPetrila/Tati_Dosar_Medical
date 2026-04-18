# CLAUDE.md — Reguli proiect `.Tati`

**Acest fișier conține reguli suplimentare pentru orice sesiune deschisă în folderul `G:\My Drive\Roly\.Tati`. Are prioritate față de regulamentul global la conflict direct.**

**Ultima revizuire:** 17 aprilie 2026 (v2).
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

7. **Timestamp-uri narative — OBLIGATORIU `date` înainte de scriere** (incident 2026-04-18 02:51):

   Înainte de a scrie orice timestamp într-un `SESSION_LOG.md`, `CHANGELOG.md`, `CONTEXT_MEDICAL.md` sau alt fișier narativ de referință, **rulează `date` în Bash** pentru a obține ora exactă a sistemului.

   ```bash
   date +"%Y-%m-%d %H:%M:%S %z"    # ex: 2026-04-18 14:32:17 +0300
   ```

   **NU presupune ora din context.** Sistemul îți dă data (`Today's date is YYYY-MM-DD`), dar NU ora. Fără verificare, tendința modelului e să invente timestamp-uri „plauzibile" (ex: 15:00, 17:30) → halucinație directă, violare R3 + Regula 8 + Regula 11.

   **Excepție:** commit-urile git au timestamp propriu automat (`git log --format=%ai`). Nu trebuie inclus manual în mesajul de commit — e deja în metadata git.

   **Cross-check:** dacă în sesiune apar ore intermediar (ex: user menționează „acum e 14:00"), verifică și cu `date` — sistemul e sursa de adevăr, nu afirmația din context.

   **Dacă observi discrepanță între un timestamp deja scris și `date` real → oprește și corectează imediat** (audit trail transparent în `CHANGELOG.md`, ca în erata din 02:51).

**Excepții (NU commit automat):**

- Sesiuni pur de citire/audit fără modificări
- Când există conflicte nerezolvate în working tree
- Când user solicită explicit "nu face push" / "doar local"
- Când working tree conține artefacte temporare (fișiere `.tmp`, `.bak`, experimente) — atunci faci commit selectiv (nu `git add .`)

**Why:** proiectul are două sisteme de backup paralele — Google Drive (sync continuu al folderului) și Git (snapshot-uri discrete cu istoric). Git oferă rollback granular, diff între versiuni, colaborare structurată cu medicii / alte instanțe AI. Pierderea unui snapshot la o sesiune importantă = pierdere de istoric trasabil pentru un dosar medical cu relevanță legală.

**How to apply:** după ultima operație de scriere din sesiune, înainte de raportul final către user, rulează secvența de commit + push. Nu aștepta ca user-ul să ceară explicit.

---

## Relația cu celelalte regulamente

Regulile de aici **extind** (nu înlocuiesc):

- Regulamentul global `C:\Users\ALIENWARE\.claude\CLAUDE.md`
- Regulile din `C:\Users\ALIENWARE\.claude\rules\` (01–05)
- Regulile medicale critice din `C:\Users\ALIENWARE\Desktop\Roly\.Tati_Dosar_Medical\REGULAMENT.md`

La conflict direct pentru lucrul în `G:\My Drive\Roly\.Tati`, regulile din acest fișier au prioritate.

---

## Changelog

- **2026-04-18 v3:** adăugată Regula 16 (git auto-commit + push la finalul fiecărei sesiuni, după crearea repo-ului privat `RolandPetrila/Tati_Dosar_Medical`).
- **2026-04-17 v2:** adăugate regulile 8-15 (OCR anti-halucinație, coordonare Gemini, backup pre-modificare, valabilitate clinică, conflict surse, manuscrise, chain of custody, web queries log); scoped regulile 6-7 pentru a elimina overhead pe decizii triviale.
- **2026-04-17 v1:** prima versiune — regulile 6 și 7 preluate din `REGULAMENT.md` al dosarului paralel.
