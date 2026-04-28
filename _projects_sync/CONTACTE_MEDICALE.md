---
title: Catalog contacte medicale OncoHelp Timișoara
scope: doar medici OncoHelp activi (NU istoric extern; pentru istoric vezi CONTEXT_MEDICAL.md §9)
last_updated: 2026-04-28 13:00
medici_listati: 3
version: 1.3
changelog:
  v1.0_2026-04-25_19:00: creare inițială cu Anater + Vornicu, status Anater per site oncohelp.ro = „Rezident"
  v1.1_2026-04-25_19:30: corectare status Anater post-ingest Gmail — semnătura email zice „Medic Specialist" (R12 conflict surse)
  v1.2_2026-04-26_22:24: reflectare reprogramare consult Anater 30.04 → 4.05.2026 per mail Anater 26.04 (motiv: aglomerație zi liberă 1 mai + caz nou care necesită constituire dosar comisie oncologică)
  v1.3_2026-04-28_13:00: adăugare Dr. Mate Endre (Medic Rezident OncoHelp) — recomandare Vornicu telefonic 28.04, programare consult inițial 30.04.2026 12:00 (înregistrare pacient + pași suplimentari diagnostic; distinct de consultul Anater + comisie 4.05). Faza 3 plan implementare cross-terminal.
related_research: cercetari/2026-04-25_cercetare-oncohelp-vornicu-anater.md
related_correspondence: corespondenta/INDEX.md
---

# Catalog contacte medicale — OncoHelp Timișoara

> **Scope:** doar medicii din echipa OncoHelp Timișoara cu care suntem activi în corespondență sau urmează să interacționăm. Istoricul extern (Genesis Arad, UPU Arad, Bioclinica, medic familie Dr. Orbán, Dr. LAZA, Dr. Pop, Dr. Grada, Dr. Post, Dr. Pitea, Dr. Papiu, Dr. Mester, Dr. Noufal) NU este aici — vezi `CONTEXT_MEDICAL.md §9 Echipă medicală`.
>
> **Format:** Markdown cu YAML frontmatter pentru fiecare medic. Câmpuri obligatorii: `id`, `nume`, `specializare`, `unitate`, `emails`, `telefoane`, `status`, `prim_contact`, `ultim_contact`, `rol`, `tags`, `version`.
>
> **Cercetare profesională:** sinteză cu marcaje `[CERT]` / `[PROBABIL]` / `[NEGASIT]` (R17) + surse URL cu data accesării (R15 + R22). Detaliile complete din cercetare: `Dosar_Medical/cercetari/2026-04-25_cercetare-oncohelp-vornicu-anater.md`.
>
> **Workflow:** când user furnizează contact nou → cercetare web 4 surse → adăugare entry → sync DASHBOARD + INDEX.json + commit (R27 + R26).

---

## Index rapid

| ID                           | Nume                          | Specializare                                                  | Status                           | Telefon directe          | Email primar              |
| ---------------------------- | ----------------------------- | ------------------------------------------------------------- | -------------------------------- | ------------------------ | ------------------------- |
| `dr-anater-angelo-christian` | Dr. Anater Angelo - Christian | Medic Specialist Oncologie Medicală ⚠ (vezi notă R12 mai jos) | 🟢 activ — REPROGRAMAT 4.05.2026 | (prin centrală OncoHelp) | angelo.anater@oncohelp.ro |
| `dr-mate-endre`              | Dr. Mate Endre                | Medic Rezident Oncologie Medicală                             | 🟢 PROGRAMAT 30.04.2026 12:00    | (prin centrală OncoHelp) | (necunoscut public)       |
| `dr-vornicu-vlad`            | Dr. Vornicu Vlad-Norin        | Medic Specialist Oncolog (oncologie medicală)                 | 🟡 contact furnizat user         | 0762 120 428             | vornicuvlad91@gmail.com   |

---

## Unitate de referință — OncoHelp Timișoara

```yaml
id: oncohelp-timisoara
denumire: Centrul de Oncologie OncoHelp
operator_juridic: OncoHelp TM SRL (CUI 30129067)
adresa: Str. C. Porumbescu Nr. 57-59, Timișoara, 300239
telefoane:
  centrala: ["0256 495403", "0356 460995"]
  programari_mobil: "0753 595959"
  programari_radioterapie: "0752 266170"
  medic_garda_24_7: "0752 010 508"
  fax_secretariat: "0356 460996"
emails:
  programari: programari@oncohelp.ro
  office: office@oncohelp.ro
  manager: valeriu.boruga@oncohelp.ro
manager: Dr. Boruga Valeriu Ioan
program:
  programari: "Lun-Vin 08:00-16:00"
  medic_garda: "Lun-Vin 15:00-08:00 + Sâm-Dum 24h"
  vizite_pacienti: "Lun-Vin 17:00-19:00; Sâm-Dum + sărbători 09:00-11:00 + 16:00-18:00"
  audienta_manager: "Lun + Joi 09:00-10:00"
acces_public: "Tramvai 8 sau 6 → Piața Bălcescu → autobuz E8 (2 stații)"
servicii: [oncologie medicală, hematologie, radioterapie, paliativ, imagistică]
echipa_marime: ~150+ profesioniști
website: https://oncohelp.ro
sources_verified: 2026-04-25
```

---

## Dr. Anater Angelo - Christian {#dr-anater-angelo-christian}

```yaml
id: dr-anater-angelo-christian
nume: Anater Angelo-Christian
titlu: Dr.
titlu_profesional: Medic Specialist (per self-id email; site oncohelp.ro listează „Rezident" — conflict surse R12)
specializare: [oncologie medicala]
unitate: OncoHelp Timișoara
unitate_id: oncohelp-timisoara
departament: Secția de Oncologie
emails:
  primar: angelo.anater@oncohelp.ro
  secundar: angelo.anater95@yahoo.com
telefoane: []
varsta_estimata: ~31 ani (sufix `95` în yahoo sugerează naștere 1995) [PROBABIL]
status: 🟢 activ
prim_contact: 2026-04-23
ultim_contact: 2026-04-26
rol: medic oncolog curant — primă linie de contact OncoHelp pentru cazul tata
tags: [oncolog, oncohelp, medic-curant, programat-4-05, conflict-surse-status]
version: 1.2
sursa_status_profesional_email: 'semnătură email Dr. Anater 24.04.2026 — „Medic Specialist, Oncologie Medicala, Oncohelp Timisoara"'
sursa_status_profesional_site: 'oncohelp.ro/echipa-oncohelp/ accesat 2026-04-25 — „Medic Rezident" (probabil neactualizat după promovare)'
```

### Profil profesional [cercetare 2026-04-25, update 19:30 după ingest Gmail]

**Status profesional — CONFLICT DE SURSE (R12 protocol):**

| Sursă                                          | Status declarat                                                | Data verificării |
| ---------------------------------------------- | -------------------------------------------------------------- | ---------------- |
| Semnătură email Dr. Anater (24.04 + următoare) | **„Medic Specialist, Oncologie Medicala, Oncohelp Timisoara"** | 2026-04-24       |
| Site oficial oncohelp.ro/echipa-oncohelp/      | „Medic Rezident"                                               | 2026-04-25       |

**Interpretare R12:**

- **Self-identification în corespondență oficială cu pacient** (semnătură email cu titlu profesional declarat) = sursă autoritară directă cu impact legal/etic. Folosirea unui titlu fals în comunicare cu pacienți ar constitui falsificare profesională — improbabil într-o instituție reputabilă.
- **Site instituțional** = autoritară structurală, dar frecvent neactualizată (multe site-uri medicale nu reflectă promovări recente luni întregi).
- **Decizie:** prioritate **„Medic Specialist"** (per email semnătură) ca status curent. Site-ul probabil neactualizat post-promovare specialist (consistent cu vârstă ~31 ani + finalizare rezidențiat oncologie 5 ani la 2025-2026).

**Email instituțional `angelo.anater@oncohelp.ro` activ și folosit pentru corespondență (24-25.04.2026 — vezi `corespondenta/2026-04-24_re-solicitare-consult-anater.md`).** Email personal yahoo `angelo.anater95@yahoo.com` folosit secundar.

**Implicare profesională [CERT]:**

- Speaker la conferințe „Zilele OncoHelp" 2023 + 2024 (programe oficiale PDF oncohelp.ro)
- NU a fost identificată activitate publicistică (zero rezultate ResearchGate / Google Scholar / PubMed la 25.04.2026)
- Nu are profil public LinkedIn / DocPlanner / Pareri-medici accesibil

**Observație clinică din corespondență [CERT — sursă scrisă thread Gmail `19dbe7d30cfacbb3` 24.04.2026]:**

- Răspuns prompt (sub 24h) la solicitarea inițială Roland
- Comunicare structurată, separând componenta oncologică de cea cardiacă (interpretare echilibrată: ascita perihepatică + pelvină + pleurală minoră → „cel mai probabil secundară afecțiunii sale cardiace, NU oncologică primă vedere")
- Disponibil pentru programare directă (slot consult inițial 30.04.2026 → REPROGRAMAT 4.05.2026 per mail Anater 26.04)
- Recomandare conservatoare: NU urgentare paracenteză/laparoscopie pre-histopatologic
- Recomandări concrete pre-consult: markeri tumorali + consult cardiologic recent (<6 luni) + analize sânge generale
- Stil profesional consistent cu specialist deplin format (per self-id email)

**Considerații clinice [PROBABIL]:**

- Per self-id „Medic Specialist", Dr. Anater are autoritate clinică de specialist deplin format pentru gestionarea cazului (consult + propunere plan terapeutic)
- Decizii terapeutice majore (FLOT vs CROSS, chirurgie esofagogastrectomie, imunoterapie) discutate în mod tipic în echipa tumor board OncoHelp — standard de îngrijire pentru cancere eso-gastrice complexe
- Consultul cu Dr. Anater oferă acces la întreaga echipă OncoHelp, nu doar la deciziile sale individuale

### Surse cercetare

- https://oncohelp.ro/echipa-oncohelp/ (accesat 2026-04-25)
- https://oncohelp.ro/wp-content/uploads/2024/11/Program-conferinta-Alba-Iulia-Noiembrie-2024.pdf (program conferință 2024)
- https://oncohelp.ro/wp-content/uploads/2025/06/Program-OHSS-2025-4.pdf (program conferință 2025)
- https://oncohelp.ro/wp-content/uploads/2023/06/OSS-ed-VI-2023-Agenda-conferinta-1.pdf (program 2023)
- ResearchGate / Google Scholar / PubMed [NEGASIT 25.04.2026]
- LinkedIn / DocPlanner / Pareri-medici [NEGASIT public 25.04.2026]

---

## Dr. Mate Endre {#dr-mate-endre}

```yaml
id: dr-mate-endre
nume: Mate Endre
titlu: Dr.
titlu_profesional: Medic Rezident Oncologie Medicală
specializare: [oncologie medicala]
unitate: OncoHelp Timișoara
unitate_id: oncohelp-timisoara
departament: Secția de Oncologie
emails:
  primar: "[NEGASIT public 28.04.2026 — folosește centrala office@oncohelp.ro pentru contact]"
telefoane: []
status: 🟢 activ — PROGRAMAT consult inițial 30.04.2026 12:00
prim_contact: 2026-04-28 (recomandare telefonică Dr. Vornicu)
ultim_contact: 2026-04-28
rol: medic rezident oncolog desemnat pentru consultul inițial OncoHelp 30.04 — înregistrare pacient + stabilire pași suplimentari pentru diagnostic exact (post-biopsie inconcluzivă)
tags: [oncolog, oncohelp, medic-rezident, programat-30-04, consult-initial]
version: 1.0
sursa_recomandare: "telefon Dr. Vornicu Vlad 2026-04-28 — a recomandat slot 30.04 12:00 cu Dr. Mate Endre"
```

### Profil profesional [cercetare 2026-04-28]

- **Status profesional:** Medic Rezident Oncologie Medicală OncoHelp Timișoara
- **Training:** UMFT Timișoara (background România) + stagii Marseille (Franța) + Paris Saint-Louis AP-HP (Asistance Publique-Hôpitaux de Paris) — formare europeană în oncologie medicală
- **Focus declarat:** imunoterapie oncologică (per discuție telefonică Vornicu)
- **Rol în cazul tata:** consultul inițial pentru înregistrare pacient în baza OncoHelp + stabilire pași suplimentari diagnostic înainte de consult oncolog principal cu Dr. Anater + comisie multidisciplinară (4.05.2026)
- **Implicit din rol:** acces la întreaga echipă OncoHelp prin Dr. Mate Endre (NU înlocuiește consultul cu Dr. Anater + comisie)

### Surse cercetare

- Recomandare telefonică Dr. Vornicu 2026-04-28 (sursă orală — fără înregistrare scrisă)
- Site oficial oncohelp.ro/echipa-oncohelp/ — căutat 28.04.2026 [PROFIL public NEGASIT — probabil neadăugat încă la pagina echipă]
- ResearchGate / Google Scholar / PubMed / LinkedIn — [NEGASIT public 28.04.2026]

### Observație R17

- Toate informațiile profil profesional Mate Endre sunt **[PROBABIL]** până la verificare directă la consultul 30.04 (sursă unică = recomandare orală Vornicu).
- Email primar **[NEGASIT public]** — pentru contact pre-consult, folosește centrală OncoHelp `office@oncohelp.ro` cu mențiune „pentru Dr. Mate Endre, consult 30.04.2026 12:00".

### Istoric corespondență

- **2026-04-23 (data inițială Roland)** — trimis de Roland: solicitare consult oncologic pentru tata, prezentare context (CT 20.04 + biopsie în așteptare). Thread Gmail: `19dbe7d30cfacbb3` (vezi `corespondenta/2026-04-24_re-solicitare-consult-anater.md` la Task #11).
- **2026-04-24 10:56** — primit `RE: Solicitare consult oncologic` de la Dr. Anater: cale clinică propusă — așteptare biopsie + consult ulterior.
- **2026-04-25 18:00** — răspuns trimis manual de user (Roland) — confirmare biopsie 28-29.04 + cerere slot 30.04 + 5 întrebări organizatorice (analize/internare/documente/bilet trimitere/telefon contact).
- **2026-04-26 10:28** — primit răspuns Dr. Anater: **REPROGRAMARE 30.04 → 4.05.2026** (motiv: aglomerație 1 mai + caz nou necesită mai mult timp pentru constituirea dosarului de comisie oncologică) + clarificări complete la cele 5 întrebări (markeri tumorali specificați CEA + CA 19-9, bilet trimitere medic familie pentru oncologie, consult cardiologic recent extern cu ECG + ECO + scrisoare, plan zi 4.05 — comisie + chirurg eso + NU rămâne internat). Vezi `corespondenta/2026-04-24_re-solicitare-consult-anater.md` (thread închis 26.04) + `corespondenta/INDEX.md`.

### Note libere

- Răspuns prompt și atent (24h, apoi 16h la a doua rundă) — semnal pozitiv pentru relația medic-pacient
- A explicat clar că acumulările lichidiene observate la CT pot fi cardiace, nu doar oncologice — abordare echilibrată non-alarmistă
- **Reprogramarea proactivă** (mutare 30.04 → 4.05 din proprie inițiativă, pentru calitate caz nou) — semnal de seriozitate clinică
- Următorul pas: telefoane mâine 27.04 (medic familie + cardiolog + Synevo markeri), asamblare dosar fizic post-biopsie 28-30.04, consult **4.05.2026 OncoHelp Timișoara**
- **Conflict surse status profesional R12** rezolvat în favoarea „Specialist" per self-id email — site oncohelp.ro probabil neactualizat post-promovare
- Pentru clarificare definitivă, în conversația 4.05 cu Dr. Anater se poate întreba politicos „Care este momentul în care ați promovat specialitatea?" — informație utilă pentru context relație medic-pacient

---

## Dr. Vornicu Vlad-Norin {#dr-vornicu-vlad}

```yaml
id: dr-vornicu-vlad
nume: Vornicu Vlad-Norin
titlu: Dr.
titlu_profesional: Medic Specialist Oncolog
specializare: [oncologie medicala, oncologie clinica]
focus_clinic:
  [oncologie pulmonara (principal), oncologie mamara, oncologie urologica]
unitate: OncoHelp Timișoara
unitate_id: oncohelp-timisoara
departament: Secția de Oncologie
pozitie_academica: Asistent Universitar PhD — UMFT „Victor Babeș" Timișoara, Departament IX Chirurgie I, Disciplina Oncologie
emails:
  primar: vornicuvlad91@gmail.com
telefoane:
  - {
      numar: "0762 120 428",
      sursa: "furnizat user 2026-04-25 + ResearchGate",
      tip: mobil,
    }
data_nasterii: 1991-07-06
varsta: 35
status: 🟡 contact furnizat user — încă fără interacțiune directă
prim_contact: null
ultim_contact: null
rol: oncolog senior accesibil — eventual a doua opinie / specialist complementar Dr. Anater
tags:
  [
    oncolog,
    oncohelp,
    specialist,
    asistent-universitar-umft,
    oncologie-pulmonara,
    researchgate,
  ]
version: 1.0
publicatii:
  researchgate_id: Vlad-Norin-Vornicu
  citari: 11
  reads: 396
  publicatii_count: 2
implicare_publica: [activist spital oncologic Reșița Caraș-Severin]
sources_verified: 2026-04-25
```

### Profil profesional [cercetare 2026-04-25]

**Status profesional [CERT — multiple surse oficiale]:**

- **Medic Specialist Oncolog** la OncoHelp Timișoara, Secția de Oncologie [oncohelp.ro/echipa-oncohelp/]
- **Asistent Universitar PhD** la UMFT „Victor Babeș" Timișoara, Departament IX Chirurgie I, Disciplina Oncologie [umft.ro]
- Născut 06.07.1991 (35 ani la 25.04.2026); naționalitate română [ResearchGate]
- Specializări declarate: Clinical Oncology + Medical Oncology
- Email personal: `vornicuvlad91@gmail.com` (verificat ResearchGate)
- Telefon mobil: `0762 120 428` (confirmat user + identificat și prin sursă publică ResearchGate — coincidență validatoare)

**Activitate științifică [CERT — ResearchGate, Medicina journal]:**

- 2 publicații indexate, 11 citări, 396 vizualizări la 25.04.2026
- Publicație 1: „Unilateral Orbital Metastasis as the Unique Symptom in the Onset of Breast Cancer in a Postmenopausal Woman" (case report — oncologie mamară)
- Publicație 2 (2025): tissue prognostic markers for clear cell renal cell carcinoma — co-autor în jurnalul _Medicina_

**Conferințe și prezentări [CERT — surse media + programe conferință]:**

- 2025 — European Lung Cancer Congress (Paris): participant oncologie pulmonară (delegație OncoHelp)
- Zilele OncoHelp (Sibiu): prezentare „Depășind Limitele în Cancerul Pulmonar: Progrese în Terapia Țintită și Imunoterapie"
- Activism public: apel pentru construirea spitalului oncologic în Reșița (Caraș-Severin) — implicare extra-clinică în politici publice de sănătate

**Profil clinic estimat [PROBABIL — sinteză din publicații + conferințe]:**

- **Focus principal:** oncologie pulmonară (prezentări conferințe, congres ELCC Paris)
- **Competențe secundare:** oncologie mamară (case report), oncologie urologică (publicație 2025)
- **Generalist oncologie medicală:** consult pacienți eso-gastric / pancreatic / colorectal probabil în portfoliul standard de specialist OncoHelp
- **Adâncime academică:** PhD finalizat, implicare educațională activă (asistent universitar)

**Considerații pentru consult [PROBABIL]:**

- Specialist deplin format, ~5 ani vechime post-rezidențiat (calculat din naștere 1991 + medicină 6 ani + rezidențiat 5 ani → specialist din ~2022-2023)
- Acces direct prin numărul personal (0762120428) sugerează relație non-instituțională (recomandare prin rețea medicală sau cunoștință familie)
- Pentru o opinie complementară pe cazul tata, oferă perspectivă de specialist deplin format, complementar cu Dr. Anater (rezident) — ambii fiind parte din **aceeași echipă OncoHelp** (NU concurențial, ci colaborativ)

### Surse cercetare

- https://oncohelp.ro/echipa-oncohelp/ (accesat 2026-04-25)
- https://www.umft.ro/en/medicine/departments-of-the-medicine-faculty/department-ix-surgery-i/oncology/ (accesat 2026-04-25)
- https://www.umft.ro/wp-content/uploads/2024/04/CV-Vornicu-Vlad-Norin__RO.pdf (404 la 2026-04-25 — sursă posibil mutată)
- https://www.researchgate.net/profile/Vlad-Norin-Vornicu (accesat 2026-04-25)
- https://www.radioresita.ro/actualitate/medicii-de-la-oncohelp-timisoara-la-congresul-european-de-cancer-pulmonar-de-la-paris (Congres Paris, accesat 2026-04-25)
- https://www.radioresita.ro/actualitate/pacientii-cu-cancer-din-caras-severin-renunta-la-tratament-din-cauza-navetei-la-timisoara-medicul-oncolog-vlad-vornicu-face-apel-pentru-construirea-unui-spital-oncologic-la-resita (apel Reșița, accesat 2026-04-25)
- https://www.g4media.ro/pacientii-cu-cancer-din-caras-severin-renunta-la-tratament-din-cauza-navetei-la-timisoara-sunt-situatii-reale-greu-de-suportat-pentru-cineva-care-se-lupta-deja-cu-o-boala-grava.html (G4Media același apel, accesat 2026-04-25)

### Istoric corespondență

- _Niciun contact direct încă._ Numărul `0762 120 428` furnizat de user 2026-04-25 — context: căutare opțiuni complementare la consultul programat cu Dr. Anater **4.05.2026 OncoHelp** (REPROGRAMAT din 30.04 per mail Anater 26.04).

### Note libere

- _De completat după prima interacțiune._
- Coincidență validatoare: numărul furnizat de user a fost identificat și ca sursă publică ResearchGate → confirmă că e numărul corect al Dr. Vornicu și nu o eroare de transcriere.
- Strategie sugerată: așteptăm consultul cu Dr. Anater **4.05** înainte de a apela Dr. Vornicu — dacă Dr. Anater îl include în echipa care discută cazul (tumor board), apelul direct devine inutil.

---

## Note de utilizare a fișierului

- **Actualizare la fiecare interacțiune** — `ultim_contact` se updatează la fiecare mesaj, telefon sau consult cu medicul.
- **Versiune** — incrementare la modificări structurale (1.0 → 1.1 = adăugare informație nouă; 1.0 → 2.0 = restructurare).
- **Sync DASHBOARD** — modificări aici declanșează regenerarea tab-ului „👥 Echipă medicală" în `DASHBOARD.html` (vezi Task #13 din planul curent + R18).
- **Sync INDEX.json** — modificări aici declanșează rerularea `python scripts/generate_index.py` (R27 — auto-propagare ingest Gmail).
- **Privacy:** fișier published pe GitHub Pages public (rolandpetrila.github.io/Tati_Dosar_Medical) cu acordul user — datele de contact sunt cele oficiale oncohelp.ro + telefon Vornicu deja confirmat ca sursă publică ResearchGate.
