# AUDIT documente_sursa/ — Raport automat

**Generat:** 2026-04-28 12:55
**Script:** `scripts/audit_documente_sursa.py` (R14 chain of custody + R26 consistență structură)

## Stats

| Metric | Valoare |
|---|---|
| Total foldere | 15 |
| Foldere populate | 14 (93%) |
| Total fișiere PDF/JPEG | 28 |
| Cu `.meta.json` direct | 18 |
| Acoperite prin `intermediate_artifacts` | 10 |
| **Coverage R14 total** | **28/28 (100%)** |

## 🟠 Foldere goale > 30 zile (R26 — semnal P1)

_(niciun folder gol > 30 zile)_

## 🔴 Foldere cu nume non-canonic (R26 violation)

_(toate folderele sunt canonice — `NN_categorie_data/`)_

## 🔴 Fișiere fără `.meta.json` (R14 violation)

_(toate fișierele au companion `.meta.json` direct sau acoperire prin `intermediate_artifacts`)_

## 🟡 Fișiere cu nume non-canonic

_(toate fișierele respectă format `YYYY-MM-DD_descriere.ext`)_

## Acțiuni propuse

- Foldere goale > 30 zile → adăugare în `TODO.md` ca P1 (obținere documente lipsă)
- `.meta.json` lipsă → completare chain of custody (R14) la următoarea procesare. Pentru artefacte intermediare derivate dintr-un PDF master, declarați-le în `intermediate_artifacts.files` în meta-ul PDF-ului master (acoperire R14 indirectă).
- Nume non-canonice → redenumire cu confirmare user (R26 + R7)

---

_Raport regenerat automat la fiecare rulare a `scripts/audit_documente_sursa.py`. Înlocuiește versiunea anterioară. Pentru istoric, consultă git log._
