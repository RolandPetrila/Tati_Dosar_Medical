# Deploy DASHBOARD pe Cloudflare Pages + Access — ghid pas cu pas

## Ce obții

- **URL fix permanent** (ex. `https://tati-dosar.pages.dev`) — trimiți URL-ul, nu fișierul
- **Login protejat cu email OTP** — doar email-urile aprobate de tine primesc cod și intră
- **Dashboard complet funcțional** pe orice telefon/laptop (JavaScript, countdown, fetch live pentru Alimentație)
- **Deploy automat la fiecare modificare locală + commit + push pe GitHub** (~1 min)
- **Privat real** — oricine accesează fără să fie în listă primește „Access denied"

## Ce NU se expune

Doar fișierele publice ale dashboardului:

- `DASHBOARD.html` (servit ca `index.html`)
- `ALIMENTATIE.md`
- `manifest.webmanifest`
- `assets/` (icoanele PWA)

**Restul fișierelor (date medicale, log-uri, context, JSON-uri Dosar_Medical) NU sunt servite** — configurarea build-ului filtrează exact ce se publică.

Cloudflare are acces read la repo-ul întreg (prin conexiunea GitHub), dar asta e analog cu GitHub Pages. Cloudflare e certificat ISO 27001 + GDPR, datele nu se indexează și nu devin publice — doar cele din output-ul build-ului.

## Timp estimat

~30-40 minute (one-time). După aceea, totul e automat.

---

## FAZA 1 — Cont Cloudflare (5 min)

1. Deschide [dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up)
2. Înregistrează-te cu email-ul tău principal (`petrilarolly@gmail.com`)
3. Verifică email-ul, setează parolă sigură
4. La "Add a website" poți sări peste (nu ai nevoie de domeniu propriu; folosim `.pages.dev`)

## FAZA 2 — Deploy Pages din GitHub (10 min)

1. În dashboard Cloudflare → meniul din stânga → **"Workers & Pages"**
2. Butonul **"Create application"** → tab **"Pages"** → **"Connect to Git"**
3. **"Connect GitHub"** → autorizezi accesul
   - La "Repository access" alege **"Only select repositories"** → selectează **doar** `Tati_Dosar_Medical`
   - NU alege "All repositories" — principiul least-privilege
4. Alege repo-ul `RolandPetrila/Tati_Dosar_Medical` → **"Begin setup"**
5. **Configurări build** (exact așa):

| Câmp                       | Valoare                          |
| -------------------------- | -------------------------------- |
| **Project name**           | `tati-dosar`                     |
| **Production branch**      | `main`                           |
| **Framework preset**       | `None`                           |
| **Build command**          | _(vezi mai jos — copiază exact)_ |
| **Build output directory** | `public`                         |

**Build command** (copy-paste integral, o singură linie):

```bash
mkdir -p public && cp DASHBOARD.html public/index.html && cp manifest.webmanifest public/ && cp ALIMENTATIE.md public/ && cp -r assets public/
```

6. **"Save and Deploy"**
7. Așteaptă ~1 minut. Vei vedea „Success! Your project is deployed" cu URL-ul (ex. `https://tati-dosar.pages.dev`)

**Verificare:** deschide URL-ul într-un tab nou. Ar trebui să vezi dashboard-ul (cu countdown CT, tab Medical, tab Alimentație).

> ⚠️ **ATENȚIE:** în acest moment URL-ul e **PUBLIC** — oricine cu link-ul vede dashboardul. Treci imediat la FAZA 3 pentru a-l proteja.

## FAZA 3 — Activare Zero Trust (5 min)

1. Întoarce-te la dashboard Cloudflare (pagina principală)
2. Meniul din stânga → **"Zero Trust"** (dacă nu apare, caută în căutare)
3. La prima intrare îți cere **"Choose a team name"**
   - Alege ceva scurt, ex. `roland-petrila` sau `petrila-family`
   - Va deveni subdomain: `roland-petrila.cloudflareaccess.com`
4. Alege plan **"Free"** (50 utilizatori gratuit — mult peste ce ne trebuie)
5. Confirmă detalii cont → **"Proceed"**

## FAZA 4 — Creare Access Application (10 min)

1. În dashboard Zero Trust → meniul din stânga → **"Access"** → **"Applications"**
2. **"Add an application"** → alege **"Self-hosted"**
3. **Configurări aplicație**:

| Câmp                   | Valoare                                                     |
| ---------------------- | ----------------------------------------------------------- |
| **Application name**   | `Dosar Tati`                                                |
| **Session duration**   | `24 hours`                                                  |
| **Application domain** | `tati-dosar.pages.dev` (URL-ul din FAZA 2, fără `https://`) |

4. **"Next"**
5. Secțiunea **"Add policies"** → **"Create new policy"**:

| Câmp                 | Valoare            |
| -------------------- | ------------------ |
| **Policy name**      | `Familie aprobată` |
| **Action**           | `Allow`            |
| **Session duration** | `24 hours`         |

6. La **"Configure rules" → "Include"**:
   - **Selector:** `Emails`
   - **Value:** adaugă pe rând email-urile aprobate, Enter după fiecare:
     - `petrilarolly@gmail.com`
     - email mama
     - email soră / frate (dacă e cazul)
     - _(înlocuiește cu adresele reale)_

7. **"Next"** → **"Add application"**

## FAZA 5 — Testare (5 min)

1. Deschide browser în **modul incognito** (Ctrl+Shift+N pe Chrome, Ctrl+Shift+P pe Firefox)
2. Navighează la `https://tati-dosar.pages.dev`
3. Cloudflare îți cere email
4. Introdu un email aprobat → primești cod OTP pe email (~30 secunde)
5. Introduci codul → ești logat → vezi dashboard-ul cu toate funcționalitățile
6. **Test negativ:** încearcă cu un email ne-aprobat → ar trebui să primești „Access denied"

Dacă toate pașii merg: SETUP-UL E COMPLET.

## FAZA 6 — Trimite URL familiei

Exemplu mesaj pentru WhatsApp:

> Dragii mei,
> Am creat o pagină care se actualizează automat cu informațiile despre dosarul tatei:
> **https://tati-dosar.pages.dev**
>
> La prima deschidere vă cere email-ul (trebuie să fie adresa pe care am aprobat-o, spuneți-mi dacă nu merge). Primiți un cod pe email, introduceți-l, și aveți acces 24h. După 24h reintroduceți codul.
>
> Pe telefon: deschideți linkul, apoi din meniul browser-ului → "Add to Home Screen" / "Adaugă la ecranul de pornire" ca să aveți shortcut direct cu iconul "Dosar .Tati".
>
> La orice modificare pe care o fac eu, voi vedeți automat ultima versiune.

---

## Ce faci la fiecare update de acum înainte

1. Modifici local `DASHBOARD.html`, `ALIMENTATIE.md` sau orice altceva
2. Claude (sau tu manual) face `git add + commit + push`
3. Cloudflare detectează push pe `main` → build automat → deploy în ~1 minut
4. Toată familia vede noua versiune la următoarea accesare (sau la F5 dacă pagina e deschisă)

**Nimic manual pe Cloudflare. Totul e declanșat de push-ul Git.**

## Management utilizatori

### Adaugi pe cineva nou

1. Zero Trust → Access → Applications → **Dosar Tati** → Policies → **Familie aprobată** → Edit
2. La "Include" → adaugă email → Save

### Scoți pe cineva

1. Același drum → ștergi email-ul din listă → Save
2. Dacă e logat, sesiunea ține până la expirare (max 24h)
3. Pentru deconectare imediată: Zero Trust → My Team → Users → revoke session

### Revoci toate sesiunile

Zero Trust → Applications → Dosar Tati → trei puncte → **Revoke all sessions**

---

## Troubleshooting

### „Nu primesc codul OTP pe email"

- Verifică spam / promoții
- Codul vine de la `noreply@notify.cloudflare.com`
- Dacă niciun email în 2 min → refresh pagina și cere cod nou

### „Build failed" pe Cloudflare

- Cloudflare Pages → Deployments → click deployment cu eroare → vezi log
- Probabil build command scris greșit — verifică-l la FAZA 2 pas 5
- Copy log + trimite-mi dacă nu dai de cap

### „Vreau să schimb URL-ul"

- Cloudflare Pages → project settings → **Custom domain**
- Sau schimbi project name (e legat de subdomain)
- Reconfigurezi Application domain în Access după schimbare

### „Cineva din listă nu primește acces"

- Verifică email-ul scris corect în policy (case-insensitive, dar tipografie)
- Asigură-te că utilizatorul introduce același email la login

### „Cred că URL-ul a scăpat unde nu trebuie"

- Oricine fără email în listă nu poate intra — Access blochează
- Pentru control suplimentar: reset policy + schimbă team name (URL Zero Trust nou) + informează familia cu noul URL
- Dacă vrei să dezactivezi totul urgent: Cloudflare Pages → project → **Pause deployment**

---

## Recenzie semi-anuală recomandată

La fiecare 6 luni, verifică:

- [ ] Lista de email-uri în Access e încă corectă (cineva s-a mutat, s-a schimbat)
- [ ] Nu sunt deployment-uri vechi care ocupă spațiu (Cloudflare șterge automat după 100)
- [ ] Cloudflare Pages → Analytics pentru a vedea cine a accesat (log-uri Access)

---

## Alternative dacă Cloudflare nu merge

Dacă dintr-un motiv întâmpini bariere (nu accepți cont nou, Cloudflare schimbă condițiile, etc.):

- **Vercel** cu "Password Protection" (plan Pro ~$20/lună — nu gratuit ca Cloudflare)
- **Netlify** cu "Password Protection" (plan Pro)
- **GitHub Pages private** (cere GitHub Pro $4/lună + fiecare utilizator cont GitHub)

Cloudflare Pages + Access pe plan Free e cea mai bună opțiune cost-beneficiu pentru cazul tău.

---

## Resurse oficiale

- [Cloudflare Pages docs](https://developers.cloudflare.com/pages/)
- [Cloudflare Zero Trust / Access docs](https://developers.cloudflare.com/cloudflare-one/)
- [GitHub integration Cloudflare Pages](https://developers.cloudflare.com/pages/configuration/git-integration/)

---

**Creat:** 2026-04-18 18:49
**Ultima revizuire:** 2026-04-18 18:49
