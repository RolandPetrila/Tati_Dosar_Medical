# DOSAR_DATE_BRUTE — Bundle JSON canonice medicale

**Generat automat:** 2026-04-30 01:40 · **Sursă:** `Dosar_Medical/*.json` (excluse: meta.json, MANIFEST, SYSTEM_HEALTH, carte_identitate, talon_pensie) · **Total documente:** 19

> **Scop:** retrieval direct în Claude Projects pentru date medicale brute (analize, imagistică, biopsie, medicație, scrisori medicale, intervenții). Sursa primară rămâne JSON-urile canonice individuale; acest bundle e mirror narativ pentru parcurs RAG eficient.
>
> **NU edita acest fișier direct** — e regenerat la fiecare commit cu modificare în `Dosar_Medical/*.json` (R31 + pre-commit hook).

---

## 📚 Cuprins

- [2012-02-17 — raport spitalizare angioplastie complet](#2012-02-17-cardiologie-vichy-stent)
- [2024-05-30 — buletin analize laborator hematologie biochimie](#2024-05-30-analize-upu-sange-1517243)
- [2024-05-30 — buletin analize urina sumar sediment](#2024-05-30-analize-upu-urina-1517290)
- [2024-05-30 — consult upu compus gastro cardio ekg scrisoare](#2024-05-30-upu-consult-gastro-cardio)
- [2024-06-04 — buletin analize serologie](#2024-06-04-anti-helicobacter-pylori-igg-77449)
- [2024-09-06 — buletin analize serologie](#2024-09-06-anti-helicobacter-pylori-igg-79765)
- [2025-06-17 — buletin analize laborator complet](#2025-06-17-buletin-analize-sange)
- [2025-10-28 — scrisoare medicala consult](#2025-10-28-scrisoare-urologie-gastroenterologie)
- [2025-11-10 — ecografie transtoracica raport](#2025-11-10-ecografie-transtoracica)
- [2025-11-10 — schema tratament manuscris](#2025-11-10-schema-medicamente)
- [2025-11-10 — scrisoare medicala consult cardiologie](#2025-11-10-scrisoare-medicala-cardiologie)
- [2025-11-28 — externare spital cura chirurgicala](#2025-11-28-externare-chirurgie-hernie)
- [2026-04-17 — bilet trimitere investigatii paraclinice](#2026-04-17-bilet-trimitere-CT)
- [2026-04-17 — buletin examen histopatologic biopsie](#2026-04-17-biopsie-esofagiana-histopatologic)
- [2026-04-17 — buletin analize laborator functie renala](#2026-04-17-buletin-bioclinica-uree-creatinina)
- [2026-04-17 — buletin examen colonoscopic](#2026-04-17-examen-colonoscopic)
- [2026-04-17 — buletin examen gastroscopic](#2026-04-17-examen-gastroscopic)
- [2026-04-20 — raport imagistica ct](#2026-04-20-ct-torace-abdomen-pelvis)
- [2026-04-29 — buletin analize laborator markeri tumorali HbA1c](#2026-04-29-buletin-bioclinica-markeri-tumorali-hba1c)
---

## <a name="2012-02-17-cardiologie-vichy-stent"></a> 2012-02-17 — Raport Spitalizare Angioplastie Complet (Cardiologie Intervențională)
**Sursă:** `Dosar_Medical/2012-02-17_cardiologie_vichy_stent.json` · **Confidence:** high · **Flags:** pdf_complet_obtinut_2026-04-28, stent_bms_confirmat, anomalie_inaltime_168_vs_178

> Documentul original franceză + traducere autorizată în română. Stent confirmat ca BMS (Bare Metal Stent — «stent gol») RX VISION 3.5 x 28 mm Abbott Nr. 1110341 — important clinic pentru deciziile pre-chirurgie esofagiană (DAPT scurt, risc tromboză in-stent foarte scăzut la 14 ani vechime). Discrepanță transcriere: în coronarografie 178 cm, în angioplastie 168 cm — probabilă eroare de transcriere; greutatea 85 kg + diagnostic «Obezitate» sugerează 168 cm e mai probabil corect (IMC 30.1 vs 26.8); de clarificat cu user.

### 👤 Pacient

  - **nume:** PETRILA
  - **prenume:** VIOREL-MIHAI
  - **nume_text_original_document:** PETRILA PETRILA VIOREL MIHAI (probabil eroare de transcriere)
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_eveniment:** 52
  - **sex:** M
  - **ocupatie_la_data_eveniment:** șofer de camion
  - **stare_civila_la_data_eveniment:** căsătorit
  - **limbi_vorbite_la_data_eveniment:** română (matern); italiană (puțin); franceză (nu vorbește)
  - **inaltime_kg_la_data_eveniment:**
      - **valoare_mentionata_coronarografie_17_02:** 178 cm
      - **valoare_mentionata_angioplastie_19_02:** 168 cm
      - **discrepanta_observata:** 10 cm — probabilă eroare de transcriere; per IMC + diagnostic 'Obezitate' din raport, 168 cm e mai probabil corect [INCERT — de clarificat cu user]
  - **greutate_kg_la_data_eveniment:** 85
  - **imc_calculat_la_data_eveniment:** 30.1 (la 168 cm) sau 26.8 (la 178 cm) — clasificare 'obezitate clasa I' (la 168) sau 'supraponderal' (la 178)
  - **dosar_nr_spital_vichy:** 112004096
  - **confidence_identificare:** high

### 👥 Medici / Unități

  - **spital_principal:**
      - **denumire_oficiala:** Centrul Spitalicesc Jacques Lacarin Vichy
      - **subtitlu:** Spital în serviciul vieții
      - **adresa:** Bulevardul Denière - Cutia poștală 2757 - 03207 Vichy Cedex, Franța
      - **telefoane_ingrijiri_intensive_vichy:**
        - 04.70.97.33.48
        - 04.70.97.33.97
      - **fax_secretariat_vichy:**
        - 04.70.97.22.57
        - 04.70.97.33.47
  - **spital_secundar_interventie:**
      - **denumire_oficiala:** Centrul Spitalicesc Moulins Yzeure
      - **rol:** Centrul de Cardiologie de Intervenție din Allier (CCIA) — unde s-a efectuat angioplastia
      - **telefoane_ingrijiri_intensive:**
        - 04.70.35.77.95
        - 04.70.35.76.73
      - **fax_secretariat:**
        - 04.70.35.77.63
        - 04.70.35.76.79
  - **structura_clinica:** Centru (Polul) de Medicină — Structură internă de medicină pentru specialitatea Cardiologie și îngrijiri intensive de cardiologie
  - **echipa_medicala_completa:**
      - **coordonator:** Dr. Xavier MARCAGGI (coordonator Centrul de Cardiologie de Intervenție din Allier; operator angioplastie 19.02)
      - **sefii_sectiei:**
        - Dr. Eddie PIERRE-JUSTIN (Șeful secției)
        - Dr. Georges AMAT (Șeful secției)
      - **medici_generalisti:**
        - Dr. Jean Jacques CLOIX (Moulins)
        - Dr. Gabriel BITAR (Vichy — A.OP angioplastie 19.02)
        - Dr. Raphael RODRIGUEZ (Moulins)
      - **medic_atasat:** Dr. Pierre LAVAUD (Vichy — operator coronarografie 17.02)
      - **interni_implicati:**
        - Djamel ADJTOUTAH (raport spitalizare 17.02)
        - Xavier CHABIN (CS 19.02 + CDU 23.02)
        - Armel NANA (CS 21.02)
      - **asistente_si_manipulatori:**
        - Me. LACOGNE Sylvie (asistentă coronarografie)
        - Me. PAQUET (manipulator A.OP coronarografie)
        - Me. THEVENON ESTELLE (asistentă angioplastie)
        - Me. REBOT Patricia (manipulator angioplastie)
  - **medic_familie_la_data_eveniment_2012:**
      - **nume:** Dr. ORBAN Ecaterina
      - **telefon_la_data_eveniment:** 0040 723 560 193 (per documentul francez)
      - **resedinta:** Nadlac
      - **observatie_continuitate:** [CERT] Aceeași persoană ca medicul familie actual în 2026 (Dr. Orbán Ecaterina-Maria, Cabinet Medical Individual Nădlac, cod parafă 718705) — continuitate de 14 ani

### 🏥 Context clinic

  - **motivul_internarii:** Dureri toracice
  - **antecedente_personale_la_data_eveniment:**
    - Niciuna semnificativă declarată
    - Tabagism activ (intoxicație tabagică)
    - Obezitate
  - **factori_de_risc_cardiovascular:**
    - Tabagism activ
    - Obezitate
    - Sex masculin >50 ani
  - **antecedent_diabet_zaharat_la_2012:** [NEGASIT — neînregistrat în acest document; DZ tip 2 a fost dezvoltat probabil ulterior 2012]
  - **antecedent_HTA_la_2012:** [NEGASIT — neînregistrat în acest document]

### 🔬 Examinări efectuate

  - **coronarografie_initiala_17_02:**
      - **procedura_nr:** 11829
      - **data:** 2012-02-17
      - **ora_inceput:** 09:54
      - **ora_sfarsit:** 10:37
      - **durata_minute:** 43
      - **operator:** Dr. Pierre LAVAUD
      - **asistente:**
        - Me. LACOGNE Sylvie
      - **manipulator:** Me. PAQUET (A.OP)
      - **cale_abordare:** artera radială dreaptă - 6 French
      - **grad_urgenta:** Urgent — spitalizat (internat)
      - **timp_scopie_minute:** 2.37
      - **doza_totala_cgycm2:** 2586.2
      - **produs_contrast:** IOMERON 350, 63 ml
      - **complicatii:** niciuna
      - **rezultate:**
          - **hemodinamica:**
              - **frecventa_cardiaca_pe_min:** 60
              - **ritm_cardiac:** ritm sinusal
              - **TA_aortica_mmHg:** 117/77
              - **TA_medie_mmHg:** 96
          - **retea_coronara_stanga:**
              - **trunchi_comun:** normal, fără stenoză
              - **IVA_proximala:** stenoză foarte compactă (70-90%)
              - **IVA_mijlocie:** stenoză subocluzivă (90-99%)
              - **circumflexa:** fără leziuni semnificative (stenoză inferioară de 50% pe marginală — per Dr. P LAVAUD 17.02)
              - **coronara_dreapta:** fără leziuni
          - **interpretare_clinica:** Stenoză lungă compactă la primul segment și începutul celui de-al doilea segment IVA, înglobând începutul primei diagonale; strat în aval IVA subțire și cu convulsii (spasmatic). Fluxul TIMI 3 restabilit prin fibrinoliză.
  - **angioplastie_19_02:**
      - **procedura_nr:** 11836
      - **data:** 2012-02-19
      - **ora_inceput:** 16:05
      - **ora_sfarsit_declarat_in_doc:** 00:00 (probabilă eroare de transcriere)
      - **durata_declarata_minute:** 965
      - **comentariu_durata:** [INCERT] 965 minute = ~16h, probabil eroare de transcriere; o angioplastie standard durează 30-90 minute
      - **operatori:**
        - Dr. Xavier MARCAGGI (operator principal)
        - Dr. Gabriel BITAR (A.OP — ajutor operație)
      - **corespondent:** URP
      - **asistente:**
        - Me. THEVENON ESTELLE
      - **manipulatori:**
        - Me. REBOT Patricia
      - **cale_abordare:** artera radială dreaptă - 6 French
      - **indicatii:** ANGHINĂ PECTORALĂ INSTABILĂ
      - **grad_urgenta:** Urgent amânat — spitalizat (internat) — zi nelucrătoare (sărbătoare, duminică)
      - **produs_contrast:** IOMERON 350 ml
      - **hemodinamica_la_inceput:**
          - **frecventa_cardiaca_pe_min:** 70
          - **ritm_cardiac:** ritm sinusal
          - **TA_aortica_mmHg:** 101/75
          - **TA_medie_mmHg:** 86
      - **material_utilizat:**
          - **ghid_dispozitive_ghidare:**
            - **nume:** TERUMO în J (Terumo) · **nr_serie:** 110711
            - **nume:** Ghidaj de sârmă BMW (Abbott) · **nr_serie:** 1111271
          - **cateter_angioplastie:**
              - **nume:** LAUNCHER EBU 3.5 6F 100 cm (Medtronic)
              - **nr_serie:** 0006023892 (sau 0006023893 — apare în ambele forme în doc)
          - **balon:**
              - **nume:** Balon Apex monorail 2.5 x 20 (Boston Scientific)
              - **nr_serie:** 14985066
              - **predilatare:** presiune maximă 10 ATM, durată 30 secunde
          - **stent_coronarian:**
              - **nume_dispozitiv:** RX VISION 3.5 x 28 mm (Abbott)
              - **nr_serie:** 1110341
              - **tip_stent:** BMS (Bare Metal Stent) — «stent gol»
              - **confirmare_BMS_in_document:**
                - «aplicat cu un stent gol VISION 3.5 x 28 mm cu un rezultat primar satisfăcător» (text Dr. MARCAGGI 19.02)
                - «Succes primar de angioplastie a arterei interventriculare anterioare proximale cu implantare a unui stent gol» (concluzie raport)
              - **presiune_durata:** 10 ATM, durată 20 secunde
      - **rezultate:**
          - **control_angiografic_final:** artera interventriculară anterioară proximală lipsită de leziune semnificativă
          - **flux_coronar_final:** TIMI 3 (normal)
          - **concluzie_oficiala:** Succes primar de angioplastie a arterei interventriculare anterioare proximale cu implantare a unui stent gol
      - **complicatii:** niciuna

### 📦 Date suplimentare

  - **cronologie_clinica:**
    - **data:** 2012-02-13 (estimat — «în urmă cu trei zile») · **eveniment:** Prima durere toracică la efort (~10 minute), în timpul ridicării de greutăți
    - **data:** 2012-02-16 noaptea · **eveniment:** Recidivă durere toracică care l-a sculat din somn (durată scurtă)
    - **data:** 2012-02-17 ~04:00 · **eveniment:** Durere toracică continuă în legătură cu necroză anterioară — preluare de SAMU pentru sindrom coronarian acut
    - **data:** 2012-02-17 07:45 · **eveniment:** Fibrinoliza cu metalize (tenecteplază) — efectuată la SAMU
    - **data:** 2012-02-17 09:54-10:37 · **eveniment:** Coronarografie de control la Centrul Spitalicesc Vichy (Procedura nr. 11829) — Dr. Pierre LAVAUD operator
    - **data:** 2012-02-17 · **eveniment:** Decizie: NU se efectuează angioplastie imediat (flux TIMI 3 obținut prin fibrinoliză, durere dispărută); reluare în 24-48h
    - **data:** 2012-02-19 16:05 — 00:00 · **eveniment:** Coronarografie de control + angioplastie coronariană (Procedura nr. 11836) — Dr. Xavier MARCAGGI operator + Dr. Gabriel BITAR (A.OP)
    - **data:** 2012-02-19 (CS — sinteză zi 19.02) · **eveniment:** Aparent fără recidivă durere toracică. Vârf troponină 150 cu descreștere. ECG persistent supradenivelare ST V2V3. Contact cu Dr. ORBAN Ecaterina (medic familie Nădlac, telefon 0040 723 560 193?)
    - **data:** 2012-02-21 · **eveniment:** Asimptomatic. Examen clinic fără particularități. Transfer la cardiologie. Mobilizare. — CS Dr. Armel NANA (Intern)
    - **data:** 2012-02-23 · **eveniment:** CDU Dr. Xavier CHABIN (Intern) — examen clinic fără semne insuficiență cardiacă, fără durere toracică, persistență supradenivelare ST V2V3, fără anomalii repolarizare
    - **data:** 2012-02-24 (estimat) · **eveniment:** Întoarcere în România cu mașina, împreună cu soția
  - **diagnostic_principal:**
      - **cod_icd10:** I21.0
      - **descriere_oficiala:** Infarct miocardic acut al peretelui anterior
      - **descriere_originala_document:** Sindrom coronarian acut ST + în antero-septo-apical
      - **tip:** principal
      - **confidence_ocr:** high
  - **diagnostice_secundare:**
    - **cod_icd10:** I25.1 · **descriere_oficiala:** Boală cardiacă aterosclerotică · **descriere_originala_document:** Stenoză foarte compactă (70-90%) artera interventriculară anterioară (IVA) proximală + stenoză subocluzivă (90-99%) IVA mijlocie · **tip:** secundar · **confidence_ocr:** high
    - **cod_icd10:** E66.9 · **descriere_oficiala:** Obezitate, nespecificată · **descriere_originala_document:** Obezitate · **tip:** asociat · **confidence_ocr:** high
    - **cod_icd10:** F17.200 · **descriere_oficiala:** Dependență de nicotină, nespecificată, necomplicată · **descriere_originala_document:** Tabagism activ · **tip:** asociat · **confidence_ocr:** high · **note:** Pacientul a renunțat la fumat în 2012 post-eveniment cardiac (per CONTEXT_MEDICAL.md §5).
    - **descriere_oficiala:** Anghină pectorală instabilă (indicație angioplastie 19.02) · **descriere_originala_document:** ANGHINĂ PECTORALĂ INSTABILĂ (indicații pentru angioplastie) · **tip:** asociat · **confidence_ocr:** high
  - **tratament_in_acut:**
      - **fibrinoliza:**
          - **medicament:** tenecteplază (TNK-tPA)
          - **denumire_comerciala_franta:** Metalyse (Metaliză)
          - **data_administrare:** 2012-02-17 07:45
          - **indicatie:** STEMI antero-septo-apical — fibrinoliza primară pre-spital (SAMU)
          - **rezultat:** succes — flux TIMI 3 obținut, durere toracică dispărută
      - **antiagregante_anticoagulant_dupa_internare:**
        - **medicament:** PLAVIX · **substanta_activa:** clopidogrel · **rol:** antiagregant plachetar (P2Y12 inhibitor)
        - **medicament:** ASPEGIC · **substanta_activa:** acid acetilsalicilic (aspirina) · **rol:** antiagregant plachetar (COX-1 inhibitor)
        - **medicament:** LOVENOX · **substanta_activa:** enoxaparină sodică · **rol:** anticoagulant injectabil (LMWH)
      - **examinare_la_primire_17_02:**
          - **stare_pacient:** conștient, cooperant
          - **durere_toracica:** fără recidivă post-fibrinoliză
          - **auscultatie_cardio_pulmonara:** fără particularități, constante hemodinamice bune
          - **ecg_evolutie:**
            - 17.02: persistență supraelevare ST
            - 23.02: persistență supraelevare ST în V2V3, fără anomalii repolarizare
  - **biomarkeri_dinamica:**
      - **troponina_varf:**
          - **valoare:** 150
          - **unitate_neclarificata:** [INCERT — unitatea de măsură nu apare explicit în traducere; probabilă pg/mL sau ng/L per pattern francez]
          - **evolutie:** în descreștere la 19.02
  - **recomandari_externare:**
    - Repatriere la Timișoara cu asistență medicală (oferit de spital)
    - Pacientul a preferat întoarcere cu mașina împreună cu soția
    - Transfer la secția de cardiologie pentru mobilizare (intern)
    - Continuare DAPT (PLAVIX + ASPEGIC) — durata neexplicită în document
  - **note_traducere:**
      - **traducator:** Blidar Ioana
      - **autorizatie:** 705/2002 Ministerul Justiției
      - **limba_originala:** franceză
      - **limba_traducere:** română
      - **nota_traducator:** «Documentul nu este semnat și nici ștampilat de emitent» — repetat pe fiecare pagină
      - **implicatie_lipsa_semnatura:** Documentul francez original poate fi un raport de spital intern fără semnătură olografă; traducerea autorizată e validă legal
  - **implicatii_clinice_2026_pentru_oncologie:**
      - **tip_stent_BMS_implicatii:**
        - [CERT] BMS (Bare Metal Stent) implantat 2012-02-19 → endotelizare completă în 4-6 săptămâni → la 14 ani vechime risc de tromboză in-stent foarte scăzut
        - [PROBABIL] DAPT (dual antiplatelet therapy) standard pentru BMS = 1 lună post-stent (vs 6-12 luni pentru DES) — pacientul a continuat doar Aspenter (monoterapie aspirina) post-2012
        - [PROBABIL — per ghiduri ESC 2017 + ACC/AHA] Pentru chirurgie majoră non-cardiacă la pacient post-BMS >12 luni, pauza Aspenter 5-7 zile pre-op este în general sigură (risc tromboză in-stent <1%)
        - [CERT] Aceasta e informație CRUCIALĂ pentru chirurgul oncolog care va evalua posibilitatea esofagectomiei — risc cardiovascular perioperator scade semnificativ vs. ipoteza unui DES
      - **ldl_actual_2025:**
          - **valoare:** 133 mg/dL (buletin 17.06.2025)
          - **tinta_ESC_post_stent:** <70 mg/dL
          - **tinta_neatinsa:** ✅ true
          - **context:** Pacientul nu administrează curent statină (TORVACARD prescris 10.11.2025 dar nu luat — clarificat user 25.04.2026). De ridicat la consult oncolog 4.05 + medic familie.
      - **evolutie_simptomatica_post_2012:** Fără recidivă SCA documentată în acest dosar — pacientul a fost stabil cardiologic 14 ani sub Aspenter + Concor + Triplixam. Episodul UPU 30.05.2024 a arătat «hs-cTnI dinamic 4.24 → 4.59 ng/L trending UP» și ECG «Markedly Abnormal» — de monitorizat, dar nu re-internat pentru SCA
  - **referinte_legate:**
      - **context_medical_md:** CONTEXT_MEDICAL.md §3 (Boală cardiacă ischemică cu stent — februarie 2012) + §5 (Stil de viață — fumat 1977-2012)
      - **schema_medicatie_actuala:** Dosar_Medical/2025-11-10_schema_medicamente.json (Aspenter 75 mg 0-1-0 — antiagregare post-stent)
      - **consult_cardiologie_recent:** Dosar_Medical/2025-11-10_scrisoare_medicala_cardiologie.json (Dr. LAZA CRISTINA, cod parafă C07842) + ECO transtoracic FE 55%
      - **episod_UPU_2024:** Dosar_Medical/2024-05-30_upu_consult_gastro_cardio.json (consult cardiologic Dr. Post Mihaela)

---

## <a name="2024-05-30-analize-upu-sange-1517243"></a> 2024-05-30 — Buletin Analize Laborator Hematologie Biochimie (Laborator Clinic)
**Sursă:** `Dosar_Medical/2024-05-30_analize_upu_sange_1517243.json` · **Buletin:** 1517243 · **Confidence:** high · **Flags:** valori_patologice_glicemie_creatinina, UPU_30_05_2024_episod_major, hiperglicemie_aproape_dubla_limita

> Analize din episodul UPU 30.05.2024. Glicemie 180.48 mg/dL (↑↑ aproape dublu față de limita 115 — hiperglicemie severă necontrolată), lymphopenie (LY% 15.4), creatinină 0.66 (↓ ușor sub limita 0.7). Restul hemoleucogramei + biochimiei — în limite normale. Examinat la analizor SYSMEX XN 1000 (hematologie) + COBAS INTEGRA 400 PLUS (biochimie) la Spitalul Clinic Județean de Urgență Arad.

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **nume_text_original_document:** PETRILA VIOREL MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 65 ani 0 luni
  - **sex:** M
  - **adresa:** Nadlac, AR
  - **nr_FO:** 1021735
  - **sectie_spital:** UPU Adulți
  - **confidence_identificare:** high

### 🧪 Analize laborator

- **categorie:** HEMATOLOGIE · **nume:** Leucocite (WBC) · **valoare_numerica:** 8.82 · **unitate:** x10^3/µL · **interval_referinta_text:** 4.00-10.00 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Eritrocite (RBC) · **valoare_numerica:** 4.93 · **unitate:** x10^6/µL · **interval_referinta_text:** 3.80-5.80 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Hemoglobina (HGB) · **valoare_numerica:** 15.1 · **unitate:** g/dL · **interval_referinta_text:** 12.60-17.40 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Hematocrit (HCT) · **valoare_numerica:** 42.8 · **unitate:** % · **interval_referinta_text:** 37.00-51.00 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Trombocite (PLT) · **valoare_numerica:** 186.0 · **unitate:** x10^3/µL · **interval_referinta_text:** 150.00-450.00 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Volum eritrocitar mediu (MCV) · **valoare_numerica:** 86.8 · **unitate:** fL · **interval_referinta_text:** 81.00-103.00 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Hemoglobina eritrocitara medie (MCH) · **valoare_numerica:** 30.6 · **unitate:** pg · **interval_referinta_text:** 27.00-34.00 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Concentrația medie Hb/Eritrocite (MCHC) · **valoare_numerica:** 35.3 · **unitate:** % · **interval_referinta_text:** 31.00-36.00 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** RDW-SD · **valoare_numerica:** 39.8 · **unitate:** fL · **interval_referinta_text:** 35.10-43.90 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** RDW-CV · **valoare_numerica:** 12.5 · **unitate:** % · **interval_referinta_text:** 11.60-14.40 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Neutrofile procentual (NE%) · **valoare_numerica:** 78.1 · **unitate:** % · **interval_referinta_text:** 45.00-80.00 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Limfocite procentual (LY%) · **valoare_numerica:** 15.4 · **unitate:** % · **interval_referinta_text:** 20.00-55.00 · **flag:** scazut · **confidence_ocr:** high · **note:** Lymphopenie — sub limita 20%.
- **categorie:** HEMATOLOGIE · **nume:** Monocite procentual (MO%) · **valoare_numerica:** 5.1 · **unitate:** % · **interval_referinta_text:** 0.00-15.00 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Eozinofile procentual (EO%) · **valoare_numerica:** 1.1 · **unitate:** % · **interval_referinta_text:** 0.00-7.00 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Bazofile procentual (BA%) · **valoare_numerica:** 0.3 · **unitate:** % · **interval_referinta_text:** 0.00-2.00 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Neutrofile absolute (NE#) · **valoare_numerica:** 6.88 · **unitate:** x10^3/µL · **interval_referinta_text:** 2.00-8.00 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Limfocite absolute (LY#) · **valoare_numerica:** 1.36 · **unitate:** x10^3/µL · **interval_referinta_text:** 1.00-4.00 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Monocite absolute (MO#) · **valoare_numerica:** 0.45 · **unitate:** x10^3/µL · **interval_referinta_text:** 0.30-1.00 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Eozinofile absolute (EO#) · **valoare_numerica:** 0.1 · **unitate:** x10^3/µL · **interval_referinta_text:** 0.05-0.70 · **flag:** normal · **confidence_ocr:** high
- **categorie:** HEMATOLOGIE · **nume:** Bazofile absolute (BA#) · **valoare_numerica:** 0.03 · **unitate:** x10^3/µL · **interval_referinta_text:** 0.00-0.20 · **flag:** normal · **confidence_ocr:** high
- **categorie:** BIOCHIMIE · **nume:** Uree (UREA) · **valoare_numerica:** 31.39 · **unitate:** mg/dL · **interval_referinta_text:** 17.13-49.25 · **flag:** normal · **confidence_ocr:** high
- **categorie:** BIOCHIMIE · **nume:** Creatinină serică · **valoare_numerica:** 0.66 · **unitate:** mg/dL · **interval_referinta_text:** 0.70-1.20 · **flag:** scazut · **confidence_ocr:** high · **note:** Ușor sub limită — neîngrijorător izolat.
- **categorie:** BIOCHIMIE · **nume:** Glucoză · **valoare_numerica:** 180.48 · **unitate:** mg/dL · **interval_referinta_text:** 82.00-115.00 · **flag:** crescut · **confidence_ocr:** high · **note:** Hiperglicemie severă — ~1.6× limita superioară. Consecvent cu DZ tip 2 necontrolat la momentul prezentării UPU.
- **categorie:** BIOCHIMIE · **nume:** AST (TGO) · **valoare_numerica:** 21.4 · **unitate:** U/L · **interval_referinta_text:** <40.0 · **flag:** normal · **confidence_ocr:** high
- **categorie:** BIOCHIMIE · **nume:** Amilaza · **valoare_numerica:** 40.5 · **unitate:** U/L · **interval_referinta_text:** 28.0-100.0 · **flag:** normal · **confidence_ocr:** high
- **categorie:** BIOCHIMIE · **nume:** ALT (TGP) · **valoare_numerica:** 33.6 · **unitate:** U/L · **interval_referinta_text:** <41.0 · **flag:** normal · **confidence_ocr:** high

### 🔢 Numere referință

  - **numar_buletin:** 1517243
  - **cod_proba:** 1517243
  - **nr_FO:** 1021735
  - **cod_formular:** FG-18-01 Editia din 28.12.2023

### 📦 Date suplimentare

  - **medic_solicitant:**
      - **nume:** Dr. Pop Florica
      - **specialitate:** medic primar medicină de urgență
      - **cod_parafa:** C79981
  - **medic_validator_laborator:**
      - **nume:** Dr. IGAS ANGELICA
      - **specialitate:** medic primar medicina de laborator
      - **cod_parafa:** 119856
  - **unitate_laborator:**
      - **denumire:** Spitalul Clinic Județean de Urgență Arad
      - **sectie:** Laborator Central
      - **acreditare:** ANMCS + SR EN ISO 15189:2013 Certificat LM 716
  - **analizoare_utilizate:**
      - **hematologie:** SYSMEX XN 1000
      - **biochimie:** COBAS INTEGRA 400 PLUS
  - **referinte_legate:**
      - **consult_asociat_UPU_30_05_2024:** Dosar_Medical/2024-05-30_upu_consult_gastro_cardio.json
      - **analize_urina_aceeasi_zi:** Dosar_Medical/2024-05-30_analize_upu_urina_1517290.json

---

## <a name="2024-05-30-analize-upu-urina-1517290"></a> 2024-05-30 — Buletin Analize Urina Sumar Sediment (Laborator Clinic)
**Sursă:** `Dosar_Medical/2024-05-30_analize_upu_urina_1517290.json` · **Buletin:** 1517290 · **Confidence:** high · **Flags:** glucozurie_pozitiva_confirmare_DZ_decompensat, corpi_cetonici_pozitivi, UPU_30_05_2024_episod_major

> Analize urină efectuate ~1h40 după analizele de sânge (1517243 la 13:05 → 1517290 la 14:52). CONFIRMĂ hiperglicemia decompensată din sânge: glucozurie (+), corpi cetonici (+), pH 7 (crescut), acid ascorbic (+). Sedimentul microscopic: 1-2 leucocite (normal). Analizor LABUMAT 2 (reflectometrie) + microscop optic.

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **nume_text_original_document:** PETRILA VIOREL MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 65 ani 0 luni
  - **sex:** M
  - **adresa:** Nadlac, AR
  - **nr_FO:** 1021735
  - **sectie_spital:** UPU Adulți
  - **confidence_identificare:** high

### 🧪 Analize laborator

- **categorie:** SEDIMENT_URINAR · **nume:** Sediment urinar microscopie · **valoare_text:** 1-2 leucocite · **metoda:** Microscopie Optică · **flag:** normal · **confidence_ocr:** high
- **categorie:** SUMAR_URINA · **nume:** Densitate · **valoare_numerica:** 1.024 · **unitate:** _(null)_ · **interval_referinta_text:** 1015-1025 · **flag:** normal · **confidence_ocr:** high
- **categorie:** SUMAR_URINA · **nume:** pH · **valoare_numerica:** 7 · **unitate:** _(null)_ · **interval_referinta_text:** 5-6 · **flag:** crescut · **confidence_ocr:** high
- **categorie:** SUMAR_URINA · **nume:** Proteine · **valoare_text:** Negativ · **interval_referinta_text:** Negativ · **flag:** normal · **confidence_ocr:** high
- **categorie:** SUMAR_URINA · **nume:** Leucocite · **valoare_text:** Negativ · **interval_referinta_text:** Negativ · **flag:** normal · **confidence_ocr:** high
- **categorie:** SUMAR_URINA · **nume:** Glucoză urinară · **valoare_text:** (+) · **interval_referinta_text:** Normal (negativ) · **flag:** crescut · **confidence_ocr:** high · **note:** Glucozurie pozitivă — corelat direct cu hiperglicemia plasmatică 180.48 mg/dL (depășește pragul renal).
- **categorie:** SUMAR_URINA · **nume:** Urobilinogen · **valoare_text:** Normal · **interval_referinta_text:** Normal · **flag:** normal · **confidence_ocr:** high
- **categorie:** SUMAR_URINA · **nume:** Pigmenți biliari · **valoare_text:** Negativ · **interval_referinta_text:** Negativ · **flag:** normal · **confidence_ocr:** high
- **categorie:** SUMAR_URINA · **nume:** Corpi cetonici · **valoare_text:** (+) · **interval_referinta_text:** Negativ · **flag:** crescut · **confidence_ocr:** high · **note:** Cetonurie — semn de decompensare metabolică DZ (posibil cetoacidoză ușoară).
- **categorie:** SUMAR_URINA · **nume:** Hematii · **valoare_text:** Negativ · **interval_referinta_text:** Negativ · **flag:** normal · **confidence_ocr:** high
- **categorie:** SUMAR_URINA · **nume:** Nitriți · **valoare_text:** Negativ · **interval_referinta_text:** Negativ · **flag:** normal · **confidence_ocr:** high
- **categorie:** SUMAR_URINA · **nume:** Acid ascorbic · **valoare_text:** (+) · **interval_referinta_text:** Negativ · **flag:** crescut · **confidence_ocr:** high · **note:** Ne-acreditat RENAR (* pe buletin). Cauză uzuală: aport vitamina C alimentar.

### 🔢 Numere referință

  - **numar_buletin:** 1517290
  - **cod_proba:** 1517290
  - **nr_FO:** 1021735

### 📦 Date suplimentare

  - **medic_validator_laborator:**
      - **nume:** Dr. AVRAM CECILIA
      - **specialitate:** medic primar medicina de laborator
  - **unitate_laborator:**
      - **denumire:** Spitalul Clinic Județean de Urgență Arad
      - **sectie:** Laborator Central
      - **acreditare:** ANMCS + SR EN ISO 15189:2013 Certificat LM 716
  - **analizoare_utilizate:**
      - **sumar_urina:** LABUMAT 2 (reflectometrie)
      - **sediment:** Microscop optic
  - **referinte_legate:**
      - **consult_asociat_UPU_30_05_2024:** Dosar_Medical/2024-05-30_upu_consult_gastro_cardio.json
      - **analize_sange_aceeasi_zi:** Dosar_Medical/2024-05-30_analize_upu_sange_1517243.json

---

## <a name="2024-05-30-upu-consult-gastro-cardio"></a> 2024-05-30 — Consult Upu Compus Gastro Cardio Ekg Scrisoare (Medicină de urgență / Gastroenterologie / Cardiologie)
**Sursă:** `Dosar_Medical/2024-05-30_upu_consult_gastro_cardio.json` · **Confidence:** medium-high · **Flags:** episod_clinic_major_pre_oncologic, troponina_dinamica, EKG_markedly_abnormal, criza_HTA, identificat_MF_orban_ecaterina, identificat_cardiolog_post_mihaela

> Episod clinic major la UPU Arad — pacient prezentat 30.05.2024 17:30 cu grețuri+vărsături (după consum sarmale) + vertij, TA 145/70, bradicardie 55 bpm. INCIDENTE CLINICE CRITICE: (1) hs-cTnI dinamic 4.24 → 4.59 ng/L (trending UP — relevant cardiologic!), (2) EKG auto Glasgow 'Anteroseptal infarct - age undetermined' + 'Markedly Abnormal ECG', (3) biletul trimitere MF Dr. Orbán menționează 'Criza HTA 200/100 mmHg' + glicemie 177 mg% + SaO2 91%. Consult gastro (Dr. Grada Sebastian) + consult cardio (Dr. Post Mihaela) + scrisoare medicală nr 0003622. Medicul de familie identificat: Dr. Orbán Ecaterina-Maria (CUI 20263730, cod parafă 718705, Cabinet Medical Individual Nădlac). ANOMALIE: Dr. Post Mihaela apare cu 2 coduri parafă pe 2 ștampile diferite (A13550 pe consultul cardio pag.2, A14555 pe scrisoarea medicală pag.9) — transcris literal așa cum apar.

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **nume_text_original_document:** PETRILA VIOREL MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 65 ani 0 luni
  - **sex:** M
  - **adresa:** Nădlac, Vasile Goldiș 42, jud. Arad
  - **confidence_identificare:** high

### 📦 Date suplimentare

  - **prezentare_urgenta:**
      - **data_ora:** 2024-05-30T17:30:00
      - **serviciu:** UPU Adulți — Spitalul Clinic Județean de Urgență Arad
      - **motivele_prezentarii:**
        - Grețuri, vărsături (după consum sarmale)
        - Vertij
      - **stare_clinica_initiala:**
          - **TA_mmHg:** 145/70
          - **AV_bpm:** 55
          - **SaO2_procent:** 97
          - **stare_generala:** conștient, cooperant
          - **auscultatie:** MV prezent bilateral fără raluri, zgomote cardiace ritmice, fără sufluri stetacustice
          - **edeme_gambiere:** absente
  - **consult_gastroenterologie:**
      - **numar_fisa:** 71735
      - **medic_solicitat:**
          - **nume:** Dr. Grada Sebastian
          - **specialitate:** medic specialist gastroenterologie
          - **cod_parafa:** G15512
      - **medic_solicitant:**
          - **nume:** Dr. Pop Florica
          - **specialitate:** medic primar medicină de urgență
          - **cod_parafa:** C79981
      - **ecografie_abdominala:**
          - **ficat:** suprafață micronodulară moderat, fără colestază intrahepatică
          - **colecist:** cu sediment
          - **CBP_VP:** normale
          - **pancreas:** hiperecogen
          - **splina_cm:** 12
          - **rinichi_stang_drept:** dimensiuni normale, fără stază
          - **anse_intestinale:** ușor dilatate flanc stâng
          - **lichid_liber_abdomen:** absent
          - **confidence_ocr:** medium
      - **diagnostic_gastro:** Sindrom dispeptic
      - **recomandari_gastro:**
        - **medicament:** Controloc · **doza:** 20 mg · **schema:** 1-0-0 · **confidence_ocr:** high
        - **medicament:** Debridat · **schema:** 3x1/zi · **confidence_ocr:** high
        - Reevaluare prin ambulator gastro
  - **consult_cardiologie:**
      - **numar_fisa:** 21735
      - **medic_solicitat:**
          - **nume:** Dr. Pop Florica
          - **cod_parafa:** C79981
      - **medic_solicitant:**
          - **nume:** Dr. Post Mihaela
          - **specialitate:** medic specialist cardiologie
          - **cod_parafa_UPU:** A13550
          - **cod_parafa_scrisoare_ambulator:** A14555
          - **note_cod_parafa:** 2 coduri parafă distincte pe 2 ștampile diferite — transcris literal; anomalie documentată
      - **antecedente_cunoscute:**
        - IM vechi
        - PTCA + stent (2011 conform scrisoare, 2012 conform restul dosarului — discrepanță scriere manuală)
        - DZ tip II
      - **examen_clinic:**
          - **TA_mmHg:** 145/70
          - **AV_bpm:** 55
          - **SaO2_procent:** 97
      - **biologie:**
          - **hs_cTnI_dinamic_ng_L:**
            - 4.24
            - 4.59
          - **hs_cTnI_trend:** crescător între 2 măsurători succesive
          - **unitate_document:** ng/L (instrument Atellica) — pe scrisoare apare 'mg/L' (inconsistență tipărit vs manuscris)
          - **hiperglicemie:** prezentă
          - **confidence_ocr:** high
      - **EKG_interpretare_manuala:**
          - **ritm:** sinusal
          - **AV_bpm:** 55
          - **ax_QRS:** intermediar
          - **unda_T_negativa_in:** aVL, V2-V5
          - **aspect:** stationar
          - **confidence_ocr:** high
      - **ecocord_interpretare:**
          - **VS:** dimensiuni normale, cinetică parietală normală, FS păstrată
          - **regurgitare_mitrala:** ușoară
          - **regurgitare_tricuspidiana:** ușoară funcțională
          - **lichid_pericardic:** absent
          - **confidence_ocr:** medium
      - **diagnostic_cardio:**
        - Sindrom dispeptic
        - Sindrom coronarian cronic
        - IM vechi
        - PTCA + stent (2011)
        - Insuficiență mitrală ușoară degenerativă
        - Insuficiență tricuspidiană ușoară funcțională
        - HTAE gradul I stadiul 3
        - DZ tip II non-insulino-necesitant
      - **recomandari_cardio:**
        - **medicament:** Aspenter · **doza:** 75 mg · **schema:** 0-1-0 · **confidence_ocr:** high
        - **medicament:** Concor · **doza:** 5 mg · **schema:** 1-0-0 · **confidence_ocr:** high
        - **medicament:** Noliterax · **doza:** 10 mg / 2.5 mg · **schema:** 1-0-0 · **confidence_ocr:** medium · **note:** Denumire incertă — posibil Noliprel / Noliterax, manuscris
        - **medicament:** Norvasc · **doza:** 5 mg · **schema:** 0-0-1 · **confidence_ocr:** high · **note:** Discrepanță între foi: consult pag.2 = 0-0-1, scrisoare pag.9 = 0-1-0
        - **medicament:** Sortis · **doza:** 80 mg · **schema:** 0-0-1 · **confidence_ocr:** high
        - Medicația comorbidităților
        - Dispensarizare cardiologică în ambulator
  - **EKG_automat_UPU:**
      - **instrument:** SE-1201 V1.42 Glasgow V28.6.0
      - **unitate:** SC:IU UPU SMURD ARAD
      - **data_ora:** 2024-05-30T15:28:00
      - **parametri_auto:**
          - **HR_bpm:** 55
          - **P_ms:** 124
          - **T_ms:** 152
          - **QRS_ms:** 120
          - **QT_QTc_ms:** 470/450
          - **PQRS_T_grade:** 43/6/85
          - **RV5_SV1_mV:** 0.38/0.652
      - **interpretari_automate:**
        - Sinus bradycardia
        - Anteroseptal infarct - age undetermined
        - Lateral T wave abnormality may be due to myocardial ischemia
        - Abnormal ECG
      - **raport_confirmat_medic:** ❌ false
  - **EKG_cabinet_medic_familie:**
      - **instrument:** CARDIO-M PLUS 2.21 / 3.12 Medical Econet GmbH
      - **data_ora:** 2024-05-30T11:30:00
      - **parametri_auto:**
          - **PR_RR_Int_ms:** 176 / 1071
          - **QRS_Dur_ms:** 102
          - **QT_QTc_ms:** 448 / 433
          - **P_R_T_axes:** 64, 30, 94
          - **SV1_RV5_RplusS_mV:** 0.67 / 0.00 / 0.67
      - **interpretari_automate:**
        - Sinus Bradycardia (HR: 50-59)
        - Normal Axis
        - possible Anteroseptal MI
        - Markedly Abnormal ECG
      - **mediu:** Cabinet Medical Individual Dr. Orbán Ecaterina, Nădlac
  - **bilet_trimitere_medic_familie:**
      - **emis_de:**
          - **nume:** Dr. Orbán Ecaterina
          - **specialitate:** medic specialist medicină generală-pediatrie
          - **CUI_cabinet:** 20263730
          - **cod_parafa:** 718705
          - **cabinet:** Cabinet Medical Individual, Nădlac
      - **data:** 2024-05-30
      - **catre:** Spitalul Județean Arad
      - **motivul_trimiterii:**
        - Criza HTA 200/100 mmHg — tratat anterior
        - Pacient cu grețuri, vărsături
        - SaO2 = 91%
        - Glicemie = 177 mg%
        - Diabet zaharat tip II dezechilibrat
      - **indicatii_terapeutice_cabinet:**
        - Perfuzie NaCl 50/100 × 2 flacoane
        - EKG ora 11:30 — modificat cu supradenivelare ne-specifică V3-V5
      - **parametri_post_tratament_cabinet:**
          - **TA_mmHg:** 110/80
          - **AV_bpm:** 53
      - **confidence_ocr:** medium-low (manuscris dens)
  - **scrisoare_medicala_cardio_ambulator:**
      - **numar_scrisoare:** 0003622
      - **formular:** ANEXA 43
      - **emis_de:**
          - **nume:** Dr. Post Mihaela
          - **specialitate:** medic specialist cardiologie
          - **cod_parafa:** A14555
      - **motivele_prezentarii:**
        - Dismnestezic (probabil)
        - Fatigabilitate la efort mediu
      - **diagnostic_complet:**
        - Sindrom coronarian cronic
        - IM vechi (2011)
        - PTCA cu 1 stent (2011)
        - HTAE gr. 3
        - Risc CV foarte înalt
        - DZ tip 2
        - Insuficiență diastolică globală VS ușoară
        - Regurgitare mitrală ușoară degenerativă
      - **antecedente_personale_patologice:**
        - DZ tip 2
        - Dislipidemie (LDL 210 mg/dL — probabil)
        - IM (2011)
        - PTCA cu 1 stent
        - Tabagism (stopat din 2011)
        - HTA gr. 3
      - **factori_risc_raportati_la_domiciliu:**
        - Diaforeză (probabil)
        - Januvia (incert — posibil medicație DZ)
        - Prestarium 10 mg × 2
        - Aspenter
        - Concor 5 mg × 1
      - **examen_clinic_ambulator:**
          - **cord:** zgomote ritmice, AV 65 bpm, fără sufluri audibile
          - **pulmonar:** MV prezent bilateral, fără raluri
          - **TA_evolutie_mmHg:**
            - 180/90
            - 160/80
      - **EKG_ambulator:**
          - **ritm:** sinusal
          - **AV_bpm:** 65
          - **ax_QRS:** intermediar
          - **unda_T_negativa_in:** aVL, V4-V5-V6
      - **tratament_recomandat:**
        - **medicament:** PRESTARIUM · **doza:** 10 mg · **schema:** 1-0-0
        - **medicament:** ASPENTER · **doza:** 75 mg · **schema:** 0-1-0
        - **medicament:** SORTIS · **doza:** 80 mg · **schema:** 0-0-1
        - **medicament:** CONCOR · **doza:** 5 mg · **schema:** 1-0-0
        - **medicament:** NORVASC · **doza:** 5 mg · **schema:** 0-1-0
      - **recomandari_suplimentare:**
        - Regim hiposodat, hipolipidic
        - Efort fizic în limita tolerabilității
        - Dacă TA ≥ 140/90 mmHg seara → medicament 10 mg suplimentar (incert)
        - Control la 1 lună (profil lipidic)
        - Control TA la 3 luni
      - **concediu_medical:** nu s-a eliberat
  - **note_administrare_manuscrise_cabinet_MF:**
      - **medicatie_administrata:**
        - **medicament:** O₂ (oxigen) · **cale:** inhalator · **confidence_ocr:** medium
        - **medicament:** Ser fiziologic 100 ml + flacon 250 ml · **cale:** i.v. perfuzie · **confidence_ocr:** high
        - **medicament:** Algocalmin · **doza:** 1 fiolă · **cale:** i.v. · **confidence_ocr:** medium
        - **medicament:** Metoclopramid · **doza:** 1 fiolă · **cale:** i.v. · **confidence_ocr:** medium
        - **medicament:** TROMBEX · **doza:** 1 cp · **cale:** p.o. · **confidence_ocr:** medium
        - **medicament:** Ser fiziologic 250 ml cu manitol (incert) · **cale:** i.v. perfuzie · **confidence_ocr:** low
      - **monitorizare_post_administrare:**
          - **AV_bpm:** 55
          - **TA_mmHg:** 140/90
      - **semnatura_emitent:** Dr. Orbán Ecaterina (cod parafă 718705)
  - **medici_implicati:**
    - **rol:** medic familie + bilet trimitere · **nume:** Dr. Orbán Ecaterina · **cod_parafa:** 718705 · **CUI_cabinet:** 20263730
    - **rol:** medic urgență UPU (solicitant gastro) · **nume:** Dr. Pop Florica · **cod_parafa:** C79981
    - **rol:** consult gastroenterologie · **nume:** Dr. Grada Sebastian · **cod_parafa:** G15512
    - **rol:** consult cardiologie UPU + scrisoare ambulator · **nume:** Dr. Post Mihaela · **cod_parafa_UPU:** A13550 · **cod_parafa_scrisoare:** A14555
  - **unitate_spital:**
      - **denumire:** Spitalul Clinic Județean de Urgență Arad
      - **sectie:** UPU Adulți
  - **referinte_legate:**
      - **analize_sange_acelasi_episod:** Dosar_Medical/2024-05-30_analize_upu_sange_1517243.json
      - **analize_urina_acelasi_episod:** Dosar_Medical/2024-05-30_analize_upu_urina_1517290.json
      - **serologie_HP_post_episod_prima:** Dosar_Medical/2024-06-04_anti_helicobacter_pylori_igg_77449.json
      - **serologie_HP_post_episod_urmare:** Dosar_Medical/2024-09-06_anti_helicobacter_pylori_igg_79765.json

---

## <a name="2024-06-04-anti-helicobacter-pylori-igg-77449"></a> 2024-06-04 — Buletin Analize Serologie (Laborator / Microbiologie)
**Sursă:** `Dosar_Medical/2024-06-04_anti_helicobacter_pylori_igg_77449.json` · **Buletin:** 77449 · **Confidence:** high · **Flags:** primul_rezultat_serologic_HP, post_episod_UPU_30_05_2024

> Primul buletin serologic IgG din seria HP la 5 zile după episodul UPU din 30.05.2024 (vezi 2024-05-30_upu_consult_gastro_cardio.json). Rezultatul >100 U/mL (masiv pozitiv) semnifică expunere anterioară la H. pylori. Al doilea buletin (79765 / 06.09.2024) este în 2024-09-06_anti_helicobacter_pylori_igg_79765.json cu aceeași valoare — consistent în timp. Rezultatul încercuit manual cu pix albastru pe document (probabil de medic la interpretare). Serologia IgG NU distinge infecție activă de antecedentă — eradicarea ar trebui confirmată prin antigen fecal sau test respirator cu uree.

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **nume_text_original_document:** PETRILA VIOREL-MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 65
  - **sex:** M
  - **adresa:** Ors. Nădlac, AR
  - **confidence_identificare:** high

### 🧪 Analize laborator

- **nume:** Anticorpi Anti Helicobacter Pylori IgG · **nume_original:** Anticorpi Anti Helicobacter Pylori IgG · **categorie:** MARKERI BOLI INFECTIOASE · **valoare_numerica:** _(null)_ · **valoare_text:** >100 · **unitate:** U/mL · **interval_referinta_min:** 0 · **interval_referinta_max:** 20 · **interval_referinta_text:** 0-20 U/mL · **flag:** crescut · **tip_proba:** ser · **metoda:** CLIA · **subcontractat:** ✅ true · **acreditat_renar:** ❌ false · **confidence_ocr:** high · **note:** Pozitiv masiv (peste 5× limita superioară a intervalului de referință). Rezultat încercuit manual pe document cu pix albastru.

### 🔢 Numere referință

  - **numar_buletin:** 77449
  - **barcode:** 0000077449
  - **cod_formular:** BA-5.8-01

### 📦 Date suplimentare

  - **medic_solicitant:**
      - **nume:** Dr. ORBÁN ECATERINA-MARIA
      - **specialitate:** MF (medicină de familie)
      - **cod_parafa:** 718705
      - **CUI_cabinet:** 20263730
      - **bilet_trimitere:** BTIAU / 04.06.24
  - **medic_validator_laborator:**
      - **nume:** Dr. Cret Anamaria
      - **specialitate:** Medic Primar Laborator
      - **cod_parafa:** A 0769
  - **unitate_laborator:**
      - **denumire:** SC Ultra ClinicaVest SRL
      - **tip:** LABORATOR DE ANALIZE MEDICALE
      - **adresa:** Oraș Pecica, str. 2, nr. 173, jud. Arad
      - **email:** laborator@ultraclinicavest.ro
      - **telefon:** 0257.468.212
      - **software:** SmartLabs 5.20 (Build 20.2305)
  - **referinte_legate:**
      - **buletin_ulterior_acelasi_pacient:** Dosar_Medical/2024-09-06_anti_helicobacter_pylori_igg_79765.json
      - **episod_clinic_declansator:** Dosar_Medical/2024-05-30_upu_consult_gastro_cardio.json

---

## <a name="2024-09-06-anti-helicobacter-pylori-igg-79765"></a> 2024-09-06 — Buletin Analize Serologie (Laborator / Microbiologie)
**Sursă:** `Dosar_Medical/2024-09-06_anti_helicobacter_pylori_igg_79765.json` · **Buletin:** 79765 · **Confidence:** high · **Flags:** control_serologic_la_3_luni_post_buletin_77449, identificat_laborator_ultra_clinicavest, identificat_medic_solicitant_orban

> Al doilea buletin serologic IgG, la ~3 luni după buletinul 77449 din 04.06.2024. Aceeași valoare >100 U/mL — consistent în timp, compatibil cu antecedente H. pylori. Serologia IgG NU distinge infecție activă de antecedentă — eradicarea ar trebui confirmată prin antigen fecal sau test respirator cu uree. Fișier redenumit 2026-04-24 (anterior '2024-09-06_anti_helicobacter_pylori_igg.json') + completat cu identificarea laboratorului (Ultra ClinicaVest Pecica) + medicului solicitant (Dr. Orbán Ecaterina-Maria) + medicului validator (Dr. Cret Anamaria).

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **nume_text_original_document:** PETRILA VIOREL-MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 65
  - **sex:** M
  - **adresa:** Ors. Nădlac, AR
  - **confidence_identificare:** high

### 🧪 Analize laborator

- **nume:** Anticorpi Anti Helicobacter Pylori IgG · **nume_original:** Anticorpi Anti Helicobacter Pylori IgG · **categorie:** MARKERI BOLI INFECTIOASE · **valoare_numerica:** _(null)_ · **valoare_text:** >100 · **unitate:** U/mL · **interval_referinta_min:** 0 · **interval_referinta_max:** 20 · **interval_referinta_text:** 0-20 U/mL · **flag:** crescut · **tip_proba:** ser · **metoda:** CLIA · **subcontractat:** ✅ true · **acreditat_renar:** ❌ false · **confidence_ocr:** high · **note:** Pozitiv masiv (peste 5× limita superioară a intervalului de referință). Semnifică expunere anterioară la H. pylori; nu diferențiază infecție activă de antecedentă. Aceeași valoare ca buletinul anterior 77449 din 04.06.2024 — persistență anticorpi IgG compatibilă cu istoricul.

### 🔢 Numere referință

  - **numar_buletin:** 79765
  - **barcode:** 0000079765
  - **cod_formular:** BA-7.4-05

### 📦 Date suplimentare

  - **medic_solicitant:**
      - **nume:** Dr. ORBÁN ECATERINA-MARIA
      - **specialitate:** MF (medicină de familie)
      - **cod_parafa:** 718705
      - **CUI_cabinet:** 20263730
      - **bilet_trimitere:** BTIAU / 03.09.24
  - **medic_validator_laborator:**
      - **nume:** Dr. Cret Anamaria
      - **specialitate:** Medic Primar Laborator
      - **cod_parafa:** A 0769
  - **unitate_laborator:**
      - **denumire:** SC Ultra ClinicaVest SRL
      - **tip:** LABORATOR DE ANALIZE MEDICALE
      - **adresa:** Oraș Pecica, str. 2, nr. 173, jud. Arad
      - **email:** laborator@ultraclinicavest.ro
      - **telefon:** 0257.468.212
      - **software:** SmartLabs 5.20 (Build 20.2305)
  - **referinte_legate:**
      - **buletin_anterior_acelasi_pacient:** Dosar_Medical/2024-06-04_anti_helicobacter_pylori_igg_77449.json
      - **episod_clinic_declansator:** Dosar_Medical/2024-05-30_upu_consult_gastro_cardio.json

---

## <a name="2025-06-17-buletin-analize-sange"></a> 2025-06-17 — Buletin Analize Laborator Complet (Laborator Clinic)
**Sursă:** `Dosar_Medical/2025-06-17_buletin_analize_sange.json` · **Confidence:** high · **Flags:** migrated_from_v1, corrected_wbc_unit

> Unitate WBC corectată v1→v2: Gemini a notat 'µg/dl' (imposibil medical). Corect: x10^3/µL. Confirmat prin magnitudinea valorii (6.54) și intervalul referință (5-10). Pentru trasabilitate, versiunea v1 e în arhiva/backup_pre-migrare_v2_2026-04-18/.

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 66
  - **sex:** M
  - **confidence_identificare:** high

### 🧪 Analize laborator

- **nume:** Leucocite (WBC) · **nume_original:** (WBC) Leucocite · **valoare_numerica:** 6.54 · **valoare_text:** 6.54 · **unitate:** x10^3/µL · **interval_referinta_min:** 5 · **interval_referinta_max:** 10 · **interval_referinta_text:** 5-10 · **flag:** normal · **confidence_ocr:** high · **note:** Unitate corectată de la 'µg/dl' (Gemini v1) la 'x10^3/µL'.
- **nume:** Limfocite absolute · **nume_original:** Lym# · **valoare_numerica:** 1.96 · **valoare_text:** 1.96 · **unitate:** x10^3/µL · **interval_referinta_min:** 1 · **interval_referinta_max:** 7.7 · **interval_referinta_text:** 1-7.7 · **flag:** normal · **confidence_ocr:** high
- **nume:** Monocite absolute · **nume_original:** Mon# · **valoare_numerica:** 0.5 · **valoare_text:** 0.50 · **unitate:** x10^3/µL · **interval_referinta_min:** 0.1 · **interval_referinta_max:** 1 · **interval_referinta_text:** 0.1-1 · **flag:** normal · **confidence_ocr:** high
- **nume:** Neutrofile absolute · **nume_original:** Neu# · **valoare_numerica:** 3.63 · **valoare_text:** 3.63 · **unitate:** x10^3/µL · **interval_referinta_min:** 1.5 · **interval_referinta_max:** 10.5 · **interval_referinta_text:** 1.5-10.5 · **flag:** normal · **confidence_ocr:** high
- **nume:** Eozinofile absolute · **nume_original:** Eos# · **valoare_numerica:** 0.44 · **valoare_text:** 0.44 · **unitate:** x10^3/µL · **interval_referinta_min:** 0 · **interval_referinta_max:** 0.7 · **interval_referinta_text:** 0-0.7 · **flag:** normal · **confidence_ocr:** high
- **nume:** Bazofile absolute · **nume_original:** Bas# · **valoare_numerica:** 0.01 · **valoare_text:** 0.01 · **unitate:** x10^3/µL · **interval_referinta_min:** 0 · **interval_referinta_max:** 0.34 · **interval_referinta_text:** 0-0.34 · **flag:** normal · **confidence_ocr:** high
- **nume:** Limfocite procentual · **nume_original:** Lym% · **valoare_numerica:** 29.9 · **valoare_text:** 29.9 · **unitate:** % · **interval_referinta_min:** 22 · **interval_referinta_max:** 55 · **interval_referinta_text:** 22-55 · **flag:** normal · **confidence_ocr:** high
- **nume:** Monocite procentual · **nume_original:** Mon% · **valoare_numerica:** 7.7 · **valoare_text:** 7.7 · **unitate:** % · **interval_referinta_min:** 0 · **interval_referinta_max:** 15 · **interval_referinta_text:** 0-15 · **flag:** normal · **confidence_ocr:** high
- **nume:** Neutrofile procentual · **nume_original:** Neu% · **valoare_numerica:** 55.4 · **valoare_text:** 55.40 · **unitate:** % · **interval_referinta_min:** 30 · **interval_referinta_max:** 75 · **interval_referinta_text:** 30-75 · **flag:** normal · **confidence_ocr:** high
- **nume:** Eozinofile procentual · **nume_original:** Eos% · **valoare_numerica:** 6.8 · **valoare_text:** 6.8 · **unitate:** % · **interval_referinta_min:** 0 · **interval_referinta_max:** 5 · **interval_referinta_text:** 0-5 · **flag:** crescut · **confidence_ocr:** high · **note:** Ușor peste limită — eozinofilie minoră. Interpretare clinică aparține medicului.
- **nume:** Bazofile procentual · **nume_original:** Bas% · **valoare_numerica:** 0.2 · **valoare_text:** 0.2 · **unitate:** % · **interval_referinta_min:** 0 · **interval_referinta_max:** 2 · **interval_referinta_text:** 0-2 · **flag:** normal · **confidence_ocr:** high
- **nume:** Hematii (RBC) · **nume_original:** (RBC) Hematii · **valoare_numerica:** 4.94 · **valoare_text:** 4.94 · **unitate:** x10^6/µL · **interval_referinta_min:** 4.5 · **interval_referinta_max:** 5.5 · **interval_referinta_text:** 4.5-5.5 · **flag:** normal · **confidence_ocr:** high
- **nume:** Hemoglobina (HGB) · **nume_original:** (HGB) Hemoglobina · **valoare_numerica:** 14.9 · **valoare_text:** 14.9 · **unitate:** g/dL · **interval_referinta_min:** 12.6 · **interval_referinta_max:** 17.4 · **interval_referinta_text:** 12.6-17.4 · **flag:** normal · **confidence_ocr:** high
- **nume:** Hematocrit (HCT) · **nume_original:** (HCT) Hematocrit · **valoare_numerica:** 43.2 · **valoare_text:** 43.2 · **unitate:** % · **interval_referinta_min:** 42 · **interval_referinta_max:** 52 · **interval_referinta_text:** 42-52 · **flag:** normal · **confidence_ocr:** high
- **nume:** Volum eritrocitar mediu (MCV) · **nume_original:** (MCV) Volum eritrocitar mediu · **valoare_numerica:** 87.3 · **valoare_text:** 87.3 · **unitate:** fL · **interval_referinta_min:** 75 · **interval_referinta_max:** 90 · **interval_referinta_text:** 75-90 · **flag:** normal · **confidence_ocr:** high
- **nume:** Hemoglobina eritrocitară medie (MCH) · **nume_original:** (MCH) Hemoglobina eritrocitara medie · **valoare_numerica:** 30.1 · **valoare_text:** 30.1 · **unitate:** pg · **interval_referinta_min:** 25 · **interval_referinta_max:** 31 · **interval_referinta_text:** 25-31 · **flag:** normal · **confidence_ocr:** high
- **nume:** Concentrația medie de Hb (MCHC) · **nume_original:** (MCHC) Concentratia medie de hemoglobina · **valoare_numerica:** 34.5 · **valoare_text:** 34.5 · **unitate:** g/dL · **interval_referinta_min:** 31.5 · **interval_referinta_max:** 37 · **interval_referinta_text:** 31.5-37 · **flag:** normal · **confidence_ocr:** high
- **nume:** Indice de distribuție a eritrocitelor (RDW) · **nume_original:** (RDW) Indice de distributie a eritrocitelor · **valoare_numerica:** 12.6 · **valoare_text:** 12.6 · **unitate:** % · **interval_referinta_min:** 10 · **interval_referinta_max:** 15 · **interval_referinta_text:** 10-15 · **flag:** normal · **confidence_ocr:** high
- **nume:** Trombocite (PLT) · **nume_original:** (PLT) Trombocite · **valoare_numerica:** 221 · **valoare_text:** 221 · **unitate:** x10^3/µL · **interval_referinta_min:** 150 · **interval_referinta_max:** 450 · **interval_referinta_text:** 150-450 · **flag:** normal · **confidence_ocr:** high
- **nume:** Plachetocrit (PCT) · **nume_original:** (PCT) Plachetocrit · **valoare_numerica:** 0.26 · **valoare_text:** 0.260 · **unitate:** mL/L · **interval_referinta_min:** 0.1 · **interval_referinta_max:** 3.5 · **interval_referinta_text:** 0.1-3.5 · **flag:** normal · **confidence_ocr:** high
- **nume:** Volum mediu trombocitar (MPV) · **nume_original:** (MPV) Volum mediu trombocitar · **valoare_numerica:** 11.8 · **valoare_text:** 11.8 · **unitate:** fL · **interval_referinta_min:** 6.5 · **interval_referinta_max:** 15 · **interval_referinta_text:** 6.5-15 · **flag:** normal · **confidence_ocr:** high
- **nume:** Indice de distribuție a trombocitelor (PDW) · **nume_original:** (PDW) Indice de distributie a trombocitelor · **valoare_numerica:** 16.3 · **valoare_text:** 16.3 · **unitate:** fL · **interval_referinta_min:** 9 · **interval_referinta_max:** 19 · **interval_referinta_text:** 9-19 · **flag:** normal · **confidence_ocr:** high
- **nume:** Uree serică · **nume_original:** Uree serica · **valoare_numerica:** 34.81 · **valoare_text:** 34.81 · **unitate:** mg/dL · **interval_referinta_min:** 17 · **interval_referinta_max:** 43 · **interval_referinta_text:** 17-43 · **flag:** normal · **confidence_ocr:** high
- **nume:** Creatinină serică · **nume_original:** Creatinina serica · **valoare_numerica:** 0.95 · **valoare_text:** 0.95 · **unitate:** mg/dL · **interval_referinta_min:** 0.8 · **interval_referinta_max:** 1.3 · **interval_referinta_text:** 0.8-1.3 · **flag:** normal · **confidence_ocr:** high · **note:** Relevant pentru pregătire CT cu contrast — în intervalul normal.
- **nume:** Glicemie · **nume_original:** Glicemie · **valoare_numerica:** 136.1 · **valoare_text:** 136.1 · **unitate:** mg/dL · **interval_referinta_min:** 70 · **interval_referinta_max:** 115 · **interval_referinta_text:** 70-115 · **flag:** crescut · **confidence_ocr:** high · **note:** Peste limita normală — compatibil cu diabet zaharat deja cunoscut (tratament Metformin/Jamesi).
- **nume:** Colesterol seric total · **nume_original:** Colesterol seric total · **valoare_numerica:** 195.44 · **valoare_text:** 195.44 · **unitate:** mg/dL · **interval_referinta_min:** _(null)_ · **interval_referinta_max:** 200 · **interval_referinta_text:** <200 · **flag:** normal · **confidence_ocr:** high
- **nume:** Trigliceride serice · **nume_original:** Trigliceride serice · **valoare_numerica:** 141.77 · **valoare_text:** 141.77 · **unitate:** mg/dL · **interval_referinta_min:** _(null)_ · **interval_referinta_max:** 203.7 · **interval_referinta_text:** <203.7 · **flag:** normal · **confidence_ocr:** high
- **nume:** HDL Colesterol · **nume_original:** HDL Colesterol · **valoare_numerica:** 33.86 · **valoare_text:** 33.86 · **unitate:** mg/dL · **interval_referinta_min:** 34.8 · **interval_referinta_max:** _(null)_ · **interval_referinta_text:** >34.8 · **flag:** scazut · **confidence_ocr:** high · **note:** Ușor sub pragul protectiv — factor minor de risc cardiovascular.
- **nume:** LDL Colesterol · **nume_original:** LDL Colesterol · **valoare_numerica:** 133.18 · **valoare_text:** 133.18 · **unitate:** mg/dL · **interval_referinta_min:** _(null)_ · **interval_referinta_max:** 159 · **interval_referinta_text:** <159 · **flag:** normal · **confidence_ocr:** high · **note:** Țintă LDL la pacient post-stent coronarian diferă (ESMO/ESC: <70 mg/dL); interpretarea aparține cardiologului.
- **nume:** Sodiu seric · **nume_original:** Sodiu seric · **valoare_numerica:** 141.3 · **valoare_text:** 141.30 · **unitate:** mmol/L · **interval_referinta_min:** 135 · **interval_referinta_max:** 148 · **interval_referinta_text:** 135-148 · **flag:** normal · **confidence_ocr:** high
- **nume:** Potasiu seric · **nume_original:** Potasiu seric · **valoare_numerica:** 3.61 · **valoare_text:** 3.61 · **unitate:** mmol/L · **interval_referinta_min:** 3.5 · **interval_referinta_max:** 5.3 · **interval_referinta_text:** 3.5-5.3 · **flag:** normal · **confidence_ocr:** high
- **nume:** Proteina C reactivă (PCR) · **nume_original:** Proteina C reactiva · **valoare_numerica:** _(null)_ · **valoare_text:** <6 · **unitate:** mg/L · **interval_referinta_min:** _(null)_ · **interval_referinta_max:** 6 · **interval_referinta_text:** <6 · **flag:** normal · **confidence_ocr:** high
- **nume:** TSH · **nume_original:** TSH · **valoare_numerica:** 1.7 · **valoare_text:** 1.700 · **unitate:** µUI/mL · **interval_referinta_min:** 0.3 · **interval_referinta_max:** 4.5 · **interval_referinta_text:** 0.3-4.5 · **flag:** normal · **confidence_ocr:** high
- **nume:** FT4 (tiroxina liberă) · **nume_original:** FT4 · **valoare_numerica:** 10.9 · **valoare_text:** 10.900 · **unitate:** pg/mL · **interval_referinta_min:** 9 · **interval_referinta_max:** 17.5 · **interval_referinta_text:** 9-17.5 · **flag:** normal · **confidence_ocr:** high
- **nume:** PSA Total · **nume_original:** PSA Total · **valoare_numerica:** 1.45 · **valoare_text:** 1.450 · **unitate:** ng/mL · **interval_referinta_min:** _(null)_ · **interval_referinta_max:** 4 · **interval_referinta_text:** <4 · **flag:** normal · **confidence_ocr:** high

### 🔢 Numere referință

  - **numar_buletin:** 87967
  - **barcode:** 0000087967
  - **bilet_trimitere:** BTIAW 9406823
  - **cod_formular:** FL-7.4-02

### 📦 Date suplimentare

  - **medic_solicitant:**
      - **nume:** Dr. ORBÁN ECATERINA-MARIA
      - **specialitate:** MF (medicină de familie)
      - **cod_parafa:** 718705
      - **CUI_cabinet:** 20263730
      - **bilet_trimitere:** BTIAW 9406823 / 10.06.2025
  - **medic_validator_laborator:**
      - **nume:** Dr. Cret Anamaria
      - **specialitate:** Medic Primar Laborator
      - **cod_parafa:** A 0769
  - **unitate_laborator:**
      - **denumire:** SC Ultra ClinicaVest SRL
      - **tip:** LABORATOR DE ANALIZE MEDICALE
      - **adresa:** Oraș Pecica, str. 2, nr. 173, jud. Arad
      - **email:** ultraclinicavest@gmail.com
      - **telefon:** 0257-468-212
      - **acreditare:** RENAR, SR EN ISO 15189:2013, Certificat LM 955
      - **software:** SmartLabs 5.0 (Build 0.2315)
  - **platitor:** Casa de Asigurări de Sănătate Arad

---

## <a name="2025-10-28-scrisoare-urologie-gastroenterologie"></a> 2025-10-28 — Scrisoare Medicala Consult (Urologie / Gastroenterologie)
**Sursă:** `Dosar_Medical/2025-10-28_scrisoare_urologie_gastroenterologie.json` · **Confidence:** high · **Flags:** migrated_from_v1, corrected_data_nasterii, corrected_icd10_format

> Corecturi v1→v2: (1) data_nasterii a fost '28-10-1959' (Gemini confundase data documentului cu data nașterii). Corectat la 1959-05-18 conform C.I. + CNP. (2) Codurile ICD-10 aveau prefix intern spital (ex. '702-N43.3'). Separat în 'cod_icd10' (standard) și 'cod_intern_spital'.

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 66
  - **sex:** M
  - **confidence_identificare:** high

### 🩺 Diagnostic

- **cod_icd10:** N43.3 · **cod_intern_spital:** 702 · **descriere_oficiala:** Hidrocel, nespecificat · **descriere_originala:** HIDROCEL DREPT · **tip:** principal · **confidence_ocr:** high
- **cod_icd10:** N45.9 · **cod_intern_spital:** 703 · **descriere_oficiala:** Orhită și epididimită, nespecificate (aici: chiste epididimare bilaterale) · **descriere_originala:** CHISTE EPIDIDIMARE BILATERALE · **tip:** principal · **confidence_ocr:** high · **note:** Codul ICD-10 exact pentru chist epididimar e N50.89 (alte afecțiuni specifice ale organelor genitale masculine); N45.9 din document e aproximare spital.
- **cod_icd10:** K40.90 · **cod_intern_spital:** 564 · **descriere_oficiala:** Hernie inghinală unilaterală sau nespecificată, fără obstrucție/gangrenă · **descriere_originala:** HERNIE INGHINALA DREAPTA · **tip:** principal · **confidence_ocr:** high
- **cod_icd10:** _(null)_ · **descriere_oficiala:** Proces proliferativ esofagian · **descriere_originala:** PROCES PROLIFERATIV ESOFAGIAN · **tip:** asociat · **confidence_ocr:** high · **note:** Prezent ca antecedent menționat în scrisoare (anterior endoscopiei din 17.04.2026).
- **cod_icd10:** K63.5 · **descriere_oficiala:** Polip al colonului · **descriere_originala:** POLIP COLON DESCENDENT · **tip:** asociat · **confidence_ocr:** high
- **cod_icd10:** K64 · **descriere_oficiala:** Hemoroizi și tromboză venoasă perianală · **descriere_originala:** BOALA HEMOROIDA · **tip:** asociat · **confidence_ocr:** high

### 📋 Recomandări

- Cură chirurgicală hernie inghinală + cură chirurgicală hidrocel + excizie chiste epididimare

### 👥 Medici / Unități

  - **nume_medic:** Dr. PITEA ALEXANDRU
  - **specialitate:** medic primar urologie
  - **cod_parafa:** A13044
  - **nr_FO_consultatii:** 6453
  - **unitate:** Complex Medical Pitea & Pitea SRL
  - **adresa:** Arad, Revoluției 45
  - **telefon:** 0749111455
  - **email:** UROLOGIE.PITEA@YAHOO.COM
  - **sectie:** Urologie

### 📦 Date suplimentare

  - **ecografie_scrotala:**
      - **patient_id_aparat:** 28-10-2025-101401
      - **sonographer:** Dr. Pitea Alexandru
      - **diagnostic_conclusion:** Hernie inghinala dreapta. Hidrocel drept. Chiste epididimare bilaterale.
      - **imagini_ecografice_numar:** 4
      - **timestamps_imagini:**
        - 2025-10-28T10:15:04
        - 2025-10-28T10:16:56
        - 2025-10-28T10:19:04
      - **dimensiuni_masurate:**
        - **nr:** 1 · **distanta_cm:** 3.85 · **confidence_ocr:** medium · **note:** rezoluție scan scăzută
        - **nr:** 2 · **distanta_cm:** 0.85 · **confidence_ocr:** medium
        - **nr:** 3 · **distanta_cm:** 3.18 · **confidence_ocr:** medium
      - **regiune_examinata:** Scrotum (Small Parts Report)
      - **echipament_software:** Urologie Arad Dr. Pitea Alexandru
      - **confidence_ocr:** medium

---

## <a name="2025-11-10-ecografie-transtoracica"></a> 2025-11-10 — Ecografie Transtoracica Raport (Cardiologie)
**Sursă:** `Dosar_Medical/2025-11-10_ecografie_transtoracica.json` · **Confidence:** high · **Flags:** pagina_1_din_document_compus, baseline_functie_cardiaca_pre_CT_si_pre_chirurgie, identificat_medic_laza_cristina_C07842

> Ecografie transtoracică tipărită — rezultate complete pentru evaluarea funcției cardiace. RELEVANȚĂ MAXIMĂ pre-esofagectomie: acest document stabilește baseline-ul cardiac al pacientului la ~5 luni pre-diagnostic oncologic. FE păstrată 55%, hipokinezie infero-bazală + septal bazal (consecvent cu IM vechi 2012), IM + IT ușoare, HVS concentrică, disfuncție diastolică tip I, AS mărit. Rezultatele susțin riscul anestezic moderat la pacient post-stent. Medic identificat: Dr. LAZA CRISTINA cod parafă C07842 (clar tipărit pe ștampilă).

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **nume_text_original_document:** Petrila Viorel
  - **varsta_la_data_document:** 66
  - **sex:** M
  - **confidence_identificare:** high
  - **note_identificare:** CNP absent pe document ECO; identificat prin cross-reference cu pagina 2 (scrisoare medicală aceeași zi) + restul dosarului.

### 📦 Date suplimentare

  - **parametri_hemodinamici_baseline:**
      - **ritm:** sinusal
      - **TA_mmHg:** 130/80
      - **FC_bpm:** 70
  - **incidenta_parasternala:**
      - **aorta_ascendenta_cm:** 3.4
      - **diametru_AS_cm:** 4.3
      - **diametru_VD_cm:** 2.6
      - **SIV_cm:** 1.4
      - **DTDVS_cm:** 4.7
      - **PPVS_cm:** 1.3
      - **aspect_valva_mitrala:** ușor fibrozate
      - **aspect_valva_aortica:** ușor fibrozate
  - **apical_4_camere:**
      - **VTD_ml:** 135
      - **VTS_ml:** 58
      - **FE_planimetric_procent:** 55
      - **suprafata_AS_cm2:** 23
  - **flux_mitral:**
      - **E_ms:** 0.6
      - **A_ms:** 0.98
      - **stenoza_mitrala:** NU
      - **insuficienta_mitrala:** DA — severitate ușoară
  - **flux_aortic:**
      - **Vmax_ms:** 1.3
      - **Pmax_mmHg:** 7
      - **stenoza_aortica:** NU
      - **insuficienta_aortica:** NU
  - **flux_tricuspidian:**
      - **stenoza_tricuspidiana:** NU
      - **insuficienta_tricuspidiana:** DA — severitate ușoară
  - **flux_pulmonar:**
      - **Vmax_ms:** 1.1
      - **Pmax_mmHg:** 5.5
      - **stenoza_pulmonara:** NU
      - **insuficienta_pulmonara:** DA — severitate ușoară
  - **cinetica_parietala:**
      - **aspect:** hipokinezie infero-bazală + hipokinezie sept bazal
      - **interpretare_clinica:** consecvent cu sechelă IM vechi (SCA ST+ 2012 antero-septo-apical post-stent IVA); confirmă zona de țesut cicatricial.
  - **lichid_pericardic:** Absent
  - **concluzii_ecografice:**
    - VS de dimensiuni normale cu funcție sistolică păstrată (FE=55%)
    - Hipokinezie infero-bazală și hipokinezie sept bazal
    - HVS concentrică
    - Disfuncție diastolică tip I
    - Insuficiența mitrală ușoară degenerativă
    - Insuficiența tricuspidiană ușoară funcțională
    - AS mărit
  - **medic_examinator:**
      - **nume:** Dr. LAZA CRISTINA
      - **specialitate:** medic primar cardiolog
      - **cod_parafa:** C07842
      - **confidence_identificare:** high
      - **note:** Prenume CRISTINA are confidență ~85% (textul complet „Dr. LAZA CRISTIN...” parțial vizibil pe ștampilă); nume „LAZA” + cod parafă C07842 sunt 100% clare.
  - **referinte_legate:**
      - **scrisoare_medicala_aceeasi_zi:** Dosar_Medical/2025-11-10_scrisoare_medicala_cardiologie.json
      - **schema_medicamentatie_aceeasi_zi_acelasi_medic:** Dosar_Medical/2025-11-10_schema_medicamente.json

---

## <a name="2025-11-10-schema-medicamente"></a> 2025-11-10 — Schema Tratament Manuscris (Cardiologie / Medicină Internă)
**Sursă:** `Dosar_Medical/2025-11-10_schema_medicamente.json` · **Confidence:** medium · **Flags:** migrated_from_v1, contains_manuscript, corrected_patient_name, ocr_errors_documented, r25_applied_2026-04-24

> Sursa: talonul de recomandare scris de mână (foto) + foto cutii medicamente Aspenter, Concor, Triplixam, Jamesi. Pe manuscris medicul a scris numele pacientului ca 'PETRICĂ VIOREL' (transcriere eronată de medic — Regula 13). Corectat la 'PETRILĂ VIOREL-MIHAI' conform C.I. + restul dosarului (concordanță perfectă a medicației cu istoricul pacientului: Aspenter post-stent 2012 + Concor/Triplixam HTA + Jamesi=sitagliptin+metformin pentru diabet). Medic prescriptor NEIDENTIFICAT (Regula 25 aplicată 2026-04-24: nume parțial ilizibil pe manuscris, refuz atribuire aproximativă; tracking în Dosar_Medical/EXTRAGERI_INCOMPLETE.md). O recomandare suplimentară (linia 4 pe talon) e tăiată cu marker albastru = anulată.

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 66
  - **sex:** M
  - **confidence_identificare:** high
  - **note_identificare:** Manuscrisul original scrie 'PETRICĂ VIOREL'. Corectat prin cross-reference cu C.I. și context clinic (medicația se potrivește istoricului pacientului).

### 💊 Tratament / Procedură

- **medicament_sau_procedura:** ASPENTER · **substanta_activa:** acid acetilsalicilic · **doza:** 75 mg · **frecventa:** 0-1-0 · **moment_administrare:** prânz · **indicatie:** antiagregant plachetar (post-stent coronarian 2012) · **detalii_ambalaj:** 28 comprimate gastrorezistente (conform foto cutie) · **producator:** Terapia · **confidence_ocr:** high
- **medicament_sau_procedura:** CONCOR · **substanta_activa:** fumarat de bisoprolol · **doza:** 5 mg · **frecventa:** 1-0-0 · **moment_administrare:** dimineața · **indicatie:** beta-blocant (cardioprotecție / HTA / frecvență cardiacă) · **detalii_ambalaj:** 60 comprimate filmate (conform foto cutie) · **producator:** Merck · **confidence_ocr:** high
- **medicament_sau_procedura:** TRIPLIXAM · **substanta_activa:** perindopril arginine + indapamidă + amlodipină · **doza:** 10 mg / 2,5 mg / 5 mg · **frecventa:** 1-0-0 · **moment_administrare:** dimineața · **indicatie:** antihipertensiv combinație triplă · **detalii_ambalaj:** 30 comprimate filmate (conform foto cutie) · **confidence_ocr:** high
- **medicament_sau_procedura:** JAMESI · **substanta_activa:** sitagliptin + clorhidrat de metformin · **doza:** 50 mg / 1000 mg · **frecventa:** 1-0-1 · **moment_administrare:** dimineața și seara · **indicatie:** antidiabetic oral combinație (inhibitor DPP-4 + biguanidă) · **detalii_ambalaj:** 56 comprimate filmate (conform foto cutie) · **producator:** Zentiva · **confidence_ocr:** high · **note:** CRITIC pentru pregătire CT cu contrast: componenta metformin trebuie oprită 48h înainte (risc acidoză lactică).
- **medicament_sau_procedura:** [MEDICAMENT_ANULAT] · **detalii_originale:** linia 4 a talonului — tăiată cu marker albastru · **confidence_ocr:** low · **note:** Recomandare anulată de medic. Conținutul nu e lizibil sub tăieturi.

### 👥 Medici / Unități

  - **medic_curant:** Dr. LAZA CRISTINA
  - **specialitate:** medic primar cardiolog
  - **cod_parafa:** C07842
  - **confidence_medic:** high
  - **metoda_identificare:** cross-reference 2026-04-24 cu ecografia transtoracică efectuată în aceeași zi (10.11.2025) de același medic — Dr. LAZA CRISTINA, cod C07842 (clar tipărit pe ștampila ECO). Schema medicamentatie manuscrisă a fost prescrisă de același cardiolog la consultul ambulator din 10.11.2025 (consult preoperator hernie). Înlocuiește marcajul NEIDENTIFICAT (R25) din varianta anterioară.
  - **referinta_ecografie:** Dosar_Medical/2025-11-10_ecografie_transtoracica.json
  - **referinta_scrisoare_medicala:** Dosar_Medical/2025-11-10_scrisoare_medicala_cardiologie.json

---

## <a name="2025-11-10-scrisoare-medicala-cardiologie"></a> 2025-11-10 — Scrisoare Medicala Consult Cardiologie (Cardiologie)
**Sursă:** `Dosar_Medical/2025-11-10_scrisoare_medicala_cardiologie.json` · **Confidence:** medium · **Flags:** manuscris_dens, pre_CT_si_pre_chirurgie_consult, identificat_medic_laza_cristina

> Scrisoare medicală scrisă de mână (formular tipizat Gutenberg Arad). Același medic Dr. LAZA CRISTINA (cod C07842) ca pe ECO din pagina 1. Confidence transcriere ~68% (manuscris dens); elemente critice clare: tratament recomandat (confirmat prin cross-reference cu schema_medicamente 10.11.2025 + foto cutii), diagnostic (IC cronică + IM vechi ~13 ani + HTAE gr.II-III + DZ tip 2), valori lab (GL 133, creat 0.85), examen clinic (TAs 130/80, FC 70, AV 70). Corecție §3 confirmată de user 2026-04-22: rândul 4 din rețeta manuscrisă a fost citit inițial 'ROSOMEZ 20 mg' — este de fapt TRIPLIXAM 10/2,5/5 mg 1-0-0.

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **nume_text_original_document:** PETRILA VIOREL
  - **varsta_la_data_document:** 66
  - **sex:** M
  - **confidence_identificare:** high

### 🩺 Diagnostic

- **descriere_oficiala:** Insuficiență coronariană cronică · **descriere_originala:** Insuficiență coronariană cronică · **tip:** principal · **confidence_ocr:** medium
- **descriere_oficiala:** Infarct miocardic vechi (~13 ani) · **descriere_originala:** IM vechi 13 ani · **tip:** antecedent · **confidence_ocr:** medium · **note:** Consistent cu SCA ST+ 2012 (stent IVA Vichy) — 13 ani = 2012→2025.

### 📦 Date suplimentare

  - **motivele_prezentarii:**
      - **text_original:** consult preoperator
      - **confidence_ocr:** medium
      - **context_probabil:** consult cardiologic pre-chirurgie hernie inghinală (intervenție efectuată 26-28.11.2025)
  - **anamneza:**
      - **antecedente_raportate:**
        - Bolnav post PTCA cu stent pe IVA (2012)
        - HTA esențială gr. II-III cu risc foarte înalt
        - Dislipidemie (probabil)
        - DZ tip 2 (probabil)
        - Stabil hemodinamic pe tratament ambulator (probabil)
      - **confidence_ocr:** low-medium
      - **note:** Scris cursiv dens — probabilitatea ~60-70% pe interpretare; diagnosticele sunt consistente cu restul dosarului.
  - **factori_risc:**
    - vârstă
    - HTA
    - dislipidemie
    - DZ tip 2
    - sedentarism
    - fost fumător
  - **examen_clinic:**
      - **general:**
          - **TA_mmHg:** 130/80
          - **status:** stabil, afebril
      - **local:**
          - **TA_mmHg:** 130/80
          - **FC_bpm:** 70
          - **HTA_prezent_compensat:** ✅ true
          - **cord:** ritmic
          - **zgomote_cardiace:** normale
          - **MV_pulmonar:** prezent fără raluri
          - **abdomen:** suplu, nedureros
  - **examene_laborator:**
      - **valori_normale:** câmp neclar (ilizibil)
      - **valori_patologice:**
          - **glicemie_mg_dL:** 133
          - **creatinina_mg_dL:** 0.85
          - **confidence_ocr:** high
  - **examene_paraclinice:**
      - **EKG:**
          - **ritm:** sinusal
          - **AV_bpm:** 80
          - **ax_QRS:** intermediar
          - **ischemie_acuta:** absent
          - **aspect_sechelar:** posibil infarct inferior
          - **confidence_ocr:** medium
      - **ECO:** vezi pagina 1 (JSON dedicat: 2025-11-10_ecografie_transtoracica.json)
  - **tratament_recomandat:**
    - **medicament:** ASPENTER · **doza:** 75 mg · **schema:** 0-1-0 · **moment:** prânz · **confidence_ocr:** medium · **note:** consecvent cu schema medicamente manuscris aceeași zi
    - **medicament:** TRIPLIXAM · **doza:** 10/2,5/5 mg · **schema:** 1-0-0 · **moment:** dimineața · **confidence_ocr:** high · **note:** CONFIRMAT user 2026-04-22 prin cross-reference Schema_medicamentatie_zilnica.jpeg (foto cutii). Corectează eroarea inițială 'ROSOMEZ 20 mg' din primul pass.
    - **medicament:** CONCOR · **doza:** 5 mg · **schema:** 1-0-0 (sau 1/2-0-0) · **moment:** dimineața · **confidence_ocr:** medium · **note:** consecvent cu schema medicamente
    - **medicament:** TORVACARD · **doza:** 10 mg sau 20 mg · **schema:** 0-0-1 · **moment:** seara · **confidence_ocr:** medium-low · **note:** doză incertă — 10 vs 20 mg; necesită clarificare
  - **recomandari_suplimentare:**
    - Repetă peste 3 luni cu profil lipidic
    - Nu este necesară revenirea pentru internare (bifat explicit)
  - **indicatie_revenire_internare:** NU
  - **concediu_medical:** nu s-a eliberat (niciuna dintre opțiuni bifată explicit)
  - **medic_examinator:**
      - **nume:** Dr. LAZA CRISTINA
      - **specialitate:** medic primar cardiolog
      - **cod_parafa:** C07842
      - **confidence_identificare:** high
      - **note:** Primele 4 litere 'LAZA' + cod parafă C07842 = clar pe ștampilă. Prenume CRISTINA ~85% confidence (parțial vizibil 'CRISTIN...').
  - **formular_tipizat:**
      - **tipografie:** Gutenberg SRL Arad
      - **telefon_tipografie:** 0257 254 330
      - **email_tipografie:** ditgutenberg@gmail.com
  - **referinte_legate:**
      - **ecografie_transtoracica_aceeasi_zi:** Dosar_Medical/2025-11-10_ecografie_transtoracica.json
      - **schema_medicamentatie_aceeasi_zi_acelasi_medic:** Dosar_Medical/2025-11-10_schema_medicamente.json
      - **eveniment_declansator_probabil:** consult preoperator hernie inghinală (chirurgie 26-28.11.2025 → 2025-11-28_externare_chirurgie_hernie.json)

---

## <a name="2025-11-28-externare-chirurgie-hernie"></a> 2025-11-28 — Externare Spital Cura Chirurgicala (Chirurgie Generală II)
**Sursă:** `Dosar_Medical/2025-11-28_externare_chirurgie_hernie.json` · **Confidence:** high · **Flags:** fuziune_surse_multiple, migrated_from_v1, canonical_for_externare_28_11_2025

> Fuziune a 3 JSON-uri Gemini care reprezintă același eveniment de externare (cura chirurgicală hernie + aderențe, 28.11.2025). Conservat: unități lab din 'Bilet_' și 'Scrisoare_' (complete), detaliile dozelor din 'Iesire_' (ambalaje+concentrații). PDF-ul sursă primar (probabil unul singur — 'Ieșire din spital.pdf') a generat multiple exporturi; după inspecția PDF-ului original se poate valida care sunt documente distincte (bilet vs. scrisoare medicală) vs. duplicate pure. Datele clinice sunt 100% identice între cele 3.

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 66
  - **sex:** M
  - **confidence_identificare:** high

### 🩺 Diagnostic

- **cod_icd10:** K40.90 · **descriere_oficiala:** Hernia inghinală unilaterală sau nespecificată, fără obstrucție sau gangrenă, nespecificată ca recidivantă · **descriere_originala:** Hernia inghinala unilaterala sau nespecificata, fara obstructie sau gangrena, nespecificata ca recidivanta · **tip:** principal · **confidence_ocr:** high
- **cod_icd10:** K66.0 · **descriere_oficiala:** Aderențe peritoneale · **descriere_originala:** Aderente peritoneale · **tip:** principal · **confidence_ocr:** high
- **cod_icd10:** K40.90 · **descriere_oficiala:** Hernie inghinală dreaptă · **descriere_originala:** HERNIE INGHINALA DREAPTA · **tip:** detaliere_lateralitate · **confidence_ocr:** high
- **cod_icd10:** K66.0 · **descriere_oficiala:** Aderențe peritoneale (mențiune majuscule) · **descriere_originala:** ADERENTE PERITONEALE · **tip:** detaliere_majuscule · **confidence_ocr:** high

### 🧪 Analize laborator

- **nume:** INR · **nume_original:** INR · **valoare_numerica:** 1.06 · **valoare_text:** 1.06 · **unitate:** _(null)_ · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high · **note:** Spitalul raportează doar 'valori normale' ca text, fără interval numeric.
- **nume:** AST (TGO) · **nume_original:** AST(TGO) · **valoare_numerica:** 15.5 · **valoare_text:** 15.5 · **unitate:** U/L · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Timp Quick / Indice Quick · **nume_original:** TQ - IQ · **valoare_numerica:** 92 · **valoare_text:** 92 · **unitate:** % · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** APTT · **nume_original:** APTT · **valoare_numerica:** 28.0 · **valoare_text:** 28.00 · **unitate:** sec · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Leucocite (WBC) · **nume_original:** Leucocite (WBC) · **valoare_numerica:** 7.3 · **valoare_text:** 7.30 · **unitate:** x10^3/µL · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Eritrocite (RBC) · **nume_original:** Eritrocite (RBC) · **valoare_numerica:** 5.02 · **valoare_text:** 5.02 · **unitate:** x10^6/µL · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Hemoglobina (HGB) · **nume_original:** Hemoglobina (HGB) · **valoare_numerica:** 15.0 · **valoare_text:** 15.00 · **unitate:** g/dL · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Hematocrit (HCT) · **nume_original:** Hematocrit (HCT) · **valoare_numerica:** 42.9 · **valoare_text:** 42.90 · **unitate:** % · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Trombocite (PLT) · **nume_original:** Trombocite (PLT) · **valoare_numerica:** 208.0 · **valoare_text:** 208.00 · **unitate:** x10^3/µL · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Volum eritrocitar mediu (MCV) · **nume_original:** Volum eritrocitar mediu (MCV) · **valoare_numerica:** 85.5 · **valoare_text:** 85.50 · **unitate:** fL · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Hemoglobina eritrocitară medie (MCH) · **nume_original:** Hemoglobina eritrocitara medie (MCH) · **valoare_numerica:** 29.9 · **valoare_text:** 29.90 · **unitate:** pg · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Concentrația medie Hb/Eritrocite (MCHC) · **nume_original:** Conc medie a Hb/Eritrocite (MCHC) · **valoare_numerica:** 35.0 · **valoare_text:** 35.00 · **unitate:** g/dL · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** RDW-SD · **nume_original:** RDW-SD · **valoare_numerica:** 39.9 · **valoare_text:** 39.90 · **unitate:** fL · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** RDW-CV · **nume_original:** RDW-CV · **valoare_numerica:** 13.1 · **valoare_text:** 13.10 · **unitate:** % · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Neutrofile procentual · **nume_original:** Neutrofile (NE%) · **valoare_numerica:** 56.8 · **valoare_text:** 56.80 · **unitate:** % · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Limfocite procentual · **nume_original:** Limfocite (LY%) · **valoare_numerica:** 26.2 · **valoare_text:** 26.20 · **unitate:** % · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Monocite procentual · **nume_original:** Monocite (MO%) · **valoare_numerica:** 8.8 · **valoare_text:** 8.80 · **unitate:** % · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Bazofile procentual · **nume_original:** Bazofile (BA%) · **valoare_numerica:** 0.7 · **valoare_text:** 0.70 · **unitate:** % · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Neutrofile absolute · **nume_original:** Neutrofile (NE#) · **valoare_numerica:** 4.15 · **valoare_text:** 4.15 · **unitate:** x10^3/µL · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Limfocite absolute · **nume_original:** Limfocite (LY#) · **valoare_numerica:** 1.91 · **valoare_text:** 1.91 · **unitate:** x10^3/µL · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Monocite absolute · **nume_original:** Monocite (MO#) · **valoare_numerica:** 0.64 · **valoare_text:** 0.64 · **unitate:** x10^3/µL · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Eozinofile absolute · **nume_original:** Eozinofile (EO#) · **valoare_numerica:** 0.55 · **valoare_text:** 0.55 · **unitate:** x10^3/µL · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Bazofile absolute · **nume_original:** Bazofile (BA#) · **valoare_numerica:** 0.05 · **valoare_text:** 0.05 · **unitate:** x10^3/µL · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Uree · **nume_original:** UREA · **valoare_numerica:** 31.7 · **valoare_text:** 31.70 · **unitate:** mg/dL · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** ALT (TGP) · **nume_original:** ALT(TGP) · **valoare_numerica:** 14.2 · **valoare_text:** 14.2 · **unitate:** U/L · **interval_referinta_text:** normale (document spital) · **flag:** normal · **confidence_ocr:** high
- **nume:** Eozinofile procentual · **nume_original:** Eozinofile (EO%) · **valoare_numerica:** 7.5 · **valoare_text:** 7.50 · **unitate:** % · **interval_referinta_text:** patologice (document spital) — peste limita 0-5% · **flag:** crescut · **confidence_ocr:** high · **note:** Eozinofilie ușoară — pattern similar cu buletinul din 17.06.2025. Consistent în timp.
- **nume:** Creatinină serică · **nume_original:** CREATININA serica · **valoare_numerica:** 0.66 · **valoare_text:** 0.66 · **unitate:** mg/dL · **interval_referinta_text:** patologice (document spital) · **flag:** patologic · **confidence_ocr:** high · **note:** Valoarea 0.66 e sub intervalul uzual 0.8-1.3 — ar putea fi 'scăzut' nu 'patologic'; documentul spital nu specifică direcția. Nu e clinic alarmant izolat.
- **nume:** Glucoză · **nume_original:** GLUCOZA · **valoare_numerica:** 129.0 · **valoare_text:** 129.00 · **unitate:** mg/dL · **interval_referinta_text:** patologice (document spital) · **flag:** crescut · **confidence_ocr:** high · **note:** Consistent cu diabetul cunoscut (vezi și 136.1 la 17.06.2025).

### 💊 Tratament / Procedură

- **medicament_sau_procedura:** ALGOCALMIN · **substanta_activa:** metamizol sodic · **detalii_originale:** 1 g/2 ml X 5 SOL. INJ. · **doza:** 1 g / 2 mL · **forma:** soluție injectabilă · **confidence_ocr:** high
- **medicament_sau_procedura:** BIOSUN SYMBIO SPOR · **substanta_activa:** probiotic multispecies · **detalii_originale:** SWP x 15cps · **forma:** capsule · **confidence_ocr:** high
- **medicament_sau_procedura:** BRAUNOL · **substanta_activa:** povidon-iod · **detalii_originale:** X 10 CUTIE CU 10 FLAC. · **indicatie:** antiseptic cutanat · **confidence_ocr:** high
- **medicament_sau_procedura:** BUPIVACAINĂ SPINAL HEAVY PANPHARMA · **substanta_activa:** bupivacaină · **detalii_originale:** 5 mg/ml X 5 · **indicatie:** anestezie rahidiană intraoperatorie · **confidence_ocr:** high
- **medicament_sau_procedura:** CLEXANE · **substanta_activa:** enoxaparină sodică · **detalii_originale:** 6000 UI (60 mg)/0,6 ml X 50 SOL. INJ. · **indicatie:** profilaxie trombotică post-operatorie · **confidence_ocr:** high
- **medicament_sau_procedura:** CLORURĂ DE SODIU · **substanta_activa:** NaCl · **detalii_originale:** 0,9% X 10 SOL. PERF. · **indicatie:** perfuzie · **confidence_ocr:** high
- **medicament_sau_procedura:** FAMODIN · **substanta_activa:** famotidină · **detalii_originale:** 40 mg X 30 COMPR. FILM. · **indicatie:** antisecretor gastric · **confidence_ocr:** high
- **medicament_sau_procedura:** GLUCOZĂ 10% · **substanta_activa:** glucoză · **detalii_originale:** 10% X 10 SOL. PERF. · **indicatie:** perfuzie · **confidence_ocr:** high
- **medicament_sau_procedura:** MIDAZOLAM HYPERICUM · **substanta_activa:** midazolam · **detalii_originale:** 5 mg/ml X 10 CUTIE · **indicatie:** sedare · **confidence_ocr:** high
- **medicament_sau_procedura:** PANTOPRAZOL TERAPIA · **substanta_activa:** pantoprazol · **detalii_originale:** 40 mg X 30 COMPR. GASTROREZ. · **indicatie:** inhibitor pompă de protoni · **confidence_ocr:** high
- **medicament_sau_procedura:** PROPOFOL MCT/LCT FRESENIUS · **substanta_activa:** propofol · **detalii_originale:** 10 mg/ml X 5 CUTIE · **indicatie:** anestezie intravenoasă · **confidence_ocr:** high
- **medicament_sau_procedura:** ZOLINEF · **substanta_activa:** cefazolin · **detalii_originale:** 1 g X 10 CUTIE CU 10 FLAC. · **indicatie:** antibioprofilaxie perioperatorie · **confidence_ocr:** high
- **medicament_sau_procedura:** Cură chirurgicală cu grefon · **tip:** procedură · **detalii_originale:** conform PO nr.1476 din 26.11.2025 · **note:** Presupune plasă sintetică pentru repararea peretelui abdominal — de clarificat tipul exact al grefonului cu medicul operator. · **confidence_ocr:** high

### 📋 Recomandări

- Control chirurgical
- Evitarea eforturilor fizice mari
- Prevenirea tromboemboliei
- RADIOGRAFIA TORACICĂ: PA/Cord cu schiță aortică, fără leziuni active pulmonare (preoperator)

### 👥 Medici / Unități

  - **sectie:** Chirurgie Generală II
  - **unitate:** de identificat din documentul original
  - **procedura_interna_spital:** PO nr. 1476 din 26.11.2025

---

## <a name="2026-04-17-bilet-trimitere-CT"></a> 2026-04-17 — Bilet Trimitere Investigatii Paraclinice (Administrativ / Gastroenterologie (trimițător) → Radiologie (destinatar))
**Sursă:** `Dosar_Medical/2026-04-17_bilet_trimitere_CT.json` · **Confidence:** high · **Flags:** bilet_CAS_decontat, genesis_medical_clinic, pre_CT_2026_04_20

> Bilet tipizat emis de C.N. Imprimeria Națională S.A. Investigații paraclinice decontate de CAS AR, nr. contract 1148. Nivel prioritate bifat: Ambulator Specialitate. Biletul autorizează CT torace + abdomen + pelvis toate cu SDC pentru diagnostic 'PROCES PROLIFERATIV ESOFAGIAN' (cod 95). A generat examinarea efectuată pe 20.04.2026 la Genesis Medical Clinic Micălaca — vezi 2026-04-20_ct_torace_abdomen_pelvis.json.

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **nume_text_original_document:** PETRILA VIOREL-MIHAI
  - **cnp:** 1590518024486
  - **adresa_document:** Nădlac
  - **cetatenia:** Ro
  - **categorie_asigurat_bifata:** Pensionar
  - **confidence_identificare:** high

### 🩺 Diagnostic

- **cod_icd10:** _(null)_ · **cod_intern_bilet:** 95 · **descriere_oficiala:** Proces proliferativ esofagian · **descriere_originala:** PROCES PROLIFERATIV ESOFAGIAN · **tip:** principal · **confidence_ocr:** high · **note:** Cod '95' este cod intern CAS / formular, nu ICD-10 standard.

### 🔢 Numere referință

  - **serie_bilet:** BCTAP
  - **numar_bilet:** 0631727
  - **cod_diagnostic:** 95
  - **tiparit_la:** C.N. Imprimeria Națională S.A.

### 📦 Date suplimentare

  - **unitate_medicala_emitenta:**
      - **denumire:** SC GENESIS MEDICAL CLINIC SRL
      - **cui:** R20295098
      - **adresa:** Arad, Bd. Revoluției nr. 3
      - **cas:** CAS AR
      - **nr_contract_conventie:** 1148
  - **medic_emitent:**
      - **nume:** Dr. Noufal Abdul Vahab
      - **nume_text_original_document:** NOUPHAL ABDUL VAHAB
      - **specialitate:** medic primar gastroenterologie
      - **cod_parafa:** C 11074
  - **investigatii_recomandate:**
    - **pozitie:** 1 · **cod_investigatie:** CT · **descriere:** TORACE (SDC) · **confidence_ocr:** high
    - **pozitie:** 2 · **cod_investigatie:** CT · **descriere:** ABDOMEN (SDC) · **confidence_ocr:** high
    - **pozitie:** 3 · **cod_investigatie:** CT · **descriere:** PELVIS (SDC) · **confidence_ocr:** high
  - **campuri_necompletate_pe_bilet:**
    - Date clinice și paraclinice care să justifice investigația (4.2)
    - Examen CT anterior DA/NU (4.3)
    - Greutate pacient (4.4.a)
    - Toleranță substanța iodată (4.4.b)
    - Substanță de contrast DA/NU explicit (4.5) — implicit DA prin 'SDC' în 4.1
    - Persoana desemnată de furnizor paraclinic (5)
    - Data prezentării pacientului + semnătura (6)
  - **nivel_prioritate:**
      - **MF:** ❌ false
      - **Urgenta:** ❌ false
      - **Amb_Spec:** ✅ true
      - **Curente:** ❌ false
      - **Altele:** ❌ false
  - **referinta_biletul_a_generat:**
      - **ct_efectuat_data:** 2026-04-20
      - **ct_efectuat_JSON:** Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json

---

## <a name="2026-04-17-biopsie-esofagiana-histopatologic"></a> 2026-04-17 — Buletin Examen Histopatologic Biopsie (Anatomopatologie)
**Sursă:** `Dosar_Medical/2026-04-17_biopsie_esofagiana_histopatologic.json` · **Confidence:** high · **Flags:** key_clinical_event, rezultat_inconcluziv_sugestiv_carcinom, necesita_imunohistochimie_sau_rebiopsie, trigger_dashboard_regen, trigger_context_medical_update

> REZULTAT INTERMEDIAR — NU diagnostic definitiv de cancer. Concluzie: țesut de granulație pe fond de ulcerație cronică, doar SUGESTIV pentru infiltrat carcinomatos. Limitare explicită: număr mic celule epiteliale atipice surprinse. Recomandare laborator: evaluare imunohistochimică pentru diagnostic de certitudine. Pas următor: consult oncolog 4.05.2026 OncoHelp (Dr. Anater) — decizie IHC pe blocul T26H06044 / rebiopsie țintită / EUS.

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **nume_text_original_document:** PETRILA VIOREL MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 66
  - **sex:** M
  - **adresa_in_document:** STR Vasile Goldiș 42, Nădlac, Arad
  - **confidence_identificare:** high

### 👥 Medici / Unități

  - **anatomopatolog_principal:**
      - **nume:** Dr. Glăja Romanița
      - **titlu_profesional:** medic primar anatomopatolog
      - **cod_parafa:** 367427
      - **rol:** semnatar raport histopatologic (concluzie + nota laboratorului)
  - **medic_specialist_macroscopie:**
      - **nume:** Dr. Teoran Samy Ștefan
      - **titlu_profesional:** medic specialist
      - **cod_parafa:** G70575
      - **rol:** evaluare macroscopică piesă
  - **medic_curant_solicitant_biopsie:**
      - **nume:** Dr. Noufal Abdul Vahab
      - **titlu_profesional:** medic primar gastroenterologie
      - **cod_parafa:** C 11074
      - **unitate:** Genesis Medical Clinic Arad
      - **rol:** prelevare biopsie endoscopică 17.04.2026 14:21
  - **laborator:**
      - **denumire:** Bioclinica SA
      - **punct_recoltare:** Bioclinica Vlaicu Arad (cod 00003)
      - **punct_lucrat:** Bioclinica SA, CAL Torontalului 1, Timișoara
      - **buletin_nr:** 26417A0362
      - **contact:** arad@bioclinica.ro
      - **site:** bioclinica.ro

### 📦 Date suplimentare

  - **diagnostic_clinic_la_trimitere:** Proces proliferativ.
  - **examen_histopatologic:**
      - **tehnica:** colorația hematoxilină-eozină (H&E)
      - **piesa_a:**
          - **tip:** Biopsie
          - **blocuri_parafina_procesate:** 1
      - **macroscopic:**
          - **descriere_originala:** Doua piese biopsice cu aspect neregulat, cafenii, elastice, cu dimensiuni de 0,2/0,1/0,1 cm ambele. Se orienteaza in totalitate, fara sectionare (T26H06044-A1).
          - **elemente_cheie:**
              - **numar_piese:** 2
              - **dimensiuni_cm:** 0,2 / 0,1 / 0,1 (ambele piese)
              - **aspect:** neregulat, cafenii, elastice
              - **orientare:** totală, fără secționare
              - **block_id:** T26H06044-A1
          - **medic_responsabil:** Dr. Teoran Samy Ștefan (medic specialist, cod parafă G70575)
          - **observatie_clinica_claude:** Cantitate sub-milimetrică de țesut prelevat — relevant pentru limitarea diagnostică menționată în nota laboratorului [PROBABIL].
      - **microscopic:**
          - **descriere_originala:** Un fragment tisular biopsic constituit din numeroase structuri vasculare cu endoteliul tumefiat, unele hiperemiate/cu marginatie leucocitara si manson leucocitar, cu orientare perpendiculara pe suprafata acoperita partial de detritus si necroza fibrinoida; prezente deopotriva elemente celulare inflamatorii mononucleate; aparent se disting celule epitelioide de talie medie, cu nucleul nucleolat, cu nucleol eozinofil si citoplasma cantitativ moderata, palid colorata/slab eozinofila, singulare/grupate. Un fragment tisular mic reprezentat in exclusivitate de epiteliu stratificat scuamos necheratinizat, cu aspecte de exocitoza (granulocite neutrofile) si de extravazate hematice, fara suport conjunctiv.
          - **componenta_inflamatorie_dominantă:**
              - **structuri_vasculare:** numeroase, cu endoteliu tumefiat, unele hiperemiate
              - **marginatie_leucocitara:** prezentă
              - **manson_leucocitar:** prezent
              - **suprafata:** acoperită parțial de detritus și necroză fibrinoidă
              - **infiltrat_inflamator:** elemente celulare inflamatorii mononucleate prezente
              - **interpretare_claude:** [CERT] Pattern compatibil cu țesut de granulație pe ulcerație cronică — confirmat în concluzia raportului.
          - **componenta_atipica_minoritara:**
              - **celule_observate:** epitelioide de talie medie
              - **caracteristici_nucleare:** nucleu nucleolat, nucleol eozinofil
              - **citoplasma:** cantitativ moderată, palid colorată / slab eozinofilă
              - **distributie:** singulare/grupate
              - **diagnostic_definitiv:** [INCERT] — celule sugestive dar insuficiente pentru carcinom
              - **interpretare_claude:** [PROBABIL] Caracteristicile nucleare (nucleol eozinofil prominent) sunt compatibile cu adenocarcinom moderat diferențiat — DAR cantitatea redusă de celule atipice împiedică diagnosticul de certitudine. Coroborat cu CT (T3-T4 infiltrativ Siewert II) și cu localizarea joncțiunii eso-gastrice, suspiciunea clinică pentru adenocarcinom rămâne ridicată.
          - **fragment_secundar:**
              - **tip_epiteliu:** epiteliu stratificat scuamos necheratinizat
              - **modificari:** exocitoză (granulocite neutrofile), extravazate hematice
              - **suport_conjunctiv:** absent
              - **interpretare_claude:** [CERT] Mucoasă esofagiană normală inflamată — fără valoare diagnostică tumorală (țesut sănătos prelevat marginal).
      - **concluzie:**
          - **text_original:** Ansamblul histologic, pe sectiuni seriate si in coloratia uzuala, pledeaza pentru tesut de granulatie pe fond de ulceratie cronica, fiind doar sugestiv pentru infiltrat carcinomatos.
          - **diagnostic_principal_morfologic:** Țesut de granulație pe fond de ulcerație cronică
          - **diagnostic_secundar_sugestiv:** Sugestiv (NU confirmat) pentru infiltrat carcinomatos
          - **verdictul_oncologic:** [INCERT] — biopsie inconcluzivă; NU confirmă, NU infirmă carcinomul
          - **marcaj_certitudine:** [INCERT]
          - **interpretare_claude:** [CERT] Rezultat clasic de biopsie superficială pe leziune ulcerată/stenozantă: prelevarea conține în principal țesut de granulație + necroză + detritus de pe suprafața leziunii, cu prea puține celule din stratul tumoral profund pentru diagnostic histologic definitiv.
      - **nota_laboratorului:**
          - **text_original:** De corelat cu datele endoscopice/imagistice (diagnostic histologic tumoral mult limitat de numarul mic al celulelor epiteliale atipice); eventuala evaluare imunohistochimica pentru diagnostic histologic de certitudine si conduita terapeutica.
          - **elemente_cheie:**
              - **corelatie_solicitata:** endoscopie + imagistică
              - **limita_explicita:** număr mic de celule epiteliale atipice surprinse în fragment
              - **recomandare_principala:** evaluare imunohistochimică (IHC) pentru diagnostic histologic de certitudine
              - **scop_recomandare:** diagnostic de certitudine + ghidarea conduitei terapeutice
  - **implicatii_clinice:**
      - **diagnostic_status:** [INCERT] — biopsie inconcluzivă; suspiciunea clinico-imagistică (CT + endoscopie) NU s-a infirmat și nici confirmat histologic
      - **stadializare_impact:** Niciun impact direct asupra stadializării TNM imagistice (rămâne T3-T4, N0-N1, M0 probabil per CT 20.04). Stadializarea finală necesită confirmare histologică.
      - **decizii_pendente:**
        - IHC pe blocul existent T26H06044 (rapid 3-7 zile, fără re-intervenție; markeri propuși clinic: pan-CK, CK7/CK20, CDX-2, p53, eventual HER2 / PD-L1 / MSI dacă se confirmă carcinom)
        - Rebiopsie țintită endoscopică cu fragmente mai numeroase, mai profunde — eventual sub ghidaj EUS (ecoendoscopie) pentru a depăși stratul superficial de granulație
        - Combinare IHC + rebiopsie programată în paralel (variantă mixtă)
      - **decident_principal:** Dr. Anater Angelo-Christian, OncoHelp Timișoara — consult 4.05.2026
      - **anatomopatolog_recomandare_explicita:** Dr. Glăja Romanița sugerează în nota laboratorului varianta IHC ca primă opțiune.
  - **context_documente_corelate:**
      - **endoscopie_recoltare:** Dosar_Medical/2026-04-17_examen_gastroscopic.json (proces proliferativ circumferențial 2/3 inferioară esofag, NEDEPĂȘIBIL endoscopic)
      - **ct_stadializare:** Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json (T3-T4, N0-N1, M0 probabil, Siewert II, ascită perihepatică + intrapelvină)
      - **bilet_trimitere_ct_initial:** Dosar_Medical/2026-04-17_bilet_trimitere_CT.json
      - **creatinina_pre_ct:** Dosar_Medical/2026-04-17_buletin_bioclinica_uree_creatinina.json (același buletin Bioclinica menționa „Examen histopatologic în curs de execuție”)
      - **consult_oncolog_pendent:** 4.05.2026 OncoHelp Timișoara — Dr. Anater Angelo-Christian (corespondență `Dosar_Medical/corespondenta/2026-04-24_re-solicitare-consult-anater.md`)
  - **monitor_automat:**
      - **sistem:** GitHub Actions + Playwright headless + ntfy.sh (repo privat RolandPetrila/Sistem_Notificari)
      - **status:** deactivated_2026-04-28
      - **note_dezactivare:** Rezultat primit; flag .DETECTED activat conform protocol monitor; user a primit notificare ntfy.sh prioritate 5.
  - **referinte_legate:**
      - **ct_rezultat_stadializare:** Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json
      - **endoscopie_recoltare:** Dosar_Medical/2026-04-17_examen_gastroscopic.json
      - **buletin_bioclinica_creatinina:** Dosar_Medical/2026-04-17_buletin_bioclinica_uree_creatinina.json
      - **bilet_trimitere_ct:** Dosar_Medical/2026-04-17_bilet_trimitere_CT.json

---

## <a name="2026-04-17-buletin-bioclinica-uree-creatinina"></a> 2026-04-17 — Buletin Analize Laborator Functie Renala (Laborator Clinic / Medicină de Laborator)
**Sursă:** `Dosar_Medical/2026-04-17_buletin_bioclinica_uree_creatinina.json` · **Buletin:** 26417A0362 · **Confidence:** high · **Flags:** pre_CT_2026_04_20, functie_renala_confirmata_normala

> Buletin emis de Bioclinica SRL Arad, punct recoltare 00003 Bioclinica Vlaicu. Recoltare în aceeași zi cu endoscopia (17.04.2026). Medic primar medicină de laborator: Dr. Statnic Maria Luminița (cod A08064). RELEVANȚĂ CRITICĂ: valori recente (3 zile) pentru pregătirea CT cu contrast din 20.04.2026 — creatinina e OK pentru contrast, nu necesită repetare. De asemenea, pe buletin apare mențiunea 'Analize în curs de execuție: Examen histopatologic' — confirmă că BIOPSIA esofagiană este procesată la Bioclinica, nu la Genesis. Contact urmărire rezultat biopsie: arad@bioclinica.ro.

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 66
  - **sex:** M
  - **confidence_identificare:** high

### 🧪 Analize laborator

- **nume:** Uree serică · **nume_original:** Uree serică · **valoare_numerica:** 33.4 · **valoare_text:** 33,4 · **unitate:** mg/dL · **interval_referinta_min:** 16.6 · **interval_referinta_max:** 48.5 · **interval_referinta_text:** 16,6 - 48,5 · **flag:** normal · **confidence_ocr:** high · **note:** Valoare în mijlocul intervalului normal.
- **nume:** Uree serică (unități SI) · **nume_original:** Uree (mmol/L) · **valoare_numerica:** 5.6 · **valoare_text:** 5,6 · **unitate:** mmol/L · **interval_referinta_min:** 2.8 · **interval_referinta_max:** 8.1 · **interval_referinta_text:** 2,8 - 8,1 · **flag:** normal · **confidence_ocr:** high · **note:** Aceeași analiză, exprimată în unități SI.
- **nume:** Creatinină serică · **nume_original:** Creatinină serică · **valoare_numerica:** 0.83 · **valoare_text:** 0,83 · **unitate:** mg/dL · **interval_referinta_min:** 0.67 · **interval_referinta_max:** 1.17 · **interval_referinta_text:** 0,67 - 1,17 · **flag:** normal · **confidence_ocr:** high · **note:** Valoare în interval normal, partea joasă. eGFR estimat CKD-EPI ≈ 95 mL/min/1.73m² (stadiu G1 = funcție renală normală). CRITIC: OK pentru CT cu contrast iodat fără protocol special; risc nefropatie induse de contrast — scăzut.
- **nume:** Creatinină serică (unități SI) · **nume_original:** Creatinină (µmol/L) · **valoare_numerica:** 73.37 · **valoare_text:** 73,37 · **unitate:** µmol/L · **interval_referinta_min:** 59.23 · **interval_referinta_max:** 103.43 · **interval_referinta_text:** 59,23 - 103,43 · **flag:** normal · **confidence_ocr:** high · **note:** Aceeași analiză, exprimată în unități SI.

### 👥 Medici / Unități

  - **medic_primar_laborator:** Dr. Statnic Maria Luminița
  - **cod_medic:** A08064
  - **unitate:** Bioclinica SRL Arad
  - **sectie:** Laborator medical
  - **punct_recoltare:** 00003 Bioclinica Vlaicu
  - **adresa_laborator:** STR Dreptății 23, ap. 17, Arad
  - **acreditare:** RENAR, SR EN ISO 15189:2023, certificat LM 207

### ⏳ Analize în curs

- **tip:** Examen histopatologic · **cod:** s (subcontractat) · **relevanta:** BIOPSIE ESOFAGIANĂ — prelevată la endoscopia din 17.04.2026, procesată la Bioclinica Arad. De urmărit cu arad@bioclinica.ro.

### 🔢 Numere referință

  - **numar_buletin:** 26417A0362

---

## <a name="2026-04-17-examen-colonoscopic"></a> 2026-04-17 — Buletin Examen Colonoscopic (Gastroenterologie)
**Sursă:** `Dosar_Medical/2026-04-17_examen_colonoscopic.json` · **Confidence:** high · **Flags:** separat_de_gastroscopie_2026-04-24, R23_integrala

> Colonoscopie efectuată concomitent cu gastroscopia la Genesis Medical Clinic Arad (Dr. Noufal Abdul Vahab). Separat într-un JSON dedicat 2026-04-24. R23 aplicat integral: toate 6 segmente colonice listate explicit (inclusiv aspecte normale), dimensiune polip documentată, reziduuri fecale menționate. Nume pacient pe document 'PETRILA VIOREL MHAI' (typo în document) — corectat la 'PETRILĂ VIOREL-MIHAI' prin cross-reference C.I.+gastroscopie aceeași zi.

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **nume_text_original_document:** PETRILA VIOREL MHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 66
  - **sex:** M
  - **confidence_identificare:** high
  - **note_identificare:** Typo în document — 'MHAI' în loc de 'MIHAI'. Identitate confirmată prin cross-reference cu gastroscopia aceeași zi (text corect) + C.I.

### 🩺 Diagnostic

- **cod_icd10:** K63.5 · **descriere_oficiala:** Polip al colonului descendent · **descriere_originala:** POLIP COLON DESCENDENT · **tip:** secundar · **confidence_ocr:** high · **detalii:** polip sesil de 8 mm
- **cod_icd10:** K64 · **descriere_oficiala:** Boală hemoroidală · **descriere_originala:** BOALA HEMOROIDALA · **tip:** secundar · **confidence_ocr:** high
- **cod_icd10:** K64.1 · **descriere_oficiala:** Hemoroizi interni grad II · **descriere_originala:** Hemoroizi interni II · **tip:** secundar · **confidence_ocr:** high

### 📋 Recomandări

- Revine pentru polipectomie (polip sesil 8 mm descendent)
- Pregătire colon optimizată pentru următoarea colonoscopie (resturi fecale în 3 segmente au limitat vizualizarea completă)

### 👥 Medici / Unități

  - **medic_curant:** Dr. Noufal Abdul Vahab
  - **medic_text_original_document:** Dr. Nouphal Abdul Vahab
  - **cod_parafa:** C. 11074
  - **specialitate_medic:** medic primar gastroenterologie
  - **unitate:** Genesis Medical Clinic Arad
  - **sectie:** Gastroenterologie

### 📦 Date suplimentare

  - **examinare_colonoscopica:**
      - **hemoroizi_mentiune_initiala:** Hemoroizi interni II
      - **segmente:**
          - **rect:**
              - **aspect:** fără modificări
              - **text_original:** fara modificari
              - **confidence_ocr:** high
          - **sigmoid:**
              - **aspect:** portiune vizibilă fără modificări
              - **calitate_pregatire:** cu resturi fecale solide
              - **text_original:** cu restuir fecale solide, portiunea vizibila fara modificari
              - **confidence_ocr:** high
          - **descendent:**
              - **aspect:** prezintă polip sesil 8 mm
              - **dimensiune_polip_mm:** 8
              - **tip_polip:** sesil
              - **recomandare:** Revine pentru polipectomie
              - **text_original:** prezinta un polip sesil de 8mm (Revine pentru polipectomie)
              - **confidence_ocr:** high
          - **transvers:**
              - **aspect:** portiune vizibilă fără modificări
              - **calitate_pregatire:** cu resturi fecale solide
              - **text_original:** cu restuir fecale solide, portiunea vizibila fara modificari
              - **confidence_ocr:** high
          - **ascendent:**
              - **aspect:** portiune vizibilă fără modificări
              - **calitate_pregatire:** cu resturi fecale solide
              - **text_original:** cu restuir fecale solide, portiunea vizibila fara modificari
              - **confidence_ocr:** high
          - **cec:**
              - **aspect:** fără modificări
              - **text_original:** fara modificari
              - **confidence_ocr:** high
      - **calitate_pregatire_globala:** suboptimă — reziduuri fecale solide în 3 segmente (sigmoid, transvers, ascendent); porțiunile vizibile fără modificări patologice; re-colonoscopia cu pregătire optimizată ar putea fi considerată la polipectomie
  - **concluzii_raport:**
    - POLIP COLON DESCENDENT
    - BOALA HEMOROIDALA
  - **referinte_legate:**
      - **gastroscopie_aceeasi_zi:** Dosar_Medical/2026-04-17_examen_gastroscopic.json
      - **bilet_trimitere_CT_declansat_de_gastroscopie:** Dosar_Medical/2026-04-17_bilet_trimitere_CT.json

---

## <a name="2026-04-17-examen-gastroscopic"></a> 2026-04-17 — Buletin Examen Gastroscopic (Gastroenterologie)
**Sursă:** `Dosar_Medical/2026-04-17_examen_gastroscopic.json` · **Confidence:** high · **Flags:** key_clinical_event, user_clarified_2026-04-22, separat_de_colonoscopie_2026-04-24

> Document-cheie: identificarea procesului proliferativ esofagian. Separat într-un JSON dedicat (2026-04-24) de fostul JSON unificat '2026-04-17_buletin_gastroenterologie.json' care conținea și colonoscopia. CLARIFICARE user 2026-04-22: interpretarea corectă a textului 'circumferentialne depasibila endoscopica' este 'CIRCUMFERENȚIAL NEDEPĂȘIBILĂ ENDOSCOPIC' (stenoză aproape completă, endoscopul nu a trecut dincolo de leziune). Coroborat cu CT 20.04.2026 ('infiltrativ', 'dificil de caracterizat dimensional').

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **nume_text_original_document:** PETRILA VIOREL MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 66
  - **sex:** M
  - **confidence_identificare:** high

### 🩺 Diagnostic

- **cod_icd10:** _(null)_ · **descriere_oficiala:** Proces proliferativ esofagian circumferențial la 2/3 inferioară, nedepășibil endoscopic (suspiciune — biopsie în lucru) · **descriere_originala:** PROCES PROLIFERATIV ESOFAGIAN · **descriere_clinica_completa_originala:** La 2/3 inferioara esofagului prezinta proces proliferativ circumferentialne depasibila endoscopica(Bio) · **tip:** principal · **confidence_ocr:** high · **note:** Diagnostic de certitudine depinde de rezultatul histopatologic al biopsiei (în lucru la Bioclinica Arad). Nu se atribuie cod ICD-10 oncologic fără confirmare histologică.

### 📋 Recomandări

- Așteptare rezultat biopsie esofagiană (estimat 7–14 zile lucrătoare — 24.04-01.05.2026)
- CT torace + abdomen + pelvis cu substanță de contrast (bilet BCTAP 0631727, URGENȚĂ) — efectuat 20.04.2026

### 👥 Medici / Unități

  - **medic_curant:** Dr. Noufal Abdul Vahab
  - **medic_text_original_document:** Dr. Nouphal Abdul Vahab
  - **cod_parafa:** C. 11074
  - **specialitate_medic:** medic primar gastroenterologie
  - **unitate:** Genesis Medical Clinic Arad
  - **sectie:** Gastroenterologie

### 📦 Date suplimentare

  - **examinare_endoscopica:**
      - **esofag:**
          - **localizare_leziune:** 2/3 inferioară a esofagului
          - **aspect:** proces proliferativ circumferențial
          - **depasibilitate_endoscopica:** NU (nedepășibil endoscopic — stenoză aproape completă)
          - **biopsie_prelevata:** ✅ true
          - **destinatie_biopsie:** Bioclinica Arad (confirmat prin buletin Bioclinica 17.04 'Analize în curs: Examen histopatologic')
          - **text_original_document:** La 2/3 inferioara esofagului prezinta proces proliferativ circumferentialne depasibila endoscopica(Bio)
          - **confidence_ocr:** high
          - **note_clarificare:** Text contopit în PDF — interpretat ca 'circumferential ne-depasibila endoscopic' (= nedepășibil). Confirmat explicit de user Roland Petrilă pe 2026-04-22.
  - **concluzii_raport:**
    - PROCES PROLIFERATIV ESOFAGIAN
  - **referinte_legate:**
      - **bilet_trimitere_CT:** Dosar_Medical/2026-04-17_bilet_trimitere_CT.json
      - **colonoscopie_aceeasi_zi:** Dosar_Medical/2026-04-17_examen_colonoscopic.json
      - **CT_rezultat_stadializare:** Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json
      - **biopsie_procesata_la:** Bioclinica Arad (urmărire rezultat: arad@bioclinica.ro)

---

## <a name="2026-04-20-ct-torace-abdomen-pelvis"></a> 2026-04-20 — Raport Imagistica Ct (Radiologie și Imagistică Medicală)
**Sursă:** `Dosar_Medical/2026-04-20_ct_torace_abdomen_pelvis.json` · **Confidence:** high · **Flags:** key_clinical_event, stadializare_imagistica, ascita_de_investigat

> Raport CT TAP N+SDC de stadializare pentru proces proliferativ esofagian. PDF digital (text extractabil nativ). Tumoră primară identificată: segment distal esofagian + joncțiune eso-gastrică (orificiu cardia + cadru gastric fundic) — clasificare probabilă Siewert II, de confirmat cu oncologul. Stadializare imagistică estimativă: T3-T4, N0-N1 (limfonoduli loco-regionali max 7.5 mm), M0 probabil. ATENȚIE CLINICĂ MAJORĂ: colecție fluidă perihepatică 15 mm + intrapelvină 28 mm = ASCITĂ — în context neoplazic esofagian avansat necesită excludere CARCINOMATOZĂ PERITONEALĂ (altfel ar fi stadiu IV). Discuție urgentă cu oncolog. Descoperiri colaterale: glandă suprarenală stângă hipertrofă heterogenă (incidentaloma? adenom?), leziune chistică subcutan perete toracic posterior 22/47.4 mm, colecție fluidă pulmonar bazal LID 9.3 mm, cardiomegalie cu ateromatoza calcara aorto-coronariană (consecvent cu antecedente SCA 2012 + stent IVA). Numele medicului ordonator apare în PDF ca 'NOUPHAL ABDUL VAHAB' (cu 'h' intercalat) — aceeași persoană cu Dr. Noufal Abdul Vahab din dosarul gastroenterologic 17.04.2026. Numele pacientului în PDF: 'PETRILA VIOREL MIHAI' (fără diacritice, prenume cu spațiu) — aceeași persoană (CNP corect).

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **nume_text_original_document:** PETRILA VIOREL MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 66
  - **sex:** M
  - **confidence_identificare:** high

### 🩺 Diagnostic

- **cod_icd10:** _(null)_ · **descriere_oficiala:** Proces expansiv infiltrativ circumferențial la joncțiunea eso-gastrică (segment distal esofagian + orificiu cardia + cadru gastric fundic), cu extensie loco-regională · **descriere_originala:** Ingrosare murala heterogen captanta de SDC decelata circumferential la nivelul segmentului distal esofagian, orificiul cardia cu cadrul gastric la nivel fundic, ce asociaza densificarea grasimii loco-regionale precum și limfonoduli de pana la 7.5 mm – proces expansiv cu aspect infiltrativ prezent, dificil de caracterizat dimensional · **tip:** principal · **confidence_ocr:** high · **note:** Clasificare anatomică probabilă: Siewert II (joncțiune eso-gastrică) — a se confirma cu echipa oncologică. Dificil de caracterizat dimensional — tumora infiltrativă, fără masă net delimitabilă. Implică atât esofagul distal cât și fundul gastric → impact asupra protocolului terapeutic (FLOT preferat față de CROSS pentru componentă gastrică).
- **cod_icd10:** _(null)_ · **descriere_oficiala:** Colecție fluidă perihepatică + intrapelvină (ascită) · **descriere_originala:** Colecție fluida perihepatica cu lama maximala de 15 mm ce asociaza colecție fluida intrapelvina cu lama maximala de 28 mm · **tip:** secundar · **confidence_ocr:** high · **note:** SEMNAL CLINIC MAJOR DE URMĂRIT: în context neoplazic esofagian avansat, ascita poate indica CARCINOMATOZĂ PERITONEALĂ (ar echivala cu stadiu IV). Diagnostic diferențial necesar: reactivă inflamatorie, hipoalbuminemie, tromboză venoasă, carcinomatoză. Necesită discuție URGENTĂ cu oncolog + posibil paracenteză diagnostică cu analiză citologică.
- **cod_icd10:** _(null)_ · **descriere_oficiala:** Glandă suprarenală stângă hipertrofă, heterogenă, fără leziuni focale · **descriere_originala:** Glanda suprarenala stânga cu aspect hipertrof, heterogena, fără leziuni focale, de monitorizat · **tip:** secundar · **confidence_ocr:** high · **note:** Descoperire incidentală. Diagnostic diferențial: incidentaloma benignă, adenom nefuncțional, hiperplazie reactivă, metastază (mai puțin probabilă fără leziune focală). Necesită evaluare endocrinologică — analize hormonale (cortizol, aldosteron, catecolamine) + follow-up imagistic.
- **cod_icd10:** J94.8 · **descriere_oficiala:** Mică colecție fluidă pulmonară bazal LID · **descriere_originala:** Colecție fluida cu lama maximala de 9.3 mm decelata pulmonar bazal LID · **tip:** secundar · **confidence_ocr:** high · **note:** Colecție fluidă de dimensiune mică. Posibil pleural minor. De urmărit evolutiv.
- **cod_icd10:** _(null)_ · **descriere_oficiala:** Leziune chistică subcutană perete toracic posterior (spațiu intercostal cXI-cXII) · **descriere_originala:** Leziune chistica rotund-ovalara incapsulata, bine definita, cu diametre de 22/47.4 mm decelata subcutan perete toracic posterior la nivelul spațiului intercostal cXI-cXII, a se corela clinic · **tip:** secundar · **confidence_ocr:** high · **note:** Radiologul a cerut explicit „a se corela clinic” — necesită evaluare la palpare. Probabil benignă (chist sebaceu, lipom, chist epidermoid) — încapsulată, bine definită, rotund-ovalară.
- **cod_icd10:** I51.7 · **descriere_oficiala:** Cardiomegalie + ateromatoză calcara aorto-coronarian · **descriere_originala:** Cardiomegalie ce asociaza placi de ateromatoza calcara la nivel aorto-coronarian · **tip:** secundar · **confidence_ocr:** high · **note:** Consecvent cu antecedentele de SCA ST+ 2012 + stent coronarian IVA (RX VISION 3.5×28 mm). Ateromatoza calcara prezentă și pe aorta abdominală + emergențe.

### 📋 Recomandări

- Consult oncolog digestiv URGENT (stadiu infiltrativ + ascită de evaluat — poate modifica tot protocolul terapeutic)
- Corelare cu rezultat biopsie esofagiană (în lucru la Bioclinica Arad, estimat 24.04-01.05.2026)
- Posibil PET-CT sau laparoscopie diagnostică cu citologie peritoneală pentru excluderea carcinomatozei (decis de oncolog)
- Evaluare endocrinologică pentru glanda suprarenală stângă (analize hormonale bazale: cortizol 8AM, aldosteron/renină, metanefrine plasmatice + follow-up imagistic)
- Corelare clinică leziune chistică subcutan perete toracic posterior (palpare, eventual ecografie superficială)
- Monitorizare evolutivă colecție fluidă pulmonar bazal LID

### 👥 Medici / Unități

  - **medic_examinator_1:**
      - **nume:** Dr. Buie Florian-Laurențiu
      - **cod_parafa:** A11818
      - **specialitate:** medic primar radiologie și imagistică medicală
  - **medic_examinator_2:**
      - **nume:** Dr. Candea Florin-Vasile
      - **cod_parafa:** F52510
      - **specialitate:** medic primar radiologie și imagistică medicală
  - **medic_ordonator:** Dr. Noufal Abdul Vahab
  - **unitate:** Genesis Medical Clinic Micălaca
  - **denumire_in_document:** Genesys
  - **specialitate_unitate:** Radiologie și Imagistică Medicală

### 🔢 Numere referință

  - **numar_inregistrare_examinare:** 284

### 📦 Date suplimentare

  - **examinare:**
      - **tip:** CT (Computer Tomography)
      - **protocol:** TAP nativ + substanță de contrast iodat (N+SDC)
      - **regiuni_scanate:**
        - torace
        - abdomen
        - pelvis
      - **data:** 2026-04-20
      - **numar_inregistrare:** 284
      - **medic_ordonator:** Dr. Noufal Abdul Vahab
      - **medic_ordonator_text_original:** NOUPHAL ABDUL VAHAB
      - **diagnostic_trimitere:** Proces proliferativ esofagian
      - **doza_radiatie:**
          - **DLP:** 2474
          - **unitate:** mGy·cm²
          - **valoare_text_original:** 2474 mGyxcm2
  - **findings_imagistice:**
      - **torace:**
          - **trahee_bronsii_principale:** permeabile
          - **parenchim_pulmonar:**
              - **condensari:** absente
              - **procese_expansive:** absente
              - **fibroza_pulmonara:** absentă
              - **emfizem_pulmonar:** absent
              - **tulburari_ventilatie:** posterobazal LID și LIS
          - **leziuni_nodulare:** câteva leziuni micronodulare calcare sechelare apical LSD, diametru maxim 6.8 mm
          - **adenopatii:**
              - **mediastinale:** absente
              - **hilare:** absente
              - **axilare:** absente
          - **colectii_fluide_torace:**
              - **pulmonar_bazal_LID:** 9.3 mm
              - **intrapericardice:** absente
          - **cord_si_vase_mari:**
              - **cardiomegalie:** prezentă
              - **ateromatoza_aorto_coronariana:** plăci calcare prezente
              - **artera_pulmonara:** calibru normal, permeabilă
              - **aorta_toracala:** calibru normal, permeabilă
          - **tiroida:** aspect normal dimensional, omogen captantă de SDC
          - **leziune_subcutana_perete_toracic:** chist rotund-ovalar încapsulat bine definit, 22/47.4 mm, spațiu intercostal cXI-cXII, a se corela clinic
      - **abdomen_pelvis:**
          - **esofag_jonctiune_gastro_esofagiana:**
              - **localizare:** segment distal esofagian + orificiu cardia + cadru gastric la nivel fundic
              - **aspect:** îngroșare murală heterogen captantă de SDC, circumferențial, proces expansiv cu aspect infiltrativ prezent
              - **extensie_loco_regionala:** densificarea grăsimii loco-regionale
              - **limfonoduli_loco_regionali:** până la 7.5 mm
              - **caracterizare_dimensionala:** dificil de caracterizat dimensional
          - **ficat:** dimensiuni și contur normale, fără prize patologice de SDC
          - **colectii_fluide_abdomen_pelvis:**
              - **perihepatica:** 15 mm
              - **intrapelvina:** 28 mm
              - **interpretare:** ascită — posibil carcinomatoză peritoneală de exclus
          - **cai_biliare:**
              - **colecist:** fără îngroșări parietale, fără calculi evidentiabili CT
              - **intra_extrahepatice:** fără dilatări
          - **vase_abdominale:**
              - **ax_spleno_portal_celiaco_mezenteric:** permeabil
              - **aorta_abdominala_VCI:** calibru normal, permeabile
              - **ateromatoza:** placi calcare mural supraetajat pe aorta abdominală + emergențe
          - **pancreas:** aspect normal
          - **splina:** aspect normal
          - **glanda_suprarenala_stanga:** hipertrofă, heterogenă, fără leziuni focale — de monitorizat
          - **glanda_suprarenala_dreapta:** aspect normal
          - **rinichi:** bilateral dimensiuni și IP normale, funcționali, secreție și excreție prezentă, fără calculi radioopaci, fără dilatații pielo-caliceale
          - **vezica_urinara:** fără modificări parietale sau intracavitare
          - **prostata:** aspect normal CT
          - **adenopatii_abdomino_pelvine:** absente
          - **modificari_osoase_suspecte_malignitate:** absente
          - **coloana_vertebrala:** modificări degenerative disco-vertebrale prezente supraetajat toraco-lombar
  - **stadializare_imagistica_estimata:**
      - **T:** T3-T4 estimat (proces expansiv infiltrativ circumferențial cu extensie loco-regională)
      - **N:** N0-N1 estimat (limfonoduli loco-regionali max 7.5 mm — sub pragul standard <10 mm, dar în context neoplazic pot fi relevanți pentru stadializare)
      - **M:** M0 probabil (fără metastaze hepatice, pulmonare, osoase, ganglionare distale vizibile la CT)
      - **confidence:** estimativă
      - **note_critica:** Ascita perihepatică + intrapelvină necesită excludere CARCINOMATOZĂ PERITONEALĂ (ar fi stadiu IV indiferent de T și N). De discutat URGENT cu oncolog. Stadializarea definitivă necesită: (1) rezultat biopsie — tip histologic; (2) posibil PET-CT pentru activitate metabolică; (3) posibil laparoscopie diagnostică pentru excluderea carcinomatozei peritoneale și prelevare citologie peritoneală.
      - **clasificare_Siewert_probabila:** II (joncțiune eso-gastrică propriu-zisă, tumoră centrată pe cardia cu extensie către esofagul distal și fundul gastric)
  - **conluzii_raport:**
    - Ingrosare murala heterogen captanta de SDC decelata circumferential la nivelul segmentului distal esofagian, orificiul cardia cu cadrul gastric la nivel fundic, ce asociaza densificarea grasimii loco-regionale precum si limfonoduli de pana la 7.5 mm – proces expansiv cu aspect infiltrativ prezent, dificil de caracterizat dimensional
    - Glanda suprarenala stânga cu aspect hipertrof, heterogena, fără leziuni focale, de monitorizat
    - Cardiomegalie ce asociaza placi de ateromatoza calcara la nivel aorto-coronarian
    - Colecție fluida cu lama maximala de 9.3 mm decelata pulmonar bazal LID
    - Colecție fluida perihepatica cu lama maximala de 15 mm ce asociaza colecție fluida intrapelvina cu lama maximala de 28 mm
  - **referinte_legate:**
      - **bilet_trimitere_JSON:** Dosar_Medical/2026-04-17_bilet_trimitere_CT.json
      - **note_referinta:** Datele biletului (serie BCTAP, nr 0631727, cod diagnostic 95, medic ordonator) sunt în JSON-ul dedicat biletului — nu se duplică aici pentru a menține documentația unică (cleanup 2026-04-24).

---

## <a name="2026-04-29-buletin-bioclinica-markeri-tumorali-hba1c"></a> 2026-04-29 — Buletin Analize Laborator Markeri Tumorali Hba1C (Laborator Clinic / Medicină de Laborator)
**Sursă:** `Dosar_Medical/2026-04-29_buletin_bioclinica_markeri_tumorali_hba1c.json` · **Buletin:** 26429A0020 · **Confidence:** high · **Flags:** pre_consult_oncolog_4_05_2026, CA_72_4_elevat_2_7x_limita, HbA1c_diabet_control_suboptimal, CA_19_9_borderline_la_limita, CEA_normal, CA_72_4_subcontractat_Timisoara

> Buletin emis de Bioclinica SRL Arad, punct recoltare 00036 Bioclinica Nădlac. Recoltare matinală à jeun (07:22), generare buletin aceeași zi 18:08. Patru analize: 3 markeri tumorali serici (CEA, CA 19-9, CA 72-4) + HbA1c (control glicemic). CA 72-4 SUBCONTRACTAT la Bioclinica Timișoara (cod laborator 26429T2632) — marker NU acoperit RENAR pentru subcontractor. Validator final: Dr. Luminița Statnic (cod A08064). Solicitate prin bilet trimitere Dr. Orbán Ecaterina-Maria (medic familie Nădlac) în pregătire consult oncolog 4.05.2026 OncoHelp Timișoara cu Dr. Anater. CA 72-4 a fost adăugat la recoltare ca marker suplimentar specific adenocarcinom gastric/eso-gastric (relevant Siewert II).

### 👤 Pacient

  - **nume:** PETRILĂ
  - **prenume:** VIOREL-MIHAI
  - **cnp:** 1590518024486
  - **data_nasterii:** 1959-05-18
  - **varsta_la_data_document:** 66
  - **sex:** M
  - **adresa:** STR Vasile Goldiș 42, Nădlac, Arad
  - **confidence_identificare:** high

### 🧪 Analize laborator

- **nume:** Antigen carcino embrionar (CEA) · **nume_original:** Antigen carcino embrionar (CEA) · **categorie:** marker_tumoral · **valoare_numerica:** 0.87 · **valoare_text:** 0,87 · **unitate:** ng/mL · **interval_referinta_min:** _(null)_ · **interval_referinta_max:** 3.8 · **interval_referinta_text:** < 3,80 · **interval_referinta_secundar:** Nefumători < 3,80 ng/mL; Fumători < 5,50 ng/mL · **metoda:** ser, ECLIA · **flag:** normal · **confidence_ocr:** high · **note:** Valoare în limita normală pentru nefumători (pacient fost fumător 1977-2012, 14 ani de abstinență — se aplică intervalul nefumători). CEA = marker tumoral nespecific (epitelial), util în monitorizarea evolutivă a cancerului colorectal, gastric, esofagian, pancreatic, pulmonar.
- **nume:** CA 19-9 · **nume_original:** CA 19-9 · **categorie:** marker_tumoral · **valoare_numerica:** 27.0 · **valoare_text:** 27,00 · **unitate:** U/mL · **interval_referinta_min:** _(null)_ · **interval_referinta_max:** 27.0 · **interval_referinta_text:** < 27,00 · **metoda:** ser, ECLIA · **flag:** borderline · **confidence_ocr:** high · **note:** Valoare exact pe limita superioară a intervalului normal. CA 19-9 = marker tumoral asociat cu adenocarcinom pancreatic, biliar, gastric, esofagian. Sensibilitate moderată; valori la limită necesită monitorizare evolutivă.
- **nume:** Hemoglobină glicozilată (HbA1c) · **nume_original:** Hemoglobină glicozilată (dozare de HbA1c) · **categorie:** control_glicemic · **valoare_numerica:** 7.5 · **valoare_text:** 7,5 · **unitate:** % · **interval_referinta_min:** 4.0 · **interval_referinta_max:** 5.6 · **interval_referinta_text:** 4,0 - 5,6 · **interval_referinta_secundar:** ADA: Normal ≤5,6%; Risc crescut diabet 5,7-6,4%; Diabet zaharat ≥6,5%. Țintă terapeutică >20 ani: <7,0% · **metoda:** sânge integral EDTA, Ion-exchange HPLC · **flag:** peste_limita · **confidence_ocr:** high · **medic_raportor:** Dr. Vorindan Anca Laura (A07744) · **note:** Valoare 7,5% — confirmă diabet zaharat tip 2 (≥6,5% per ADA). Depășește ținta terapeutică recomandată ADA pentru pacient >20 ani (<7,0%) → control glicemic suboptimal cu schema actuală (Jamesi 50/1000 mg, 1-0-1). Reflectă glicemia medie pe ultimele 2-3 luni (~169 mg/dL estimat). Notă document: schimbare valori biologice de referință începând cu 18.05.2024.
- **nume:** CA 72-4 · **nume_original:** CA 72-4ˢ · **categorie:** marker_tumoral · **valoare_numerica:** 18.59 · **valoare_text:** 18,59 · **unitate:** U/mL · **interval_referinta_min:** _(null)_ · **interval_referinta_max:** 6.9 · **interval_referinta_text:** < 6,90 · **metoda:** ser, ECLIA · **flag:** peste_limita · **confidence_ocr:** high · **subcontractat:** ✅ true · **laborator_subcontractor:** Bioclinica Timișoara (26429T2632) · **adresa_subcontractor:** BLD Cetății 53B, Timișoara · **medic_raportor:** Dr. Gaiță Pîrvan Corina (D15815) · **acreditare_renar:** ❌ false · **acreditare_note:** Analiză subcontractată — NU acoperită de acreditarea RENAR pentru subcontractor (per notă explicativă buletin: 'Analizele și punctele de recoltare marcate (*) NU sunt acoperite de acreditarea RENAR'; respectiv 'Analizele marcate (s) sunt subcontractate'). · **note:** Valoare 18,59 U/mL — depășește limita superioară (<6,90) de aproximativ 2,7 ori. CA 72-4 = marker tumoral cu specificitate ridicată pentru adenocarcinom gastric, gastro-esofagian și ovarian. Sensibilitate ~30-50%, dar specificitate superioară CA 19-9 pentru patologia gastrică. Analiza a fost adăugată la recoltare ca marker suplimentar față de lista inițială (CEA + CA 19-9 + HbA1c) în context Siewert II suspect (CT 20.04.2026).

### 👥 Medici / Unități

  - **medic_validator_buletin:** Dr. Luminița Statnic
  - **cod_medic_validator:** A08064
  - **specialitate_validator:** medic primar medicină de laborator
  - **unitate:** Bioclinica SRL Arad
  - **sectie:** Laborator medical
  - **punct_recoltare:** 00036 Bioclinica Nădlac
  - **adresa_laborator:** STR Dreptății 23, ap. 17, Arad
  - **acreditare:** RENAR, SR EN ISO 15189:2023, certificat LM 207
  - **subcontractor:**
      - **denumire:** Bioclinica Timișoara
      - **cod_laborator:** 26429T2632
      - **adresa:** BLD Cetății 53B, Timișoara
      - **operator_juridic:** Bioclinica SA
      - **analize_subcontractate:**
        - CA 72-4

### 🔢 Numere referință

  - **numar_buletin:** 26429A0020
  - **cod_punct_recoltare:** 00036
  - **cod_laborator_subcontractor:** 26429T2632

### 🏥 Context clinic

  - **scop_recoltare:** pregătire consult oncolog 4.05.2026 OncoHelp Timișoara (Dr. Anater Angelo-Christian)
  - **bilet_trimitere:** Dr. Orbán Ecaterina-Maria, medic familie, Cabinet Medical Individual Nădlac
  - **data_bilet_trimitere:** 2026-04-27 sau 2026-04-28 (per task TODO P0)
  - **documente_corelate:**
    - 2026-04-17_buletin_bioclinica_uree_creatinina.json (funcție renală pre-CT)
    - 2026-04-17_biopsie_esofagiana_histopatologic.json (biopsie inconcluzivă, sugestiv carcinom)
    - 2026-04-20_ct_torace_abdomen_pelvis.json (Siewert II probabil, T3-T4 N0-N1 M0)

---

_Sfârșit bundle. 19 documente canonice incluse._
