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
├── documente_sursa/                  Scanurile și fișierele originale (structură v2026-04-24 — 14 foldere, 99_altele ELIMINAT)
│   ├── 01_identitate/                Carte identitate, pașaport
│   ├── 02_cardiologie_2012/          Stent Vichy 2012 (🟡 PDF de obținut)
│   ├── 03_hernie_anterior/           Prima operație de hernie (🟡 dată necunoscută)
│   ├── 04_helicobacter_2024/         Serologie H. pylori iunie + septembrie 2024
│   ├── 05_analize_laborator/         Buletine analize sânge / urină (cronologic)
│   ├── 06_urologie_gastro_2025/      Consult urologie + ECO scrotală 28.10.2025 (Dr. Pitea)
│   ├── 07_hernie_2025_11/            Intervenție hernie noiembrie 2025 (Dr. Papiu)
│   ├── 08_schema_tratament/          Scheme medicație manuscrise (10.11.2025)
│   ├── 09_endoscopie_2026_04/        Gastroscopie + colonoscopie 17.04.2026 (Dr. Noufal)
│   ├── 10_administrativ_pensie/      Talon pensie, dovezi asigurare CASS
│   ├── 11_CT_stadializare_2026/      Bilet trimitere CT + raport CT 20.04.2026 (Dr. Buie + Dr. Candea)
│   ├── 12_biopsie_2026/              Rezultat biopsie (🟡 așteptare Bioclinica)
│   ├── 13_cardiologie_ambulator_2025/  Consult cardiologie + ECO 10.11.2025 (Dr. LAZA CRISTINA)
│   └── 14_UPU_2024_05_30/            Episod UPU Arad 30.05.2024 (Dr. Post + Dr. Grada + Dr. Pop)
│
│   [Convenție R26: NN_categorie_data/ unde NN crește continuu; 99_altele/ eliminat 2026-04-24 — documente noi se plasează în folder tematic sau se creează 15_... conform convenției]
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
├── Documente_Informative/            Ghiduri operaționale + documente informative pentru familie
│   ├── GHID_CONSULT_ONCOLOG.md       (ex: checklist acțiune programare consult oncolog)
│   └── ...                           (orice alt ghid / explicație / material informativ viitor)
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

### Documente informative (ghiduri, explicații, materiale pentru familie)

**Locație:** `Documente_Informative/` (rădăcina proiectului)
**Format:** `GHID_SUBIECT.md` sau `SUBIECT_YYYY-MM-DD.md` (UPPERCASE pentru titlu când e material pregătit pentru citire rapidă de familie/pacient)
**Exemple:**

- `GHID_CONSULT_ONCOLOG.md` (checklist acțiune programare consult)
- `GHID_NUTRITIE_OPERATIE.md` (material viitor, exemplu)
- `EXPLICATIE_PROTOCOL_FLOT.md` (material viitor, exemplu)

**NU se salvează la rădăcina proiectului direct.** Rădăcina e rezervată fișierelor structurale (CLAUDE.md, CONTEXT_MEDICAL.md, TODO.md, CHANGELOG.md, etc.).

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

### Ce merge în ce folder (structură actuală 2026-04-24)

| Tip document                                         | Folder                           |
| ---------------------------------------------------- | -------------------------------- |
| CI, pașaport                                         | `01_identitate/`                 |
| Stent Vichy 2012 (la obținere PDF)                   | `02_cardiologie_2012/`           |
| Prima hernie (la identificare)                       | `03_hernie_anterior/`            |
| Serologie/internare H. pylori 2024                   | `04_helicobacter_2024/`          |
| Buletine analize sânge/urină — orice dată            | `05_analize_laborator/`          |
| Consult urologie + ECO scrotală 28.10.2025           | `06_urologie_gastro_2025/`       |
| Intervenție hernie noiembrie 2025                    | `07_hernie_2025_11/`             |
| Scheme medicație (rețete manuscrise cronologice)     | `08_schema_tratament/`           |
| Gastroscopie + colonoscopie 17.04.2026               | `09_endoscopie_2026_04/`         |
| Talon pensie, dovezi asigurare                       | `10_administrativ_pensie/`       |
| Bilet trimitere CT + raport CT 20.04.2026 + CD DICOM | `11_CT_stadializare_2026/`       |
| Rezultat biopsie (la primire)                        | `12_biopsie_2026/`               |
| Consult cardiologie ambulator 10.11.2025 (Dr. LAZA)  | `13_cardiologie_ambulator_2025/` |
| Episod UPU 30.05.2024 (criza HTA + hiperglicemie)    | `14_UPU_2024_05_30/`             |

**`99_altele/` eliminat 2026-04-24** — conținutul a fost redistribuit în folderele tematice după integrarea documentelor din Arhiva_Generala.

### Pentru consulturi viitoare

Pe măsură ce apar consulturi noi (oncolog, endocrinolog, etc.), se creează subfoldere noi **continuând numerotarea de la 15**:

- `15_oncolog_YYYY-MM/` (la prima vizită oncolog digestiv)
- `16_endocrinologie_YYYY-MM/` (la prima vizită endocrinolog pentru glanda suprarenală stângă)
- etc.

**Regula R26:** nu se re-crează `99_altele/`. Un document care nu se încadrează în categoriile existente declanșează crearea unui folder tematic dedicat.

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

| Categorie                                         | Versionare               | Metodă                                                            |
| ------------------------------------------------- | ------------------------ | ----------------------------------------------------------------- |
| Fișiere de configurare (CLAUDE.md, REGULAMENT.md) | La fiecare modificare    | Arhivă în `arhiva/versiuni_config/`                               |
| `CONTEXT_MEDICAL.md`                              | La modificări majore     | Arhivă în `arhiva/`                                               |
| Rapoarte generate (docx, pdf)                     | La fiecare versiune nouă | Sufix `_vN`, vechiul în `rapoarte_generate/versiuni_anterioare/`  |
| Documente sursă                                   | Imutabile                | Nu se rescriu niciodată                                           |
| Interpretări, cercetări                           | În general imutabile     | Dacă trebuie actualizate, se creează versiune nouă cu sufix `_v2` |

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

---

<!-- AUTO-GENERATED START -->

## 🗺 Hartă completă auto-generată

> ⚙️ **Generat automat:** 2026-04-26T19:22:02 de `scripts/regenerate_structura.py`. NU edita manual această secțiune — modificările se pierd la următoarea regenerare. Pentru cuprinsul fix vezi secțiunile non-auto de mai sus.

### 📊 Statistici live

- **Total fișiere proiect (excl. .git):** 218
- **Markdown (.md):** 96
- **JSON (.json):** 65
- **HTML (.html):** 7
- **Total size:** 50509.1 KB

### 🧭 Index thematic (caut...)

| Caut...                                        | Mergi la                                                                 |
| ---------------------------------------------- | ------------------------------------------------------------------------ |
| biopsie  | `Dosar_Medical/documente_sursa/12_biopsie_2026/` · `TODO.md` · `Documente_Informative/EXPLICATIE_CONSULT_ONCOLOG_SCENARII.md` |
| medic / oncolog / programare  | `Dosar_Medical/CONTACTE_MEDICALE.md` · `CONTEXT_MEDICAL.md (§9 Echipă medicală)` · `TODO.md (Calendar + P0)` |
| corespondență email medici  | `Dosar_Medical/corespondenta/INDEX.md` · `Dosar_Medical/corespondenta/2026-04-*.md` |
| dietă / alimentație  | `ALIMENTATIE.md` · `DASHBOARD.html (tab Alimentație)` |
| CT 20.04.2026  | `Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json` · `Dosar_Medical/documente_sursa/11_CT_stadializare_2026/` · `CONTEXT_MEDICAL.md §2` |
| endoscopie / colonoscopie 17.04.2026  | `Dosar_Medical/2026-04-17_examen_gastroscopic.json` · `Dosar_Medical/2026-04-17_examen_colonoscopic.json` · `Dosar_Medical/documente_sursa/09_endoscopie_2026_04/` |
| medicație + interacțiuni  | `CONTEXT_MEDICAL.md §4` · `Dosar_Medical/2025-11-10_schema_medicamente.json` · `Dosar_Medical/rapoarte_generate/2026-04-18_raport_reactii_adverse_jamesi_triplixam.docx` |
| monitor automat biopsie ntfy.sh  | `TODO.md (secțiunea Monitor automat)` · `C:\Users\ALIENWARE\Desktop\Roly\Sistem_Notificari_Telefon\ (repo extern)` |
| DASHBOARD live (familie)  | `DASHBOARD.html` · `https://rolandpetrila.github.io/Tati_Dosar_Medical/` |
| reguli + protocol  | `CLAUDE.md (loader)` · `REGULAMENT.md (R1-10 medicale)` · `REGULI_CLAUDE_CODE.md (R6-29 specifice)` |
| system health monitor R28  | `Dosar_Medical/SYSTEM_HEALTH.json` · `scripts/system_health_check.py` |
| plan execuție curent  | `PLAN_IMPLEMENTARE_2026-04-25.md (status în frontmatter)` |

### 🌳 Arbore folder (depth 3)

```
.Tati/  (7 subfoldere, 27 fișiere root)
├── .claude/  (1 fișiere)
│   ├── settings.local.json  (1.9 KB)
├── .ruff_cache/  (4 fișiere)
│   ├── 0.14.2/  (2 fișiere)
│   │   ├── 11311870640459399777  (0.1 KB)
│   │   ├── 4361782613845319426  (0.2 KB)
│   ├── .gitignore  (0.0 KB)
│   ├── CACHEDIR.TAG  (0.0 KB)
├── assets/  (4 fișiere)
│   ├── generate_icons.py  (2.2 KB)
│   ├── icon-192.png  (1.1 KB)
│   ├── icon-512.png  (3.4 KB)
│   ├── icon-maskable-512.png  (2.5 KB)
├── Documentatie_Initiala/  (19 fișiere)
│   ├── BAZA_CUNOSTINTE.md  (9.4 KB)
│   ├── CHANGELOG.md  (3.7 KB)
│   ├── CLAUDE.md  (5.7 KB)
│   ├── CONTEXT_MEDICAL.md  (10.1 KB)
│   ├── GLOSAR.md  (10.6 KB)
│   ├── HISTORY_CLAUDE_MD.md  (9.8 KB)
│   ├── INSTALARE.md  (8.3 KB)
│   ├── kit_claude_code_dosar_medical.zip  (50.1 KB)
│   ├── PLAN_reorganizare_claude_md_2026-04-23.md  (8.6 KB)
│   ├── PRIMUL_PROMPT.md  (6.8 KB)
│   ├── README.md  (2.0 KB)
│   ├── REGULAMENT.md  (9.6 KB)
│   ├── REGULI_DETALIATE.md  (14.0 KB)
│   ├── START.md  (3.8 KB)
│   ├── STRUCTURA_PROIECT.md  (9.3 KB)
│   ├── SURSE_MEDICALE.md  (7.5 KB)
│   ├── TEMPLATES.md  (9.7 KB)
│   ├── TODO.md  (7.0 KB)
│   ├── WORKFLOW.md  (9.2 KB)
├── Documente_Informative/  (4 fișiere)
│   ├── CLAUDE.md  (3.5 KB)
│   ├── EXPLICATIE_CONSULT_ONCOLOG_SCENARII.md  (74.5 KB)
│   ├── GHID_APEL_ONCOHELP.md  (11.1 KB)
│   ├── GHID_CONSULT_ONCOLOG.md  (22.5 KB)
├── Dosar_Medical/  (156 fișiere)
│   ├── arhiva/  (36 fișiere)
│   │   ├── context_medical_versiuni/  (15 fișiere)
│   │   ├── json_versiuni/  (3 fișiere)
│   │   ├── versiuni_config/  (18 fișiere)
│   ├── cercetari/  (2 fișiere)
│   │   ├── 2026-04-25_cercetare-oncohelp-vornicu-anater.md  (15.4 KB)
│   │   ├── SINTEZA_CLINICI_ONCOLOGIE.md  (34.3 KB)
│   ├── comunicare_medici/  (0 fișiere)
│   ├── corespondenta/  (6 fișiere)
│   │   ├── 2026-04-22_solicitare-dr-cip-recomandare-lusca.md  (7.7 KB)
│   │   ├── 2026-04-23_broadcast-solicitari-clinici.md  (6.6 KB)
│   │   ├── 2026-04-23_solicitare-sprijin-oncohelp.md  (5.2 KB)
│   │   ├── 2026-04-24_raspuns-iocn-mester.md  (4.3 KB)
│   │   ├── 2026-04-24_re-solicitare-consult-anater.md  (12.4 KB)
│   │   ├── INDEX.md  (7.3 KB)
│   ├── documente_sursa/  (55 fișiere)
│   │   ├── 01_identitate/  (3 fișiere)
│   │   ├── 02_cardiologie_2012/  (0 fișiere)
│   │   ├── 03_hernie_anterior/  (0 fișiere)
│   │   ├── 04_helicobacter_2024/  (3 fișiere)
│   │   ├── 05_analize_laborator/  (6 fișiere)
│   │   ├── 06_urologie_gastro_2025/  (3 fișiere)
│   │   ├── 07_hernie_2025_11/  (6 fișiere)
│   │   ├── 08_schema_tratament/  (3 fișiere)
│   │   ├── 09_endoscopie_2026_04/  (6 fișiere)
│   │   ├── 10_administrativ_pensie/  (3 fișiere)
│   │   ├── 11_CT_stadializare_2026/  (6 fișiere)
│   │   ├── 12_biopsie_2026/  (0 fișiere)
│   │   ├── 13_cardiologie_ambulator_2025/  (3 fișiere)
│   │   ├── 14_UPU_2024_05_30/  (13 fișiere)
│   ├── interpretari/  (0 fișiere)
│   │   ├── cronologic/  (0 fișiere)
│   │   ├── jurnal_simptome/  (0 fișiere)
│   ├── rapoarte_generate/  (12 fișiere)
│   │   ├── .ruff_cache/  (3 fișiere)
│   │   ├── versiuni_anterioare/  (0 fișiere)
│   │   ├── 2026-04-18_raport_reactii_adverse_jamesi_triplixam.docx  (46.1 KB)
│   │   ├── 2026-04-18_raport_reactii_adverse_jamesi_triplixam.meta.json  (3.0 KB)
│   │   ├── 2026-04-19_ghid_cancer_esofagian_complet.docx  (63.3 KB)
│   │   ├── 2026-04-19_ghid_cancer_esofagian_complet.meta.json  (2.4 KB)
│   │   ├── 2026-04-22_explicatie_consult_oncolog_scenarii.docx  (63.5 KB)
│   │   ├── 2026-04-22_explicatie_consult_oncolog_scenarii.meta.json  (4.5 KB)
│   │   ├── generate_explicatie_scenarii.py  (85.6 KB)
│   │   ├── generate_ghid_cancer_esofagian.py  (80.7 KB)
│   │   ├── generate_reactii_adverse_docx.py  (35.1 KB)
│   ├── 2012-02-17_cardiologie_vichy_stent.json  (3.4 KB)
│   ├── 2012-02-17_cardiologie_vichy_stent.json.meta.json  (2.0 KB)
│   ├── 2023-06-12_carte_identitate.json  (2.3 KB)
│   ├── 2023-06-12_carte_identitate.json.meta.json  (1.3 KB)
│   ├── 2024-05-30_analize_upu_sange_1517243.json  (9.2 KB)
│   ├── 2024-05-30_analize_upu_sange_1517243.json.meta.json  (0.8 KB)
│   ├── 2024-05-30_analize_upu_urina_1517290.json  (5.2 KB)
│   ├── 2024-05-30_analize_upu_urina_1517290.json.meta.json  (0.8 KB)
│   ├── 2024-05-30_upu_consult_gastro_cardio.json  (13.1 KB)
│   ├── 2024-05-30_upu_consult_gastro_cardio.json.meta.json  (1.1 KB)
│   ├── 2024-06-04_anti_helicobacter_pylori_igg_77449.json  (3.5 KB)
│   ├── 2024-06-04_anti_helicobacter_pylori_igg_77449.json.meta.json  (1.1 KB)
│   ├── 2024-09-06_anti_helicobacter_pylori_igg_79765.json  (3.8 KB)
│   ├── 2024-09-06_anti_helicobacter_pylori_igg_79765.json.meta.json  (1.1 KB)
│   ├── 2025-06-17_buletin_analize_sange.json  (14.7 KB)
│   ├── 2025-06-17_buletin_analize_sange.json.meta.json  (1.7 KB)
│   ├── 2025-10-28_scrisoare_urologie_gastroenterologie.json  (4.3 KB)
│   ├── 2025-10-28_scrisoare_urologie_gastroenterologie.json.meta.json  (1.6 KB)
│   ├── 2025-11-01_talon_pensie_asigurare.json  (1.9 KB)
│   ├── 2025-11-01_talon_pensie_asigurare.json.meta.json  (1.2 KB)
│   ├── 2025-11-10_ecografie_transtoracica.json  (4.1 KB)
│   ├── 2025-11-10_ecografie_transtoracica.json.meta.json  (1.1 KB)
│   ├── 2025-11-10_schema_medicamente.json  (4.8 KB)
│   ├── 2025-11-10_schema_medicamente.json.meta.json  (2.8 KB)
│   ├── 2025-11-10_scrisoare_medicala_cardiologie.json  (5.9 KB)
│   ├── 2025-11-10_scrisoare_medicala_cardiologie.json.meta.json  (1.2 KB)
│   ├── 2025-11-28_externare_chirurgie_hernie.json  (14.9 KB)
│   ├── 2025-11-28_externare_chirurgie_hernie.json.meta.json  (1.7 KB)
│   ├── 2026-04-17_bilet_trimitere_CT.json  (3.5 KB)
│   ├── 2026-04-17_bilet_trimitere_CT.json.meta.json  (0.9 KB)
│   ├── 2026-04-17_buletin_bioclinica_uree_creatinina.json  (4.2 KB)
│   ├── 2026-04-17_buletin_bioclinica_uree_creatinina.json.meta.json  (1.3 KB)
│   ├── 2026-04-17_examen_colonoscopic.json  (4.7 KB)
│   ├── 2026-04-17_examen_colonoscopic.json.meta.json  (0.9 KB)
│   ├── 2026-04-17_examen_gastroscopic.json  (3.9 KB)
│   ├── 2026-04-17_examen_gastroscopic.json.meta.json  (0.9 KB)
│   ├── 2026-04-20_ct_torace_abdomen_pelvis.json  (13.2 KB)
│   ├── 2026-04-20_ct_torace_abdomen_pelvis.json.meta.json  (1.9 KB)
│   ├── CLAUDE.md  (21.2 KB)
│   ├── CONTACTE_MEDICALE.md  (16.2 KB)
│   ├── EXTRAGERI_INCOMPLETE.md  (5.0 KB)
│   ├── MANIFEST.json  (14.9 KB)
│   ├── PLAN_audit_remediere_v2_2026-04-18.md  (7.3 KB)
│   ├── SCHEMA_JSON_v2.md  (7.6 KB)
│   ├── SYSTEM_HEALTH.json  (2.3 KB)
├── scripts/  (3 fișiere)
│   ├── generate_index.py  (8.2 KB)
│   ├── regenerate_structura.py  (8.6 KB)
│   ├── system_health_check.py  (7.2 KB)
├── .gitignore  (0.9 KB)
├── ALIMENTATIE.md  (48.0 KB)
├── AUDIT_EXTRAGERE_2026-04-24.md  (28.3 KB)
├── AUDIT_EXTRAGERE_2026-04-26.md  (20.1 KB)
├── BAZA_CUNOSTINTE.md  (9.4 KB)
├── CHANGELOG.md  (149.5 KB)
├── CLAUDE.md  (9.4 KB)
├── CONTEXT_MEDICAL.md  (53.2 KB)
├── DASHBOARD.html  (175.4 KB)
├── GLOSAR.md  (10.6 KB)
├── index.html  (0.3 KB)
├── INDEX.json  (34.2 KB)
├── info_tati.txt  (1.6 KB)
├── manifest.webmanifest  (0.9 KB)
├── PLAN_IMPLEMENTARE_2026-04-25.md  (52.4 KB)
├── README.md  (2.0 KB)
├── REGULAMENT.md  (11.9 KB)
├── REGULI_CLAUDE_CODE.md  (30.0 KB)
├── SESSION_LOG.md  (97.2 KB)
├── START.md  (3.8 KB)
├── STRUCTURA_PROIECT.md  (23.9 KB)
├── SURSE_MEDICALE.md  (7.5 KB)
├── tati.png  (138.8 KB)
├── TEMPLATES.md  (9.7 KB)
├── TODO.md  (37.6 KB)
├── WEB_QUERIES.md  (14.9 KB)
├── WORKFLOW.md  (9.2 KB)
```

<!-- AUTO-GENERATED END -->
