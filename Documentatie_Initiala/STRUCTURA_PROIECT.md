# STRUCTURA_PROIECT.md — Organizarea folderelor

**Acest fișier descrie structura completă a dosarului, convențiile de denumire și regulile pentru adăugarea de fișiere noi.**

## Structura folderelor

```
dosar_medical_petrila/
│
├── README.md                         Vedere de ansamblu
├── CLAUDE.md                         Instrucțiuni principale pentru Claude Code
├── START.md                          Protocol inițiere sesiune
├── REGULAMENT.md                     Reguli stricte de operare
├── WORKFLOW.md                       Metodologie de lucru
├── STRUCTURA_PROIECT.md              Acest fișier
├── CONTEXT_MEDICAL.md                Starea medicală curentă (fișier central)
├── BAZA_CUNOSTINTE.md                Proceduri de mentinere a bazei de cunoștințe
├── SURSE_MEDICALE.md                 Surse medicale autoritare
├── TEMPLATES.md                      Template-uri pentru documente noi
├── GLOSAR.md                         Termeni medicali cu definiții
├── TODO.md                           Acțiuni curente
├── CHANGELOG.md                      Istoricul modificărilor
│
├── documente_sursa/                  Scanurile și fișierele originale
│   ├── 01_identitate/
│   │   └── 2023-06-12_carte_identitate.pdf
│   │
│   ├── 02_cardiologie_2012/          Istoric stent
│   │
│   ├── 03_hernie_anterior/           Prima operație de hernie
│   │
│   ├── 04_helicobacter_2024-05-30/   Episod H. pylori
│   │
│   ├── 05_hernie_2025-11/            Hernia din noiembrie 2025
│   │
│   ├── 06_endoscopie_2026-04-17/     Endoscopia + colonoscopia
│   │   └── 2026-04-17_bilet_trimitere_CT.jpg
│   │
│   ├── 07_biopsie_2026-04/           Rezultat biopsie (de primit)
│   │
│   ├── 08_CT_stadializare_2026/      CT de stadializare (de primit)
│   │
│   ├── 09_analize_laborator/         Toate analizele cronologic
│   │   └── YYYY-MM-DD_tip_analiza.pdf
│   │
│   ├── 10_retete/                    Rețete curente și istorice
│   │
│   ├── 11_consulturi/                Scrisori medicale, bilete consult
│   │
│   └── 99_altele/                    Orice alt document
│
├── interpretari/                     Sintezele / interpretările documentelor
│   ├── 2026-04-14_ecografie.md
│   ├── 2026-04-17_endoscopie.md
│   └── cronologic/
│       └── toate_evenimentele.md     Linie de timp unificată
│
├── rapoarte_generate/                Documente produse pentru uz extern
│   ├── dosar_medical_2026-04-17_v1.docx
│   ├── fisa_colectare_informatii_2026-04-17_v1.docx
│   └── versiuni_anterioare/
│       └── (versiunile vechi ale rapoartelor, arhivate)
│
├── cercetari/                        Cercetări pe teme medicale specifice
│   ├── 2026-04-17_carcinom_esofagian_tratament.md
│   ├── 2026-04-18_stadializare_TNM.md
│   └── ...
│
├── comunicare_medici/                Documente pregătite pentru medici
│   ├── 2026-04-18_oncolog_sinteza.md
│   ├── 2026-04-18_oncolog_intrebari.md
│   └── ...
│
├── arhiva/                           Versiuni anterioare ale fișierelor
│   ├── CONTEXT_MEDICAL_v1_2026-04-17.md
│   └── versiuni_config/              Modificările fișierelor de configurare
│
└── .git/                             Git pentru versionare (recomandat)
```

## Convenții de denumire

### Fișiere de configurare și structură
**Format:** `MAJUSCULE.md`
**Exemple:** `CLAUDE.md`, `REGULAMENT.md`, `CONTEXT_MEDICAL.md`

### Fișiere de date generate
**Format:** `snake_case.md`
**Exemple:** `carcinom_esofagian_tratament.md`, `intrebari_oncolog.md`

### Documente sursă (scanuri, PDF-uri)
**Format:** `YYYY-MM-DD_descriere_scurta.ext`
**Exemple:**
- `2026-04-17_bilet_trimitere_CT.pdf`
- `2024-05-30_bilet_externare.pdf`
- `2012-03-15_raport_coronarografie.pdf`

Dacă data exactă nu se cunoaște, folosește `YYYY-MM_descriere.ext` sau `YYYY_descriere.ext`.

### Rapoarte generate pentru download
**Format:** `tip_raport_YYYY-MM-DD_vN.ext`
**Exemple:**
- `dosar_medical_2026-04-17_v1.docx`
- `sinteza_pentru_oncolog_2026-04-20_v1.docx`

### Versiuni arhivate
**Format:** `{nume_original}_{data_arhivării}.{ext}`
**Exemple:**
- `CONTEXT_MEDICAL_2026-04-17.md`
- `dosar_medical_2026-04-17_v1.docx` (în `rapoarte_generate/versiuni_anterioare/`)

## Reguli pentru organizarea documentelor sursă

### Principii

1. **Un document fizic = un fișier digital.** Scanurile multi-pagină se salvează ca PDF, nu ca imagini separate.
2. **Denumire descriptivă.** Nu `IMG_20260417_105234.jpg` — redenumește la `2026-04-17_bilet_CT.jpg`.
3. **Subfolder clar.** Fiecare episod medical are propriul subfolder.
4. **Data prima.** Formatul `YYYY-MM-DD_` la începutul numelui asigură sortarea cronologică.

### Ce merge în ce folder

| Tip document | Folder |
|---|---|
| CI, card sănătate | `01_identitate/` |
| Documente stent 2012 | `02_cardiologie_2012/` |
| Prima operație de hernie | `03_hernie_anterior/` |
| Episod H. pylori 2024 | `04_helicobacter_2024-05-30/` |
| Hernia noiembrie 2025 | `05_hernie_2025-11/` |
| Endoscopie, colonoscopie, bilete aprilie 2026 | `06_endoscopie_2026-04-17/` |
| Rezultat biopsie (când vine) | `07_biopsie_2026-04/` |
| CT de stadializare (raport + CD DICOM) | `08_CT_stadializare_2026/` |
| Analize de laborator, în orice moment | `09_analize_laborator/` |
| Rețete | `10_retete/` |
| Scrisori de consult, bilete de trimitere | `11_consulturi/` |
| Orice altceva | `99_altele/` |

### Pentru consulturi viitoare

Pe măsură ce apar consulturi noi (oncolog, etc.), se creează subfoldere noi:
- `12_oncolog_YYYY-MM/`
- `13_tratament_YYYY/`
- etc.

## Reguli pentru interpretări și cercetări

### `interpretari/`

Pentru fiecare document sursă important se creează un fișier de interpretare cu același prefix de dată:

- Document sursă: `documente_sursa/06_endoscopie_2026-04-17/2026-04-17_buletin_endoscopie.pdf`
- Interpretare: `interpretari/2026-04-17_endoscopie.md`

Fișierul de interpretare conține:
- Citate factuale din document
- Explicații ale termenilor medicali
- Interpretare calibrată
- Întrebări generate pentru medic
- Acțiuni declanșate

### `cercetari/`

Pentru teme de studiu sau investigație generală (nu legate de un document specific):

- `2026-04-17_carcinom_esofagian_tratament.md`
- `2026-04-18_centre_oncologice_timisoara.md`

## Reguli pentru versionare

### Ce se versionează

| Categorie | Versionare | Metodă |
|---|---|---|
| Fișiere de configurare (CLAUDE.md, REGULAMENT.md) | La fiecare modificare | Arhivă în `arhiva/versiuni_config/` |
| `CONTEXT_MEDICAL.md` | La modificări majore | Arhivă în `arhiva/` |
| Rapoarte generate (docx, pdf) | La fiecare versiune nouă | Sufix `_vN`, vechiul în `rapoarte_generate/versiuni_anterioare/` |
| Documente sursă | Imutabile | Nu se rescriu niciodată |
| Interpretări, cercetări | În general imutabile | Dacă trebuie actualizate, se creează versiune nouă cu sufix `_v2` |

### Git — recomandare

Întreg folderul se ține sub control Git. Fiecare modificare semnificativă se commit-ează cu mesaj descriptiv:

```bash
git add CONTEXT_MEDICAL.md
git commit -m "update: adăugat rezultat CT stadializare (2026-04-22)"
```

Această abordare permite:
- Istoric complet al modificărilor
- Revertirea oricărei modificări greșite
- Sincronizare între dispozitive (GitHub privat recomandat)
- Backup implicit

**Notă:** repository-ul Git trebuie să fie **privat** dată fiind natura sensibilă a datelor.

## Reguli pentru fișiere mari

### Imagini (>5 MB)

- Comprimare la dimensiuni rezonabile (JPG quality 85-90)
- Păstrare original în `documente_sursa/{folder}/originale/` dacă este esențial
- Referire în interpretare: `vezi documente_sursa/06_.../2026-04-17_img1.jpg`

### CD-uri DICOM

CT-urile și RMN-urile vin pe CD cu imagini DICOM. Procedura recomandată:

1. Copiază întregul conținut al CD-ului într-un subfolder dedicat: `08_CT_stadializare_2026/DICOM/`
2. Export raportul radiologului separat ca PDF dacă nu este deja.
3. Pentru vizualizare rapidă, se poate folosi un viewer DICOM (RadiAnt, Horos, OsiriX).

## Reguli pentru backup

### Backup local

Dosar sincronizat cu un serviciu de stocare de încredere (Google Drive, Dropbox, OneDrive — folder privat):

- Sincronizare automată
- Versionare activă (payloadurile permit revertirea)

### Backup extern

O copie pe un disk extern fizic, actualizată lunar. Crucial în caz de pierdere simultană a dispozitivului principal și a stocării cloud.

### Git remote

Dacă se folosește Git, un remote privat pe GitHub/GitLab/Bitbucket:
- Repository **privat** (NICIODATĂ public)
- `.gitignore` nu este necesar pentru acest proiect — toate fișierele se includ.

## Modificări asupra structurii

Structura descrisă în acest fișier **nu se modifică decât cu acordul explicit al utilizatorului**. Orice propunere de schimbare:

1. Se discută cu utilizatorul.
2. Se documentează motivul.
3. Se implementează gradual, cu migrare completă.
4. Se actualizează `STRUCTURA_PROIECT.md`.
5. Se logează în `CHANGELOG.md`.

---

**Ultima revizuire:** 17 aprilie 2026.
