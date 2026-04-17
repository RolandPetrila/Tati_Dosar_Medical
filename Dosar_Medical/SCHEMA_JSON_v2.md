# SCHEMA_JSON v2.0 — Structura canonică pentru documentele medicale

**Versiune:** 2.0
**Data creare:** 2026-04-18
**Autor:** Claude Code, aprobat de Roland Petrilă

---

## Obiective

1. **Consistență** — toate documentele din `Dosar_Medical/` au aceeași structură la nivelul 1 de chei.
2. **Parse-ability AI** — separate explicit `valoare_numerica` și `valoare_text`, `interval_referinta_min/max/text`, `flag` uniform.
3. **Trasabilitate** — `sursa_pdf`, `procesat_de`, `confidence_ocr` per câmp sensibil.
4. **Cronologie** — date în ISO 8601 (`YYYY-MM-DD`).
5. **Anti-halucinație** — Regula 8 din `CLAUDE.md` proiect: marchez ce e incert, nu completez din context.

## Structura completă

```json
{
  "_metadata": {
    "schema_version": "2.0",
    "nume_fisier": "YYYY-MM-DD_slug.json",
    "tip_document": "bilet_iesire | scrisoare_medicala | buletin_analize | schema_tratament | carte_identitate | talon_pensie | buletin_endoscopie | ...",
    "specialitate": "Chirurgie Generală | Cardiologie | Gastroenterologie | Laborator | ...",
    "data_document": "YYYY-MM-DD",
    "sursa_pdf": "nume_fisier_original.pdf | .jpeg",
    "sursa_locatie": "documente_sursa/NN_subfolder/",
    "procesat_de": "Gemini | Claude_Opus_4.7 | Roland_manual",
    "data_procesare": "YYYY-MM-DD",
    "ocr_quality": "good | partial | failed | n/a",
    "confidence_overall": "high | medium | low",
    "flags": [
      "duplicate_of:alt_fisier.json",
      "verified_against:CI_pdf",
      "contains_manuscript",
      "contains_ocr_errors",
      "requires_review"
    ],
    "notes": "observații libere, discrepanțe, surse secundare"
  },

  "pacient": {
    "nume": "PETRILĂ",
    "prenume": "VIOREL-MIHAI",
    "cnp": "1590518024486",
    "data_nasterii": "1959-05-18",
    "varsta_la_data_document": 66,
    "sex": "M",
    "confidence_identificare": "high | medium | low",
    "note_identificare": "opțional — dacă documentul conține identificator diferit/parțial"
  },

  "diagnostic": [
    {
      "cod_icd10": "K40.90",
      "descriere_oficiala": "Hernia inghinală unilaterală, fără obstrucție/gangrenă",
      "descriere_originala": "text exact din PDF, păstrat ad litteram",
      "cod_intern_spital": "564",
      "tip": "principal | secundar | asociat",
      "confidence_ocr": "high | medium | low"
    }
  ],

  "analize_laborator": [
    {
      "nume": "Glicemie",
      "nume_original": "GLUCOZA",
      "valoare_numerica": 136.1,
      "valoare_text": "136.1",
      "unitate": "mg/dL",
      "interval_referinta_min": 70,
      "interval_referinta_max": 115,
      "interval_referinta_text": "70-115",
      "flag": "normal | crescut | scazut | patologic | critic | necunoscut",
      "confidence_ocr": "high | medium | low",
      "note": "opțional"
    }
  ],

  "tratament": [
    {
      "medicament_sau_procedura": "ASPENTER",
      "substanta_activa": "acid acetilsalicilic",
      "doza": "75 mg",
      "frecventa": "1-0-0",
      "moment_administrare": "dimineața",
      "durata": "cronic | 7 zile | ...",
      "indicatie": "antiagregant post-stent",
      "detalii_ambalaj": "28 cpr gastrorezistente",
      "detalii": "text liber suplimentar",
      "confidence_ocr": "high | medium | low"
    }
  ],

  "recomandari": [
    "Control chirurgical la 7 zile",
    "Evitarea eforturilor fizice mari"
  ],

  "medici_unitati": {
    "medic_curant": "Dr. Noufal Abdul Vahab",
    "unitate": "Genesis Medical Clinic Arad",
    "sectie": "Gastroenterologie",
    "medic_trimitator": "opțional",
    "cod_unitate": "opțional"
  },

  "numere_referinta": {
    "numar_bilet": "BCTAP 0631727",
    "numar_dosar": "42/355336",
    "alte_identificatori": {}
  }
}
```

## Reguli de completare

### 1. Câmpuri obligatorii

La nivel de `_metadata`:

- `schema_version`, `nume_fisier`, `tip_document`, `data_document`, `sursa_pdf`, `procesat_de`, `data_procesare`, `ocr_quality`.

La nivel de `pacient`:

- `nume`, `prenume`, `cnp`, `data_nasterii`, `sex`.

### 2. Câmpuri opționale (absența = câmp inexistent, NU null cu excepția nevoii explicite)

- `cod_icd10` poate fi `null` DOAR dacă documentul nu îl conține și nu există mapping evident.
- `interval_referinta_*` absent dacă laboratorul nu furnizează — NU inventat.
- `valoare_numerica` absent dacă valoarea e exclusiv text (ex. `"pozitiv"`, `"absent"`).

### 3. Date ambiguă din manuscris sau OCR

- `descriere_originala` păstrează **textul brut** din PDF.
- `descriere_oficiala` e versiunea corectată/normalizată.
- `confidence_ocr`: `low` dacă <80% siguranță.
- `_metadata.flags` include `contains_ocr_errors` dacă e cazul.

### 4. Unități lab

Convenții obligatorii:

- `mg/dL` (nu `mg/dl`)
- `x10^3/µL` (nu `10^3/ul` sau `µg/dl`)
- `mmol/L`
- `U/L`
- `%`
- `ng/mL`
- `µUI/mL`
- `pg/mL`

### 5. Flaguri lab (`flag`)

| Flag         | Criteriu                                                              |
| ------------ | --------------------------------------------------------------------- |
| `normal`     | valoare ∈ interval referință                                          |
| `crescut`    | valoare > max interval                                                |
| `scazut`     | valoare < min interval                                                |
| `patologic`  | documentul însuși marchează "patologic" fără direcție clară           |
| `critic`     | valoare cu semnificație clinică imediată (decis de om, nu de automat) |
| `necunoscut` | lipsa interval referință                                              |

### 6. Date ISO 8601

Toate datele: `YYYY-MM-DD`. Conversia din format românesc `DD.MM.YYYY` se face la procesare. Câmpul `data_document` e mereu în ISO.

### 7. Diacritice

- Nume pacient: păstrat cu diacritice dacă e în C.I. (`PETRILĂ`).
- Text medical: păstrat ca în document original (dacă medicul a scris fără diacritice, rămâne așa în `descriere_originala`).

## Exemplu minimal

```json
{
  "_metadata": {
    "schema_version": "2.0",
    "nume_fisier": "2026-04-17_buletin_gastroenterologie.json",
    "tip_document": "buletin_endoscopie_colonoscopie",
    "specialitate": "Gastroenterologie",
    "data_document": "2026-04-17",
    "sursa_pdf": "Gastroscopic_Colonoscopic.pdf",
    "sursa_locatie": "documente_sursa/09_endoscopie_2026_04/",
    "procesat_de": "Gemini",
    "data_procesare": "2026-04-17",
    "ocr_quality": "good",
    "confidence_overall": "high"
  },
  "pacient": {
    "nume": "PETRILĂ",
    "prenume": "VIOREL-MIHAI",
    "cnp": "1590518024486",
    "data_nasterii": "1959-05-18",
    "varsta_la_data_document": 66,
    "sex": "M",
    "confidence_identificare": "high"
  },
  "diagnostic": [
    {
      "cod_icd10": null,
      "descriere_oficiala": "Proces proliferativ esofagian",
      "descriere_originala": "PROCES PROLIFERATIV ESOFAGIAN",
      "tip": "principal",
      "confidence_ocr": "high"
    }
  ],
  "analize_laborator": [],
  "tratament": [],
  "recomandari": ["Revine pentru polipectomie"],
  "medici_unitati": {
    "medic_curant": "Dr. Noufal Abdul Vahab",
    "unitate": "Genesis Medical Clinic Arad",
    "sectie": "Gastroenterologie"
  }
}
```

## Migrare v1 → v2

Regulile aplicate la migrarea JSON-urilor Gemini:

1. Înveliș `_metadata` îmbogățit cu noile câmpuri; vechi păstrate.
2. `pacient` îmbogățit cu `varsta_la_data_document`, `confidence_identificare`.
3. `diagnostic[]` primește `descriere_originala`, `cod_intern_spital`, `tip`, `confidence_ocr`.
4. `analize_laborator[]` primește `valoare_numerica`, `interval_referinta_min/max`, `flag`, `confidence_ocr`.
5. Corecturi de date factuale aplicate, cu `_metadata.notes` care documentează modificarea.

---

**Ultima revizuire:** 2026-04-18.
