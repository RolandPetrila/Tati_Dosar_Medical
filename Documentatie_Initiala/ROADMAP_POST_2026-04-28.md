---
title: Roadmap recomandări amânate post plan implementare 2026-04-28
created_at: 2026-04-28 13:00
created_by: Claude_Opus_4.7_1M (Faza 3 plan implementare cross-terminal)
target_review_date: 2026-05-26 (după consult 4.05 + 3 săptămâni)
sources:
  - .claude-outputs/audit/2026-04-28_031943/audit_report.md
  - .claude-outputs/imbunatatiri/2026-04-28_032030/RECOMANDARI_IMBUNATATIRI.md
  - .claude-outputs/improve/2026-04-28_032615/{improve_report.md,roadmap.md}
filter_aplicat: filtre 4-criteriilor (RELEVANT pentru consult 4.05, UTIL ROI≥7, NATIV stack existent, LOGIC nu rupe workflow)
recomandari_implementate_2026-04-28: 10 (audit/redenumire + 3 fixes + N4 audit script + T1 schema + 4 DASHBOARD changes + N1 briefing DOCX + Mate Endre CONTACTE)
recomandari_amanate: 25 (8 funcții noi + 7 existente + 10 tehnice)
status: 🔴 PENDING — review după 2026-05-26
---

# Roadmap recomandări amânate post 2026-04-28

> **Scop:** lista recomandărilor din `.claude-outputs/imbunatatiri/2026-04-28_032030/` și `.claude-outputs/improve/2026-04-28_032615/` care **NU au fost implementate** în Faza 1+2+3 al planului 2026-04-28 (deadline critic 4.05 consult oncolog).
>
> **Filtru aplicat:** RELEVANT pentru consult 4.05 ÎNDEPĂRTAT / UTIL ROI<7 / OVERKILL pentru scala curentă / RUPE workflow existent. Aceste 25 recomandări sunt VALIDE dar amânate strategic.
>
> **Review programat:** 2026-05-26 (după consult oncolog 4.05 + 3 săptămâni de stabilizare). User decide la review care intră în următorul plan implementare.

---

## 🟡 Funcții noi amânate (8)

| ID  | Titlu                                            | Complexitate | Impact  | Condiție declanșare                                                                        | Sursa                            |
| --- | ------------------------------------------------ | ------------ | ------- | ------------------------------------------------------------------------------------------ | -------------------------------- |
| N2  | Restore JSON din backup automat                  | Medie        | Mediu   | După un incident real de corupție JSON nedetectat ca cel din 26.04 + 28.04                 | RECOMANDARI_IMBUNATATIRI.md §N2  |
| N5  | Fuse.js search global în DASHBOARD               | Mică         | Mare UX | Dacă user simte nevoie reală de căutare rapidă pe DASHBOARD în consult medical (post 4.05) | RECOMANDARI_IMBUNATATIRI.md §N5  |
| N6  | Email→TODO automat (Gmail trigger)               | Medie        | Mediu   | După ce volumul de mailuri Gmail crește >5/săpt + user obosește de ingest manual           | RECOMANDARI_IMBUNATATIRI.md §N6  |
| N7  | Trend analiză valori laborator (linie temporală) | Medie        | Mediu   | După acumulare ≥5 buletine analize comparabile (post-chimio start)                         | RECOMANDARI_IMBUNATATIRI.md §N7  |
| N8  | Heartbeat extern monitor proces                  | Medie        | Robust  | Dacă monitor ntfy bioclinica eșuează silent în viitor (incident real)                      | RECOMANDARI_IMBUNATATIRI.md §N8  |
| N9  | Slash command `/dosar`                           | Mică         | UX      | Dacă apar 3+ comenzi recurente pe care user le scrie repetat (ex: status, todo, contact)   | RECOMANDARI_IMBUNATATIRI.md §N9  |
| N10 | Reverse-lookup INDEX.json (medic→toate JSON-uri) | Medie        | Mediu   | Dacă apar consulturi multiple cu medici diferiți și e nevoie de view per-medic             | RECOMANDARI_IMBUNATATIRI.md §N10 |
| N11 | Hook audit auto la commit (pre-push)             | Mică         | Robust  | După T1 hook activat (necesită jsonschema framework instalat)                              | RECOMANDARI_IMBUNATATIRI.md §N11 |

---

## 🟡 Existente — extinderi amânate (7)

| ID  | Titlu                                                   | Complexitate | Impact    | Condiție declanșare                                                              | Sursa                            |
| --- | ------------------------------------------------------- | ------------ | --------- | -------------------------------------------------------------------------------- | -------------------------------- |
| E1  | Logger structurat în scripts/\_logging.py               | Mică         | Mediu     | După un incident debug greu (script eșuat fără context)                          | RECOMANDARI_IMBUNATATIRI.md §E1  |
| E3  | Boundary regex pentru pattern auto-detect               | Mică         | Mic       | Dacă scripturile cer fine-tuning pe pattern-uri noi de fișiere                   | RECOMANDARI_IMBUNATATIRI.md §E3  |
| E5  | Countdown automatic în DASHBOARD (zile până consult)    | Mică         | UX        | Dacă user vrea reminder visual pentru următorul eveniment cheie                  | RECOMANDARI_IMBUNATATIRI.md §E5  |
| E7  | Extindere LIMITS în system_health_check (categorii noi) | Mică         | Mediu     | Dacă apar metrici noi de monitorizat (ex: număr corespondență, număr biopsii)    | RECOMANDARI_IMBUNATATIRI.md §E7  |
| E8  | R23+R25 thresholds tuning în Dosar_Medical/CLAUDE.md    | Mică         | Mic       | Dacă apar conflicte R23 vs R25 sau false positives la documente parțial lizibile | RECOMANDARI_IMBUNATATIRI.md §E8  |
| E9  | ARIA WCAG full compliance pentru DASHBOARD              | Medie        | Mic-mediu | Dacă user/familie sunt non-văzători sau folosesc screen reader                   | RECOMANDARI_IMBUNATATIRI.md §E9  |
| E10 | Q&A primer pentru orientare rapidă noi sesiuni Claude   | Mică         | Mic       | Dacă apar sesiuni noi frecvente cu context restart                               | RECOMANDARI_IMBUNATATIRI.md §E10 |

---

## 🟡 Tehnice — amânate (10)

| ID  | Titlu                                                      | Complexitate | Impact    | Condiție declanșare                                                                          | Sursa                                         |
| --- | ---------------------------------------------------------- | ------------ | --------- | -------------------------------------------------------------------------------------------- | --------------------------------------------- |
| T2  | Split DASHBOARD.html în fișiere separate (lazy-load)       | Medie        | Perf      | Dacă timpul render mobil >3s (măsurat real) sau bandwidth Drive sync e o problemă            | RECOMANDARI_IMBUNATATIRI.md §T2               |
| T3  | CSP headers pentru DASHBOARD GitHub Pages                  | Mică         | Sec       | Dacă apare risc de XSS (puțin probabil dat repo public cu contributors limitate)             | RECOMANDARI_IMBUNATATIRI.md §T3               |
| T4  | Logging structurat pentru toate scripturile Python         | Medie        | Mediu     | După T1 + N11 (cluster logging)                                                              | RECOMANDARI_IMBUNATATIRI.md §T4               |
| T5  | Type hints + mypy strict pentru scripturile Python         | Medie        | Mediu     | Dacă scriptele ajung >500 linii fiecare și apar bug-uri de tipare                            | RECOMANDARI_IMBUNATATIRI.md §T5               |
| T6  | Dependency pinning + lockfile (requirements.txt + uv.lock) | Mică         | Robust    | Dacă apar conflicte de versiuni între maleficient (Windows + GitHub Actions)                 | RECOMANDARI_IMBUNATATIRI.md §T6               |
| T7  | Test suite (pytest) pentru scripturile critice             | Medie        | Robust    | Dacă scripturile ating maturitate productiv (post-stabilizare 6+ luni)                       | RECOMANDARI_IMBUNATATIRI.md §T7               |
| T8  | README.md cuprinzător la rădăcină                          | Mică         | Mic       | Dacă proiectul e share-uit cu colaboratori externi (medici, familie extinsă)                 | RECOMANDARI_IMBUNATATIRI.md §T8               |
| T9  | Lighthouse audit DASHBOARD (perf + a11y + SEO)             | Mică         | Mic-mediu | Dacă DASHBOARD devine principal canal de comunicare cu medici (necesar audit profesional)    | RECOMANDARI_IMBUNATATIRI.md §T9               |
| T10 | CHANGELOG.md restructurare (versiuni semantice)            | Mică         | Mic       | Dacă CHANGELOG ajunge >300 KB (curent 168 KB; growth ~10 KB/săpt)                            | RECOMANDARI_IMBUNATATIRI.md §T10              |
| —   | Activare hook T1 jsonschema (după pip install)             | Mică         | Robust    | După confirmare user pentru `pip install pre-commit check-jsonschema` + `pre-commit install` | TODO.md §P3 + .pre-commit-config.yaml DORMANT |

---

## 📊 Rezumat per categorie

| Categorie       | Total amânate | Implementate 28.04                               | Rate implementare |
| --------------- | ------------- | ------------------------------------------------ | ----------------- |
| Funcții noi (N) | 8             | 3 (N1 briefing, N3 antecedente, N4 audit)        | 27%               |
| Existente (E)   | 7             | 2 (E4 badge, E6 tel/mailto)                      | 22%               |
| Tehnice (T)     | 10            | 1 (T1 schema PARTIAL — hook activation pendantă) | 9%                |
| **Total**       | **25**        | **6**                                            | **19%**           |

Plus: 4 acțiuni audit/cleanup imediate (redenumire 4 fișiere R26 + 2 MD extragere + 1 fix M3 + 1 fix E2 + tati.png cleanup).

---

## 📅 Calendar review

- **2026-05-26** (3 săpt post-consult 4.05): primul review formal — user decide care din cele 25 amânate intră în plan implementare următor (eventuale priorități post-evoluție clinică)
- **2026-08-31** (3 luni): al doilea review — dacă proiectul ajunge la maturitate stabilă, multe T-uri devin relevante
- **Trigger neprogramat:** dacă apare incident real care declanșează una din condițiile de mai sus (ex: corupție JSON nedetectat → N2 + N11)

---

## Note pentru sesiuni viitoare Claude

- Lista de mai sus este SURSA UNICĂ pentru deciderea „ce facem next" dincolo de 4.05 — NU re-genera analiză din `.claude-outputs/` la fiecare sesiune
- Pentru detaliu spec implementare per recomandare → `.claude-outputs/imbunatatiri/2026-04-28_032030/RECOMANDARI_IMBUNATATIRI.md` §<ID>
- Update acest fișier la fiecare review cu status implementat / amânat / abandonat
