---
title: Index master corespondență medicală tata
last_scan: 2026-04-25 19:30
scan_type: full_history (R27 first ingest)
threads_total: 11
threads_active: 1
last_processed_thread_id: 19dc4e472df6e379 (mesaj Roland 25.04 18:00 în thread Anater 19dbe7d30cfacbb3)
version: 1.0
auto_loaded: false (citește la cerere)
---

# Index corespondență medicală — Petrila Viorel-Mihai

> **Sursă autoritară** pentru orice afirmație de tipul „medicul X a recomandat Y" sau „a fost programat la Z" (R27).
>
> **Comenzi disponibile (vezi `REGULI_CLAUDE_CODE.md §Regula 27`):**
>
> - `verifică gmail nou` — incremental scan față de `last_processed_thread_id` de mai sus
> - `verifică gmail oncohelp` — re-scan focalizat OncoHelp
> - `verifică gmail [keyword]` — scan custom

---

## Threaduri active

| Data ultim | Thread                                                                     | Subiect                          | Participanți        | Status                                 |
| ---------- | -------------------------------------------------------------------------- | -------------------------------- | ------------------- | -------------------------------------- |
| 2026-04-25 | [re-solicitare-consult-anater](2026-04-24_re-solicitare-consult-anater.md) | RE: Solicitare consult oncologic | Roland ↔ Dr. Anater | 🟡 așteptare răspuns clarificări 25.04 |

## Threaduri încheiate (cu răspuns medic)

| Data       | Thread                                                                                   | Subiect                                                              | Participanți               | Status                                                                        |
| ---------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------- | ----------------------------------------------------------------------------- |
| 2026-04-24 | [raspuns-iocn-mester](2026-04-24_raspuns-iocn-mester.md)                                 | Raspuns IOCN -solicitare consult oncologic                           | Dr. Mester (IOCN) → Roland | ⚪ încheiat — second opinion disponibilă                                      |
| 2026-04-22 | [solicitare-dr-cip-recomandare-lusca](2026-04-22_solicitare-dr-cip-recomandare-lusca.md) | Solicitare sfat medical pentru tatăl meu (66 ani) - proces esofagian | Roland ↔ Dr. Cip           | ⚪ încheiat — recomandare adjuvant Zeolit/AHCC (de discutat la consult 30.04) |

## Threaduri broadcast (fără răspuns uman)

| Data       | Thread                                                                     | Subiect                                                                    | Destinatar                                   | Status                                |
| ---------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------- | ------------------------------------- |
| 2026-04-23 | [solicitare-sprijin-oncohelp](2026-04-23_solicitare-sprijin-oncohelp.md)   | Solicitare sprijin medical pentru tatăl meu (66 ani)                       | OncoHelp programări + office                 | ⚪ răspuns pe thread separat (Anater) |
| 2026-04-23 | [broadcast-solicitari-clinici](2026-04-23_broadcast-solicitari-clinici.md) | Solicitare sprijin medical pentru tatăl meu (66 ani) — broadcast 5 clinici | Medisprof + IOCN office + Amethyst + MedLife | ⚪ vezi fișier dedicat                |

## Statistici scan

- **Threaduri totale procesate:** 11 (după filtru relevanță medicală — exclus Hidroelectrica + LinkedIn + GitHub Sistem_Notificari workflow notifications)
- **Mailuri totale relevante:** 11 (4 răspuns medici primite + 7 mailuri Roland trimise / forwarded)
- **Atașamente menționate (per mail Roland):** 7 (rezultat endoscopie + colonoscopie + CT + analize + schema medicație + Franța 2012 + bilet trimitere) — listate, **NU descărcate** (politică R27 — la cerere user, return URL Gmail)
- **Contacte noi identificate:**
  - **Dr. Anater Angelo - Christian** (OncoHelp) — adăugat în CONTACTE_MEDICALE.md (status corectat 25.04: per semnătură email = „Medic Specialist", site oncohelp.ro listează „Rezident" — conflict surse R12)
  - **Dr. Vornicu Vlad-Norin** (OncoHelp) — adăugat în CONTACTE_MEDICALE.md (cercetare web Task #10)
  - **Dr. Andra Meșter** (IOCN Cluj) — păstrat în `CONTEXT_MEDICAL.md §9` ca istoric extern (NU în CONTACTE_MEDICALE.md — scope OncoHelp activi)
  - **Dr. Cip** (medicină alternativă) — păstrat doar în corespondență, NU în catalog medic curant
- **Adrese clinici contactate:**
  - OncoHelp Timișoara — răspuns pozitiv, programat 30.04
  - IOCN Cluj — răspuns pozitiv (second opinion disponibilă)
  - Medisprof Cluj — auto-reply only
  - MedLife — auto-reply (CNP cont aplicație) only
  - Amethyst Cluj — fără răspuns

## Threaduri non-medicale exclude din scan

- `19db7b6988a8708a` + `19db7b4e40803196` — GitHub workflow notifications (Sistem_Notificari biopsie monitor) — NOT medical correspondence
- `19da6b5a2b4a403a` ("Dosar Medical - Petrila Viorel"), `19da44828c6bd64b` ("tati") — self-emails Roland (notes personale) — NOT correspondence with medical staff
- Hidroelectrica facturi (multiple) — NOT relevant
- LinkedIn job notifications (Genesis Medtech) — NOT relevant
- Linterul a căutat „Genesis" și a returnat aceste — match nume firmă diferită (Genesis Medtech ≠ Genesis Medical Clinic Arad)

## Comenzi disponibile (R27)

```
verifică gmail nou           # ce e nou față de 19dc4e472df6e379
verifică gmail oncohelp      # re-scan focalizat OncoHelp
verifică gmail bioclinica    # caută mailuri Bioclinica (rezultat biopsie când apare)
verifică gmail [Anater|Vornicu|Mester]   # focalizat per medic
```

## Auto-propagare la fiecare scan (R27)

1. **CONTACTE_MEDICALE.md** — adăugare/update emailuri/telefoane noi (doar OncoHelp activi)
2. **CONTEXT_MEDICAL.md** — instrucțiuni medicale primite cu marcaj sursă `[per mail Dr. X 2026-MM-DD]`
3. **TODO.md** — programări/termene noi
4. **SESSION_LOG.md** + **CHANGELOG.md** — log scan cu data + commit
5. **DASHBOARD.html** — tab Echipă medicală + bannere relevante (R18 declanșator)
6. **INDEX.json** — regenerat (Task #12)
7. **Backup R10** + commit + push (R16)

## Atașamente — politică R27

Atașamentele sunt **listate** cu nume + tip + URL deep-link Gmail thread, **NU descărcate** local. Threaduri cu atașamente:

- **Mailuri inițiale Roland (broadcast 23.04 + Cip 22.04 + OncoHelp 23.04):** 7 atașamente identice = endoscopie + colonoscopie + CT + analize + schema medicație + Franța 2012 + bilet trimitere. Acestea sunt **deja arhivate fizic** în `Dosar_Medical/documente_sursa/` — sursa autoritară e PDF-ul, NU emailul.
- **Mailurile primite (Anater + Mester + Cip + auto-replies):** ZERO atașamente (răspunsuri text-only).

La cererea user („găsește atașamentul X"), returnez instant numele + URL thread Gmail + sumar din extras + pointer la copia PDF în `Dosar_Medical/documente_sursa/`.
