# CLAUDE.md — Proiect `.Tati` (auto-loader minimalist)

**Versiune:** 12.0 (arhitectură restructurată) | **Data:** 2026-04-23

> **Fișier auto-încărcat de Claude Code la pornirea în `G:\My Drive\Roly\.Tati`.**
> Scop: loader minimalist care direcționează spre reguli și context.

---

## Identitate proiect

**Dosar medical real** pentru pacient **PETRILĂ VIOREL-MIHAI** (n. 18.05.1959, tatăl user-ului Roland). Suspiciune proces proliferativ eso-gastric (Siewert II probabil) identificat la endoscopie 17.04.2026, CT stadializare 20.04.2026 (T3-T4 N0-N1 M0 probabil + ascită de elucidat), biopsie în așteptare.

**Sensibilitate clinică și legală:** fiecare afirmație medicală poate influența decizii clinice. Presupunerile implicite sunt interzise (vezi Regulile 7, 17, 22).

**Limba:** română. Commiturile git sunt automate la final de sesiune (Regula 16).

---

## Ordine citire obligatorie la prima interacțiune

Citești în această ordine, înainte de orice răspuns substanțial:

1. **`REGULAMENT.md`** — reguli medicale fundamentale (1-10): siguranța clinică, limbaj, cercetare, documentare, interacțiune, confidențialitate, documente pentru medici/familie, escaladare, feedback, principiu director.
2. **`REGULI_CLAUDE_CODE.md`** — reguli specifice Claude Code (6-22 extinse): AskUserQuestion, marcaje certitudine, mod de lucru, git auto-commit, dashboard sync, curățenie folder, verificare proactivă.
3. **`CONTEXT_MEDICAL.md`** — starea clinică curentă a pacientului.
4. **`TODO.md`** — calendar + acțiuni P0-P3 active.

**Dacă lucrezi în subfolder specializat, citești suplimentar:**

- `Dosar_Medical/CLAUDE.md` — reguli OCR + chain of custody + valabilitate clinică + coordonare Gemini + backup pre-modificare (Regulile 8, 9, 10, 11, 13, 14, 15)
- `Documente_Informative/CLAUDE.md` — reguli plasare documente pentru medici/familie (Regula 19 + shortcut Regula 17)

---

## Harta regulilor (unde găsești ce)

| Regulă | Subiect                                                                    | Fișier care o conține                                                                      |
| ------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 1-10   | Reguli fundamentale medicale                                               | `REGULAMENT.md`                                                                            |
| 6      | Confirmare fișiere la final de mesaj                                       | `REGULI_CLAUDE_CODE.md`                                                                    |
| 7      | AskUserQuestion pe decizii medicale                                        | `REGULI_CLAUDE_CODE.md`                                                                    |
| 8      | Protecție anti-halucinație OCR                                             | `Dosar_Medical/CLAUDE.md`                                                                  |
| 9      | Coordonare Claude ↔ Gemini                                                 | `Dosar_Medical/CLAUDE.md`                                                                  |
| 10     | Backup înainte de modificări majore                                        | `Dosar_Medical/CLAUDE.md`                                                                  |
| 11     | Marcaj valabilitate clinică temporală                                      | `Dosar_Medical/CLAUDE.md`                                                                  |
| 12     | Procedură conflict surse autoritare                                        | `REGULI_CLAUDE_CODE.md`                                                                    |
| 13     | Transcriere documente manuscrise                                           | `Dosar_Medical/CLAUDE.md`                                                                  |
| 14     | Chain of custody documente sursă                                           | `Dosar_Medical/CLAUDE.md`                                                                  |
| 15     | Log cercetări web                                                          | `Dosar_Medical/CLAUDE.md`                                                                  |
| 16     | Git auto-commit + push la final                                            | `REGULI_CLAUDE_CODE.md` (+ protocol extins în `Documentatie_Initiala/REGULI_DETALIATE.md`) |
| 17     | Marcaje certitudine `[CERT]`/`[PROBABIL]`/`[INCERT]`/`[NEGASIT]`           | `REGULI_CLAUDE_CODE.md` (+ exemple în `REGULI_DETALIATE.md`)                               |
| 18     | Sincronizare `DASHBOARD.html` la actualizări medicale                      | `REGULI_CLAUDE_CODE.md` (+ protocol în `REGULI_DETALIATE.md`)                              |
| 19     | Documente informative în `Documente_Informative/`                          | `Documente_Informative/CLAUDE.md`                                                          |
| 20     | Mod de lucru: cercetare → status → AskUserQuestion → confirmare → execuție | `REGULI_CLAUDE_CODE.md`                                                                    |
| 21     | Curățenie fluidă folder, zero ciorne                                       | `REGULI_CLAUDE_CODE.md`                                                                    |
| 22     | Verificare proactivă + eliminare info neverificate                         | `REGULI_CLAUDE_CODE.md` (+ protocol în `REGULI_DETALIATE.md`)                              |

**Notă overlap R6/R7:** Regulile 6 și 7 apar în două locuri cu versiuni diferite:

- `REGULAMENT.md` — versiunea **generică** (kit inițial Claude.ai, aplicabilă general)
- `REGULI_CLAUDE_CODE.md` — versiunea **scoped** (aplicabilă la fișiere de referință / decizii cu impact medical)

**La conflict direct, versiunea scoped are prioritate** pentru deciziile cu impact medical.

**Istoric evoluție reguli:** `Documentatie_Initiala/HISTORY_CLAUDE_MD.md`.
**Exemple extinse + matrice:** `Documentatie_Initiala/REGULI_DETALIATE.md` (citit on-demand).

---

## Relația cu celelalte regulamente

Regulile din proiectul `.Tati` **extind** (nu înlocuiesc):

- Regulamentul global `C:\Users\ALIENWARE\.claude\CLAUDE.md`
- Regulile din `C:\Users\ALIENWARE\.claude\rules\` (01-05)
- Regulile medicale critice din `C:\Users\ALIENWARE\Desktop\Roly\.Tati_Dosar_Medical\REGULAMENT.md` (dosar paralel, sursă originală)

**La conflict direct pentru lucrul în `G:\My Drive\Roly\.Tati`, regulile din acest proiect au prioritate.**

Coexistență cu `GEMINI.md` din același folder: vezi Regula 9 (în `Dosar_Medical/CLAUDE.md`).

---

## Path-uri echivalente

- **Principal (Google Drive):** `G:\My Drive\Roly\.Tati\`
- **Mirror Desktop:** `C:\Users\ALIENWARE\Desktop\Roly\.Tati\` (calea canonică pentru git commit — Regula 16)

Ambele sunt sincronizate; lucrezi în cea deschisă în Claude Code. Git commit-urile se fac pe Desktop (repo `RolandPetrila/Tati_Dosar_Medical`).

---

## Note pentru Claude Code

- **Fișier minimalist, intenționat.** Conținutul detaliat este în `REGULI_CLAUDE_CODE.md` + nested CLAUDE.md-uri pentru a evita avertismentul „Large CLAUDE.md" (restructurare 2026-04-23).
- **Nu inventa reguli.** Dacă nu găsești o regulă acoperită explicit, întreabă user-ul (Regula 7, 20).
- **Nu crea fișiere noi la rădăcină** decât dacă sunt explicit necesare — plasare preferată: `Documente_Informative/` (informativ), `Dosar_Medical/` (date medicale structurate), `Documentatie_Initiala/` (meta-documentație proiect).
