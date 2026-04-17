# TODO.md — Acțiuni curente

**Fișier de evidență a tuturor acțiunilor de făcut. Se actualizează continuu — la adăugarea și completarea fiecărei acțiuni.**

**Ultima actualizare:** 17 aprilie 2026.

---

## Calendar — date cheie

| Data | Eveniment | Status |
|---|---|---|
| 17.04.2026 | Endoscopie + colonoscopie efectuate | ✅ Finalizat |
| 17.04.2026 | Bilet trimitere CT emis | ✅ Finalizat |
| {de confirmat} | Efectuare CT stadializare | 🟡 De programat |
| {17.04.2026 + 7-14 zile} | Rezultat biopsie (estimat) | 🟡 În așteptare |
| {după primirea rezultatelor} | Consult oncolog digestiv | 🟡 De programat |

---

## P0 — Critic, de efectuat IMEDIAT

### [P0] Programare CT de stadializare

**Context:** Bilet URGENȚĂ emis pe 17.04.2026. Cu cât se face mai repede, cu atât stadializarea este mai rapidă.
**Deadline:** în maxim 3-5 zile de la emitere.
**Sub-task-uri:**
- [ ] Sunat la Genesis Medical Clinic Micălaca pentru programare
- [ ] Verificat disponibilitatea pe zilele următoare
- [ ] Rezervare confirmată + data + ora

**Generat din:** bilet trimitere BCTAP 0631727
**Data creării:** 17.04.2026

### [P0] Obținere analize prealabile pentru CT

**Context:** CT cu contrast iodat necesită verificarea funcției renale.
**Deadline:** înainte de CT.
**Sub-task-uri:**
- [ ] Creatinină serică (recent sau nou-efectuată)
- [ ] Uree
- [ ] Hemoleucogramă completă
- [ ] Glicemie à jeun

**Dacă nu există analize recente:**
- [ ] Solicitare bilet de trimitere pentru analize (medic de familie) SAU efectuare privat
- [ ] Efectuare analize
- [ ] Obținere rezultate

**Generat din:** `CONTEXT_MEDICAL.md`, secțiunea 8 — pregătire CT
**Data creării:** 17.04.2026

### [P0] Pregătire pacient pentru CT cu contrast

**Context:** Pacientul are diabet tratat cu Metformin — oprire obligatorie 48h înainte.
**Sub-task-uri:**
- [ ] **Oprire Metformin cu 48h înainte de CT** (acțiune critică)
- [ ] Hidratare abundentă cu apă în ziua dinaintea CT
- [ ] Repaus alimentar 4-6 ore înainte de examinare
- [ ] Verificare alergii (iod, fructe de mare) — de confirmat cu familia
- [ ] Pregătire documente de dus: buletin, card sănătate, bilet trimitere original, analize recente, buletin endoscopie

**Generat din:** `CONTEXT_MEDICAL.md`, `REGULAMENT.md` (siguranța medicală)
**Data creării:** 17.04.2026

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

- [ ] Sincronizare cu Google Drive (folder privat)
- [ ] Backup pe disk extern
- [ ] Configurare Git pentru versionare automată

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

- ✅ 17.04.2026: Endoscopie digestivă superioară efectuată
- ✅ 17.04.2026: Colonoscopie efectuată
- ✅ 17.04.2026: Biopsie esofagiană prelevată
- ✅ 17.04.2026: Bilet trimitere CT emis
- ✅ 14.04.2026: Ecografie abdominală efectuată
- ✅ 30.05.2024: Tratament H. pylori efectuat cu succes

---

## Note

- Acțiunile cu deadline strict sunt marcate clar.
- Când o acțiune este finalizată, se mută în secțiunea „Acțiuni finalizate” cu data completării.
- Acțiunile noi care apar se adaugă la nivelul de prioritate corespunzător.
- La fiecare sesiune, Claude Code verifică statusul acțiunilor deschise și raportează.

---

**Ultima revizuire:** 17 aprilie 2026.
