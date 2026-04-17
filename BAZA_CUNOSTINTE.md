# BAZA_CUNOSTINTE.md — Menținerea bazei de cunoștințe

**Acest fișier descrie cum se construiește și se menține baza de cunoștințe — regulile pentru a se asigura că informațiile sunt corecte, actualizate și ușor accesibile.**

## Principii fundamentale

### 1. Sursa de adevăr

**`CONTEXT_MEDICAL.md` este sursa de adevăr pentru starea pacientului.** Dacă apare o contradicție între un alt fișier și `CONTEXT_MEDICAL.md`, prioritatea este:

1. Verificarea sursei primare (documentul original)
2. Actualizarea `CONTEXT_MEDICAL.md` dacă este necesar
3. Corectarea fișierului secundar

### 2. Trasabilitate

Fiecare afirmație factuală trebuie să aibă sursă identificabilă:

- Dacă provine dintr-un document medical → referință la fișierul din `documente_sursa/`
- Dacă provine dintr-o cercetare web → citare cu link și data accesării
- Dacă provine de la pacient / familie → menționat ca „informație raportată de [sursă]”
- Dacă este o interpretare → marcat explicit ca „interpretare preliminară”

### 3. Imutabilitatea documentelor sursă

Documentele sursă (scanuri, PDF-uri originale) sunt **imutabile**. Nu se modifică niciodată. Pentru corecții, se creează fișiere de interpretare separate.

### 4. Actualizare reactivă și proactivă

- **Reactivă:** la fiecare informație nouă primită, actualizezi fișierele relevante imediat.
- **Proactivă:** o dată pe săptămână (sau la cerere), verifici coerența întregului dosar, detectezi informații învechite, semnalezi actualizări necesare.

## Cum se construiește baza de cunoștințe

### Ciclul de îmbogățire

```
Informație nouă → Parsare → Clasificare → Structurare → Integrare → Verificare → Log
```

### Etapele detaliate

#### 1. Parsare

Extrage conținutul brut din sursa nouă:
- Text din PDF / imagine / document Word
- Date cheie (datele, valorile, numele)
- Structură logică (secțiuni, tabele)

#### 2. Clasificare

Stabilește:
- Categoria documentului (analiză, imagistică, consult, rețetă, etc.)
- Episodul medical aferent (stent 2012, H. pylori 2024, hernie 2025, etc.)
- Data și autorul

#### 3. Structurare

Creează o reprezentare structurată a informațiilor noi — un fișier de interpretare în `interpretari/` cu:
- Metadate (tip, data, sursa)
- Conținut brut relevant
- Interpretare / explicație
- Impact asupra stării curente

#### 4. Integrare

Actualizează fișierele de stare:
- `CONTEXT_MEDICAL.md` — secțiunile relevante
- `TODO.md` — acțiuni noi declanșate
- `GLOSAR.md` — termeni noi întâlniți
- `CHANGELOG.md` — log al operației

#### 5. Verificare

- Re-citește toate fișierele modificate.
- Verifică coerența.
- Confirmă cu utilizatorul dacă există interpretări nebanale.

#### 6. Log

Înregistrează operația în `CHANGELOG.md`.

## Proceduri specifice

### Procedura P1 — Document nou adăugat în `documente_sursa/`

**Trigger:** utilizatorul anunță că a adăugat un fișier nou sau detectezi un fișier nou la startul unei sesiuni.

**Pași:**
1. Citește conținutul fișierului (text, imagine → OCR/descriere).
2. Creează `interpretari/{YYYY-MM-DD}_{tip}.md` cu sinteza.
3. Actualizează `CONTEXT_MEDICAL.md` cu noile informații factuale.
4. Adaugă termeni noi în `GLOSAR.md`.
5. Generează acțiuni în `TODO.md` (ex: „de întrebat medicul despre valoarea X”).
6. Loghează în `CHANGELOG.md`.
7. Prezintă utilizatorului sinteza și listează modificările făcute.

### Procedura P2 — Rezultat de investigație nou

**Trigger:** utilizatorul trimite un rezultat nou (biopsie, CT, analize).

**Pași:** aceiași ca P1, cu atenție specială la:
- **Citare exactă a concluziei** din raport
- **Clarificarea termenilor** necunoscuți (web search + glosar)
- **Re-evaluare ipoteze** în `CONTEXT_MEDICAL.md`, secțiunea 10 (Evaluare preliminară)
- **Acțiuni imediate** derivate (programări, întrebări pentru medici)

### Procedura P3 — Consult medical efectuat

**Trigger:** utilizatorul raportează că s-a făcut un consult.

**Pași:**
1. Întreabă detaliat despre ce s-a discutat (folosește `ask_user_input` structurat).
2. Creează `comunicare_medici/{data}_{specialist}_rezultat_consult.md`.
3. Integrează recomandările în `CONTEXT_MEDICAL.md`.
4. Transferă acțiunile în `TODO.md`.
5. Actualizează echipa medicală în `CONTEXT_MEDICAL.md`, secțiunea 9.
6. Loghează.

### Procedura P4 — Simptom nou raportat

**Trigger:** utilizatorul raportează un simptom nou.

**Pași:**
1. Detaliază simptomul: când a început, caracteristici, evoluție, factori agravanți/atenuanți.
2. Evaluează dacă este un „steag roșu” (vezi `REGULAMENT.md` — urgențele medicale).
3. Actualizează `CONTEXT_MEDICAL.md`, secțiunea 6.
4. Dacă este relevant pentru următorul consult, adaugă în `TODO.md` ca „de menționat la consultul {medic}”.
5. Loghează.

### Procedura P5 — Medicație schimbată

**Trigger:** pacientul începe/oprește/modifică doza unui medicament.

**Pași:**
1. Confirmă cu utilizatorul detaliile exacte (nume, doză, ritm, medicul care a prescris).
2. Actualizează `CONTEXT_MEDICAL.md`, secțiunea 4.
3. Verifică interacțiunile cu medicația existentă (cercetare).
4. Verifică impactul asupra investigațiilor programate (ex: anticoagulante înainte de biopsie).
5. Loghează.

### Procedura P6 — Programare făcută

**Trigger:** utilizatorul anunță o programare.

**Pași:**
1. Notează în `TODO.md`, secțiunea „Calendar”.
2. Dacă este CT cu contrast sau procedură invazivă, generează un checklist de pregătire.
3. Cu 2-3 zile înainte, proactiv reamintește de pregătirea necesară.

### Procedura P7 — Corecție / retractare

**Trigger:** o informație anterior documentată se dovedește greșită.

**Pași:**
1. **Nu șterge** informația greșită.
2. Marchează-o ca retractată: `~~textul greșit~~ [retractat — motiv]`.
3. Adaugă informația corectă.
4. Loghează explicit în `CHANGELOG.md`: `[CORECȚIE]: ...`.
5. Dacă greșeala a condus la alte erori în dosar, verifică și corectează-le.

## Calitatea informației — niveluri

Pentru fiecare afirmație din dosar, este util să identifici nivelul de certitudine:

| Nivel | Descriere | Marcare |
|---|---|---|
| 1 — Confirmat | Direct din document medical oficial | Text simplu |
| 2 — Raportat | Raportat de pacient / familie, neverificat | „Raportat de [sursă]: ...” |
| 3 — Derivat | Concluzie logică din informații confirmate | „Pe baza X și Y, se poate deduce că...” |
| 4 — Estimat | Estimare cu nivel de încredere | „Estimez cu probabilitate X%” |
| 5 — De verificat | Necesită confirmare | `[DE VERIFICAT: ...]` |

## Verificarea periodică

### Săptămânal (recomandat)

Sesiune de întreținere, declanșată de utilizator:

1. Re-citește `CONTEXT_MEDICAL.md` complet.
2. Verifică `TODO.md` — elimină/completează acțiuni finalizate.
3. Verifică `CHANGELOG.md` — ultimele 10 intrări.
4. Verifică `documente_sursa/` — există fișiere noi neprocesate?
5. Verifică `GLOSAR.md` — există termeni folosiți în alte fișiere dar neadăugați?
6. Raportează utilizatorului un „raport de sănătate” al dosarului.

### La fiecare sesiune (automat)

La începutul fiecărei sesiuni (vezi `START.md`):

1. Confirmă că ai citit fișierele de configurare.
2. Confirmă statusul curent.
3. Raportează orice inconsistență detectată.

## Integrarea rezultatelor de cercetare

### Cercetări pe teme medicale

Rezultatele cercetărilor (`cercetari/*.md`) pot conține informații generale despre condiții medicale. Aceste informații:

- **NU se copiază** automat în `CONTEXT_MEDICAL.md` (care este specific pacientului).
- Se **referenționează** din `CONTEXT_MEDICAL.md` când este relevant: „Pentru detalii despre adenocarcinom esofagian, vezi `cercetari/2026-04-20_adenocarcinom.md`”.
- Se **actualizează** când găsești informații mai recente sau mai precise.

### Relația între cercetare și caz specific

Orice afirmație despre pacient trebuie să distingă:

- Ce este adevărat pentru **majoritatea pacienților cu condiția X** (informație generală)
- Ce este adevărat pentru **acest pacient specific** (informație concretă)

Exemplu bun:
> „În cancerul esofagian local avansat (stadiu III), supraviețuirea medie la 5 ani este de 15-25% [sursă: NCI 2024]. Pentru tatăl nostru, stadiul exact nu este încă stabilit — așteptăm rezultatele biopsiei și ale CT-ului.”

Exemplu greșit:
> „Tatăl are 15-25% șanse de supraviețuire.” [fără stadiu confirmat, fără sursă]

## Menținerea glosarului

Orice termen medical întâlnit într-un document sau răspuns se adaugă în `GLOSAR.md` dacă:

- Nu este deja acolo
- Este nerelațional cu jargonul medical general

Intrarea în glosar conține:
- Termenul
- Traducerea / explicația în termeni accesibili
- Contextul în care a apărut (opțional)
- Sursa explicației (dacă nu este cunoștință generală)

## Politica privind sursele externe

Când utilizatorul primește informații din surse externe (alt medic, cunoștință cu experiență medicală, articol citit):

1. **Notează sursa** ca „raportat din [sursă]”.
2. **Nu integra direct** în `CONTEXT_MEDICAL.md` fără confirmare din sursă autoritară.
3. **Cercetează** și confirmă.
4. Dacă informația este confirmată, integreaz-o cu citare.
5. Dacă este infirmată, notează în `CHANGELOG.md` și informează utilizatorul.

---

**Ultima revizuire:** 17 aprilie 2026.
