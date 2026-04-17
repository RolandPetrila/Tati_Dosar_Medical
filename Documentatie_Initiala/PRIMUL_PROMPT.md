# PRIMUL_PROMPT.md — Ghid pentru prima sesiune Claude Code

**Acest fișier este pentru tine (Roland), NU pentru Claude Code. Conține șabloane pentru primul mesaj pe care îl trimiți lui Claude Code după ce ai deschis folderul.**

---

## Înainte de prima sesiune

1. Verifică că folderul conține toate fișierele de configurare:
   - `README.md`, `CLAUDE.md`, `START.md`, `REGULAMENT.md`, `WORKFLOW.md`
   - `STRUCTURA_PROIECT.md`, `CONTEXT_MEDICAL.md`, `BAZA_CUNOSTINTE.md`
   - `SURSE_MEDICALE.md`, `TEMPLATES.md`, `GLOSAR.md`
   - `TODO.md`, `CHANGELOG.md`

2. Asigură-te că ești în folderul corect și că Claude Code pornește cu opțiunea **Opus** și **max effort** (`--model opus` sau setarea echivalentă din VS Code).

3. Creează subfolderele goale (Claude Code le va popula):
   ```
   mkdir -p documente_sursa/{01_identitate,02_cardiologie_2012,03_hernie_anterior,04_helicobacter_2024-05-30,05_hernie_2025-11,06_endoscopie_2026-04-17,07_biopsie_2026-04,08_CT_stadializare_2026,09_analize_laborator,10_retete,11_consulturi,99_altele}
   mkdir -p interpretari/jurnal_simptome interpretari/cronologic
   mkdir -p rapoarte_generate/versiuni_anterioare
   mkdir -p cercetari comunicare_medici
   mkdir -p arhiva/versiuni_config
   ```

4. Inițializează Git (recomandat):
   ```
   git init
   git add .
   git commit -m "Inițializare dosar medical"
   ```

---

## Primul prompt — Template

Copiază și trimite ca prim mesaj lui Claude Code:

```
Salut. Citește în ordine: README.md, CLAUDE.md, START.md, REGULAMENT.md, 
CONTEXT_MEDICAL.md, WORKFLOW.md, apoi TODO.md și ultimele intrări din 
CHANGELOG.md. După ce ai citit totul, confirmă că ai înțeles contextul 
conform procedurii din START.md (sinteză stare curentă, acțiuni deschise, 
gata de lucru).
```

Claude Code va răspunde conform protocolului din `START.md` cu:
- Confirmare că a citit fișierele
- Sinteza stării curente în 2-3 rânduri
- Lista acțiunilor deschise
- „Aștept instrucțiuni”

Dacă nu răspunde conform protocolului, reamintește-i explicit:
```
Te rog să urmezi protocolul descris în START.md, secțiunea „Confirmarea către utilizator”.
```

---

## Al doilea prompt — Stabilire plan de lucru

După ce Claude Code a confirmat înțelegerea, stabilește direcția de lucru:

### Opțiunea A — Construire bază de date din ce avem

```
Bun. Avem deja câteva documente generate de Claude.ai, și anume:
- dosar_medical_petrila_viorel-mihai.docx
- fisa_colectare_informatii_petrila.docx
- 00_CONTEXT_MEDICAL_TATI.md

Le voi adăuga în folderul documente_sursa/99_altele/ sau în rapoarte_generate/
le voi adăuga. Analizează-le integral și integrează informațiile din ele în 
baza noastră de cunoștințe conform procedurii A din WORKFLOW.md. La final, 
raportează ce s-a integrat și ce rămâne de completat.
```

### Opțiunea B — Procesare documente sursă

```
În documente_sursa/ am plasat [descriere fișiere noi]. Procesează-le conform 
procedurii A din WORKFLOW.md: extrage informațiile, creează fișierele de 
interpretare în interpretari/, actualizează CONTEXT_MEDICAL.md, TODO.md, 
GLOSAR.md și CHANGELOG.md. Prezintă-mi sinteza finală.
```

### Opțiunea C — Cercetare specifică

```
Aș vrea să cercetezi [tema] folosind procedura D din WORKFLOW.md. Folosește 
doar surse de nivel 1-3 din SURSE_MEDICALE.md. Generează fișierul de 
cercetare în cercetari/ și prezintă-mi sinteza executivă.
```

### Opțiunea D — Pregătire consult

```
Avem un consult programat cu [specialist] pe [data]. Pregătește pachetul 
complet conform procedurii B din WORKFLOW.md: sinteză în 
comunicare_medici/, listă de întrebări prioritizate, listă de documente 
de dus. Folosește template-urile T2 și T3.
```

---

## Exemple de prompt-uri ulterioare

### După primirea unui rezultat

```
Primit [tip rezultat]. L-am plasat în [cale]. 
Procesează conform procedurii C din WORKFLOW.md. 
La final vreau:
1. Interpretarea în termeni accesibili
2. Actualizarea CONTEXT_MEDICAL.md
3. Lista întrebărilor generate pentru medic
4. Actualizarea TODO.md cu acțiunile declanșate
```

### După un consult medical

```
Ieri am fost la consult cu [medicul]. Uite ce s-a discutat:
[descriere liberă a consultului]

Procesează conform procedurii B (post-consult) din WORKFLOW.md.
Structurează informațiile și integrează-le în dosar.
```

### Pentru o zi de rutină

```
Raport săptămânal: verifică coerența dosarului, identifică informații 
învechite, propune 3 acțiuni prioritare pentru săptămâna următoare.
```

### Când pacientul raportează un simptom nou

```
Tata raportează [simptom]: [detalii — când a început, caracteristici].
Procesează conform procedurii P4 din BAZA_CUNOSTINTE.md.
```

---

## Când Claude Code face greșeli

### Dacă inventează informații

```
OPREȘTE. Afirmația [X] nu are sursă verificabilă. 
Regula 2 din REGULAMENT.md, secțiunea 1 este clară: „NU inventa”.
Revocă afirmația. Actualizează CHANGELOG.md cu o intrare CORECTIE.
Apoi continuă cu informația corectă sau marchează ca „de verificat”.
```

### Dacă sare peste ciclul CLARIFICĂ → PLANIFICĂ → CONFIRMĂ

```
Oprește execuția. Urmează ciclul complet din WORKFLOW.md. Fă plan, 
prezintă-mi planul, așteaptă confirmarea mea.
```

### Dacă dă opinie clinică sau „diagnostic”

```
Depășești limitele din REGULAMENT.md, secțiunea 1.1.
Nu diagnostici. Retrage afirmația. Reformulează ca ipoteză preliminară 
cu nivel de încredere specificat, și menționează că diagnosticul 
aparține medicilor.
```

### Dacă folosește limbaj catastrofic sau anxiogen

```
Reformulează fără limbaj alarmist. Prezintă faptele calibrate, cu 
incertitudinile specificate. Regula 1.1 (NU panica) din REGULAMENT.md.
```

---

## Sfaturi de eficiență

### Pentru sesiuni lungi

- Împarte sarcinile mari în faze. Confirmă fiecare fază înainte de a trece la următoarea.
- La fiecare ~30 min de lucru, cere un status update.
- Salvează / commit-ează după fiecare fază majoră.

### Pentru prompt-uri clare

- Un prompt, o sarcină principală.
- Dacă ai multiple cereri, numerotează-le.
- Dacă cererea este complexă, atașează un rezumat al contextului (chiar dacă ar trebui să fie deja încărcat).

### Pentru verificări

- La sfârșitul fiecărei sesiuni, cere un „raport de sesiune”:
  ```
  Raport de sesiune: ce s-a modificat, ce fișiere sunt noi, 
  ce acțiuni sunt acum în TODO, ce urmează.
  ```

### Pentru backup

- După fiecare sesiune importantă, fă git commit.
- Săptămânal, sincronizează cu cloud privat.
- Lunar, backup pe disk extern.

---

## Notă finală

Acest fișier rămâne pentru referință. Nu se introduce în context-ul lui Claude Code la fiecare sesiune — este un aide-memoire pentru tine. Poți să-l ignori complet odată ce ești confortabil cu fluxul de lucru.
