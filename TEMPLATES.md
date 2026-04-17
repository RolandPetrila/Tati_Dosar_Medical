# TEMPLATES.md — Template-uri pentru documente noi

**Acest fișier conține template-uri reutilizabile pentru cele mai frecvente tipuri de documente care se generează în timpul gestionării dosarului.**

Copiază template-ul relevant, completează cu datele reale, salvează în folderul potrivit conform `STRUCTURA_PROIECT.md`.

---

## Template T1: Interpretare document medical

**Destinație:** `interpretari/{YYYY-MM-DD}_{tip}.md`

```markdown
# Interpretare: {Tip document}

**Data document:** {YYYY-MM-DD}
**Data interpretării:** {YYYY-MM-DD}
**Sursă:** `documente_sursa/{folder}/{fisier}`
**Tip:** {endoscopie / CT / biopsie / analize / etc.}
**Medic emitent:** {Dr. Nume, specialitate, unitate}

## 1. Date factuale extrase

{Citate directe relevante din document, păstrând formularea exactă}

## 2. Termeni medicali

| Termen | Explicație |
|---|---|
| {termen 1} | {explicație accesibilă} |
| {termen 2} | {explicație accesibilă} |

Termenii noi vor fi adăugați și în `GLOSAR.md`.

## 3. Interpretare

{Explicație în termeni accesibili a ceea ce conține documentul, fără speculații peste ceea ce este scris explicit.}

## 4. Evaluare calibrată

{Dacă documentul permite o evaluare clinică — cu nivel de încredere clar specificat. Dacă nu, marchează ca „nu permite evaluare fără informații suplimentare”.}

## 5. Impact asupra stării curente

{Cum modifică acest document starea documentată în `CONTEXT_MEDICAL.md`.}

## 6. Întrebări generate pentru medic

- {întrebare 1}
- {întrebare 2}

## 7. Acțiuni declanșate

- [ ] {acțiune 1}
- [ ] {acțiune 2}

Acțiunile vor fi transferate în `TODO.md`.

## 8. Note

{Observații suplimentare, contexte neclare, lucruri de urmărit.}

---

*Acest document este o interpretare preliminară și nu înlocuiește evaluarea unui specialist.*
```

---

## Template T2: Sinteză pentru consult medical

**Destinație:** `comunicare_medici/{YYYY-MM-DD}_{specialist}_sinteza.md`

```markdown
# Sinteză pentru consult — {Specialist}

**Pacient:** Petrilă Viorel-Mihai (n. 18.05.1959)
**Data consultului:** {YYYY-MM-DD, ora}
**Medic:** {Dr. Nume, unitate}
**Motivul consultului:** {concis}

## 1. Sinteză în 3 rânduri

{Rezumat maxim 3 linii pentru preluare rapidă.}

## 2. Istoric relevant pentru această specialitate

{Extras din `CONTEXT_MEDICAL.md`, filtrat pentru relevanța specialității.}

## 3. Investigații recente

| Data | Investigație | Concluzie principală |
|---|---|---|
| {data} | {tip} | {concluzie scurtă} |

## 4. Simptome actuale

{Listă concisă, cronologic.}

## 5. Medicație curentă

{Listă cu doze, cu semnalarea specifică a medicației relevante pentru specialist.}

## 6. Antecedente personale importante

- {antecedent 1}
- {antecedent 2}

## 7. Alergii

{Enumeră sau „Nicio alergie cunoscută”.}

## 8. Ce știe pacientul despre diagnosticul suspectat

{Calibrarea informației oferite pacientului.}

## 9. Documente atașate / de adus la consult

- {document 1}
- {document 2}

---

*Document pregătit pentru consult. Ultima actualizare: {data}.*
```

---

## Template T3: Întrebări pentru consult medical

**Destinație:** `comunicare_medici/{YYYY-MM-DD}_{specialist}_intrebari.md`

```markdown
# Întrebări pentru consult — {Specialist}

**Pacient:** Petrilă Viorel-Mihai
**Data consultului:** {YYYY-MM-DD}
**Medic:** {Dr. Nume}

## Prioritate 1 — Obligatoriu de întrebat

1. {întrebare critică 1}
2. {întrebare critică 2}
3. {întrebare critică 3}

## Prioritate 2 — Dacă e timp

1. {întrebare importantă 1}
2. {întrebare importantă 2}

## Prioritate 3 — Nice to know

1. {întrebare utilă 1}

## Observații

- Răspunsurile se notează aici sau pe un document separat.
- Dacă o întrebare nu primește răspuns, transferă în `TODO.md` pentru următorul consult.

---

## Spațiu pentru răspunsurile medicului (de completat DURING/POST consult)

### Răspuns la Î1
{...}

### Răspuns la Î2
{...}
```

---

## Template T4: Raport cercetare pe temă

**Destinație:** `cercetari/{YYYY-MM-DD}_{tema}.md`

```markdown
# Cercetare: {Tema}

**Data:** {YYYY-MM-DD}
**Scop:** {de ce se face această cercetare — ce întrebare / decizie sprijină}
**Context:** {legătura cu starea pacientului, dacă există}

## 1. Sinteză executivă

{3-5 puncte cheie, utile pentru preluare rapidă.}

## 2. Detaliul cercetării

{Corpul cercetării, structurat pe secțiuni logice.}

### 2.1 {Subsecțiune 1}

{Conținut cu citări.}

### 2.2 {Subsecțiune 2}

{Conținut cu citări.}

## 3. Aplicabilitate pentru cazul nostru

{Cum se aplică informațiile la situația specifică a pacientului — fără a pretinde diagnosticul sau prescripția.}

## 4. Întrebări deschise

- {întrebare rămasă nesoluționată 1}
- {întrebare rămasă nesoluționată 2}

## 5. Surse citate

1. {Sursă 1} — {autoritate}, {data}, {link}, (accesat {data}).
2. {Sursă 2} — ...

## 6. Nivel de încredere

{Evaluare a calității informațiilor — bazat pe numărul și calitatea surselor.}

---

*Cercetare informativă. Nu constituie recomandare medicală.*
```

---

## Template T5: Jurnal simptome (intrare zilnică)

**Destinație:** `interpretari/jurnal_simptome/{YYYY-MM}.md` (un fișier pe lună)

```markdown
# Jurnal simptome — {Luna, Anul}

## {YYYY-MM-DD}

**Starea generală (1-10):** {valoare}
**Greutate:** {kg}
**Apetit (1-10):** {valoare}
**Energie (1-10):** {valoare}
**Somn:** {ore, calitate}

### Parametri
- Tensiune: {sistolica/diastolica mmHg}, puls: {bpm}
- Glicemie à jeun: {mg/dL}
- Temperatură: {°C} {moment}

### Simptome observate

| Simptom | Intensitate (1-10) | Durata | Context |
|---|---|---|---|
| {simptom} | {valoare} | {durata} | {context} |

### Alimentație
- Mic dejun: {...}
- Prânz: {...}
- Cină: {...}
- Observații: {aversiuni, dificultăți}

### Medicație
- [x] Toate medicamentele uzuale administrate la ore uzuale
- [ ] Modificări (descriere): {...}

### Alte observații

{Comportament atipic, oboseală neobișnuită, simptome noi etc.}

---

## {YYYY-MM-DD+1}

...
```

---

## Template T6: Intrare în CHANGELOG

**Format pentru o intrare nouă în `CHANGELOG.md`:**

```markdown
## {YYYY-MM-DD HH:MM}

**Tip:** {ADAUGARE / MODIFICARE / CORECTIE / ARHIVARE}
**Fișier(e) afectat(e):** `{fisier1}`, `{fisier2}`
**Descriere:** {Ce s-a modificat, concret.}
**Motiv:** {De ce s-a făcut modificarea.}
**Sursă informație (dacă aplicabil):** {document / consult / cercetare}
**Făcut de:** {utilizator / Claude Code}

---
```

---

## Template T7: Acțiune nouă în TODO

**Format pentru o intrare nouă în `TODO.md`:**

```markdown
### [{prioritate: P0 / P1 / P2 / P3}] {Titlu scurt}

**Context:** {de ce este necesar}
**Deadline:** {YYYY-MM-DD sau „continuu”}
**Sub-task-uri:**
- [ ] {pas 1}
- [ ] {pas 2}

**Generat din:** {fișier sau eveniment care a generat acțiunea}
**Data creării:** {YYYY-MM-DD}
```

**Scala priorităților:**
- **P0** — critic, de efectuat imediat (acțiuni legate de siguranță medicală, programări urgente)
- **P1** — important, de efectuat în câteva zile
- **P2** — util, de efectuat în săptămânile următoare
- **P3** — util pe termen mediu

---

## Template T8: Adaugare termen nou în GLOSAR

**Format pentru o intrare nouă în `GLOSAR.md`:**

```markdown
### {Termen}

**Definiție:** {explicație accesibilă în 1-3 fraze}

**Context medical:** {în ce situații apare termenul, ce implicații are}

**Întâlnit în:** `{fișier}` ({data})

**Sursă definiție:** {opțional — dacă definiția e luată dintr-o sursă specifică}
```

---

## Template T9: Scrisoare oficială pentru medic

**Destinație:** `comunicare_medici/{YYYY-MM-DD}_scrisoare_{destinatar}.md`

```markdown
# Scrisoare medicală

**Către:** {Dr. Nume, titlu, unitate}
**De la:** {Petrilă Viorel-Mihai / reprezentant legal}
**Data:** {YYYY-MM-DD}
**Subiect:** {Scurt rezumat al scopului}

---

Stimate / Stimată {Dr. Nume},

{Introducere — 1-2 fraze care descriu cine este pacientul și scopul scrisorii.}

## Istoric medical relevant

{Paragraf factual cu istoricul relevant pentru această comunicare.}

## Situația actuală

{Descrierea stării curente și a problemei care motivează scrisoarea.}

## Solicitare / întrebare

{Ceea ce se cere — consult, a doua opinie, trimitere la alt specialist, clarificare asupra unui aspect.}

## Documente atașate

- {document 1}
- {document 2}

## Date de contact

{Contact pentru răspuns.}

Cu respect,
{Nume}

---

*Atașamente listate în pachet separat.*
```

---

## Template T10: Pregătire procedură invazivă

**Destinație:** `comunicare_medici/{YYYY-MM-DD}_pregatire_{procedura}.md`

```markdown
# Pregătire pentru {procedura} — {Data procedurii}

**Pacient:** Petrilă Viorel-Mihai
**Data programării:** {YYYY-MM-DD, ora}
**Unitate:** {Nume}

## Cu 7 zile înainte

- [ ] {acțiune}

## Cu 3 zile înainte

- [ ] {acțiune}

## Cu 48h înainte

- [ ] **OPRIRE METFORMIN** (dacă procedura implică contrast iodat)
- [ ] {acțiune}

## Cu 24h înainte

- [ ] {acțiune}

## În ziua procedurii — dimineață

- [ ] Repaus alimentar ({interval})
- [ ] {acțiune}

## De dus la procedură

- [ ] Buletinul
- [ ] Cardul de sănătate
- [ ] Biletul de trimitere original
- [ ] Analize recente
- [ ] {alte documente}

## Reluare medicație

- {când și ce se reia după procedură}

## Ce se așteaptă ca rezultat

- Imediat: {informații pe loc}
- În 24-48h: {raport scris}
- Mai târziu: {alte rezultate cu timp de procesare mai lung}
```

---

## Note privind folosirea template-urilor

- Template-urile sunt **puncte de plecare**, nu structuri rigide. Adaptează-le contextului.
- Dacă un câmp nu se aplică, elimină-l în loc să lași placeholder gol.
- Dacă ai nevoie de o structură nouă care nu e aici, propune un template nou pentru a fi adăugat la acest fișier.

---

**Ultima revizuire:** 17 aprilie 2026.
