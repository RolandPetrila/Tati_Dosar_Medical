---
sursa_pdf: 2026-04-28_opis_consult_initial_oncohelp.pdf
locatie_sursa: Dosar_Medical/documente_sursa/15_consult_initial_oncologie_2026/
data_eveniment: 2026-04-28 (transmitere OPIS) → 2026-04-30 12:00 (consult programat)
tip_document: OPIS — Borderou documente pentru primul consult oncologie
emitent: OncoHelp Timișoara (recepție programări)
limba: română
extragere_efectuata_de: Claude_Opus_4.7_1M
data_extragere: 2026-04-28
metoda_extragere: propagare strict-extractivă R23 din PDF digital nativ (1 pagină, 273.3 KB)
coverage: "100% — 1 pagină procesată"
json_canonic_corespondent: NU există JSON canonic dedicat — informația esențială este în meta.json companion (cele 8 puncte) + context consult în CONTEXT_MEDICAL §6 (acțiuni în curs)
---

# OPIS — Borderou documente pentru primul consult la Oncologie

> **Acest fișier este o transcriere strict-extractivă a documentului PDF OPIS oficial OncoHelp Timișoara, primit de pacient/familie pe 2026-04-28 ca pregătire pentru consultul inițial cu Dr. Mate Endre programat la 2026-04-30 ora 12:00.**

---

## Documentele necesare la primul consult la Oncologie (per OPIS oficial)

1. **Bilet de trimitere către Oncologie**
2. **Buletin** (carte de identitate)
3. **Card de sănătate**
4. **Adeverință de salariat (de la locul de muncă) SAU cupon de pensie**
5. **COPIE după rezultatul examenului histopatologic (BIOPSIE)**
6. **COPIE după scrisoarea medicală / biletul de ieșire din spital unde s-a efectuat biopsia / operația**
7. **COPIE după ALTE DOCUMENTE MEDICALE care susțin diagnosticul altor boli cronice** (diabet zaharat, boli renale, pulmonare, hipertensiune arterială, infarct miocardic, hipercolesterolemie, boli neurologice, digestive, psihiatrice sau alte boli cronice)
8. **Schemă cu medicamentele pe care și le administrează și modul în care și le administrează** (momentul de administrare pe parcursul zilei și doza medicamentului)

---

## Context consult inițial OncoHelp

- **Data programată:** 2026-04-30 ora 12:00
- **Medic programat:** Dr. Mate Endre (Medic Rezident Oncologie Medicală)
- **Unitate:** OncoHelp Timișoara, Str. Ciprian Porumbescu 57-59, 300239
- **Scop consult:** înregistrare pacient în baza de date OncoHelp + stabilire pași suplimentari pentru diagnostic exact (post-biopsie inconcluzivă)
- **Recomandare obținută de la:** Dr. Vornicu Vlad-Norin (telefon, 2026-04-28)
- **Prezența pacientului:** OPȚIONALĂ — Vornicu a recomandat că pot veni doar Roland + Maria cu documentația, NU obligatoriu cu pacientul

---

## Status colectare documente (per CONTEXT_MEDICAL §6 + dosar fizic)

| Punct OPIS                     | Document                                                                                                                           | Status în dosar                                                                              |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| 1 — Bilet trimitere Oncologie  | Bilet trimitere către Oncologie (de la medic familie sau gastroenterolog)                                                          | [DE OBȚINUT — întreabă user-ul, posibil Dr. Orbán Ecaterina sau Dr. Noufal]                  |
| 2 — Buletin                    | Carte identitate (`documente_sursa/01_identitate/2023-06-12_carte_identitate.pdf`)                                                 | ✅ disponibil digital                                                                        |
| 3 — Card sănătate              | Card sănătate fizic (la pacient)                                                                                                   | [DE LUAT FIZIC]                                                                              |
| 4 — Cupon pensie               | `documente_sursa/10_administrativ_pensie/2025-11-01_talon_pensie_scan.jpeg`                                                        | ✅ disponibil digital                                                                        |
| 5 — Histopatologic             | `documente_sursa/12_biopsie_2026/2026-04-17_biopsie_esofagiana_histopatologic.pdf`                                                 | ✅ disponibil digital (rezultat 27.04 — INCONCLUZIV, sugestiv carcinomatos, recomandare IHC) |
| 6 — Scrisoare medicală biopsie | NU s-a efectuat operație; biopsia s-a făcut în endoscopie de zi (`documente_sursa/09_endoscopie_2026_04/`)                         | ✅ disponibil (buletin gastroscopie + colonoscopie 17.04)                                    |
| 7 — Alte boli cronice          | DZ tip 2 (`schema_medicamente`), HTA (`scrisoare cardiologie 10.11.2025`), stent IVA 2012 (`cardiologie_vichy_stent`), hernie 2025 | ✅ toate disponibile                                                                         |
| 8 — Schemă medicamente         | `documente_sursa/08_schema_tratament/2025-11-10_schema_medicamente_manuscrise.json` + sinteză actuală în `CONTEXT_MEDICAL §4`      | ✅ disponibil                                                                                |

**Notă R23:** acest tabel de status este derivativ (corelare OPIS cu inventar dosar `.Tati`); transcrierea OPIS-ului propriu-zis (cele 8 puncte) este în secțiunea anterioară.

---

## Note suplimentare (extras meta.json companion)

- **Sursă PDF:** OncoHelp Timișoara — transmis digital către pacient/familie pe 2026-04-28
- **Folder dedicat creat:** `15_consult_initial_oncologie_2026/` (al 15-lea folder în structură R26 — adăugare 2026-04-28)
- **Mutat de Claude din rădăcina `Dosar_Medical/`** unde fusese plasat de user inițial (2026-04-28 dimineața), conform R26 (consistență structură foldere documente sursă)

---

## Observații pre-consult 30.04 (din `CONTEXT_MEDICAL §6` — sesiune planificare 28.04)

- Consultul cu Dr. Mate Endre 30.04 12:00 este distinct de consultul cu Dr. Anater + comisie programat pentru 4.05 (deadline critic). Mate Endre este consult inițial pentru înregistrare; Anater este consultul oncolog principal cu comisie multidisciplinară.
- Pe parcursul lui 30.04 sunt 3 evenimente:
  1. 08:30 Arad — consult cardiologic ambulator (programat 27.04)
  2. ~10:00 plecare Arad → Timișoara (~50 km, ~1h)
  3. 12:00 OncoHelp Timișoara — consult inițial Dr. Mate Endre

---

## Referințe legate

- `CONTEXT_MEDICAL.md §6` (Acțiuni în curs — secvența 30.04)
- `Dosar_Medical/CONTACTE_MEDICALE.md` (echipă medicală — Dr. Anater + Dr. Mate Endre + alți medici OncoHelp)
- `Documente_Informative/GHID_CONSULT_ONCOLOG.md` (ghid pregătire consult oncolog — checklist documente complet)
- `Dosar_Medical/2026-04-17_biopsie_esofagiana_histopatologic.json` (rezultat biopsie — punct 5 OPIS)
- `Dosar_Medical/documente_sursa/15_consult_initial_oncologie_2026/2026-04-28_opis_consult_initial_oncohelp.pdf.meta.json` (chain of custody R14)
