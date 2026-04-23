# PLAN — Reorganizare arhitectură CLAUDE.md

**Data start:** 2026-04-23 03:20 +0300
**Declanșator:** Claude Code alert „Large CLAUDE.md will impact performance (43.4k chars > 40.0k)"
**Autor plan:** Claude Opus 4.7 (sesiune orchestrator `.Tati`)
**User:** Roland Petrilă (confirmat direcția + mod „all în una sesiune")

---

## 1. Scop

Reducere footprint `CLAUDE.md` proiect `.Tati` de la ~43.4k → ~4k (sub 10% din actual), prin aplicarea filozofiei deja validate de user în workspace-ul paralel `.Tati_Documente_Medicale` și în `Regulamente_Globale/`:

- **CLAUDE.md = pointer, nu depozit** (auto-loader minimalist)
- **Reguli detaliate = fișier dedicat** (`REGULI_CLAUDE_CODE.md` nou)
- **Reguli specifice zonă = nested CLAUDE.md** (Dosar_Medical/, Documente_Informative/)
- **Exemple extinse + changelog = on-demand** (Documentatie_Initiala/)
- **REGULAMENT.md existent (Regulile 1-10 medicale) = NEATINS**

---

## 2. Arhitectură target

```
G:\My Drive\Roly\.Tati\
│
├── CLAUDE.md                    ← ~4k   GUVERNANȚĂ auto-load
│                                  Identitate + ordine citire + harta regulilor + pointers
│
├── REGULAMENT.md                ← ~11k  EXISTENT, NEATINS (Regulile 1-10 medicale de bază)
│
├── REGULI_CLAUDE_CODE.md        ← ~15k  NOU — Regulile 6-22 compactate (rule + Why + How)
│                                  Exemplele extinse → pointer REGULI_DETALIATE.md
│
├── CONTEXT_MEDICAL.md           ← păstrat  STATIC — fapte clinice pacient
├── TODO.md                      ← păstrat  VOLATIL — calendar + P0-P3
├── CHANGELOG.md                 ← păstrat  APPEND istoric
├── SESSION_LOG.md               ← păstrat  APPEND coord Claude/Gemini
├── WEB_QUERIES.md               ← păstrat  APPEND log cercetări
├── ALIMENTATIE.md               ← păstrat
├── DASHBOARD.html               ← păstrat
├── GLOSAR.md                    ← păstrat
├── STRUCTURA_PROIECT.md         ← păstrat
│
├── Dosar_Medical\
│   ├── CLAUDE.md                ← ~7k   NOU — Regulile 8, 9, 10, 11, 13, 14, 15
│   │                               (OCR + Gemini coord + backup + valabilitate + manuscrise + chain + WEB)
│   └── [...] (JSON-uri, arhiva, cercetari — neatinse)
│
├── Documente_Informative\
│   ├── CLAUDE.md                ← ~2k   NOU — Regula 19 + shortcut Regula 17
│   └── [...] (GHID_*.md — neatinse)
│
└── Documentatie_Initiala\
    ├── PLAN_reorganizare_claude_md_2026-04-23.md  ← ACEST FIȘIER
    ├── REGULI_DETALIATE.md      ← ~13k  NOU — exemple extinse Regula 17, matrice Regula 11,
    │                               protocol extins Regula 16/18/22
    └── HISTORY_CLAUDE_MD.md     ← ~4k   NOU — changelog v1→v11 extras
```

### Mapare reguli pe fișiere (acoperire 100%)

| Regulă                                         | Locație nouă                                                            | Motiv                                       |
| ---------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------- |
| 6 (confirmare fișiere final mesaj)             | `REGULI_CLAUDE_CODE.md`                                                 | always-on, aplicabil oriunde                |
| 7 (AskUserQuestion pe date medicale)           | `REGULI_CLAUDE_CODE.md`                                                 | always-on critic                            |
| 8 (OCR anti-halucinație)                       | `Dosar_Medical/CLAUDE.md`                                               | se aplică doar la procesare documente sursă |
| 9 (coordonare Gemini)                          | `Dosar_Medical/CLAUDE.md`                                               | specific pentru dosar                       |
| 10 (backup pre-modificare)                     | `Dosar_Medical/CLAUDE.md`                                               | fișiere de referință în Dosar_Medical/      |
| 11 (valabilitate clinică)                      | `Dosar_Medical/CLAUDE.md`                                               | specific citare date clinice                |
| 12 (conflict surse autoritare)                 | `REGULI_CLAUDE_CODE.md`                                                 | always-on                                   |
| 13 (manuscrise)                                | `Dosar_Medical/CLAUDE.md`                                               | specific OCR                                |
| 14 (chain of custody)                          | `Dosar_Medical/CLAUDE.md`                                               | specific documente sursă                    |
| 15 (WEB_QUERIES log)                           | `Dosar_Medical/CLAUDE.md`                                               | specific cercetări medicale                 |
| 16 (git auto-commit + push)                    | `REGULI_CLAUDE_CODE.md` + protocol extins în `REGULI_DETALIATE.md`      | always-on core, detalii timestamp on-demand |
| 17 (marcaje certitudine)                       | `REGULI_CLAUDE_CODE.md` + exemple extinse în `REGULI_DETALIATE.md`      | always-on core                              |
| 18 (sincronizare DASHBOARD)                    | `REGULI_CLAUDE_CODE.md` + protocol extins în `REGULI_DETALIATE.md`      | always-on core                              |
| 19 (Documente_Informative/)                    | `Documente_Informative/CLAUDE.md` + shortcut în `REGULI_CLAUDE_CODE.md` | specific zonă                               |
| 20 (mod lucru cercetare→status→Ask→confirmare) | `REGULI_CLAUDE_CODE.md`                                                 | always-on critic                            |
| 21 (curățenie fluidă, zero ciorne)             | `REGULI_CLAUDE_CODE.md`                                                 | always-on                                   |
| 22 (verificare proactivă [INCERT])             | `REGULI_CLAUDE_CODE.md` + protocol extins în `REGULI_DETALIATE.md`      | always-on core                              |

---

## 3. Checklist execuție

- [x] **Pas 0.5** — Creare acest PLAN (Regula R-PLAN)
- [ ] **Pas 0** — Backup CLAUDE.md actual în `Dosar_Medical/arhiva/versiuni_config/` + test empiric nested CLAUDE.md
- [ ] **Pas 1** — Rescriere `CLAUDE.md` rădăcină (~4k)
- [ ] **Pas 2** — Creare `REGULI_CLAUDE_CODE.md` (~15k)
- [ ] **Pas 3** — Creare `Dosar_Medical/CLAUDE.md` (~7k)
- [ ] **Pas 4** — Creare `Documente_Informative/CLAUDE.md` (~2k)
- [ ] **Pas 5** — Creare `Documentatie_Initiala/REGULI_DETALIATE.md` (~13k)
- [ ] **Pas 6** — Creare `Documentatie_Initiala/HISTORY_CLAUDE_MD.md` (~4k)
- [ ] **Pas 7** — Verificare integritate + update SESSION_LOG + CHANGELOG + MEMORY + commit + push

---

## 4. Reguli siguranță

1. **Backup OBLIGATORIU (Regula 10)** — CLAUDE.md actual se arhivează ÎNAINTE de prima modificare.
2. **Niciun fișier medical atins** — CONTEXT_MEDICAL.md, TODO.md, JSON-uri, DASHBOARD.html rămân intacte.
3. **REGULAMENT.md existent NEATINS** — conține Regulile 1-10 fundamentale medicale, e util cum e.
4. **Verificare integritate la Pas 7** — checklist explicit: fiecare regulă 6-22 din CLAUDE.md vechi e acoperită în noua arhitectură.
5. **Stop-and-ask dacă pică ceva** — conform Regula 20, nu inventez decizii la problemă.
6. **Test empiric la Pas 0** — verific că nested CLAUDE.md e detectat contextual de Claude Code înainte de a mă angaja pe restul pașilor.

---

## 5. Jurnal execuție (append pe parcurs)

### 2026-04-23 03:20 — Start

- Task-uri #1-9 create via TaskCreate
- Backup arhiva/versiuni_config/ are deja 4 versiuni istorice CLAUDE.md; adaug una nouă la Pas 0
- REGULAMENT.md verificat (11k, Regulile 1-10 medicale) → PĂSTRAT
- REGULI_CLAUDE_CODE.md (fișier NOU) va conține Regulile 6-22 în loc de extindere REGULAMENT.md existent

### [updates se adaugă pe parcurs]

---

## 6. Rollback dacă ceva pică

```bash
# Restore CLAUDE.md principal
cp "Dosar_Medical/arhiva/versiuni_config/CLAUDE_pre-reorganizare-v12_2026-04-23_[HHMM].md" CLAUDE.md

# Șterge fișierele noi create
rm REGULI_CLAUDE_CODE.md
rm Dosar_Medical/CLAUDE.md
rm Documente_Informative/CLAUDE.md
rm Documentatie_Initiala/REGULI_DETALIATE.md
rm Documentatie_Initiala/HISTORY_CLAUDE_MD.md

# Git reset la ultimul commit
git reset --hard HEAD
```

---

## 7. Criteriu succes

- `CLAUDE.md` rădăcină sub 5k caractere
- Avertismentul Claude Code „Large CLAUDE.md" NU mai apare
- Toate cele 17 reguli (6-22) acoperite în noua arhitectură
- Integritate semantică: nicio regulă pierdută, doar reorganizată
- Commit + push curat către `origin/main`
