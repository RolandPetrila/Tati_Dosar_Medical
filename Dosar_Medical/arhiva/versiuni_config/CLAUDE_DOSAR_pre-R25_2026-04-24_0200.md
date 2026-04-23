# CLAUDE.md — `Dosar_Medical/` (reguli nested specifice)

**Versiune:** 12.1 (adăugare R23 extragere integrală) | **Data:** 2026-04-24

> **Acest fișier conține reguli care se aplică DOAR când Claude lucrează cu conținutul din `Dosar_Medical/`** (extrageri OCR, JSON-uri medicale structurate, documente sursă, chain of custody, backup pre-modificare).
>
> Se încarcă **contextual** — nu consumă context când lucrezi în alte zone ale proiectului.
>
> **Regulile 6, 7, 12, 16, 17, 18, 20, 21, 22 se aplică always-on** — sunt în `REGULI_CLAUDE_CODE.md` la rădăcină.
>
> **Regula 19** (Documente_Informative) se încarcă **contextual** — e în `Documente_Informative/CLAUDE.md` (nested, ca acest fișier).

---

## Regula 8 — Protecție anti-halucinație OCR

La text provenit din OCR (PDF scanat, fotografie document), niciodată nu completezi zone ilizibile din context.

**Protocol:**

1. Text corupt / caractere lipsă → marchează `[ILIZIBIL]` sau `[INCERT]` la transcriere
2. Existența unui `Eroare_Format_*.txt` pentru un document = semnal că OCR-ul a eșuat → tratează originalul ca sursă primară, cere re-scanare / transcriere manuală
3. NU inventa valori care „par logice în context"
4. Cifre din analize / doze cu incertitudine OCR → `[CIFRĂ INCERTĂ: X sau Y]` + escaladare
5. **Sub-clauză 8.1 — cuvinte contopite:** NU deduce interpretarea unui text contopit dintr-un PDF („circumferentialne depasibila"). Păstrează textul original literal + listează variantele de segmentare + escaladează la user pentru clarificare (incident 2026-04-19).

**Why:** în `Dosar_Medical/` există deja `Eroare_Format_*.txt` — dovadă că digitizarea e imperfectă. O cifră halucinată într-o analiză = risc clinic direct.

**How to apply:** la fiecare procesare de PDF scanat sau fotografie document medical.

---

## Regula 9 — Coordonare Claude ↔ Gemini

În folderul `.Tati` coexistă `GEMINI.md` cu reguli diferite (permite modificare directă în orice subfolder). Pentru a evita conflicte silent:

**Protocol:**

1. La deschidere sesiune: verifică timestamp-ul ultimelor modificări în `CHANGELOG.md` și în fișierele de referință
2. La modificări majore în fișiere de referință: adaugă linie în `SESSION_LOG.md`:

   ```
   [YYYY-MM-DD HH:MM] [Claude|Gemini] [slug-operație] [lista-fișiere]
   ```

3. Înainte de a suprascrie conținut modificat recent (< 1 oră) de celălalt agent → STOP, cere confirmare user
4. NU presupune că celălalt agent a greșit; poate fi lucru deliberat

**Why:** doi agenți pe același dosar fără coordonare = conflicte silent, pierdere de informație. GEMINI.md permite modificări libere, deci Claude trebuie să fie cel defensiv.

**How to apply:** la orice sesiune care modifică fișiere de referință, verifică `SESSION_LOG.md` și loghează propria intenție.

---

## Regula 10 — Backup înainte de modificări majore

Înainte de orice modificare structurală la un fișier de referință, creezi backup explicit în `arhiva/`.

**„Modificare majoră" =**

- Rescriere de secțiune întreagă
- Ștergere sau mutare de conținut
- Schimbare format / structură
- Update la date medicale deja înregistrate

**Format backup:**

```
arhiva/[nume_fisier]_pre-[slug-operatie]_YYYY-MM-DD_HHMM.ext
```

Exemplu: `arhiva/CONTEXT_MEDICAL_pre-adaugare-CT-toracic_2026-04-17_2345.md`

Pentru backup-urile CLAUDE.md folosește `Dosar_Medical/arhiva/versiuni_config/` (convenția sesiunilor anterioare).

**Why:** Google Drive nu are git; singurul mecanism real de rollback = copia explicită. Regula existentă „nu ștergi" e incompletă fără „salvezi înainte de a modifica structural".

**How to apply:** backup = PRIMUL pas într-o secvență de modificare majoră, apoi modifici.

---

## Regula 11 — Marcaj valabilitate clinică temporală

Orice dată medicală temporală se marchează cu vechimea la citare.

**Praguri:**

| Tip informație                  | < 3 luni                | 3-6 luni                               | 6-12 luni                          | > 12 luni            |
| ------------------------------- | ----------------------- | -------------------------------------- | ---------------------------------- | -------------------- |
| Analiză laborator               | validă fără avertisment | `[de reverificat dacă decizia o cere]` | `[POTENȚIAL STALE]` + reverificare | repetare obligatorie |
| Imagistică (CT/RMN/ECO)         | validă                  | validă cu mențiunea datei              | reverificare                       | repetare obligatorie |
| Ghiduri terapeutice (ESMO/NCCN) | validă                  | validă                                 | verifică ediția curentă            | ediția e obsolete    |

**Matrice extinsă + cazuri speciale:** `Documentatie_Initiala/REGULI_DETALIATE.md` §R11.

**Why:** o cifră corectă acum 8 luni poate fi irelevantă clinic astăzi. Prezentare fără context temporal = informație înșelătoare.

**How to apply:** la orice citare de valoare numerică din dosar, include data sursei.

---

## Regula 13 — Transcriere documente scrise de mână

Pentru text manuscris (scrisori medicale, bilete de trimitere, rețete):

**Protocol:**

1. Transcriere cu marcaj confidence: `[TRANSCRIERE confidence ~60%: „text aproximativ"]`
2. Cuvânt ambiguu → variante: `[„aspirin" | „aspirină" | „aspirat"]`
3. Nume proprii (medic, spital, medicament) → confidence obligatoriu
4. Cifre (doze, date) → confidence obligatoriu; la <80% confidence → cere confirmare user

**Why:** manuscrisul medical e notoriu dificil de descifrat; interpretare greșită a unei doze = risc.

**How to apply:** la fiecare scanare de document manuscris, înainte de integrare în `CONTEXT_MEDICAL.md`.

---

## Regula 14 — Chain of custody documente sursă

Pentru fiecare document nou adăugat în `Dosar_Medical/`, creezi fișier însoțitor metadata.

**`[nume_document].meta.json`:**

```json
{
  "source_document": "nume_fisier.pdf",
  "received_date": "YYYY-MM-DD",
  "received_from": "spital X / cabinet Y / pacient / familie",
  "digitized_by": "scanner / foto / email / portal online",
  "digitized_date": "YYYY-MM-DD",
  "transcriber": "Claude / Gemini / Roland manual",
  "ocr_quality": "good / partial / failed",
  "chain_notes": "orice informație relevantă"
}
```

**Why:** la consult secundar sau litigiu, proveniența unui document e parte din valoarea lui clinică și legală.

**How to apply:** la adăugarea oricărui document nou în `Dosar_Medical/`, creezi `.meta.json` corespunzător.

---

## Regula 15 — Log cercetări web

Pentru fiecare cercetare web care produce conținut introdus în dosar, log în `WEB_QUERIES.md` (la rădăcina proiectului):

**Format:**

```markdown
## YYYY-MM-DD HH:MM — [slug-subiect]

- **Query:** "...exact ce ai căutat..."
- **Surse acceptate:** [URL-uri + motiv acceptare]
- **Surse respinse:** [URL-uri + motiv respingere: comercial / blog / outdated / nu peer-reviewed]
- **Concluzie introdusă în:** [fișier + secțiune]
- **Data publicării materialului:** [când a fost publicat / ultima actualizare]
```

**Why:** la verificare ulterioară, user sau medicul trebuie să poată reconstitui de unde vine o afirmație.

**How to apply:** după fiecare cercetare web care generează conținut factual introdus într-un fișier de referință.

---

## Regula 23 — Extragere integrală din documente medicale sursă

Orice element medical dintr-un document sursă (PDF, scan, foto, manuscris) DEVINE parte din JSON-ul structurat — fără filtrare pe criteriu de „relevanță clinică" decisă de AI.

**Interzis explicit:**

- Considerarea unui element ca „de fundal", „colateral fără impact", „normal irelevant"
- Rezumarea secțiunilor descriptive („aspect normal [organ]") fără menționare în JSON
- Filtrarea pe criteriul „probabil benign", „sechelar vechi", „fără impact decizional"
- Omiterea valorilor tehnice (doză radiație DLP, parametri tehnici examinare, numere buletin)

**Obligatoriu în JSON:**

1. Toate findings-urile pozitive (leziuni, modificări, anomalii) — detaliate
2. Toate findings-urile negative explicite („aspect normal [organ]") — listate într-o secțiune dedicată
3. Parametri tehnici ai examinării (doze, aparat, substanță contrast, volum)
4. Toate valorile numerice din buletine (nu doar „în limite normale")

**Validare post-extragere:**

- Re-citire PDF sursă la final, confirmare zero omisiuni
- Marcaj în `.meta.json`: `"completeness_verified": "YYYY-MM-DD"`, `"coverage": "100%"`, `"validator": "claude-opus-4-7"`

**Why:** AI nu are autoritate clinică să decidă ce element medical e relevant. Incident 2026-04-23: tulburări ventilație posterobazal + noduli apicali sechelari + modificări degenerative disco-vertebrale + aspecte normale (colecist, pancreas, splină, prostată, suprarenală dreaptă, tiroidă, aortă, artera pulmonară) + doza radiație DLP = **omise din `CONTEXT_MEDICAL.md`** deși prezente în JSON sursă (`2026-04-20_ct_torace_abdomen_pelvis.json`). Root cause: filtrare subiectivă pe „relevanță clinică" clasificată greșit ca „de fundal". Elemente omise relevante pre-esofagectomie (spirometrie, kinetoterapie respiratorie, anamneză TBC vechi).

**How to apply:** pas 1 obligatoriu = extragere literală integrală în JSON ÎNAINTE de orice interpretare sau rezumat. Validare la finalul extragerii = re-citește PDF-ul și confirmă coverage 100%. Propagarea rezultatului JSON în `CONTEXT_MEDICAL.md` este acoperită de **Regula 24** (în `REGULI_CLAUDE_CODE.md`).

---

## Reguli complementare (pointeri)

Pentru reguli care se aplică și în `Dosar_Medical/` dar sunt always-on (`REGULI_CLAUDE_CODE.md` la rădăcină):

- **Regula 17** (marcaje `[CERT]`/`[PROBABIL]`/`[INCERT]`/`[NEGASIT]`) — toate JSON-urile și documentele generate respectă marcajul
- **Regula 22** (verificare proactivă `[INCERT]`) — aplicabilă pe JSON-uri + rapoarte + sinteze
- **Regula 10 backup** se corelează cu **Regula 21 curățenie** (arhivarea e pentru versiuni de referință modificate structural, NU pentru ciorne)

## Note pentru lucrul în `Dosar_Medical/`

- **Subfoldere:** `arhiva/` (backup-uri), `cercetari/` (sinteze cercetare web validate), `documente_sursa/` (scanuri originale, READ-ONLY), `rapoarte_generate/` (DOCX-uri pentru medici).
- **JSON-urile medicale** respectă schema documentată în `SCHEMA_JSON_v2.md`. Modificările la schemă se coordonează cu workspace-ul paralel `.Tati_Documente_Medicale` (vezi DECIZII_FORMAT_FISIERE v3.0 propusă acolo).
- **Documentele sursă** (`.pdf`, `.jpeg`) sunt **READ-ONLY** absolut — nu se suprascriu, redenumesc, șterg.
