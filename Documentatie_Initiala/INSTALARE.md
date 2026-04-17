# INSTALARE.md — Ghid de instalare și inițializare

**Instrucțiuni pas cu pas pentru setarea inițială a folderului pe laptop și pregătirea pentru lucrul cu Claude Code.**

---

## Pasul 1 — Crearea folderului principal

**[ACTUALIZARE 2026-04-18]** Locația reală a proiectului pe laptopul utilizatorului:

```
C:\Users\ALIENWARE\Desktop\Roly\.Tati\
```

Folderul `.Tati\` este sincronizat automat prin Google Drive către:

```
G:\My Drive\Roly\.Tati\
```

Versiunea de referință pentru lucru este Desktop (canonical); Drive-ul este doar target de sincronizare.

**Notă:** recomandarea originală din kit (nu pe Desktop, folder privat) este ignorată conștient — folderul Desktop este localizat într-un director părinte `.Tati\` (prefix punct, tratat ca ascuns pe unele sisteme), iar sincronizarea Drive oferă backup automat.

Istoric (exemplu generic, păstrat pentru referință):

```
C:\Users\roland\Documents\Dosar_Medical_Tata\
```

sau pe Linux/Mac:

```
~/Documents/Dosar_Medical_Tata/
```

---

## Pasul 2 — Copierea fișierelor din kit

Copiază toate fișierele `.md` din acest set (primit ca download) direct în folderul principal.

**Fișierele obligatorii:**

- `README.md`
- `CLAUDE.md`
- `START.md`
- `REGULAMENT.md`
- `WORKFLOW.md`
- `STRUCTURA_PROIECT.md`
- `CONTEXT_MEDICAL.md`
- `BAZA_CUNOSTINTE.md`
- `SURSE_MEDICALE.md`
- `TEMPLATES.md`
- `GLOSAR.md`
- `TODO.md`
- `CHANGELOG.md`
- `PRIMUL_PROMPT.md` (pentru referință, nu este citit de Claude Code)
- `INSTALARE.md` (acest fișier)

---

## Pasul 3 — Crearea subfolderelor

Deschide un terminal (PowerShell pe Windows sau Terminal pe Mac/Linux), navighează în folder și execută:

**Pe Windows (PowerShell):**

```powershell
cd C:\Users\roland\Documents\Dosar_Medical_Tata

mkdir documente_sursa\01_identitate
mkdir documente_sursa\02_cardiologie_2012
mkdir documente_sursa\03_hernie_anterior
mkdir documente_sursa\04_helicobacter_2024-05-30
mkdir documente_sursa\05_hernie_2025-11
mkdir documente_sursa\06_endoscopie_2026-04-17
mkdir documente_sursa\07_biopsie_2026-04
mkdir documente_sursa\08_CT_stadializare_2026
mkdir documente_sursa\09_analize_laborator
mkdir documente_sursa\10_retete
mkdir documente_sursa\11_consulturi
mkdir documente_sursa\99_altele

mkdir interpretari\jurnal_simptome
mkdir interpretari\cronologic

mkdir rapoarte_generate\versiuni_anterioare

mkdir cercetari
mkdir comunicare_medici

mkdir arhiva\versiuni_config
```

**Pe Linux/Mac (Terminal):**

```bash
cd ~/Documents/Dosar_Medical_Tata

mkdir -p documente_sursa/{01_identitate,02_cardiologie_2012,03_hernie_anterior,04_helicobacter_2024-05-30,05_hernie_2025-11,06_endoscopie_2026-04-17,07_biopsie_2026-04,08_CT_stadializare_2026,09_analize_laborator,10_retete,11_consulturi,99_altele}
mkdir -p interpretari/{jurnal_simptome,cronologic}
mkdir -p rapoarte_generate/versiuni_anterioare
mkdir -p cercetari comunicare_medici
mkdir -p arhiva/versiuni_config
```

---

## Pasul 4 — Plasarea documentelor existente

Copiază în folder documentele deja generate pe Claude.ai:

### În `rapoarte_generate/`:

- `dosar_medical_petrila_viorel-mihai.docx`
- `fisa_colectare_informatii_petrila.docx`

### În `documente_sursa/01_identitate/`:

- `2023-06-12_carte_identitate.pdf` (redenumire de la `C_I__-_Petrila_Viorel.pdf`)

### În `documente_sursa/06_endoscopie_2026-04-17/`:

- `2026-04-17_bilet_trimitere_CT.jpg` (bilet BCTAP 0631727)

### În `documente_sursa/99_altele/`:

- `00_CONTEXT_MEDICAL_TATI.md` (generat inițial pe Claude.ai — poate fi folosit pentru completări)

---

## Pasul 5 — Inițializare Git (recomandat)

Git permite versionarea automată și backup pe GitHub privat.

### Inițializare locală:

```bash
cd Dosar_Medical_Tata
git init
git add .
git commit -m "Inițializare dosar medical — 17 aprilie 2026"
```

### Opțional — backup pe GitHub privat:

1. Creează un repository **privat** pe GitHub (numit, de exemplu, `dosar-medical-tata`).
2. Conectează repository-ul local:
   ```bash
   git remote add origin https://github.com/{username}/dosar-medical-tata.git
   git branch -M main
   git push -u origin main
   ```

**ATENȚIE:** repository-ul MUSTĂ fie PRIVAT, nu public. Datele medicale sunt sensibile.

---

## Pasul 6 — Configurare sincronizare cloud

Pentru backup automat, folosește un serviciu cloud privat:

### Google Drive / OneDrive / Dropbox

- Plasează folderul `Dosar_Medical_Tata` în folderul sincronizat al serviciului (ex: `Google Drive\Dosar_Medical_Tata`).
- Verifică că sincronizarea este activă.
- Serviciul va menține automat o copie în cloud, cu versiuni anterioare accesibile.

### Verificări de securitate:

- Contul cloud are autentificare în doi pași activată.
- Folderul NU este partajat cu nimeni în mod automat.
- Accesul este limitat la utilizatorul principal.

---

## Pasul 7 — Deschiderea în VS Code

1. Deschide VS Code.
2. `File → Open Folder...` și selectează `Dosar_Medical_Tata`.
3. În partea stângă, vei vedea întreaga structură de fișiere.

---

## Pasul 8 — Inițializarea sesiunii Claude Code

### Pornirea Claude Code:

În terminalul integrat VS Code (`Ctrl + ` ` backtick), pornește Claude Code cu modelul Opus:

```bash
claude
```

Apoi selectează modelul **Claude Opus** și nivelul **Max effort** din setările Claude Code (vezi documentația Claude Code pentru comenzile specifice).

### Primul mesaj către Claude Code:

Copiază template-ul din `PRIMUL_PROMPT.md`, secțiunea „Primul prompt — Template”, și trimite-l.

---

## Pasul 9 — Test de funcționare

După primul răspuns al lui Claude Code, verifică:

1. ✅ A citit toate fișierele de configurare (a menționat explicit)
2. ✅ A dat sinteză corectă a stării curente (pacientul, diagnosticul suspectat)
3. ✅ A listat acțiunile din TODO.md
4. ✅ A așteptat instrucțiuni („aștept instrucțiuni”)

Dacă toate bifele sunt ok, setup-ul este corect. Dacă nu, reamintește-i explicit să urmeze `START.md`.

---

## Pasul 10 — Rutină de lucru recomandată

### Zilnic (1-2 minute)

- Verificare mesaje / rapoarte noi de la medici.
- Dacă apar documente noi, plasează-le în folderele potrivite.

### La fiecare document nou

- Deschide VS Code, pornește Claude Code.
- Primul mesaj: „Am adăugat [fișier] în [cale]. Procesează-l conform procedurii A din WORKFLOW.md.”
- După procesare, verifică sinteza și ratifică.
- Git commit: `git add . && git commit -m "Adăugare {document}"`

### Săptămânal

- Sesiune de verificare: „Raport săptămânal — verifică coerența dosarului, propune acțiuni.”
- Git push către GitHub privat (dacă folosit).
- Backup manual pe disk extern (lunar).

### Înainte de fiecare consult

- Sesiune de pregătire: „Pregătește pachetul complet pentru consultul de mâine cu [medic] conform procedurii B.”
- Printează / salvează documentele pregătite pe telefon.
- Ia cu tine la consult.

### După fiecare consult

- Sesiune de integrare: „Consultul a fost azi. Uite ce s-a discutat: [...]. Integrează în dosar.”

---

## Troubleshooting

### Claude Code nu citește fișierele

Verifică că ești în folderul corect: în terminal, `pwd` (Linux/Mac) sau `pwd` în PowerShell trebuie să arate calea către `Dosar_Medical_Tata`.

### Claude Code dă răspunsuri în engleză

Reamintește explicit: „Regula din REGULAMENT.md, secțiunea 2.1: răspunsurile sunt în română.”

### Claude Code sare peste proceduri

Reamintește explicit: „Urmează `WORKFLOW.md`. Ciclul complet CLARIFICĂ → PLANIFICĂ → CONFIRMĂ → EXECUTĂ → VALIDEAZĂ → URMĂTOR.”

### Claude Code face afirmații fără surse

Reamintește explicit: „Regula din `REGULAMENT.md`, secțiunea 1.2: cifre și protocoale cu sursă verificabilă.”

---

## Verificare finală setup

Folder `Dosar_Medical_Tata` conține:

```
✅ 15 fișiere .md de configurare (nivel rădăcină)
✅ 12 subfoldere în documente_sursa/
✅ 2 subfoldere în interpretari/
✅ 1 subfolder în rapoarte_generate/
✅ folder cercetari/
✅ folder comunicare_medici/
✅ 1 subfolder în arhiva/
✅ Git inițializat (.git/)
✅ Documente existente plasate în locațiile corecte
✅ Sincronizare cloud activă
```

---

## Resurse utile

- Documentație Claude Code: https://docs.claude.com/en/docs/claude-code
- Documentație Git: https://git-scm.com/doc
- Tutorial Markdown (pentru editarea manuală a fișierelor): https://www.markdownguide.org/cheat-sheet/

---

**Ultima revizuire:** 17 aprilie 2026.
