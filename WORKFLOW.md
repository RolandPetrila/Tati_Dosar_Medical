# WORKFLOW.md — Metodologia de lucru

**Acest fișier descrie ciclul obligatoriu de execuție și procedurile pentru operațiile frecvente.**

## Ciclul central de execuție

Pentru orice sarcină nontrivială, aplică ciclul în ordine strictă:

```
CLARIFICĂ (95%+) → PLANIFICĂ → CONFIRMĂ → EXECUTĂ → VALIDEAZĂ → URMĂTOR
```

### Etapa 1: CLARIFICĂ

**Scop:** să ajungi la o înțelegere de 95%+ asupra a ceea ce se cere.

**Acțiuni:**
- Reformulează cererea cu cuvintele tale și verifică cu utilizatorul.
- Identifică ambiguitățile și întreabă explicit.
- Folosește `ask_user_input` pentru întrebări structurate.
- Nu trece mai departe până când nu ai claritate completă.

**Criteriu de ieșire:** poți explica sarcina în 1-2 propoziții cu toate detaliile esențiale.

### Etapa 2: PLANIFICĂ

**Scop:** să structurezi execuția înainte de a acționa.

**Acțiuni:**
- Listează pașii concreți pe care îi vei face.
- Identifică fișierele care vor fi create sau modificate.
- Identifică sursele de informație necesare (web search, documente existente, utilizator).
- Estimează timpul și complexitatea.
- Identifică riscuri sau puncte de eșec.

**Criteriu de ieșire:** ai un plan scris, pe pași, în răspuns.

### Etapa 3: CONFIRMĂ

**Scop:** obținerea aprobării explicite a utilizatorului înainte de execuție.

**Acțiuni:**
- Prezintă planul utilizatorului.
- Evidențiază deciziile nebanale pe care le vei lua.
- Cere confirmare directă: „Confirm să execut acest plan?”
- Acceptă modificările propuse și reintri în ciclu dacă este necesar.

**Criteriu de ieșire:** confirmare explicită „da” de la utilizator.

### Etapa 4: EXECUTĂ

**Scop:** realizarea efectivă a sarcinii.

**Acțiuni:**
- Execută pașii din plan, în ordinea stabilită.
- Nu te abate de la plan fără motivare clară.
- Dacă apare o situație neprevăzută, oprește-te și revin la ciclul CLARIFICĂ.
- Documentează acțiunile pe măsură ce le execuți.

**Criteriu de ieșire:** toți pașii din plan sunt completați.

### Etapa 5: VALIDEAZĂ

**Scop:** verificarea corectitudinii și completitudinii.

**Acțiuni:**
- Re-citește toate fișierele modificate / create.
- Verifică coerența cu restul dosarului.
- Verifică că regulile din `REGULAMENT.md` sunt respectate.
- Actualizează `CHANGELOG.md`.
- Identifică efecte secundare (de exemplu: actualizează `TODO.md` dacă apar acțiuni noi).

**Criteriu de ieșire:** prezinți utilizatorului rezultatul și confirmi ce s-a făcut.

### Etapa 6: URMĂTOR

**Scop:** tranziția către sarcina următoare sau închiderea sesiunii.

**Acțiuni:**
- Întreabă utilizatorul dacă rezultatul este satisfăcător.
- Întreabă dacă urmează o sarcină nouă.
- Sau: sugerează următoarele acțiuni, pe baza `TODO.md`.
- Dacă se închide sesiunea, verifică că toate modificările sunt salvate și loggate.

## Excepții de la ciclu

Ciclul se poate scurtcircuita DOAR pentru:

1. **Întrebări informaționale simple** („care este vârsta pacientului?”) → răspuns direct.
2. **Căutări factuale simple** („ce înseamnă adenocarcinom?”) → căutare + răspuns.
3. **Corecții triviale** (typo-uri, formatări minore) → execută și anunță.

Pentru orice altceva (generare de documente, actualizare a `CONTEXT_MEDICAL.md`, modificări de configurare, cercetări complexe), ciclul este obligatoriu.

---

## Proceduri specifice

### Procedura A: Procesarea unui document medical nou

Când utilizatorul adaugă un document nou în `documente_sursa/` (scan al unui buletin de analize, bilet de trimitere, raport imagistic, etc.):

1. **Preluare:** confirmă cu utilizatorul locația fișierului și tipul așteptat.
2. **Extracție:** extrage textul / datele cheie. Pentru imagini, folosește OCR sau descriere vizuală.
3. **Structurare:** creează o fișă de sinteză a documentului în `interpretari/{data}_{descriere}.md`.
4. **Actualizare `CONTEXT_MEDICAL.md`:** adaugă informațiile noi în secțiunile corespunzătoare.
5. **Glosar:** dacă apar termeni noi, adaugă-i în `GLOSAR.md`.
6. **TODO:** dacă apar acțiuni (ex: „de întrebat medicul despre valoarea Y”), adaugă în `TODO.md`.
7. **CHANGELOG:** loghează operația cu data, fișierul procesat și modificările făcute.
8. **Confirmare:** prezintă utilizatorului sinteza documentului și modificările făcute.

### Procedura B: Pregătirea pentru un consult medical

Când utilizatorul anunță un consult care va avea loc:

1. **Identifică consultul:** ce specialist, când, unde, ce așteptări.
2. **Sinteză:** creează `comunicare_medici/{data}_{specialist}_sinteza.md` cu:
   - Datele pacientului (identificare)
   - Istoricul relevant pentru specialitatea consultată
   - Medicația curentă
   - Rezultatele recente de interes
   - Simptomele noi
3. **Întrebări:** creează `comunicare_medici/{data}_{specialist}_intrebari.md` cu lista întrebărilor prioritizate.
4. **Documente de luat:** creează o listă concretă de documente de adus la consult.
5. **După consult:** utilizatorul va reveni cu rezultatul; actualizezi dosarul conform procedurii A.

### Procedura C: Interpretarea unui rezultat de laborator sau imagistic

Când apare un rezultat nou (biopsie, CT, analize, etc.):

1. **Citire integrală:** citește TOT documentul, nu doar concluzia.
2. **Verificare termeni:** pentru orice termen medical necunoscut, `GLOSAR.md` întâi, apoi web search.
3. **Sinteză factuală:** creează un fișier `interpretari/{data}_{tip_investigatie}.md` cu:
   - Datele investigației (data, unitate, medic)
   - Citate directe din concluzie
   - Interpretare în termeni accesibili (fără speculații)
   - Întrebări generate pentru medic
   - Acțiuni declanșate (TODO)
4. **Actualizare `CONTEXT_MEDICAL.md`.**
5. **Nu speculezi asupra implicațiilor** — prezinți faptele, sugerezi întrebări, trimiți la medic.

### Procedura D: Cercetare pe o temă specifică

Când utilizatorul cere „caută informații despre X” sau „explică-mi Y”:

1. **Clarificare:** ce anume vrea să afle — generalități, date actuale, date specifice cazului?
2. **Identificare surse:** selectează 2-5 surse din `SURSE_MEDICALE.md` relevante pentru tema.
3. **Căutare web:** execută căutări structurate, preferând sursele autoritare.
4. **Sinteză:** structurează rezultatul într-un fișier în `cercetari/{data}_{tema}.md`.
5. **Citează sursele** pentru fiecare afirmație.
6. **Prezintă** utilizatorului — nu fișierul întreg, ci sinteza cu link către fișier pentru detalii.

### Procedura E: Actualizarea `CONTEXT_MEDICAL.md`

Acesta este fișierul-cheie care trebuie să fie întotdeauna actualizat. Orice modificare:

1. **Backup:** copiază versiunea curentă în `arhiva/CONTEXT_MEDICAL_{data}.md` DACĂ modificarea este majoră.
2. **Editează** fișierul curent.
3. **Actualizează** secțiunea „Ultima actualizare” cu data și descrierea.
4. **CHANGELOG:** loghează modificarea.

Pentru modificări mici (o linie, o valoare), nu creezi versiune arhivă — doar actualizezi și loghezi.

### Procedura F: Generarea unui document pentru download

Când utilizatorul cere un document Word (docx), PDF sau altă formă descărcabilă:

1. **Clarifică** destinatarul și scopul.
2. **Plan:** structura documentului, secțiunile incluse, tonul.
3. **Confirmă** cu utilizatorul structura.
4. **Generează** folosind instrumentele disponibile (python-docx, etc.).
5. **Validează** formatul (încarcă fișierul generat, verifică structura).
6. **Stochează** în `rapoarte_generate/` cu numele conform convenției.
7. **Versionează** — dacă există deja o versiune similară, creează `_v2.docx` și arhivează `_v1`.
8. **Prezintă** utilizatorului fișierul final.

---

## Utilizarea instrumentelor (ask_user_input)

### Principii

- Maximum 3 întrebări per rundă.
- Opțiuni clare, mutually exclusive când e posibil.
- Întrebări într-o singură direcție — nu întreba ceva ce ai putea determina singur.

### Când folosești ask_user_input

- Culegi informații medicale structurate de la pacient / familie.
- Confirmi preferințe de format (lungime, nivel de detaliu).
- Alegi între opțiuni de cercetare / structurare.

### Când NU folosești ask_user_input

- Întrebări deschise cu răspuns liber → scrie direct.
- Întrebări tehnice de cod → direct.
- Clarificări conversaționale simple → direct.

---

## Frecvența actualizărilor fișierelor

| Fișier | Frecvență |
|---|---|
| `CONTEXT_MEDICAL.md` | La fiecare informație nouă |
| `TODO.md` | La fiecare acțiune identificată / completată |
| `CHANGELOG.md` | La fiecare modificare în dosar |
| `GLOSAR.md` | Când apare un termen nou |
| `SURSE_MEDICALE.md` | Rar — doar când utilizatorul adaugă sau cere |
| `CLAUDE.md` / `REGULAMENT.md` / `WORKFLOW.md` | Doar cu aprobare explicită |

---

## Când te oprești și întrebi

Opri execuția și întreabă utilizatorul atunci când:

- Informația primită este incompletă sau contradictorie.
- O regulă din `REGULAMENT.md` este în tensiune cu cererea.
- Apare o situație medicală potențial urgentă.
- Ai nevoie să iei o decizie care afectează structura dosarului.
- Nu ești sigur ce metodologie (A, B, C, D, E, F) se aplică.

**Nu încerca să improvizezi.** Calitatea este mai importantă decât viteza.

---

**Ultima revizuire:** 17 aprilie 2026.
