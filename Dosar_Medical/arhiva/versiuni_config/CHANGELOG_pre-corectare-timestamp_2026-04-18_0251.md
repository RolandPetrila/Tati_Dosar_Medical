# CHANGELOG.md — Istoricul modificărilor

**Jurnal cronologic al tuturor modificărilor din dosar. Intrările cele mai recente sunt sus.**

---

## 2026-04-18 (sesiune Claude_Opus_4.7, continuare 3) — Integrare buletin Bioclinica 17.04

**Tip:** ADAUGARE DOCUMENT NOU + ACTUALIZARE

**Fișiere afectate:**

- `Dosar_Medical/2026-04-17_buletin_bioclinica_uree_creatinina.json` (nou, schema v2.0)
- `Dosar_Medical/documente_sursa/05_analize_laborator/2026-04-17_buletin_bioclinica_uree_creatinina.jpeg` (nou — scan original)
- `Dosar_Medical/documente_sursa/05_analize_laborator/2026-04-17_buletin_bioclinica_uree_creatinina.jpeg.meta.json` (nou — chain of custody)
- `CONTEXT_MEDICAL.md` — tabel creatinină actualizat + notă despre localizarea biopsiei
- `TODO.md` — `[P0] Analize prealabile CT` marcat COMPLET
- `CHANGELOG.md` + `SESSION_LOG.md`

**Descriere:**

Integrat buletinul Bioclinica nr. 26417A0362 din 17.04.2026 (recoltat 14:21, emis 17:07, medic primar Dr. Statnic Maria Luminița). Conține uree (33.4 mg/dL, normal) + creatinină (0.83 mg/dL, normal; eGFR CKD-EPI ~95 → stadiu G1).

**Consecințe pentru CT 20.04.2026:**

- Funcție renală confirmată NORMALĂ cu valoare recentă (3 zile vechime)
- Nu se impune repetarea analizelor înainte de CT
- Protocol contrast standard — fără prehidratare IV sau ajustări
- Risc nefropatie post-contrast — scăzut

**Consecință suplimentară (observație critică):**

Pe buletin apare mențiunea „Examen histopatologic în curs de execuție" → **biopsia esofagiană este procesată la Bioclinica Arad** (nu la Genesis, cum se presupunea inițial). Contact urmărire: arad@bioclinica.ro.

**Sursă informație:** utilizator (Roland Petrilă) — a trimis scanul buletinului.

**Făcut de:** Claude Code (Opus 4.7, 1M context).

---

## 2026-04-18 (sesiune Claude_Opus_4.7, continuare 2) — Confirmare CT 20.04 + plan pregătire

**Tip:** ACTUALIZARE DATE MEDICALE

**Fișiere afectate:** `CONTEXT_MEDICAL.md`, `TODO.md`.

**Descriere:**

- Confirmată programarea CT torace+abdomen+pelvis cu contrast pentru **LUNI 20.04.2026 ora 17:00** la Genesis Medical Clinic Micălaca.
- Recalculate deadline-urile pentru pregătirea medicației: STOP Jamesi sâmbătă 18.04 ora 17:00 (H-48); reluare miercuri 22.04 ora 17:00 (H+48) după creatinină normală.
- Adăugat plan alimentație pre-CT (cină duminică 20:00, gustare luni 11:00, doar apă până la CT).
- Semnalat STALE al creatininei (ultima 28.11.2025 — 5 luni vechime) — necesare analize actualizate.
- Atenționare Triplixam (indapamidă diuretic + perindopril IECA) — de clarificat cu radiologul la confirmare telefonică.
- Confirmare absență alergii — P0 critic, încă neconfirmat.

**Sursă informație:** utilizator (Roland Petrilă) — a confirmat programarea CT.

**Făcut de:** Claude Code (Opus 4.7, 1M context).

---

## 2026-04-18 (sesiune Claude_Opus_4.7, continuare) — Git init + push + Regula 16

**Tip:** ADAUGARE + MODIFICARE

**Fișiere afectate:** `CLAUDE.md` (proiect), `REGULAMENT.md`, `.gitignore` (nou), `CHANGELOG.md`, `SESSION_LOG.md`.

**Descriere:**

- Inițializat Git local (`git init -b main`)
- Creat `.gitignore` minimal (OS artifacts + safety net secrete)
- Primul commit `ee642d2`: 81 fișiere, +10.207 linii
- Creat repo privat `RolandPetrila/Tati_Dosar_Medical` pe GitHub (de către user manual)
- Remote `origin` configurat + `main` pushed cu tracking
- **Regula 16** adăugată în `CLAUDE.md` (proiect): git auto-commit + push la finalul fiecărei sesiuni cu modificări de referință
- Cross-reference Regula 16 adăugat în `REGULAMENT.md` secțiunea 4.5

**Motiv:** versionare structurată, rollback granular, backup paralel cu Google Drive, trasabilitate pe istoric dosar medical.

**Făcut de:** Claude Code (Opus 4.7, 1M context).

---

## 2026-04-18 (sesiune Claude_Opus_4.7) — Audit + migrare v2 + reorganizare structurală

**Tip:** MIGRARE_MAJORĂ

**Declanșator:** audit cerut de Roland Petrilă; aprobare execuție completă primită.

### Date corectate (erori în JSON-urile Gemini v1)

- **CNP** în `Talon_Pensie_Asigurare_2025.json`: `1590518244861` → `1590518024486` (ancora: C.I. + 6 alte documente).
- **Data nașterii** în `Dosar_Urologie_Gastroenterologie_2025.json`: `28-10-1959` → `1959-05-18`.
- **Nume pacient** în `Schema_Medicamente_10_11_2025.json`: `PETRICA` → `PETRILĂ` (medicul scrisese eronat pe manuscris).
- **Unitate WBC** în `Buletin_Analize_Sange_17_06_2025.json`: `µg/dl` (imposibil medical) → `x10^3/µL`.
- **Coduri ICD-10** în `Dosar_Urologie_Gastroenterologie_2025.json`: eliminat prefixul intern spital (ex. `702-N43.3` → `N43.3`, cod intern separat).
- **Unități lab** în `Iesire_Din_Spital_Chirurgie_28_11_2025.json`: completate din fișierul paralel `Bilet_Iesire_`.

### Dedup

- 3 JSON-uri chirurgie 28.11.2025 → 1 canonic `2025-11-28_externare_chirurgie_hernie.json`. Originalele arhivate în `Dosar_Medical/arhiva/duplicate_chirurgie_28_11_2025/`.

### Fișiere create (Dosar_Medical/)

- 9 JSON-uri canonice la schema v2.0 (vezi MANIFEST.json pentru listă)
- `PLAN_audit_remediere_v2_2026-04-18.md` — planul sesiunii
- `SCHEMA_JSON_v2.md` — specificația structurii canonice
- `MANIFEST.json` — index cronologic al întregului dosar
- 11 fișiere `.meta.json` (chain of custody — Regula 14)

### Fișiere create (rădăcina proiectului .Tati/)

- `SESSION_LOG.md` — log sesiuni Claude/Gemini (Regula 9)
- `WEB_QUERIES.md` — log cercetări web (Regula 15)
- `CONTEXT_MEDICAL.md` — copiat din `Documentatie_Initiala/` + reconciliat cu JSON-uri (v1.1)
- `CHANGELOG.md` (acest fișier)
- `README.md`, `START.md`, `REGULAMENT.md`, `WORKFLOW.md`, `STRUCTURA_PROIECT.md`, `BAZA_CUNOSTINTE.md`, `TEMPLATES.md`, `SURSE_MEDICALE.md`, `GLOSAR.md`, `TODO.md` — copiate din `Documentatie_Initiala/` la rădăcina proiectului (conform STRUCTURA_PROIECT.md)

### Fișiere modificate

- `REGULAMENT.md`: adăugat preambul de cross-reference către `CLAUDE.md` proiect v2 (Regulile 6-15)
- `Documentatie_Initiala/INSTALARE.md`: path real adăugat (canonical `C:\Users\ALIENWARE\Desktop\Roly\.Tati\`, sync target `G:\My Drive\Roly\.Tati\`)
- `CONTEXT_MEDICAL.md`: reconciliere extensivă cu date confirmate din JSON-uri (secțiuni 1 date pacient, 3 antecedente, 4 medicație, 7.3 colonoscopie, 8 pregătire CT, 9 echipă medicală)

### Structura de foldere creată (în Dosar_Medical/)

- `documente_sursa/01_identitate`…`99_altele` (13 subfoldere)
- `interpretari/jurnal_simptome/`, `interpretari/cronologic/`
- `rapoarte_generate/versiuni_anterioare/`
- `cercetari/`, `comunicare_medici/`
- `arhiva/backup_pre-migrare_v2_2026-04-18/`, `arhiva/duplicate_chirurgie_28_11_2025/`, `arhiva/context_medical_versiuni/`, `arhiva/versiuni_config/`

### Scanuri mutate + redenumite la format ISO (YYYY-MM-DD_slug.ext)

| Vechi                             | Nou                                                                                    |
| --------------------------------- | -------------------------------------------------------------------------------------- |
| `C.I. - Petrila Viorel.pdf`       | `documente_sursa/01_identitate/2023-06-12_carte_identitate.pdf`                        |
| `Gastroscopic_Colonoscopic.pdf`   | `documente_sursa/09_endoscopie_2026_04/2026-04-17_buletin_endoscopie_colonoscopie.pdf` |
| `Ieșire din spital.pdf`           | `documente_sursa/07_hernie_2025_11/2025-11-28_externare_chirurgie_hernie.pdf`          |
| `Schema_Medicamente.jpeg`         | `documente_sursa/08_schema_tratament/2025-11-10_schema_medicamente_manuscris.jpeg`     |
| `Casa_judeteana_de_pensii.jpeg`   | `documente_sursa/10_administrativ_pensie/2025-11-01_talon_pensie_scan.jpeg`            |
| `Apr 17, Doc 2-7.pdf` (6 fișiere) | `documente_sursa/99_altele/2026-04-17_doc_neidentificat_{2-7}.pdf`                     |

### Fișiere șterse (backup-urile rămân în `arhiva/`)

- 10 JSON-uri Gemini v1 din rădăcina `Dosar_Medical/` (identice ca conținut cu cele din `arhiva/backup_pre-migrare_v2_2026-04-18/`)

### Validare finală

- ✅ 21 JSON-uri (9 canonice + 1 MANIFEST + 11 .meta.json) — toate parse OK
- ✅ CONTEXT_MEDICAL.md v1 arhivat în `Dosar_Medical/arhiva/context_medical_versiuni/CONTEXT_MEDICAL_v1_2026-04-17.md`
- ✅ Scanurile originale intacte (doar redenumite și mutate; conținutul binar neschimbat)

### Nerezolvat / rămas pentru sesiuni viitoare

- 6 PDF-uri `2026-04-17_doc_neidentificat_{2-7}.pdf` — de deschis și identificat conținutul
- Schema_Medicamente: numele exact al Dr. LAZĂR de identificat
- Unitatea/secția exactă pentru chirurgia 28.11.2025 (JSON are `de identificat`)
- Status alergii pacient — P0, CRITIC pentru CT cu contrast
- HbA1c recent — P1, relevant pentru monitorizare diabet

**Făcut de:** Claude Code (Opus 4.7, 1M context) — sesiunea a durat de la ~15:00 la ~17:00 pe 2026-04-18.

---

## 2026-04-17/18 — Inițializare dosar + procesare Gemini (retroactiv)

**Tip:** CREARE

**Descriere:** Inițializare kit documentație (Claude.ai) și procesare inițială a PDF-urilor medicale de către Gemini în JSON-uri v1. Detalii în `SESSION_LOG.md`.

**Făcut de:** Claude.ai (web) + Gemini.

---

## Formatul intrărilor viitoare

Fiecare modificare nouă se adaugă la începutul acestui fișier, deasupra intrării precedente, în formatul:

```markdown
## YYYY-MM-DD (HH:MM opțional) — [Titlu scurt]

**Tip:** [CREARE / MODIFICARE / CORECTIE / ARHIVARE / ADAUGARE / MIGRARE]
**Fișier(e) afectat(e):** `fisier1`, `fisier2`
**Descriere:** Ce s-a modificat, concret.
**Motiv:** De ce s-a făcut modificarea.
**Sursă informație (dacă aplicabil):** document / consult / cercetare
**Făcut de:** utilizator / Claude Code / Gemini
```
