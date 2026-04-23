# EXTRAGERI_INCOMPLETE.md — Log elemente NEEXTRASE din documente sursă

**Scop:** transparență pentru orice AI/user care deschide proiectul — listă completă a elementelor medicale care NU s-au integrat în dosarul structurat (JSON + `CONTEXT_MEDICAL.md`) pentru că sursele au fost indescifrabile (manuscris ilizibil, OCR eșuat, scan degradat).

**Obligatoriu (conform Regula 25):**

1. **La detectare element indescifrabil** în procesare document → adaugă intrare în acest fișier (format standard mai jos) + informează user-ul ACTIV în mesaj
2. **La start sesiune** cu procesare documente noi → citire obligatorie acest fișier pentru context (evită re-întrebarea user-ului pe elemente deja confirmate ca inaccesibile)
3. **La rezolvare** (clarificare telefonică, re-scanare, transcriere manuală user) → update status la 🟡 → ✅ + data rezolvării + sursă de verificare

**Referință regulă completă:** vezi `Regula 25` în `Dosar_Medical/CLAUDE.md` („Prioritate claritate > completitudine la surse indescifrabile").

**Reguli adiacente:**

- `Regula 8` (OCR anti-halucinație) — `Dosar_Medical/CLAUDE.md`
- `Regula 13` (transcriere manuscrise cu confidence) — `Dosar_Medical/CLAUDE.md`
- `Regula 23` (extragere integrală din surse) — `Dosar_Medical/CLAUDE.md`
- `Regula 24` (propagare integrală JSON → `CONTEXT_MEDICAL.md`) — `REGULI_CLAUDE_CODE.md`

---

## Format intrare standard

```markdown
## YYYY-MM-DD — [slug_document]

- **Document sursă:** `Dosar_Medical/documente_sursa/.../fisier.ext`
- **Tip problemă:** manuscris ilizibil / OCR eșuat / scan degradat / text tăiat / altele
- **Elemente NE-integrate (aplicare R25):** [listă + motiv pentru fiecare]
- **Elemente integrate parțial (CERT):** [ce a fost clar + sursă]
- **Impact clinic:** [dacă are implicații pentru tratament / decizii / monitorizare]
- **Acțiune propusă pentru rezolvare:** [clarificare telefonică / re-scanare / transcriere manuală user / acceptare lipsă]
- **TODO.md ref:** [task-ul P0-P3 corespunzător, dacă există]
- **Status:** 🟡 deschis / ✅ rezolvat (YYYY-MM-DD — cum)
```

---

## 2026-04-24 — schema medicamente 10.11.2025 (manuscris parțial ilizibil)

- **Document sursă:** `Dosar_Medical/documente_sursa/08_schema_tratament/2025-11-10_schema_medicamente_manuscris.jpeg`
- **Tip problemă:** manuscris parțial ilizibil (numele medicului prescriptor) + text tăiat cu marker (linia 4 a talonului — recomandare anulată de medic)
- **Elemente NE-integrate (aplicare R25):**
  - **Numele medicului prescriptor** — transcriere "Dr. LAZĂR" cu confidence LOW (surname parțial ilizibil, prenume necunoscut, unitate necunoscută). Conform R25, refuz atribuire cu confidence <90% pe elemente critice (nume medic curant).
  - **Linia 4 a talonului** (recomandare tăiată cu marker albastru) — conținut nelizibil sub tăieturi; recomandare anulată de medic → conținut irelevant clinic, dar se notează existența pentru chain of custody.
- **Elemente integrate parțial (CERT):**
  - Medicația (Aspenter 75 mg, Concor 5 mg, Triplixam 10/2.5/5 mg, Jamesi 50/1000 mg) — confirmat prin fotografii cutii (denumire comercială + doză tipărite pe ambalaj) + ritm administrare scris de mână lizibil (0-1-0, 1-0-0, 1-0-0, 1-0-1)
  - Pacient: PETRILĂ VIOREL-MIHAI (corectat retroactiv din manuscris original „PETRICĂ VIOREL" — eroare medic la scris — via cross-reference cu carte identitate + context clinic)
  - Data documentului: 10.11.2025 (lizibil)
- **Impact clinic:** minim — schema de medicație e clară și utilizabilă; atribuirea prescriptor e necunoscută, dar nu afectează continuitatea tratamentului. Identificarea medicului curant rămâne utilă pentru context (schimbare doze pre-chirurgie esofagiană, consultanță post-diagnostic).
- **Acțiune propusă pentru rezolvare:** clarificare telefonică cu familia pentru identificarea medicului prescriptor (cabinet, nume complet, specialitate, unitate)
- **TODO.md ref:** `[P1] Identificare medic prescriptor schema 10.11.2025 (manuscris parțial ilizibil — R25)`
- **Status:** 🟡 deschis

---

## Istoric completitudine

- **2026-04-24:** fișier creat post-adoptare Regula 25; prima intrare = schema medicamente 10.11.2025 (LAZĂR)
