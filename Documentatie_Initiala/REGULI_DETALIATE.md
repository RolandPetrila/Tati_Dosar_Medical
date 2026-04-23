# REGULI_DETALIATE.md — Protocoale extinse și exemple

**Versiune:** 12.0 | **Data:** 2026-04-23

> **Fișier referință on-demand.** Conține detaliile extinse care nu încap în formele compacte din `REGULI_CLAUDE_CODE.md` și `Dosar_Medical/CLAUDE.md`.
>
> Se citește **DOAR când regula respectivă necesită clarificare pe caz concret** (exemple, matrici, edge cases). Nu face parte din always-on.

---

## §R11 — Matrice extinsă valabilitate clinică (din `Dosar_Medical/CLAUDE.md`)

### Cazuri speciale praguri temporale

| Tip informație specifică             | Interval valid clinic                                    | Notă                                          |
| ------------------------------------ | -------------------------------------------------------- | --------------------------------------------- |
| Hemoleucogramă (WBC, HGB, PLT)       | 1-3 luni (context boala acută), 3-6 luni (cronic stabil) | în oncologie activă: 2-4 săptămâni            |
| Funcție renală (creatinină, eRFG)    | 1-3 luni (pacient stabil), 24-48h (pre-contrast iodat)   | pre-CT → Regula 16 Jamesi                     |
| Funcție hepatică (TGO, TGP, GGT)     | 3 luni stabil, 1 lună schimbare terapie                  |                                               |
| Markeri tumorali (PSA, CEA, CA 19-9) | 3-6 luni follow-up, 1-3 luni tratament activ             | depinde de protocol                           |
| HbA1c                                | 3 luni (standard ADA)                                    | media ultimele 2-3 luni glicemie              |
| Coagulogramă (INR, APTT)             | 1-7 zile (anticoagulant), 1-3 luni (screening)           |                                               |
| Ecografie abdominală                 | 6-12 luni normală, 3 luni patologie activă               |                                               |
| CT/RMN de stadializare               | 3-6 luni follow-up, la orice modificare simptomatică     |                                               |
| Endoscopie digestivă                 | 6-12 luni (surveillance), la simptome noi                | Barrett: 3-5 ani depinde de gradul displaziei |
| RCP medicament (SmPC)                | 12 luni ediția oficială                                  | verificare EMA/ANMDMR recentă                 |
| Ghid ESMO                            | 2-3 ani ediția majoră, anual update                      |                                               |
| Ghid NCCN                            | update lunar sau trimestrial pe versiune                 | versiune explicit                             |
| AJCC staging                         | 5-8 ani între ediții majore (ediția 9 — 2024)            |                                               |

### Format citare cu data

```markdown
Glicemia pacientului a fost 136,1 mg/dL la **17.06.2025** (9 luni vechime la 2026-04-23 → `[POTENȚIAL STALE]`, reverificare recomandată pre-consult oncolog).
```

---

## §R16 — Protocol extins timestamp (din `REGULI_CLAUDE_CODE.md`)

### Format timestamp per tip fișier (convenție proiect)

| Fișier                                  | Format                                             | Exemplu                                      |
| --------------------------------------- | -------------------------------------------------- | -------------------------------------------- |
| `SESSION_LOG.md`                        | `YYYY-MM-DD HH:MM` (fără secunde, fără timezone)   | `2026-04-23 03:20`                           |
| `CHANGELOG.md`                          | `YYYY-MM-DD HH:MM` (același format ca SESSION_LOG) | `2026-04-23 03:20`                           |
| `CONTEXT_MEDICAL.md`                    | Data simplă `YYYY-MM-DD` sau text narativ          | `17 aprilie 2026`                            |
| `_metadata.data_procesare` din JSON-uri | ISO 8601 complet `YYYY-MM-DDTHH:MM:SS+03:00`       | `2026-04-23T03:20:00+03:00`                  |
| `WEB_QUERIES.md`                        | `YYYY-MM-DD HH:MM`                                 | `2026-04-23 03:20`                           |
| Backup-uri `arhiva/`                    | `YYYY-MM-DD_HHMM` (sufix nume fișier)              | `CLAUDE_pre-reorganizare_2026-04-23_0320.md` |

**Timezone implicit:** ora locală România (EET/EEST = UTC+2 / UTC+3). `date +"%z"` returnează `+0300` în DST (aprilie-octombrie) și `+0200` în afara DST.

### Comenzi de obținere exactă

```bash
date +"%Y-%m-%d %H:%M:%S %z"   # Ex: 2026-04-23 03:20:32 +0300
date +"%Y-%m-%dT%H:%M:%S%:z"   # ISO 8601: 2026-04-23T03:20:32+03:00
date +"%Y-%m-%d_%H%M"          # Pentru backup: 2026-04-23_0320
```

### Edge cases

1. **Sesiune >1 oră** — o singură rulare `date` la start devine stale. Refresh per bloc >15 min de scrieri.
2. **User menționează o oră intermediară** („acum e 14:00") — verifică cu `date`; sistemul e sursa de adevăr.
3. **Commit git** are timestamp propriu (`git log --format=%ai`). NU include manual în mesajul commit.
4. **Discrepanță timestamp deja scris vs. `date` real** — oprește, corectează imediat, audit trail transparent în `CHANGELOG.md` (erata în 02:51 din 2026-04-18 — exemplu consacrat).

---

## §R17 — Exemple complete marcaje certitudine (din `REGULI_CLAUDE_CODE.md`)

### Bonus format intern

- Marcajele se scriu **la începutul paragrafului sau al afirmației** (nu la sfârșit).
- Un paragraf care combină afirmații de certitudini diferite → se împarte în sub-paragrafe, fiecare cu propriul marcaj.
- În tabele → coloană dedicată „Sursă" sau „Certitudine" dacă sunt multe rânduri.

### Exemplu CORECT

> [CERT] Metforminul trebuie oprit cu 48h înainte de CT cu contrast iodat (RCP Janumet, secțiunea 4.4, Electronic Medicines Compendium UK, consultat 18.04.2026, https://www.medicines.org.uk/emc/product/4295/smpc).
>
> [PROBABIL] La pacienții vârstnici cu funcție renală la limită, pauza poate fi prelungită la 72h, deși RCP nu specifică explicit — convenție clinică bazată pe farmacocinetică sitagliptin la eRFG < 45 mL/min.
>
> [INCERT] Riscul exact de acidoză lactică la pacienții care omit pauza depinde de doza de metformin + funcția renală + volumul de contrast — nu există valoare unică citabilă, datele din studii observaționale diferă între cohorte.
>
> [NEGASIT] Rata exactă a acidozei lactice la pacienții care au ignorat pauza de 48h și au funcție renală normală — verificat SmPC Janumet (v.06.2021) + FDA label + PubMed „metformin CT contrast lactic acidosis normal renal function" — nu există date consolidate dincolo de case reports rare.
>
> ---
>
> **Surse citate:**
>
> 1. RCP Janumet — Electronic Medicines Compendium UK, v.06.2021, consultat 18.04.2026 (https://www.medicines.org.uk/emc/product/4295/smpc)
> 2. ESUR Guidelines on Contrast Agents — v.10, 2018, consultat 18.04.2026 (https://www.esur.org/guidelines/)
>
> **Ce NU am găsit:** rata precisă acidoză lactică la pacienți care omit pauza; pragul exact eRFG la care pauza devine > 48h.
>
> **ATENȚIE: Acest document NU înlocuiește consultul medical.**

### Exemplu GREȘIT (anti-pattern)

> Metforminul se oprește 48h înainte. (fără marcaj, fără sursă)
>
> Metforminul cauzează acidoza lactică la aproximativ 5% din pacienți. (cifră fără [CERT] + sursă — dacă nu e în RCP, cifra nu se folosește)

### Sursă primară > sursă secundară

Dacă Wikipedia / site comercial / blog / AI tool (inclusiv alt Claude / ChatGPT / Gemini) contrazic o sursă primară (SmPC / ghid), **sursa primară câștigă**. Nu se citează AI-ul ca sursă.

---

## §R18 — Protocol complet sincronizare `DASHBOARD.html`

### Conținut obligatoriu dashboard (secțiuni)

1. **Header** — nume pacient, vârstă, data ultimei actualizări a dashboardului
2. **Countdown CT** / următorul eveniment medical major (JavaScript live)
3. **Status clinic curent** — suspiciune + faza investigațiilor
4. **Medicație activă** — tabel cu schema zilnică + marcaje STOP temporar / pauză
5. **Alergii** — verde dacă free, roșu dacă confirmate
6. **Analize recente** — valori + unități + interval referință + trend + flag normal/anormal
7. **Timeline antecedente** — cronologic, din 2012 până azi
8. **Echipă medicală** — specialitate, nume, unitate, contact
9. **Acțiuni deschise** — P0 (roșu), P1 (galben), P2/P3 (verde)
10. **Întrebări pregătite pentru consulturi** — grupate pe specialist
11. **Footer** — sursă date (link la `CONTEXT_MEDICAL.md`), atenționare „nu înlocuiește consultul medical"

### Reguli conținut (coroborate cu Regulile 11 + 17)

- Orice cifră citează data sursei (data analizei, nu data dashboardului)
- Afirmațiile factuale respectă marcajul R17 — când nu e evident, indicație textuală scurtă
- Date volatile (analize > 6 luni) primesc marcaj `[POTENȚIAL STALE]` R11
- Câmpurile goale se marchează „De completat" (nu inventezi)

### Reguli tehnice

- CSS inline în `<style>`, **fără dependențe externe** (offline-first, funcționează direct din Google Drive)
- Limbă: română, ton profesional dar accesibil familiei
- Palette: albastru medical + verde OK + galben atenție + roșu critic
- Font: system fonts (Segoe UI / -apple-system / sans-serif) — fără web fonts
- Responsiv pentru desktop + imprimare A4 (`@media print`)
- Encoding UTF-8, declarat explicit în `<head>`

### Tab-uri (începând v6)

Dashboardul are 2 tab-uri: `medical` (default, conținutul clinic) și `alimentatie` (ghidul culinar). Tab-ul Alimentație folosește strategie hibridă:

- Încearcă `fetch('ALIMENTATIE.md')` la încărcare (vizualizare live pe browserele care permit)
- Fallback pe conținutul embedded în `<script type="text/markdown" id="md-alimentatie">` (Chrome/Edge blochează `fetch()` pe `file://`)

Parser Markdown minimal inline, fără dependențe externe.

### Procedură regenerare la declanșator

1. Citește `CONTEXT_MEDICAL.md` + `TODO.md` + JSON-urile relevante din `Dosar_Medical/`
2. Suprascrie complet `DASHBOARD.html` (nu patch parțial)
3. Actualizează câmpul „Ultima generare" din header cu timestamp-ul obținut via `date` (§R16)
4. Logează în `CHANGELOG.md` + `SESSION_LOG.md`
5. Include în commit-ul final al sesiunii (R16)

### Excepție — regenerare parțială (declanșator #9 Regula 18)

Modificare `ALIMENTATIE.md` singur → actualizează **DOAR** blocul `<script type="text/markdown" id="md-alimentatie">` + variabila `lastRegen` din JS (tab-ul Alimentație). Nu regenerezi integral.

---

## §R22 — Protocol concret verificare proactivă

### Protocol concret pentru o afirmație `[INCERT]`

1. **Identifică întrebarea factuală exactă** (ex: „rolul Dr. X la instituția Y")
2. **Caută pe surse primare** (WebFetch pe pagina oficială profil medic, WebSearch pe nume + rol)
3. **Evaluează rezultatele:**
   - Confirmare pe sursă oficială → `[CERT]` + citare URL + data
   - Confirmare pe sursă secundară reputabilă → `[CERT]` cu precizarea sursei (secundară) + data
   - Doar pe surse neutralizabile → `[PROBABIL]` cu explicație
   - Nimic → `[NEGASIT]` cu enumerarea surselor consultate
   - Contrazicere explicită → **șterge afirmația** + log `CHANGELOG.md`
4. **Loghează decizia** în `CHANGELOG.md` dacă a implicat modificare semnificativă

### Ierarhie surse acceptabile (detalii)

**Rang 1 — Sursa primară oficială:**

- Site instituțional oficial (spital, universitate, registru)
- SmPC / RCP (Electronic Medicines Compendium UK, ANMDMR RO, EMA)
- Ghid clinic major (ESMO, NCCN, AJCC, AHA/ESC, WHO)

**Rang 2 — Sursa secundară reputabilă:**

- PubMed (articole peer-reviewed, preferabil review sau studii majore)
- CASPA (pentru asociații și studii clinice în România)
- Ministerul Sănătății România (pentru date administrative)
- UpToDate / Medscape / Mayo Clinic (pentru context clinic extins)

**Rang 3 — Media medicală recunoscută:**

- MediChub, Viață Medicală, Medical Virtual (doar cu cross-reference la primare)
- Comunicate oficiale asociații medicale cu origine verificabilă

**NU acceptabile:**

- Wikipedia (terțiar, editabil anonim — poate fi folosit doar ca punct de plecare pentru căutare)
- Forumuri, grupuri Facebook, Reddit
- Blog-uri personale (chiar ale medicilor — lipsă validare peer)
- Site-uri comerciale (agregatori de clinici, farmacii online)
- Alt AI (Gemini, ChatGPT, alt Claude) ca sursă primară — nu se citează AI ca sursă

### Exemplu aplicat (sesiunea 2026-04-23)

**Verificare Dr. Sîrbu Daniela „Șef Spitalizare Continuă" la OncoHelp:**

1. Întrebarea factuală: rolul intern Dr. Sîrbu Daniela la Secția Oncologie OncoHelp Timișoara
2. Surse consultate:
   - WebFetch pe `oncohelp.ro/echipa-oncohelp/dr-sirbu-daniela-medic-primar-oncolog/` → 404 (pagină individuală inexistentă)
   - WebSearch pe „Sîrbu Daniela OncoHelp Timișoara Șef Spitalizare Continuă"
3. Rezultate:
   - timpolis.ro → confirmare rol (Rang 3, cross-referencing)
   - oncohelp.ro roster public → confirmare prezență echipă (Rang 1)
4. Decizie: **CONFIRMAT** → upgrade `[INCERT]` → `[CERT]` + surse + data
5. Log: `CHANGELOG.md` intrare 2026-04-23 02:16 (remedieri post-review)

### Propagare corecții retroactive

Dacă găsești că un marcaj `[CERT]` existent conținea date incorecte / outdated:

1. Corectezi imediat conținutul
2. Log în `CHANGELOG.md` cu tag-ul **`corectie-retroactiva`** în prima linie (pentru audit rapid)
3. Dacă corecția afectează rapoarte generate (DOCX) → regenerează rapoartele afectate
4. Update `MEMORY.md` dacă memoria descrie info corectată

---

## Când să consulți acest fișier

- Ai o afirmație medicală pe care vrei s-o marchezi cu certitudine — §R17
- Ai o valoare numerică veche și vrei să știi ce prag de vechime să aplici — §R11
- Trebuie să regenerezi `DASHBOARD.html` și ai dubiu pe secțiuni — §R18
- Găsești un `[INCERT]` existent și vrei să-l verifici conform Regulii 22 — §R22
- Trebuie să scrii un timestamp și vrei format exact — §R16

Când subiectul e clar în formele compacte din `REGULI_CLAUDE_CODE.md` / `Dosar_Medical/CLAUDE.md`, **nu e nevoie să consulți acest fișier** — forma compactă e suficientă.
