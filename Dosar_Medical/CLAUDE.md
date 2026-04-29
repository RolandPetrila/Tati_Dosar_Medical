# CLAUDE.md — `Dosar_Medical/` (reguli nested specifice)

**Versiune:** 12.3 (adăugare R26 consistență structură foldere + semnalare devieri) | **Data:** 2026-04-24

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

**How to apply:** pas 1 obligatoriu = extragere literală integrală în JSON ÎNAINTE de orice interpretare sau rezumat. Validare la finalul extragerii = re-citește PDF-ul și confirmă coverage 100%. Propagarea rezultatului JSON în `CONTEXT_MEDICAL.md` este acoperită de **Regula 24** (în `REGULI_CLAUDE_CODE.md`). Documentele indescifrabile se tratează conform **Regula 25** (mai jos).

---

## Regula 25 — Prioritate claritate > completitudine la surse indescifrabile

Documentele medicale sursă care nu pot fi citite clar (manuscris ilizibil, scan degradat, OCR eșuat) **NU se integrează în JSON structurat al dosarului**. Se păstrează ca sursă fizică pentru revizuire manuală (user, familie, medicul curant).

**Interzis:**

- Transcriere cu „confidence aproximativ" pentru elemente medicale critice (doze, nume medicamente, date, valori laborator, nume medici curanți, spitale)
- Presupunere variante contextuale ca fiind acceptabile pentru integrare (ex: `[„aspirin" | „aspirină" | „aspirat"]` — alegere arbitrară între variante)
- Marcaj `[ILIZIBIL]` ca substituit pentru date reale (perpetuează info incompletă, nu rezolvă problema)

**Permis:**

- **Integrare parțială:** dacă o parte a documentului e clar descifrabilă (ex: cutii medicamente fotografiate lizibil + doze scrise de mână clar), aceasta se integrează. Partea ilizibilă se OMIT COMPLET din JSON — nu se marchează cu placeholder.
- `.meta.json` marchează pentru transparență chain of custody: `"indescifrabil_partial": true, "excluded_elements": ["nume medic", "dată prescriere", ...]`.
- **Escaladare la user:** pentru elemente critice ilizibile (doze, nume medicamente), alertă pentru transcriere manuală sau clarificare telefonică cu medicul emitent.

**Tracking obligatoriu (`Dosar_Medical/EXTRAGERI_INCOMPLETE.md`):**

- Fiecare detectare de element indescifrabil → intrare în `Dosar_Medical/EXTRAGERI_INCOMPLETE.md` (format standard definit în fișier).
- **Notificare ACTIVĂ user în mesaj** la fiecare detectare: menționez explicit „am identificat X elemente din documentul Y care NU s-au integrat din cauza caracterului indescifrabil — v. EXTRAGERI_INCOMPLETE.md".
- **Citire obligatorie** la start sesiune de către orice AI care procesează documente noi — `EXTRAGERI_INCOMPLETE.md` listează ce NU e în dosar, pentru ca AI-ul să nu presupună că info lipsește accidental și să nu re-întrebe user-ul pe elemente deja confirmate ca inaccesibile.

**Relația cu R23 (extragere integrală):** R25 este excepția la R23. R23 cere integrare integrală A CEEA CE POATE FI CITIT CLAR. Sursă indescifrabilă integral → nu se integrează deloc. Sursă parțial descifrabilă → integrează doar partea clară; partea ilizibilă se omite (fără placeholder).

**Relația cu R13 (transcriere manuscrise):** R13 oferă metodologia de transcriere cu confidence; R25 spune când să renunți la transcriere. Dacă R13 generează transcriere cu sub-elemente `[INCERT]`/`[ILIZIBIL]` pe elemente critice → decizia R25 este „scoate elementele respective, păstrează doar CERT".

**Why:** incident 2025-11-10 schema medicamente — numele pacientului transcris „PETRICĂ" din manuscris, corectat retroactiv la „PETRILĂ"; Dr. LAZĂR rămâne parțial ilizibil. Info eronată din transcriere cu confidence slab e mai periculoasă decât absența info (medicul cere clarificare la info lipsă, dar info greșită poate trece neobservată).

**How to apply:** la fiecare document manuscris / scan degradat / OCR eșuat, primul pas = decide categoria:

1. **Lizibil integral** → R23 aplicabil (integrare completă)
2. **Parțial lizibil** → R23 + R25 (integrare selectivă + scoatere elemente ilizibile, FĂRĂ placeholder)
3. **Indescifrabil integral** → neintegrat; marcaj în `.meta.json` + document rămâne sursă fizică + intrare în `EXTRAGERI_INCOMPLETE.md`

După decizie, notificare user în mesaj + intrare în `EXTRAGERI_INCOMPLETE.md` (obligatoriu pentru categoriile 2 și 3).

---

## Regula 26 — Consistență structură foldere documente sursă + semnalare devieri

Toate documentele sursă din `Dosar_Medical/documente_sursa/` urmează același model de organizare, pentru a permite regăsire rapidă în consult medical critic și indexare automată viitoare.

**Convenție foldere:** `NN_categorie_data/`

- `NN` = număr ordinal cu zero padding (01, 02, ..., 99)
- `categorie` = lowercase cu underscore, descriptiv (`identitate`, `analize_laborator`, `hernie_2025_11`, `CT_stadializare_2026`, etc.)
- `data` = `YYYY` sau `YYYY_MM` (anul + luna unde relevant pentru delimitarea evenimentelor)
- **Excepție istorică:** `99_altele/` a existat până 2026-04-24 ca catch-all **PROVIZORIU** — **ELIMINAT** după integrarea conținutului din Arhiva_Generala. Nu se re-creează — documentele nedigitizate/neclasificate se plasează direct în folderul tematic corespunzător sau se creează folder nou dedicat.

**Convenție fișiere în folder:**

- PDF/imagine sursă: `YYYY-MM-DD_descriere_scurta.{pdf,jpeg,jpg,png}`
- `.meta.json` companion obligatoriu (chain of custody — Regula 14): `YYYY-MM-DD_descriere_scurta.{ext}.meta.json`

**Categorii folosite în proiect (status 2026-04-24 post integrare Arhiva_Generala + Boala_Actuala + audit remediere):**

| Folder                               | Conținut așteptat                                                                                             | Status                                                                                                                                                                                  |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `01_identitate/`                     | Carte identitate, pașaport                                                                                    | ✅ populat (2023-06-12_carte_identitate.pdf + .meta.json)                                                                                                                               |
| `02_cardiologie_2012/`               | Stent Vichy 2012                                                                                              | ✅ populat 2026-04-28 (`2012-02-17_cardiologie_vichy_stent.pdf` + meta + extragere MD; redenumit 2026-04-28 din `Document_Cardiologie_Vichy_2012.pdf` conform R26; stent confirmat BMS) |
| `03_hernie_anterior/`                | Hernie anterioară (dată necunoscută)                                                                          | 🟡 folder gol — document de identificat                                                                                                                                                 |
| `04_helicobacter_2024/`              | Serologie H. pylori IgG iunie+septembrie 2024                                                                 | ✅ populat (2024-06-04 + 2024-09-06 buletine integrate în 1 PDF)                                                                                                                        |
| `05_analize_laborator/`              | Buletine analize sânge / urină / serologie                                                                    | ✅ populat (2025-06-17 panel complet + 2026-04-17 bioclinica uree/creatinină)                                                                                                           |
| `06_urologie_gastro_2025/`           | Scrisoare urologie + ecografie scrotală 28.10.2025                                                            | ✅ populat (Dr. Pitea)                                                                                                                                                                  |
| `07_hernie_2025_11/`                 | Intervenție hernie noiembrie 2025 (Dr. Papiu)                                                                 | ✅ populat (bilet iesire + scrisoare anexa43)                                                                                                                                           |
| `08_schema_tratament/`               | Scheme medicație manuscrise                                                                                   | ✅ populat (2025-11-10 + .meta.json)                                                                                                                                                    |
| `09_endoscopie_2026_04/`             | Buletine gastroscopie + colonoscopie 17.04.2026                                                               | ✅ populat (Dr. Noufal Abdul Vahab, 2 JPEG separate)                                                                                                                                    |
| `10_administrativ_pensie/`           | Talon pensie, dovezi asigurare                                                                                | ✅ populat (talon 11/2025 + .meta.json)                                                                                                                                                 |
| `11_CT_stadializare_2026/`           | Bilet trimitere CT + raport CT 20.04.2026                                                                     | ✅ populat (BCTAP 0631727 + 2026-04-20_ct_torace_abdomen_pelvis.pdf, redenumit 2026-04-28 din `CT - Genesys.pdf` conform R26; mutat de user 2026-04-24 din fostul 99_altele/)           |
| `12_biopsie_2026/`                   | Rezultat biopsie Bioclinica                                                                                   | 🟡 folder gol — așteptare rezultat histopatologic (monitor automat ntfy activ 24/7)                                                                                                     |
| `13_cardiologie_ambulator_2025/`     | Consult cardiologie + ECO 10.11.2025 (Dr. LAZA CRISTINA)                                                      | ✅ populat (adăugat 2026-04-24 din Arhiva_Generala)                                                                                                                                     |
| `14_UPU_2024_05_30/`                 | Episod UPU Arad 30.05.2024 (Dr. Post + Dr. Grada + Dr. Pop Florica)                                           | ✅ populat (adăugat 2026-04-24 din Arhiva_Generala; 1 PDF + 10 JPEG pagini intermediare — vezi `intermediate_artifacts` în PDF meta.json)                                               |
| `15_consult_initial_oncologie_2026/` | OPIS consult inițial OncoHelp 30.04.2026 (Dr. Mate Endre)                                                     | ✅ populat 2026-04-28 (PDF OPIS 8 puncte + meta.json + extragere MD; folder creat 2026-04-28 R26)                                                                                       |
| `16_analize_markeri_2026_04/`        | Markeri tumorali (CEA, CA 19-9, CA 72-4) + HbA1c 29.04.2026 (Bioclinica Nădlac, validator Dr. Statnic A08064) | ✅ populat 2026-04-29 (PDF buletin 26429A0020 + meta.json + extragere MD; folder creat 2026-04-29 R26; PDF redenumit din `Bioclinica_Analize_Markeri_Sange.pdf`)                        |

**Note structurale:**

- **Totalul curent: 16 foldere** (01–16, continuu, fără goluri în numerotare). `99_altele/` eliminat 2026-04-24.
- **Foldere populate: 14/16.** Foldere goale justificate: `03_hernie_anterior/` (dată necunoscută; per user — documente vechi pierdute), `12_biopsie_2026/` (rezultat primit 28.04 ca PDF, deja ingerat).
- **La document nou care nu se încadrează în 01–16:** creare folder nou `17_categorie_data/` conform convenției + update acest tabel.

**Obligatoriu (semnalare devieri):**

1. La orice citire/procesare document sursă: AI verifică dacă fișierul respectă convenția de nume + folder.
2. La orice **DEVIERE detectată** (nume fișier non-canonic, fișier în folder greșit, lipsă `.meta.json` companion, lipsă folder dedicat pentru tip nou document) → **menționez EXPLICIT user-ul în mesajul activ** + propun corecție concretă (unde să fie mutat, cum să fie redenumit).
3. NU fac mutări/redenumiri tăcute — propun, aștept confirmare user (Regula 20). Excepție: reparări triviale consimțite explicit anterior.
4. Devieri cunoscute persistente (listate în tabelul de mai sus cu status 🟡) — NU se re-raportează la fiecare sesiune, doar la schimbare status (populare, mutare, identificare conținut).

**Why:** consistența structurii reduce timpul de căutare/regăsire în consult medical critic + previne fișiere uitate în catch-all + permite indexare automată viitoare + disciplinează procesul de digitizare. User a inițiat curățenia 2026-04-24 mutând `CT - Genesys.pdf` din `99_altele/` în `11_CT_stadializare_2026/` și a cerut explicit codificarea acestui model unitar + semnalarea proactivă a devierilor. Sesiunea 2026-04-24 (seara) a finalizat eliminarea completă a `99_altele/` după integrarea restului conținutului din Arhiva_Generala în folderele tematice corespunzătoare (13_cardiologie_ambulator_2025/, 14_UPU_2024_05_30/) — R26 formalizează principiul.

**How to apply:** la fiecare interacțiune cu `Dosar_Medical/documente_sursa/`, verificare consistență; la sesiune nouă de procesare documente, scan proactiv al folder-elor pentru devieri și raportare tablou status către user; la digitizare document nou, ALEG folder-ul corect existent sau propun unul nou dacă nu există categorie adecvată.

**Relație cu Regula 14 (chain of custody):** R14 cere `.meta.json` per document (ce date + cum ajungea + de cine procesat); R26 codifică unde și cum se structurează fizic documentul sursă. Ambele sunt complementare — R26 presupune R14 aplicat.

**Relație cu Regula 21 (curățenie, zero ciorne):** R21 interzice ciorne pe disc; R26 interzice documente în locuri non-canonice. Ambele susțin ordinea dosarului.

---

## Reguli complementare (pointeri)

Pentru reguli care se aplică și în `Dosar_Medical/` dar sunt always-on (`REGULI_CLAUDE_CODE.md` la rădăcină):

- **Regula 17** (marcaje `[CERT]`/`[PROBABIL]`/`[INCERT]`/`[NEGASIT]`) — toate JSON-urile și documentele generate respectă marcajul
- **Regula 22** (verificare proactivă `[INCERT]`) — aplicabilă pe JSON-uri + rapoarte + sinteze
- **Regula 10 backup** se corelează cu **Regula 21 curățenie** (arhivarea e pentru versiuni de referință modificate structural, NU pentru ciorne)

## Note pentru lucrul în `Dosar_Medical/`

- **Subfoldere:** `arhiva/` (backup-uri), `cercetari/` (sinteze cercetare web validate), `documente_sursa/` (scanuri originale, READ-ONLY), `rapoarte_generate/` (DOCX-uri pentru medici).
- **JSON-urile medicale** respectă schema documentată în `SCHEMA_JSON_v2.md`. Modificările la schemă se coordonează cu workspace-ul paralel `.Tati_Documente_Medicale` (vezi DECIZII_FORMAT_FISIERE v3.0 propusă acolo).
- **Documentele sursă** (`.pdf`, `.jpeg`) sunt **READ-ONLY la nivel de conținut bytes** — nu se suprascriu, nu se modifică intern, nu se șterg.

  **Excepție pentru filename — redenumire R26 retroactivă:** redenumirea fișierului e permisă DOAR pentru aplicarea convenției R26 (`YYYY-MM-DD_descriere.ext`) când documentul a fost adăugat înainte de codificarea R26 sau cu nume non-canonic. Condiții obligatorii cumulative:
  1. **Conținut bytes neatins** — nu se modifică binarul; `git mv` păstrează identitate (R100 sau procent înalt rename detection)
  2. **Trasabilitate explicită** — câmp `source_document_renamed_from` în `.meta.json` companion cu numele original + data redenumirii + motivul (R26)
  3. **Naming note** — câmp `naming_note` în `.meta.json` cu istoric redenumire
  4. **Backup R10 pre-redenumire** — JSON canonic + meta.json (rollback recoverable)
  5. **Update cross-references** — toate referințele live (CONTEXT_MEDICAL §, DASHBOARD embed, MANIFEST, GHID-uri, alte JSON-uri) actualizate la noul nume
  6. **Notificare user** — semnalare explicită în mesajul activ + commit message (R26 + R20)

  **Precedent documentat:** Faza 1 plan implementare cross-terminal 2026-04-28 (commit `4c9bdd8`) — 6 redenumiri R26 retroactive în `02_cardiologie_2012/`, `11_CT_stadializare_2026/`, `12_biopsie_2026/`. Backup R10 în `arhiva/context_medical_versiuni/`.

  **Niciodată ștergere** documente sursă — git history păstrează istoric, dar fișierul fizic rămâne accesibil în arborele de lucru pentru consult medical.
