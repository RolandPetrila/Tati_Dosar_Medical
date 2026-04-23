# CLAUDE.md — `Documente_Informative/` (reguli nested specifice)

**Versiune:** 12.0 | **Data:** 2026-04-23

> **Acest fișier conține reguli care se aplică DOAR când Claude lucrează cu conținutul din `Documente_Informative/`** (materiale operaționale: ghiduri, explicații, checklist-uri pentru Roland sau familie).
>
> Se încarcă **contextual** — nu consumă context când lucrezi în alte zone ale proiectului.

---

## Regula 19 — Documente informative în `Documente_Informative/` (NU la rădăcină)

**Context:** user a solicitat explicit pe 2026-04-22 să nu se mai salveze documente operaționale/informative (ghiduri, explicații, materiale pentru familie) direct la rădăcina proiectului — acea zonă e rezervată fișierelor structurale (`CLAUDE.md`, `REGULAMENT.md`, `REGULI_CLAUDE_CODE.md`, `CONTEXT_MEDICAL.md`, `TODO.md`, `CHANGELOG.md`, `DASHBOARD.html`, etc.).

**Locație canonică:** `Documente_Informative/` (rădăcina proiectului, CamelCase consistent cu `Documentatie_Initiala/` și `Dosar_Medical/`).

**Tip conținut destinat aici:**

- Ghiduri acționabile pentru Roland sau familie (`GHID_*.md`)
- Explicații simplificate ale unor termeni medicali / protocoale
- Materiale de pregătire pentru consulturi / intervenții
- Checklist-uri operaționale care nu sunt parte din structura dosarului medical propriu-zis
- Orice alt material informativ care NU e:
  - date structurate medicale (→ `Dosar_Medical/*.json`)
  - documente sursă digitizate (→ `Dosar_Medical/documente_sursa/`)
  - rapoarte DOCX generate pentru medici (→ `Dosar_Medical/rapoarte_generate/`)
  - fișiere de stare proiect (→ rădăcină)

**Format denumire:** `GHID_SUBIECT.md` sau `EXPLICATIE_SUBIECT.md` sau `MATERIAL_SUBIECT_YYYY-MM-DD.md` — UPPERCASE pentru titlul principal, descriptiv pentru scanare rapidă de familie.

**Why:** rădăcina proiectului aglomerată cu documente operaționale face navigarea dificilă și amestecă fișierele de configurare (care nu se ating) cu materialele de lucru zilnice (care se multiplică în timp).

**How to apply:** la orice cerere viitoare de creare ghid / explicație / material pentru familie / medic → destinația e `Documente_Informative/`, NU rădăcina. Fișiere informative existente incorect plasate se pot muta cu ocazie, cu confirmarea user.

---

## Regula 17 (shortcut pentru documente informative)

**Documentele din `Documente_Informative/` sunt destinate familiei/pacientului și conțin frecvent afirmații medicale factuale.** Prin urmare, **Regula 17 (marcaje certitudine) se aplică integral** la conținutul generat aici.

**Reguli minime obligatorii:**

- Fiecare afirmație medicală factuală → marcată `[CERT]` / `[PROBABIL]` / `[INCERT]` / `[NEGASIT]`
- Secțiune „Surse citate" la final (URL + data accesării + versiunea sursei)
- Secțiune „Ce NU am găsit" (transparență pentru întrebările neacoperite)
- Atenționare finală: „NU înlocuiește consultul medical."

**Detalii complete Regula 17:** `REGULI_CLAUDE_CODE.md` §R17 + exemple complete în `Documentatie_Initiala/REGULI_DETALIATE.md` §R17.

---

## Note pentru lucrul în `Documente_Informative/`

- Fișierele din acest folder sunt citite de **familia pacientului** (non-medici). Limbajul trebuie accesibil, fără jargon medical nedefinit.
- Generările DOCX ale acestor ghiduri (dacă user solicită) merg în `Dosar_Medical/rapoarte_generate/` (convenție consacrată).
- La crearea unui ghid nou → declanșator potențial pentru update la `CONTEXT_MEDICAL.md` (dacă conține informații noi) + log în `CHANGELOG.md`.
