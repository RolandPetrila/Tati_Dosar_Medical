# START.md — Protocol de inițiere sesiune

**Acest fișier descrie exact ce să faci când deschizi proiectul pentru prima dată sau la începutul oricărei sesiuni noi.**

## Secvența obligatorie de citire

Citește fișierele în ordinea de mai jos, complet, înainte de orice altă acțiune:

1. `README.md` — vedere de ansamblu (1 min)
2. `CLAUDE.md` — instrucțiuni principale (obligatoriu) (3 min)
3. `REGULAMENT.md` — reguli stricte (obligatoriu) (3 min)
4. `CONTEXT_MEDICAL.md` — starea medicală actuală (obligatoriu) (5 min)
5. `WORKFLOW.md` — metodologia (obligatoriu) (3 min)
6. `TODO.md` — acțiunile deschise (obligatoriu) (2 min)
7. `CHANGELOG.md` — ultimele 10 intrări (recomandat) (2 min)
8. `STRUCTURA_PROIECT.md` — organizarea folderelor (la nevoie)
9. `SURSE_MEDICALE.md` — surse autoritare (la nevoie, înainte de cercetări medicale)
10. `GLOSAR.md` — termeni medicali (la nevoie)

## Verificarea înțelegerii — checklist intern

Înainte de a răspunde primului mesaj al utilizatorului, asigură-te că poți răspunde la:

1. **Cine este pacientul?** (nume, vârstă, statut civil, reședință)
2. **Care este suspiciunea clinică principală?**
3. **Ce investigații au fost făcute și ce se așteaptă?**
4. **Care sunt comorbiditățile cu impact pe investigațiile în curs?**
5. **Care sunt medicamentele zilnice cu impact pe CT cu contrast?**
6. **Care sunt acțiunile deschise din `TODO.md`?**
7. **Care este ultima modificare din `CHANGELOG.md`?**
8. **Există fișiere în `documente_sursa/` care nu au fost încă procesate?**

Dacă un element nu este clar după citirea fișierelor, NU improviza — întreabă utilizatorul să clarifice.

## Confirmarea către utilizator

La începutul sesiunii, răspunde cu un mesaj scurt care conține:

```
Dosar citit și încărcat.

Status curent: [2-3 rânduri de sinteză a situației medicale]

Acțiuni deschise ({N}):
- [prioritate] {acțiune} — {deadline / termen}
- ...

Ultima actualizare dosar: {data} — {descriere scurtă}

Aștept instrucțiuni.
```

## Ce faci DACĂ...

### ...fișierele lipsesc sau sunt corupte

NU genera conținut inventat pentru a acoperi lipsa. Raportează utilizatorului: „Fișierul X lipsește / este gol. Am nevoie să îl restaurezi sau să confirm că pot genera o versiune inițială.”

### ...există fișiere noi în `documente_sursa/` care nu sunt menționate în `CHANGELOG.md`

Raportează: „Am detectat fișiere noi în `documente_sursa/` care nu sunt procesate:
- `{fișier}` ({data adăugării, dacă o poți determina din filesystem})
...
Să le procesez acum?”

### ...fișierele sunt contradictorii

Raportează contradicția către utilizator. NU încerca să o rezolvi singur.

### ...utilizatorul îți cere să execuți o acțiune fără să fi confirmat înțelegerea

Confirmă mai întâi. Ciclul `CLARIFICĂ → PLANIFICĂ → CONFIRMĂ` (vezi `WORKFLOW.md`) nu se scurtcircuitează decât pentru acțiuni triviale (răspuns la o întrebare pur informațională, căutare simplă).

### ...este prima sesiune și folderul este gol (doar fișierele kit)

Raportează: „Dosarul este inițializat dar gol. Confirm să pornim procesul de construire a bazei de cunoștințe?” și așteaptă.

## Limbă și ton

- Răspunde în română.
- Ton profesional, concis, fără preambul.
- Fără emoticoane decât dacă utilizatorul le folosește.
- Lucrurile critice (medicale, de siguranță) se evidențiază clar (bold, notă, etc.).

## Limitare inițială

În prima sesiune nu executa modificări semnificative ale fișierelor de configurare (`CLAUDE.md`, `REGULAMENT.md`, etc.) fără confirmare explicită și fără a păstra versiunea anterioară în `arhiva/versiuni_config/`.

## Gata de lucru

După parcurgerea acestei secvențe, ești operațional. Sarcina următoare vine de la utilizator.
