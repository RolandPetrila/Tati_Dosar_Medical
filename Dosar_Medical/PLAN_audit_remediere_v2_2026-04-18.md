# PLAN — Audit + remediere + migrare la schema v2.0

**Data creare:** 2026-04-18
**Autor:** Claude Code (sesiune Opus 4.7, 1M context)
**Declanșator:** audit cerut de Roland Petrilă; aprobare pentru execuție completă primită.

---

## Scop

Remedierea erorilor critice identificate la audit în JSON-urile generate de Gemini, unificarea structurii sub o schemă canonică v2.0, dedup, adăugarea documentelor nedigitizate (C.I., talon pensie scan), și aducerea structurii de proiect în conformitate cu `STRUCTURA_PROIECT.md`.

## Decizii arhitecturale fixate

1. **Locație canonică:** `C:\Users\ALIENWARE\Desktop\Roly\.Tati\` (sincronizată către `G:\My Drive\Roly\.Tati\` via Google Drive).
2. **Schema JSON:** v2.0 (documentată în `SCHEMA_JSON_v2.md`).
3. **Dedup chirurgie 28.11.2025:** 3 JSON-uri → 1 canonic, cu câmp `_metadata.flags.duplicate_of`.
4. **Documentație:** fișierele `.md` utile se copiază la rădăcina proiectului; `Documentatie_Initiala/` rămâne ca **kit inițial nemodificat** (arhivă istorică semantică).
5. **Nu se șterge nimic:** Regula 4.1 din REGULAMENT.md — tot ce e înlocuit se arhivează în `arhiva/`.
6. **Redenumire la format `YYYY-MM-DD_slug.ext`:** se face ca ultim pas, după ce toate JSON-urile sunt funcționale.

## Corecturi critice confirmate (date verificate multi-sursă)

| #   | Fișier                                        | Câmp                             | Valoare greșită                        | Valoare corectă                                              | Sursa adevărului                                                                                                                         |
| --- | --------------------------------------------- | -------------------------------- | -------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | `Talon_Pensie_Asigurare_2025.json`            | `pacient.cnp`                    | `1590518244861`                        | `1590518024486`                                              | C.I. PDF + 6 alte JSON-uri                                                                                                               |
| 2   | `Dosar_Urologie_Gastroenterologie_2025.json`  | `pacient.data_nasterii`          | `28-10-1959`                           | `1959-05-18`                                                 | C.I. PDF + CNP-segment 590518                                                                                                            |
| 3   | `Schema_Medicamente_10_11_2025.json`          | `pacient.nume/prenume`           | `PETRICA VIOREL`                       | `PETRILĂ VIOREL-MIHAI`                                       | C.I. + 9 alte JSON-uri. (Notă: manuscrisul medicului scrie "PETRICĂ" — eroare de redactare medic; se documentează în `_metadata.notes`.) |
| 4   | `Buletin_Analize_Sange_17_06_2025.json`       | `analize_laborator[WBC].unitate` | `µg/dl`                                | `x10^3/µL`                                                   | imposibilitate fizică/medicală                                                                                                           |
| 5   | `Iesire_Din_Spital_Chirurgie_28_11_2025.json` | multiple `unitate: null`         | toate                                  | completate din fișierul paralel `Bilet_Iesire_...`           | cross-reference                                                                                                                          |
| 6   | `Dosar_Urologie_Gastroenterologie_2025.json`  | `diagnostic[*].cod_icd10`        | `702-N43.3`, `703-N45.9`, `564-K40.90` | `N43.3`, `N45.9`, `K40.90` (codul intern spital în câmp nou) | standard ICD-10 oficial                                                                                                                  |

## Etape execuție

### Faza A — Structură + backup ✅

- [x] Creare foldere `documente_sursa/01_identitate`…`99_altele`, `interpretari/`, `rapoarte_generate/`, `arhiva/`, `cercetari/`, `comunicare_medici/`
- [x] Copiere toate 10 JSON-uri existente în `arhiva/backup_pre-migrare_v2_2026-04-18/`

### Faza B — Documente arhitecturale

- [ ] `PLAN_audit_remediere_v2_2026-04-18.md` (acest fișier)
- [ ] `SCHEMA_JSON_v2.md` (specificație schema)

### Faza C — Migrare 10 JSON-uri la v2.0

- [ ] `Dosar_Cardiologie_Vichy_2012.json` → `2012-02-17_cardiologie_vichy_stent.json`
- [ ] `Buletin_Analize_Infectioase_06_09_2024.json` → `2024-09-06_anti_helicobacter_pylori_igg.json`
- [ ] `Buletin_Analize_Sange_17_06_2025.json` → `2025-06-17_buletin_analize_sange.json` (+ fix unitate WBC)
- [ ] `Dosar_Urologie_Gastroenterologie_2025.json` → `2025-10-28_scrisoare_urologie_gastroenterologie.json` (+ fix data_nasterii, ICD-10)
- [ ] `Talon_Pensie_Asigurare_2025.json` → `2025-11-01_talon_pensie_asigurare.json` (+ fix CNP)
- [ ] `Schema_Medicamente_10_11_2025.json` → `2025-11-10_schema_medicamente.json` (+ fix nume, note manuscris)
- [ ] `Buletin_Gastroenterologie_17_04_2026.json` → `2026-04-17_buletin_gastroenterologie.json`

### Faza D — Dedup chirurgie

- [ ] Fuziune 3 JSON-uri chirurgie 28.11.2025 → `2025-11-28_iesire_spital_chirurgie.json` canonic
- [ ] Celelalte 2 marcate `duplicate_of` și mutate la `arhiva/duplicate_chirurgie_28_11_2025/`

### Faza E — JSON-uri noi

- [ ] `2023-06-12_carte_identitate.json` (date din C.I.)
- [ ] Date din Casa_judeteana_de_pensii.jpeg integrate în `2025-11-01_talon_pensie_asigurare.json` (complement la talon)

### Faza F — `.meta.json` chain of custody

- [ ] Câte un `.meta.json` pentru fiecare document sursă (PDF/JPEG)

### Faza G — MANIFEST + SESSION_LOG + WEB_QUERIES

- [ ] `MANIFEST.json` — index cronologic
- [ ] `SESSION_LOG.md` — reconstituire retroactivă Gemini + log sesiune curentă
- [ ] `WEB_QUERIES.md` — stub gol

### Faza H — Documentație la rădăcină + corecturi

- [ ] Copiere `.md`-uri utile din `Documentatie_Initiala/` la rădăcina proiectului
- [ ] Corecturi path în `INSTALARE.md` (real vs. fictiv)
- [ ] `Documentatie_Initiala/` neatinsă ca kit original

### Faza I — Reconciliere `CONTEXT_MEDICAL.md`

- [ ] Completare secțiuni "de completat" cu date confirmate din JSON-uri
- [ ] Marcare sursă pentru fiecare câmp adăugat

### Faza J — Redenumire

- [ ] `mv` pentru toate fișierele la format ISO
- [ ] Mutare scan-uri sursă în subfolderele tematice `documente_sursa/XX_*/`

### Faza K — Validare finală

- [ ] Re-citire JSON-uri noi (JSON-parse OK)
- [ ] Verificare cross-reference MANIFEST ↔ fișiere reale
- [ ] `CHANGELOG.md` actualizat
- [ ] Raport final utilizator

## Siguranță

- Backup-ul original e intact în `arhiva/backup_pre-migrare_v2_2026-04-18/`.
- La orice eroare de parse sau rezultat neașteptat → stop și raportare către user (Regula R-RECOVERY din CLAUDE.md global).
- Nicio modificare pe `G:\My Drive\Roly\.Tati\` direct — lucrul e strict pe `Desktop`, sincronizarea se face prin Google Drive client.

## Note pentru sesiuni viitoare

- Orice document nou adăugat → rulez procedura A din `WORKFLOW.md`.
- Orice conflict cu datele deja validate → se oprește și se întreabă utilizatorul.
- Structura de foldere e stabilă; orice schimbare = propunere cu confirmare.
