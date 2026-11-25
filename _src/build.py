#!/usr/bin/env python3
"""
Statischer Seitengenerator für villa-belvedere.

    python3 _src/build.py

erzeugt alle HTML-Seiten (it / de / en), sitemap.xml, robots.txt, 404.html und
site.webmanifest direkt im Wurzelverzeichnis des Repositorys (GitHub Pages).
"""
import datetime
import importlib
import json
import os
import re
import sys
from html import escape
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import SITE_URL, FORM_ENDPOINT, LEGAL, BRAND  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = (urlparse(SITE_URL).path.rstrip("/") + "/") or "/"
TODAY = datetime.date.today().isoformat()
YEAR = datetime.date.today().year

LANGS = ["it", "de", "en"]
DEFAULT_LANG = "it"
LOCALE = {"it": "it_IT", "de": "de_DE", "en": "en_GB"}
LANG_NAME = {"it": "Italiano", "de": "Deutsch", "en": "English"}
COUNTRY = {"it": "Italia", "de": "Italien", "en": "Italy"}

# Seitenschlüssel -> URL-Pfad je Sprache (sprechende, sprachspezifische Slugs)
SLUGS = {
    "home":        {"it": "",                         "de": "de/",                        "en": "en/"},
    "conte":       {"it": "olio-del-conte/",          "de": "de/oel-des-grafen/",         "en": "en/the-counts-oil/"},
    "energia":     {"it": "olio-energia-della-vita/", "de": "de/oel-energie-des-lebens/", "en": "en/oil-energy-of-life/"},
    "olivicoltori": {"it": "gli-olivicoltori/",       "de": "de/die-oelbauern/",          "en": "en/the-olive-growers/"},
    "contatti":    {"it": "contatti/",                "de": "de/kontakt/",                "en": "en/contact/"},
    "legal":       {"it": "note-legali/",             "de": "de/impressum/",              "en": "en/legal-notice/"},
    "privacy":     {"it": "privacy/",                 "de": "de/datenschutz/",            "en": "en/privacy-policy/"},
    "sitemap":     {"it": "mappa-del-sito/",          "de": "de/sitemap/",                "en": "en/sitemap/"},
}
NAV = ["home", "conte", "energia", "olivicoltori", "contatti"]
NOINDEX = {"legal", "privacy"}          # Rechtstexte nicht in den Suchindex
PRIORITY = {"home": "1.0", "conte": "0.9", "energia": "0.9", "olivicoltori": "0.8",
            "contatti": "0.6", "sitemap": "0.3"}

CONTENT = {l: importlib.import_module(f"content_{l}") for l in LANGS}


def url(key, lang, absolute=False):
    p = BASE + SLUGS[key][lang]
    return (SITE_URL.rstrip("/") + "/" + SLUGS[key][lang]) if absolute else p


def resolve(html, lang):
    html = html.replace("{{BASE}}", BASE)
    html = re.sub(r"\{\{link:(\w+)\}\}", lambda m: url(m.group(1), lang), html)
    return html


LOGO = ('<svg class="logo" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
        '<circle cx="40" cy="22" r="9" fill="currentColor" opacity=".9"/>'
        '<path d="M8 50 C24 40 36 34 56 30" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round"/>'
        '<path d="M22 43 q6 -12 16 -10 q-6 10 -16 10z M34 37 q10 -2 14 6 q-10 2 -14 -6z" fill="currentColor"/>'
        '</svg>')


def csp():
    form = urlparse(FORM_ENDPOINT)
    origin = f"{form.scheme}://{form.netloc}"
    return ("default-src 'self'; img-src 'self' data:; style-src 'self'; font-src 'self'; "
            f"script-src 'self'; connect-src 'self' {origin}; form-action 'self' {origin}; "
            "base-uri 'self'; object-src 'none'; upgrade-insecure-requests")


def json_ld(lang, key, page):
    ui = CONTENT[lang].UI
    org = {
        "@type": "Organization",
        "@id": SITE_URL + "/#org",
        "name": LEGAL["company"],
        "alternateName": BRAND,
        "url": SITE_URL + "/",
        "logo": SITE_URL + "/assets/img/icon-512.png",
        "description": CONTENT[lang].PAGES["home"]["description"],
        "foundingLocation": {"@type": "Place", "name": "Monte Pisano, Toscana, Italia"},
        "founder": [{"@type": "Person", "name": "Ralph Striewski"},
                    {"@type": "Person", "name": "Christina Striewski"}],
    }
    site = {
        "@type": "WebSite", "@id": SITE_URL + "/#website", "url": SITE_URL + "/",
        "name": BRAND, "inLanguage": LANGS, "publisher": {"@id": SITE_URL + "/#org"},
    }
    ptype = page.get("schema", "WebPage")
    web = {
        "@type": ptype, "@id": url(key, lang, True) + "#webpage", "url": url(key, lang, True),
        "name": page["title"], "description": page["description"], "inLanguage": lang,
        "isPartOf": {"@id": SITE_URL + "/#website"}, "about": {"@id": SITE_URL + "/#org"},
        "dateModified": TODAY,
    }
    if page.get("hero"):
        web["primaryImageOfPage"] = SITE_URL + "/assets/img/" + __import__("lib").fallback_jpg(page["hero"])
    graph = [org, site, web]
    if key != "home":
        graph.append({
            "@type": "BreadcrumbList", "@id": url(key, lang, True) + "#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": ui["nav"]["home"], "item": url("home", lang, True)},
                {"@type": "ListItem", "position": 2, "name": page.get("nav", page["h1"]), "item": url(key, lang, True)},
            ]})
        web["breadcrumb"] = {"@id": url(key, lang, True) + "#breadcrumb"}
    if ptype == "Article":
        graph.append({
            "@type": "Article", "headline": page["h1"], "inLanguage": lang,
            "mainEntityOfPage": {"@id": url(key, lang, True) + "#webpage"},
            "author": {"@id": SITE_URL + "/#org"}, "publisher": {"@id": SITE_URL + "/#org"},
            "image": SITE_URL + "/assets/img/" + __import__("lib").fallback_jpg(page["hero"]),
            "datePublished": "2026-11-23", "dateModified": TODAY,
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))


def header(lang, key):
    ui = CONTENT[lang].UI
    items = []
    for k in NAV:
        cur = ' aria-current="page"' if k == key else ""
        items.append(f'<li><a href="{url(k, lang)}"{cur}>{ui["nav"][k]}</a></li>')
    langs = []
    for l in LANGS:
        cur = ' aria-current="true"' if l == lang else ""
        langs.append(
            f'<li><a href="{url(key, l)}" hreflang="{l}" lang="{l}" title="{LANG_NAME[l]}"{cur}>'
            f'<span aria-hidden="true">{l.upper()}</span><span class="sr-only">{LANG_NAME[l]}</span></a></li>')
    return f"""<a class="skip" href="#main">{ui['skip']}</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{url('home', lang)}" aria-label="{BRAND} – {ui['nav']['home']}">{LOGO}<span>{BRAND}</span></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
      <span class="nav-toggle-bar" aria-hidden="true"></span><span class="sr-only">{ui['menu']}</span>
    </button>
    <nav id="site-nav" class="site-nav" aria-label="{ui['nav_label']}">
      <ul class="nav-list">{''.join(items)}</ul>
      <ul class="lang-switch" aria-label="{ui['lang_label']}">{''.join(langs)}</ul>
    </nav>
  </div>
</header>"""


def hero(lang, key, page):
    if not page.get("hero"):
        return f'<div class="page-head"><div class="wrap"><h1>{page["h1"]}</h1></div></div>'
    from lib import img
    home = key == "home"
    cls = "hero hero--home" if home else "hero"
    kicker = f'<p class="kicker">{page["kicker"]}</p>' if page.get("kicker") else ""
    lead = f'<p class="lead">{page["lead"]}</p>' if page.get("lead") else ""
    cta = page.get("hero_cta", "")
    return f"""<section class="{cls}">
  {img(page['hero'], page.get('hero_alt', ''), '100vw', eager=True, cls='hero-img')}
  <div class="hero-shade" aria-hidden="true"></div>
  <div class="wrap hero-text">{kicker}<h1>{page['h1']}</h1>{lead}{cta}</div>
</section>"""


def breadcrumb(lang, key, page):
    if key == "home":
        return ""
    ui = CONTENT[lang].UI
    return (f'<nav class="breadcrumb wrap" aria-label="{ui["breadcrumb"]}"><ol>'
            f'<li><a href="{url("home", lang)}">{ui["nav"]["home"]}</a></li>'
            f'<li><span aria-current="page">{page.get("nav", page["h1"])}</span></li></ol></nav>')


def footer(lang):
    ui = CONTENT[lang].UI
    nav = "".join(f'<li><a href="{url(k, lang)}">{ui["nav"][k]}</a></li>' for k in NAV)
    legal = "".join(f'<li><a href="{url(k, lang)}">{ui["nav"][k]}</a></li>' for k in ("legal", "privacy", "sitemap"))
    langs = " · ".join(f'<a href="{url("home", l)}" hreflang="{l}" lang="{l}">{LANG_NAME[l]}</a>' for l in LANGS)
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <p class="footer-brand">{LOGO}<span>{BRAND}</span></p>
      <p>{ui['footer_claim']}</p>
      <address>{LEGAL['company']}<br>{LEGAL['street']}<br>{LEGAL['zip_city']} – {COUNTRY[lang]}<br>
      {ui['vat']}: {LEGAL['vat']}</address>
    </div>
    <nav aria-label="{ui['footer_nav']}"><p class="footer-h">{ui['footer_nav']}</p><ul>{nav}</ul></nav>
    <nav aria-label="{ui['footer_legal']}"><p class="footer-h">{ui['footer_legal']}</p><ul>{legal}</ul>
      <p class="footer-h">{ui['lang_label']}</p><p>{langs}</p></nav>
  </div>
  <div class="wrap footer-bottom">
    <p>{ui['info_only']}</p>
    <p>© {YEAR} {LEGAL['company']} · {ui['images_note']}</p>
  </div>
</footer>"""


def render(lang, key):
    c = CONTENT[lang]
    page = c.PAGES[key]
    title = page["title"]
    if BRAND not in title and len(title) + len(BRAND) + 3 <= 65:
        title = f"{title} | {BRAND}"
    alts = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{url(key, l, True)}">' for l in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{url(key, DEFAULT_LANG, True)}">'
    og_alt = "\n".join(f'<meta property="og:locale:alternate" content="{LOCALE[l]}">' for l in LANGS if l != lang)
    robots = "noindex, follow" if key in NOINDEX else "index, follow, max-image-preview:large"
    og_img = SITE_URL + "/assets/img/og-villa-belvedere.jpg"
    body_cls = f"page-{key}"
    main = resolve(page["body"], lang)
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(page['description'])}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url(key, lang, True)}">
{alts}
<meta http-equiv="Content-Security-Policy" content="{csp()}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="theme-color" content="#2b1f2e">
<meta name="color-scheme" content="light">
<link rel="preload" href="{BASE}assets/fonts/cormorant-garamond-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{BASE}assets/css/style.css">
<noscript><link rel="stylesheet" href="{BASE}assets/css/nojs.css"></noscript>
<link rel="icon" href="{BASE}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{BASE}assets/img/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="{BASE}assets/img/apple-touch-icon.png">
<link rel="manifest" href="{BASE}site.webmanifest">
<meta property="og:type" content="{'article' if page.get('schema') == 'Article' else 'website'}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{escape(page['title'])}">
<meta property="og:description" content="{escape(page['description'])}">
<meta property="og:url" content="{url(key, lang, True)}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{escape(c.UI['og_alt'])}">
<meta property="og:locale" content="{LOCALE[lang]}">
{og_alt}
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json_ld(lang, key, page)}</script>
<script src="{BASE}assets/js/main.js" defer></script>
</head>
<body class="{body_cls}">
{header(lang, key)}
<main id="main" tabindex="-1">
{hero(lang, key, page)}
{breadcrumb(lang, key, page)}
{main}
</main>
{footer(lang)}
</body>
</html>
"""
    return resolve(html, lang)


def sitemap_page_body(lang):
    """Inhalt der HTML-Sitemap (für Besucher)."""
    ui = CONTENT[lang].UI
    items = "".join(
        f'<li><a href="{url(k, lang)}">{ui["nav"][k]}</a> – {CONTENT[lang].PAGES[k]["description"]}</li>'
        for k in NAV + ["legal", "privacy"])
    other = "".join(
        f'<li lang="{l}"><a href="{url("sitemap", l)}" hreflang="{l}">{LANG_NAME[l]}</a></li>'
        for l in LANGS if l != lang)
    return (f'<section class="section"><div class="wrap prose"><ul class="sitemap-list">{items}</ul>'
            f'<h2>{ui["lang_label"]}</h2><ul>{other}</ul></div></section>')


def page_404():
    blocks = []
    for l in LANGS:
        c = CONTENT[l].UI
        blocks.append(f'<div lang="{l}" class="nf-block"><h2>{c["nf_title"]}</h2><p>{c["nf_text"]}</p>'
                      f'<p><a class="btn" href="{url("home", l)}">{c["nf_link"]}</a></p></div>')
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>404 | {BRAND}</title>
<meta name="robots" content="noindex">
<link rel="stylesheet" href="{BASE}assets/css/style.css">
<link rel="icon" href="{BASE}favicon.svg" type="image/svg+xml">
</head>
<body class="page-404">
<main id="main" class="nf">
  <p class="brand nf-brand">{LOGO}<span>{BRAND}</span></p>
  <h1>404</h1>
  {''.join(blocks)}
</main>
</body>
</html>
"""


def sitemap_xml():
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml" '
           'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    from lib import fallback_jpg
    for key in SLUGS:
        if key in NOINDEX:
            continue
        for lang in LANGS:
            page = CONTENT[lang].PAGES[key]
            out.append("  <url>")
            out.append(f"    <loc>{url(key, lang, True)}</loc>")
            out.append(f"    <lastmod>{TODAY}</lastmod>")
            out.append(f"    <priority>{PRIORITY.get(key, '0.5')}</priority>")
            for l in LANGS:
                out.append(f'    <xhtml:link rel="alternate" hreflang="{l}" href="{url(key, l, True)}"/>')
            out.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{url(key, DEFAULT_LANG, True)}"/>')
            for im in page.get("images", [page["hero"]] if page.get("hero") else []):
                out.append(f"    <image:image><image:loc>{SITE_URL}/assets/img/{fallback_jpg(im)}</image:loc></image:image>")
            out.append("  </url>")
    out.append("</urlset>")
    return "\n".join(out) + "\n"


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    count = 0
    for lang in LANGS:
        CONTENT[lang].PAGES["sitemap"]["body"] = sitemap_page_body(lang)
        for key in SLUGS:
            write(SLUGS[key][lang] + "index.html", render(lang, key))
            count += 1
    write("404.html", page_404())
    write("sitemap.xml", sitemap_xml())
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    write("site.webmanifest", json.dumps({
        "name": f"{BRAND} – Olio extravergine del Monte Pisano", "short_name": BRAND,
        "lang": "it", "start_url": BASE, "scope": BASE, "display": "browser",
        "background_color": "#f8efdf", "theme_color": "#2b1f2e",
        "icons": [{"src": f"{BASE}assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": f"{BASE}assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
                  {"src": f"{BASE}favicon.svg", "sizes": "any", "type": "image/svg+xml"}],
    }, ensure_ascii=False, indent=2))
    print(f"{count} Seiten + 404, sitemap.xml, robots.txt, site.webmanifest geschrieben (BASE={BASE})")


if __name__ == "__main__":
    main()
