# Villa Belvedere – Website

Mehrsprachige Informations-Website (Italienisch = Hauptsprache, Deutsch, Englisch) für das biologische
Olivenöl extra vergine der Azienda Agricola Villa Belvedere am Monte Pisano.

- Reines statisches HTML/CSS (+ 2 KB JavaScript) → schnell, sicher, ideal für Google.
- **Keine Cookies, kein Tracking, keine externen Schriften/CDNs** → kein Cookie-Banner nötig.
- **Kein Verkauf**: keine Preise, kein Warenkorb, keine Kaufaufforderung → kein Fernabsatzvertrag.

## Sitemap (Seitenstruktur)

| Reiter | Italienisch (Standard) | Deutsch | Englisch |
|---|---|---|---|
| Home | `/` | `/de/` | `/en/` |
| Öl des Grafen | `/olio-del-conte/` | `/de/oel-des-grafen/` | `/en/the-counts-oil/` |
| Öl, Energie des Lebens | `/olio-energia-della-vita/` | `/de/oel-energie-des-lebens/` | `/en/oil-energy-of-life/` |
| Die Ölbauern | `/gli-olivicoltori/` | `/de/die-oelbauern/` | `/en/the-olive-growers/` |
| Kontakt | `/contatti/` | `/de/kontakt/` | `/en/contact/` |
| Impressum (Footer) | `/note-legali/` | `/de/impressum/` | `/en/legal-notice/` |
| Datenschutz (Footer) | `/privacy/` | `/de/datenschutz/` | `/en/privacy-policy/` |
| HTML-Sitemap (Footer) | `/mappa-del-sito/` | `/de/sitemap/` | `/en/sitemap/` |

Dazu: `sitemap.xml` (mit hreflang-Verknüpfungen und Bildern), `robots.txt`, `404.html`, `site.webmanifest`.

## Technik & SEO

- Eigene, sprechende URLs je Sprache; `hreflang` (it/de/en + `x-default` → it) auf jeder Seite und in der Sitemap.
- `canonical`, Meta-Description, Open Graph / Twitter-Card mit eigenem Vorschaubild (1200×630).
- Strukturierte Daten (JSON-LD): Organization, WebSite, WebPage/Article/AboutPage/ContactPage, BreadcrumbList.
- Semantisches HTML, genau eine H1 pro Seite, Alt-Texte, Skip-Link, Tastaturbedienung, sichtbarer Fokus.
- Responsive Bilder (WebP in 3 Größen, `srcset`/`sizes`, feste Breite/Höhe gegen Layout-Sprünge, Lazy Loading,
  Hero mit `fetchpriority="high"`), Schrift lokal (Cormorant Garamond, OFL) mit `preload`.
- Content-Security-Policy, Referrer-Policy, kein Inline-JavaScript.
- Impressum und Datenschutz sind `noindex` (stehen nicht in Google, sind aber von jeder Seite im Footer verlinkt).

## Inhalte bearbeiten

Die HTML-Seiten werden **erzeugt** – bitte nicht direkt die `index.html`-Dateien bearbeiten, sondern:

| Was | Datei |
|---|---|
| Domain, Formular-Endpoint, Impressumsdaten | `_src/config.py` |
| Texte Italienisch / Deutsch / Englisch | `_src/content_it.py`, `_src/content_de.py`, `_src/content_en.py` |
| Design (Farben, Schriften, Layout) | `assets/css/style.css` |
| Bilder | siehe `_src/BILD-PROMPTS.md` |

Danach neu erzeugen:

```bash
python3 _src/build.py
```

(benötigt Python 3 mit Pillow: `pip install pillow`). Platzhalter stehen in `[eckigen Klammern]` und
sind auf der Website **gelb markiert**, bis sie ersetzt sind.

## Vor dem Livegang – Checkliste

1. **Impressum/Datenschutz**: alle `[...]`-Felder in `_src/config.py` ausfüllen (Inhaber, Adresse, Telefon,
   E-Mail, PEC, Partita IVA, Codice Fiscale, REA, Bio-Kontrollstelle und Code).
2. **Kontaktformular**: bei Formspree (oder einem anderen Formular-Dienst) ein Formular anlegen, den Endpoint
   in `FORM_ENDPOINT` eintragen und Anbieterdaten in `FORM_PROVIDER` prüfen. Ein Auftragsverarbeitungsvertrag
   (DPA) mit dem Anbieter abschließen.
3. **Bio-Angaben**: „biologico/Bio“ nur verwenden, wenn die Zertifizierung besteht (VO (EU) 2018/848).
4. **Gesundheitsangabe Polyphenole**: nur stehen lassen, wenn der Laborwert ≥ 250 mg/kg Hydroxytyrosol und
   Derivate beträgt (VO (EU) 432/2012). Sonst den Kasten auf „Öl, Energie des Lebens“ entfernen.
5. **Laborwerte** in der Tabelle eintragen, historische Angaben (Grafenfamilie, Jahreszahlen) prüfen.
6. **Eigene Domain** (z. B. `villabelvedere.xyz`): in `_src/config.py` `SITE_URL` ändern, `build.py`
   ausführen, in GitHub unter *Settings → Pages → Custom domain* eintragen und *Enforce HTTPS* aktivieren.
   Erst dann liegt `robots.txt` im Wurzelverzeichnis der Domain, wo Google sie liest.
7. **Google Search Console**: Domain bestätigen und `sitemap.xml` einreichen.
8. Rechtstexte abschließend von einer Fachperson (Anwalt/Kammer) prüfen lassen – die Texte sind sorgfältige
   Vorlagen, aber keine Rechtsberatung.

## Bilder neu erzeugen (Platzhalter)

```bash
python3 _src/images.py && node _src/rasterize.js && python3 _src/optimize.py && node _src/icons.js && python3 _src/build.py
```
