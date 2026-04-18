# TODO.md — Acțiuni curente

**Fișier de evidență a tuturor acțiunilor de făcut. Se actualizează continuu — la adăugarea și completarea fiecărei acțiuni.**

**Ultima actualizare:** 19 aprilie 2026 02:27.

---

## Calendar — date cheie

| Data                                | Eveniment                                                       | Status                                    |
| ----------------------------------- | --------------------------------------------------------------- | ----------------------------------------- |
| 17.04.2026                          | Endoscopie + colonoscopie efectuate                             | ✅ Finalizat                              |
| 17.04.2026                          | Bilet trimitere CT emis                                         | ✅ Finalizat                              |
| **18.04.2026**                      | **STOP Jamesi (H-48 pre-CT)**                                   | ✅ Finalizat                              |
| ~~19.04.2026 — analize creatinină~~ | ~~de efectuat~~ → ✅ ACOPERIT (buletin Bioclinica 17.04.2026)   | ✅ Finalizat                              |
| 19.04.2026                          | Hidratare activă (plan confirmat de familie)                    | 📅 PROGRAMAT                              |
| **20.04.2026 17:00**                | **CT torace + abdomen + pelvis cu contrast (Genesis Micălaca)** | 📅 PROGRAMAT                              |
| **22.04.2026**                      | Reluare Jamesi (H+48 post-CT, după creatinină OK)               | 🟡 Follow-up                              |
| {17.04.2026 + 7-14 zile}            | Rezultat biopsie (estimat 24.04-01.05)                          | 🟡 În așteptare · monitor automat activ ↓ |
| {după primirea rezultatelor}        | Consult oncolog digestiv                                        | 🟡 De programat                           |

---

## 🔔 Monitor automat rezultat biopsie — ACTIV

**Sistem independent** care verifică automat portalul Bioclinica la fiecare 30 min, 24/7, și notifică instant pe telefonul Roland (ntfy.sh, prioritate urgentă) când apare rezultatul histopatologic. **Nu depinde de laptop pornit** — rulează pe GitHub Actions.

- **Repo privat:** `RolandPetrila/Sistem_Notificari` (nu e parte din dosarul `.Tati`, e hub separat pentru notificări reutilizabile)
- **Folder local:** `C:\Users\ALIENWARE\Desktop\Roly\Sistem_Notificari_Telefon\`
- **Mecanism:** Playwright headless → login Bioclinica (credențialele — cod buletin, cod acces, CNP — stocate ca GitHub Secrets în repo-ul privat, **nu** în acest dosar) → detecție text „histopatologic" în afara secțiunii „în curs de execuție" → ntfy.sh priority 5 → se oprește automat după prima notificare (flag `.DETECTED`)
- **Abonament telefon ntfy:** topicul folosit de monitor trăiește doar în Secrets privat + aplicația ntfy pe telefon (nu e scris aici în dosarul public)
- **Activat:** 2026-04-19 02:27 (commit `cf675ec`)

**Acțiune așteptată:** niciuna din partea ta; primești notificare pe telefon când e cazul.

---

## P0 — Critic, de efectuat IMEDIAT

### [P0] ✅ Programare CT de stadializare — COMPLET

**Status:** confirmat LUNI 20.04.2026 ora 17:00 la Genesis Medical Clinic Micălaca (confirmat 18.04.2026).

- [x] Sunat la Genesis Medical Clinic Micălaca pentru programare
- [x] Rezervare confirmată: 20.04.2026, 17:00

**Follow-up deschis:**

- [ ] Confirmare telefonică cu 24h înainte
- [ ] Întrebare explicită radiologului: „Triplixam — mențin integral sau omit doza duminică/luni?"
- [ ] Întrebare: cât durează raportul? Se primește CD cu DICOM?

### [P0] ✅ Analize prealabile pentru CT — COMPLET pentru funcția renală

**Status (18.04.2026):** Buletin Bioclinica nr. 26417A0362 din 17.04.2026 integrat în dosar.

- [x] **Creatinină serică:** 0.83 mg/dL (normală, eGFR ~95) ✅
- [x] **Uree serică:** 33.4 mg/dL (normală) ✅
- [ ] Hemoleucogramă completă — opțional, ultima e din 28.11.2025; nu e blocant pentru CT
- [ ] Glicemie à jeun — opțional, ultima 136 mg/dL (17.06.2025); nu e blocant

**Concluzie:** funcția renală OK pentru contrast iodat, protocol CT standard. Nu se mai impune obținerea de alte analize înainte de luni.

**Notă bonus:** același buletin Bioclinica menționează „examen histopatologic în curs" — **biopsia esofagiană se procesează la Bioclinica Arad**.

**Sursă:** `Dosar_Medical/2026-04-17_buletin_bioclinica_uree_creatinina.json`
**Data închiderii:** 18.04.2026

### [P0] Pregătire pacient pentru CT luni 20.04.2026 ora 17:00

**Context:** Deadline-uri exacte pentru medicație și pregătire.
**Sub-task-uri cu deadline:**

- [x] ✅ **SÂMBĂTĂ 18.04: STOP Jamesi** (H-48 înainte de CT) — EXECUTAT (confirmat de familie 18.04.2026 13:28)
- [x] ✅ **Analize creatinină + uree** — Bioclinica 17.04.2026: creatinină 0.83 (normală), uree 33.4 (normală). **VALID pentru CT 20.04.**
- [x] ✅ **Plan hidratare duminică 1.5-2 L apă plată** — confirmat de familie 18.04.2026
- [ ] Duminică seara ~20:00: ultima masă mai consistentă
- [ ] Luni ~11:00: gustare ușoară — ultima înainte de CT
- [ ] Luni dimineață: ia NORMAL Aspenter + Concor + Triplixam (cu excepție dacă radiologul spune altfel pentru Triplixam)
- [x] ✅ **Confirmare alergii** — fără alergii la iod / fructe de mare / contrast anterior (confirmat de familie 18.04.2026 13:28)
- [ ] Pregătire documente: CI, card CAS, bilet BCTAP 0631727, analize recente, buletin endoscopie 17.04
- [ ] Miercuri 22.04: reluare Jamesi DOAR după creatinină normală post-CT

**Generat din:** `CONTEXT_MEDICAL.md`, `REGULAMENT.md` (siguranța medicală), confirmare programare CT 20.04.2026
**Data creării:** 17.04.2026 | **Actualizare:** 18.04.2026

---

## P1 — Important, de efectuat în câteva zile

### [P1] Colectare informații medicale suplimentare de la familie

**Context:** Multe detalii importante lipsesc (lista exactă de medicamente, alergii, grupa sanguină, istoric detaliat).
**Sub-task-uri:** vezi `fisa_colectare_informatii_petrila.docx` (din rapoarte_generate/)

- [ ] Lista completă de medicamente (denumiri comerciale, doze, orar)
- [ ] Alergii confirmate (medicamente, alimente, contrast iodat anterior)
- [ ] Grupa sanguină și Rh
- [ ] Greutatea și înălțimea actuală
- [ ] HbA1c recent — pentru control diabet
- [ ] Tensiunea arterială uzuală

**Data creării:** 17.04.2026

### [P1] Obținere și scanare documente istorice

**Sub-task-uri:**

- [ ] Bilet externare 2012 (stent coronarian)
- [ ] Bilet externare 30.05.2024 (H. pylori)
- [ ] Documente hernie noiembrie 2025 (raport operator, bilet externare)
- [ ] Documente hernie anterioară (data de identificat)
- [ ] Analize recente dacă există
- [ ] Buletin endoscopie 17.04.2026 (de obținut de la Genesis Arad)
- [ ] Buletin colonoscopie 17.04.2026

**Destinație:** `documente_sursa/` conform `STRUCTURA_PROIECT.md`

**Data creării:** 17.04.2026

### [P1] Clarificare tip hernie noiembrie 2025

**Context:** Dacă a fost hernie hiatală, este direct relevantă pentru patologia esofagiană actuală.
**Sub-task-uri:**

- [ ] Întrebat pacientul / familia despre tipul exact al herniei
- [ ] Obținut raport operator
- [ ] Integrare informație în `CONTEXT_MEDICAL.md`

**Data creării:** 17.04.2026

---

## P2 — Util, de efectuat în săptămânile următoare

### [P2] Identificare și contactare oncolog digestiv

**Context:** Pentru a avea un consult pregătit imediat ce primim rezultatele biopsiei și CT.
**Sub-task-uri:**

- [ ] Evaluare opțiuni: Arad, Timișoara, Cluj (conform `CONTEXT_MEDICAL.md`)
- [ ] Recomandare de la Dr. Noufal Abdul Vahab (dacă e posibil)
- [ ] Verificare disponibilitate, costuri, timp de așteptare
- [ ] Programare preventivă (dacă permit, se pot anula dacă nu e cazul)

### [P2] Jurnal simptome — început de la data startului

**Context:** Util pentru consultul oncolog și monitorizare evoluție.
**Sub-task-uri:**

- [ ] Creare template în `interpretari/jurnal_simptome/`
- [ ] Rugat pacientul / familia să noteze zilnic

### [P2] Verificare status asigurare CAS

**Sub-task-uri:**

- [ ] Confirmare status pensionar → asigurat automat
- [ ] Card CAS valabil
- [ ] Card European de Sănătate (opțional)

### [P2] Completare antecedente familiale detaliate

**Sub-task-uri:**

- [ ] Afecțiuni parinti (cauze deces, vârsta)
- [ ] Afecțiuni frați / surori
- [ ] Cancere în familie extinsă
- [ ] Alte boli cu componentă ereditară

---

## P3 — Util pe termen mediu

### [P3] Documentare istoric de fumat detaliat

Pentru evaluare mai precisă a expunerii (calculul „pachete-an”).

- [ ] Numărul de țigări/zi în medie
- [ ] Perioade de consum variat
- [ ] Tip de tutun

### [P3] Documentare expuneri profesionale

- [ ] Istoric ocupațional
- [ ] Expuneri posibile (pesticide, azbest, solvenți)

### [P3] Backup și organizare dosar

- [x] Sincronizare cu Google Drive (folder privat) — ✅ proiectul rulează din Google Drive (sync continuu)
- [ ] Backup pe disk extern
- [x] Configurare Git pentru versionare automată — ✅ repo GitHub + auto-commit Regula 16 (2026-04-18)

---

## Întrebări pregătite pentru consulturi viitoare

### Pentru Dr. Noufal Abdul Vahab (gastroenterolog)

- În ce segment al esofagului este leziunea?
- Dimensiunea aproximativă?
- Aspect (ulcerativ, vegetant, stenozant)?
- Este circumferențială sau parțială?
- A fost observat esofag Barrett?
- Ce a arătat colonoscopia?
- Când sunt gata rezultatele biopsiei?
- Ne recomandă un oncolog anume?

### Pentru centrul CT (Genesis Micălaca)

- Cât durează până la raportul radiologului?
- Se primește CD cu imagini DICOM?
- Costul dacă facem privat?

### Pentru viitorul oncolog

- Stadiul TNM exact?
- Tipul histologic?
- Opțiuni de tratament — ordonate?
- Prognostic realist?
- Trialuri clinice disponibile?
- Imunoterapie?
- Gestionarea comorbidităților (diabet, stent) în timpul tratamentului?

---

## Acțiuni finalizate (arhivă recentă)

- ✅ **18.04.2026 21:04**: GitHub Pages configurat pentru distribuție live-sync `DASHBOARD.html`. URL: https://rolandpetrila.github.io/Tati_Dosar_Medical/ — auto-deploy la fiecare `git push`. Repo mutat public intenționat. `index.html` redirect adăugat la rădăcina repo-ului.
- ✅ **18.04.2026 03:31**: Raport reacții adverse Jamesi + Triplixam generat în format `.docx` — `Dosar_Medical/rapoarte_generate/2026-04-18_raport_reactii_adverse_jamesi_triplixam.docx` (47 KB, ~30 pagini). Marcaj certitudine conform Regula 17 nouă. Observație clinică documentată: combinație sitagliptin + perindopril → risc crescut angioedem (RCP Triplixam 4.5). De prezentat familiei + medicului curant.
- ✅ **18.04.2026 03:10**: Remediere audit Regula 16 sub-clauza 7 (clarificări + logare retroactivă commit `478048f`). Detalii în `CHANGELOG.md`.
- ✅ **18.04.2026**: Audit complet Dosar_Medical — migrare JSON la schema v2.0, corecturi date (CNP talon, data nașterii urologie, nume manuscris, unități lab), dedup chirurgie 3→1, creare JSON identitate, `.meta.json`-uri chain-of-custody, reorganizare subfoldere tematice, reconciliere CONTEXT_MEDICAL.md. Detalii în `CHANGELOG.md`.
- ✅ 17.04.2026: Endoscopie digestivă superioară efectuată
- ✅ 17.04.2026: Colonoscopie efectuată
- ✅ 17.04.2026: Biopsie esofagiană prelevată
- ✅ 17.04.2026: Bilet trimitere CT emis
- ✅ 14.04.2026: Ecografie abdominală efectuată
- ✅ 30.05.2024: Tratament H. pylori efectuat cu succes

---

## Acțiuni noi deschise de audit (18.04.2026)

### [P0] ✅ Confirmare status alergii pacient (pre-CT) — FINALIZAT

**Rezultat (18.04.2026 13:28):** Pacientul NU are alergii la iod, fructe de mare sau contrast iodat anterior. Fără alergii medicamentoase cunoscute. Confirmat de Roland Petrilă (familie).

- [x] Interogare directă pacient + familia: alergii la medicamente, iod, fructe de mare → negative
- [x] Notare în `CONTEXT_MEDICAL.md`, secțiunea 11

**Notă:** confirmarea rămâne valabil să fie repetată verbal la radiolog înainte de injectarea contrastului.

### [P1] Identificare conținut PDF-uri nedigitizate

**Context:** 6 PDF-uri `2026-04-17_doc_neidentificat_{2-7}.pdf` în `Dosar_Medical/documente_sursa/99_altele/` fără conținut cartografiat.

- [ ] Deschidere fiecare PDF
- [ ] Anunț Claude Code: `proces [nume_fisier], corelează cu JSON-ul v2 corespunzător`
- [ ] Actualizare `.meta.json` corespunzător

### [P1] Digitizare documente lipsă

- [ ] PDF original cardiologie Vichy 2012 (pentru tipul exact al stent-ului DES vs. BMS)
- [ ] Document externare episod H. pylori 30.05.2024
- [ ] Buletin ecografie abdominală 14.04.2026

### [P1] Identificare Dr. LAZĂR (prescriere 10.11.2025)

**Context:** nume medic parțial ilizibil pe manuscris.

### [P2] HbA1c recent

**Context:** monitorizare control diabet cu Jamesi; ultima HbA1c necunoscută.

### [P2] Prezentare raport reacții adverse familiei + medic

**Context:** raport generat 18.04.2026 — `Dosar_Medical/rapoarte_generate/2026-04-18_raport_reactii_adverse_jamesi_triplixam.docx`.

- [ ] Printare/trimitere familie (pregătire înainte de CT)
- [ ] Atenționare către medicul curant despre interacțiunea sitagliptin + perindopril (risc angioedem) — de întrebat dacă e utilă monitorizare adițională sau dacă combinația trebuie reevaluată post-CT

### [P2] Verificare versiune curentă SmPC Triplixam pe ANMDMR

**Context:** SmPC-ul Servier folosit pentru raport e versiunea 06.2021 (vechime ~5 ani). Pentru decizii terapeutice majore, se verifică versiunea curentă pe anm.ro.

- [ ] Căutare „Triplixam 10/2.5/5" pe nomenclator.anm.ro
- [ ] Comparare cu conținutul raportului — actualizare dacă există diferențe semnificative

### [P2] ✅ Clarificare conținut arhivă `2025-11-01_talon_pensie_asigurare.zip` — FINALIZAT

**Decizie (18.04.2026 13:28):** ȘTERS la cererea user-ului. JSON-urile canonice sunt în `Dosar_Medical/`, iar git-ul păstrează istoricul complet — backup-ul zip era redundant.

### [P2] Clarificare rezolvare simultană hidrocel + chiste epididimare

**Context:** scrisoarea din 28.10.2025 indica ambele intervenții în plus față de hernie; biletul de externare 28.11.2025 menționează doar hernia + aderențe.

---

## Note

- Acțiunile cu deadline strict sunt marcate clar.
- Când o acțiune este finalizată, se mută în secțiunea „Acțiuni finalizate” cu data completării.
- Acțiunile noi care apar se adaugă la nivelul de prioritate corespunzător.
- La fiecare sesiune, Claude Code verifică statusul acțiunilor deschise și raportează.

---

**Ultima revizuire:** 17 aprilie 2026.
