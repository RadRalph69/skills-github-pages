"""Hilfsfunktionen für die Inhaltsdateien (content_*.py)."""
import os
from functools import lru_cache
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")


@lru_cache(None)
def variants(name):
    """Liefert [(breite, höhe, datei)] der vorhandenen WebP-Varianten eines Bildes."""
    from PIL import Image
    out = []
    for f in sorted(os.listdir(IMG)):
        if f.startswith(name + "-") and f.endswith(".webp"):
            w = f[len(name) + 1:-5]
            if w.isdigit():
                with Image.open(os.path.join(IMG, f)) as im:
                    out.append((im.width, im.height, f))
    out.sort()
    if not out:
        raise FileNotFoundError(f"Bild {name} fehlt – erst images.py/rasterize.js/optimize.py ausführen")
    return out


def fallback_jpg(name):
    for f in os.listdir(IMG):
        if f.startswith(name + "-") and f.endswith(".jpg"):
            return f
    return variants(name)[-1][2]


def img(name, alt, sizes="100vw", eager=False, cls=""):
    v = variants(name)
    w, h, _ = v[-1]
    srcset = ", ".join(f"{{{{BASE}}}}assets/img/{f} {vw}w" for vw, _, f in v)
    attrs = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="{{{{BASE}}}}assets/img/{fallback_jpg(name)}" srcset="{srcset}" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{escape(alt)}" {attrs}>')


def fig(name, alt, caption=None, cls="", sizes="(min-width: 960px) 50vw, 100vw"):
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    c = f' class="{cls}"' if cls else ""
    return f"<figure{c}>{img(name, alt, sizes)}{cap}</figure>"


def ph(text):
    """Markiert einen Platzhalter, der später ersetzt werden muss (gelb hinterlegt)."""
    return f'<span class="ph" title="Platzhalter">[{text}]</span>'


def link(key, text, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{{{{link:{key}}}}}">{text}</a>'


# --------------------------------------------------------------------------- #
# Layout-Bausteine (gemeinsam für alle Sprachen)
# --------------------------------------------------------------------------- #
def section(inner, cls="", sid=None, label=None):
    i = f' id="{sid}"' if sid else ""
    a = f' aria-labelledby="{label}"' if label else ""
    return f'<section class="section {cls}"{i}{a}><div class="wrap">{inner}</div></section>'


def split(text, figure, rev=False):
    return f'<div class="split{" split--rev" if rev else ""}"><div class="prose">{text}</div>{figure}</div>'


def h2(text, hid=None, kicker=None):
    k = f'<p class="kicker">{kicker}</p>' if kicker else ""
    i = f' id="{hid}"' if hid else ""
    return f"{k}<h2{i}>{text}</h2>"


def cards(items, more):
    """items: [(page_key, image, alt, title, text)]"""
    out = []
    for key, im, alt, title, text in items:
        out.append(
            f'<article class="card">{img(im, alt, "(min-width: 960px) 33vw, 100vw")}'
            f'<div class="card-body"><h3><a class="card-link" href="{{{{link:{key}}}}}">{title}</a></h3>'
            f'<p>{text}</p><p class="more" aria-hidden="true">{more} →</p></div></article>')
    return f'<div class="cards">{"".join(out)}</div>'


def portraits(items):
    """items: [(image, alt, name, role, quote)]"""
    out = []
    for im, alt, name, role, quote in items:
        out.append(
            f'<figure class="portrait">{img(im, alt, "(min-width: 960px) 25vw, 50vw")}'
            f'<figcaption><strong>{name}</strong><span>{role}</span>'
            f'<blockquote><p>{quote}</p></blockquote></figcaption></figure>')
    return f'<div class="portraits">{"".join(out)}</div>'


def facts(items):
    return '<dl class="facts">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in items) + "</dl>"


def timeline(items):
    """items: [(jahr, titel, text)]"""
    return '<ol class="timeline">' + "".join(
        f'<li><p class="tl-year">{y}</p><h3>{t}</h3><p>{x}</p></li>' for y, t, x in items) + "</ol>"


def band(image, alt, quote, cite):
    return (f'<section class="band">{img(image, alt, "100vw", cls="band-img")}<div class="band-shade" aria-hidden="true"></div>'
            f'<div class="wrap band-text"><blockquote><p>{quote}</p><footer>{cite}</footer></blockquote></div></section>')


def table(caption, head, rows, note=None):
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    tr = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    n = f'<p class="table-note">{note}</p>' if note else ""
    return f'<div class="table-wrap"><table class="data"><caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>{n}'


def note(text, cls="note"):
    return f'<aside class="{cls}">{text}</aside>'


def calendar(items):
    return '<ol class="calendar">' + "".join(
        f'<li><p class="cal-m">{m}</p><h3>{t}</h3><p>{x}</p></li>' for m, t, x in items) + "</ol>"


def btn(key, text, cls="btn"):
    return f'<a class="{cls}" href="{{{{link:{key}}}}}">{text}</a>'


def contact_form(F, lang):
    from config import FORM_ENDPOINT
    opts = "".join(f"<option>{t}</option>" for t in F["topics"])
    privacy = F["privacy"].replace("{link}", f'<a href="{{{{link:privacy}}}}">{F["privacy_link"]}</a>')
    return f"""<form class="form" action="{FORM_ENDPOINT}" method="POST" data-js-form
      data-ok="{F['ok']}" data-err="{F['err']}" data-sending="{F['sending']}">
  <p class="form-req"><span aria-hidden="true">*</span> {F['required']}</p>
  <div class="field"><label for="f-name">{F['name']} <span aria-hidden="true">*</span></label>
    <input id="f-name" name="name" type="text" autocomplete="name" required maxlength="120"></div>
  <div class="field"><label for="f-email">{F['email']} <span aria-hidden="true">*</span></label>
    <input id="f-email" name="email" type="email" autocomplete="email" required maxlength="200"></div>
  <div class="field"><label for="f-topic">{F['topic']}</label>
    <select id="f-topic" name="topic">{opts}</select></div>
  <div class="field"><label for="f-msg">{F['message']} <span aria-hidden="true">*</span></label>
    <textarea id="f-msg" name="message" rows="7" required maxlength="5000"></textarea></div>
  <div class="hp" aria-hidden="true"><label for="f-hp">{F['hp']}</label>
    <input id="f-hp" name="_gotcha" type="text" tabindex="-1" autocomplete="off"></div>
  <input type="hidden" name="_language" value="{lang}">
  <div class="field field--check"><input id="f-privacy" name="privacy_consent" type="checkbox" value="yes" required>
    <label for="f-privacy">{privacy} <span aria-hidden="true">*</span></label></div>
  <button class="btn" type="submit">{F['send']}</button>
  <p class="form-status" role="status" aria-live="polite"></p>
</form>"""
