#!/usr/bin/env python3
"""
Erzeugt die generischen Platzhalter-Illustrationen (SVG) für Villa Belvedere.

Die Bilder sind stilisierte, flache Illustrationen in den Farben eines Olivenhains
bei Sonnenuntergang. Sie dienen als Platzhalter, bis echte Fotos bzw. KI-Bilder
(siehe _src/BILD-PROMPTS.md) eingesetzt werden.

Aufruf:  python3 _src/images.py   ->  schreibt SVGs nach _src/svg/
Danach:  node _src/rasterize.js    ->  erzeugt WebP/JPG unter assets/img/
"""
import math
import os
import random

OUT = os.path.join(os.path.dirname(__file__), "svg")

# Farbpalette "Olivenhain bei Sonnenuntergang"
C = {
    "night": "#2b1f2e",
    "plum": "#4a2c3f",
    "wine": "#7a3b3f",
    "terracotta": "#b5603a",
    "orange": "#d9822b",
    "amber": "#e9a23b",
    "gold": "#f2c46d",
    "honey": "#f7dc9c",
    "cream": "#f8efdf",
    "rose": "#e7a593",
    "olive_dark": "#2f3320",
    "olive": "#545b33",
    "olive_mid": "#6f7744",
    "olive_light": "#9aa36d",
    "silver": "#b9bf98",
    "stone": "#d8c2a0",
    "stone_dark": "#a88c66",
    "roof": "#9c4a2f",
}


# --------------------------------------------------------------------------- #
# Grundbausteine
# --------------------------------------------------------------------------- #
def svg_doc(w, h, body, defs=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
        f"<defs>{defs}{GRAIN_FILTER}</defs>{body}"
        f'<rect width="{w}" height="{h}" filter="url(#grain)" opacity=".16" style="mix-blend-mode:multiply"/>'
        "</svg>"
    )


GRAIN_FILTER = (
    '<filter id="grain" x="0" y="0" width="100%" height="100%">'
    '<feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="7" result="n"/>'
    '<feColorMatrix type="saturate" values="0"/>'
    "</filter>"
    '<filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="18"/></filter>'
    '<filter id="blur6" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6"/></filter>'
)


def lin_grad(gid, stops, x1=0, y1=0, x2=0, y2=1):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<linearGradient id="{gid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{s}</linearGradient>'


def rad_grad(gid, stops, cx=0.5, cy=0.5, r=0.5):
    s = "".join(
        f'<stop offset="{o}" stop-color="{c}" stop-opacity="{a}"/>' for o, c, a in stops
    )
    return f'<radialGradient id="{gid}" cx="{cx}" cy="{cy}" r="{r}">{s}</radialGradient>'


def sky(w, h, gid="sky", stops=None):
    stops = stops or [
        (0, C["plum"]),
        (0.35, C["wine"]),
        (0.62, C["orange"]),
        (0.82, C["gold"]),
        (1, C["honey"]),
    ]
    return lin_grad(gid, stops), f'<rect width="{w}" height="{h}" fill="url(#{gid})"/>'


def sun(cx, cy, r, gid="sunglow"):
    d = rad_grad(
        gid,
        [(0, "#fff6d8", 1), (0.18, C["honey"], 0.95), (0.45, C["gold"], 0.35), (1, C["orange"], 0)],
    )
    b = (
        f'<circle cx="{cx}" cy="{cy}" r="{r * 6}" fill="url(#{gid})"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff3cf"/>'
    )
    return d, b


def clouds(w, y0, rng, n=6, color=C["rose"], opacity=0.35):
    out = []
    for _ in range(n):
        x = rng.uniform(-100, w)
        y = y0 + rng.uniform(-60, 60)
        L = rng.uniform(180, 520)
        hgt = rng.uniform(6, 16)
        out.append(
            f'<ellipse cx="{x + L / 2:.0f}" cy="{y:.0f}" rx="{L / 2:.0f}" ry="{hgt:.0f}" '
            f'fill="{color}" opacity="{opacity * rng.uniform(.6, 1.1):.2f}"/>'
        )
    return "".join(out)


def ridge(w, h, base, amp, rng, color, waves=4, opacity=1.0):
    phases = [rng.uniform(0, 2 * math.pi) for _ in range(waves)]
    freqs = [rng.uniform(0.6, 1.4) * (i + 1) for i in range(waves)]
    pts = []
    steps = 80
    for i in range(steps + 1):
        x = w * i / steps
        y = base
        for k in range(waves):
            y -= amp / (k + 1) * math.sin(freqs[k] * x / w * math.pi * 2 + phases[k])
        pts.append(f"{x:.1f},{y:.1f}")
    return (
        f'<path d="M0,{h} L{" L".join(pts)} L{w},{h} Z" fill="{color}" opacity="{opacity}"/>'
    )


def ridge_y(w, base, amp, seed, waves, x):
    """y-Position eines Rückens (gleiche Formel wie ridge) – um Objekte darauf zu setzen."""
    rng = random.Random(seed)
    phases = [rng.uniform(0, 2 * math.pi) for _ in range(waves)]
    freqs = [rng.uniform(0.6, 1.4) * (i + 1) for i in range(waves)]
    y = base
    for k in range(waves):
        y -= amp / (k + 1) * math.sin(freqs[k] * x / w * math.pi * 2 + phases[k])
    return y


def olive_tree(x, y, s, rng, trunk=C["olive_dark"], dark=C["olive"], light=C["olive_light"],
               rim=None, silhouette=False):
    """Knorriger Olivenbaum mit breiter, lockerer Krone."""
    out = []
    tw = 9 * s
    lean = rng.uniform(-14, 14) * s
    th = rng.uniform(46, 62) * s
    # Stamm – zwei verdrehte Stränge
    for side in (-1, 1):
        x0 = x + side * tw * 0.6
        out.append(
            f'<path d="M{x0 - tw * .7:.1f},{y:.1f} C{x0 - tw:.1f},{y - th * .4:.1f} '
            f'{x + lean + side * tw * 1.6:.1f},{y - th * .6:.1f} {x + lean + side * tw * 1.2:.1f},{y - th:.1f} '
            f'L{x + lean + side * tw * .2:.1f},{y - th:.1f} '
            f'C{x + lean:.1f},{y - th * .55:.1f} {x0 + tw * .3:.1f},{y - th * .35:.1f} {x0 + tw * .7:.1f},{y:.1f} Z" '
            f'fill="{trunk}"/>'
        )
    # Äste
    for _ in range(4):
        ax = x + lean + rng.uniform(-30, 30) * s
        ay = y - th - rng.uniform(10, 30) * s
        out.append(
            f'<path d="M{x + lean:.1f},{y - th + 4:.1f} Q{(x + lean + ax) / 2 + rng.uniform(-8, 8) * s:.1f},'
            f'{y - th - 4 * s:.1f} {ax:.1f},{ay:.1f}" stroke="{trunk}" stroke-width="{2.6 * s:.1f}" '
            f'fill="none" stroke-linecap="round"/>'
        )
    # Krone
    cx, cy = x + lean, y - th - 22 * s
    blobs = []
    for _ in range(int(16 + rng.random() * 8)):
        bx = cx + rng.gauss(0, 34) * s
        by = cy + rng.gauss(0, 13) * s - abs(bx - cx) * 0.08
        rx = rng.uniform(16, 30) * s
        ry = rng.uniform(9, 16) * s
        blobs.append((bx, by, rx, ry))
    for bx, by, rx, ry in blobs:
        out.append(f'<ellipse cx="{bx:.1f}" cy="{by:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{dark}"/>')
    if not silhouette:
        for bx, by, rx, ry in blobs[: len(blobs) // 2]:
            out.append(
                f'<ellipse cx="{bx - rx * .2:.1f}" cy="{by - ry * .35:.1f}" rx="{rx * .62:.1f}" '
                f'ry="{ry * .5:.1f}" fill="{light}" opacity=".75"/>'
            )
    if rim:
        for bx, by, rx, ry in blobs[:6]:
            out.append(
                f'<ellipse cx="{bx + rx * .25:.1f}" cy="{by - ry * .45:.1f}" rx="{rx * .5:.1f}" '
                f'ry="{ry * .28:.1f}" fill="{rim}" opacity=".55"/>'
            )
    return "".join(out)


def cypress(x, y, h, color=C["olive_dark"], w=None):
    w = w or h * 0.16
    return (
        f'<path d="M{x},{y - h} C{x + w * .75},{y - h * .7} {x + w * .6},{y - h * .15} {x + w * .3},{y} '
        f'L{x - w * .3},{y} C{x - w * .6},{y - h * .15} {x - w * .75},{y - h * .7} {x},{y - h} Z" fill="{color}"/>'
    )


def _tower(tx, tw, th, y, H, s, wall, roof):
    o = [f'<rect x="{tx}" y="{y - th}" width="{tw}" height="{th - H + 2}" fill="{wall}"/>',
         f'<polygon points="{tx - 7 * s},{y - th} {tx + tw / 2},{y - th - 22 * s} {tx + tw + 7 * s},{y - th}" fill="{roof}"/>']
    for i in range(3):
        o.append(f'<rect x="{tx + 8 * s + i * 12 * s}" y="{y - th + 10 * s}" width="{5 * s}" height="{7 * s}" fill="{C["olive_dark"]}"/>')
    return o


def villa(x, y, s, wall=C["stone"], shade=C["stone_dark"], roof=C["roof"], lit=True, tower=False):
    """Toskanisches Bauernhaus (auf Wunsch mit Taubenturm; Belvedere hat keinen)."""
    W, H = 190 * s, 74 * s
    tx, tw, th = x + 40 * s, 46 * s, 128 * s
    win = C["honey"] if lit else C["olive_dark"]
    o = []
    # Nebengebäude
    o.append(f'<rect x="{x + W - 10 * s}" y="{y - 48 * s}" width="{70 * s}" height="{48 * s}" fill="{shade}"/>')
    o.append(
        f'<polygon points="{x + W - 16 * s},{y - 48 * s} {x + W + 25 * s},{y - 66 * s} {x + W + 66 * s},{y - 48 * s}" fill="{roof}"/>'
    )
    # Haupthaus
    o.append(f'<rect x="{x}" y="{y - H}" width="{W}" height="{H}" fill="{wall}"/>')
    o.append(f'<rect x="{x + W * .62}" y="{y - H}" width="{W * .38}" height="{H}" fill="{shade}" opacity=".55"/>')
    o.append(
        f'<polygon points="{x - 10 * s},{y - H} {x + W / 2},{y - H - 30 * s} {x + W + 10 * s},{y - H}" fill="{roof}"/>'
    )
    # Turm (nur wenn gewünscht)
    if tower:
        o.extend(_tower(tx, tw, th, y, H, s, wall, roof))
    # Fenster & Loggia
    for i, fx in enumerate((0.1, 0.36, 0.52, 0.78)):
        o.append(
            f'<rect x="{x + W * fx}" y="{y - H + 14 * s}" width="{12 * s}" height="{16 * s}" '
            f'fill="{win if i % 2 == 0 else C["olive_dark"]}" opacity=".9"/>'
        )
    for i in range(3):
        ax = x + W * 0.36 + i * 26 * s
        o.append(
            f'<path d="M{ax},{y} L{ax},{y - 22 * s} A{10 * s},{10 * s} 0 0 1 {ax + 20 * s},{y - 22 * s} L{ax + 20 * s},{y} Z" fill="{C["olive_dark"]}" opacity=".85"/>'
        )
    return "".join(o)


def person(x, y, h, color=C["night"], kind="man", rng=None):
    """Silhouette einer Person (Höhe h, Füße bei y)."""
    s = h / 100
    o = []
    hx, hy = x, y - 90 * s
    o.append(f'<circle cx="{hx}" cy="{hy}" r="{7.5 * s}" fill="{color}"/>')
    if kind in ("man", "farmer", "beater"):
        o.append(
            f'<path d="M{x - 12 * s},{y - 80 * s} Q{x},{y - 86 * s} {x + 12 * s},{y - 80 * s} L{x + 10 * s},{y - 45 * s} '
            f'L{x + 8 * s},{y} L{x + 2 * s},{y} L{x},{y - 40 * s} L{x - 2 * s},{y} L{x - 8 * s},{y} L{x - 10 * s},{y - 45 * s} Z" fill="{color}"/>'
        )
    else:  # Frau mit Rock
        o.append(
            f'<path d="M{x - 10 * s},{y - 80 * s} Q{x},{y - 86 * s} {x + 10 * s},{y - 80 * s} L{x + 9 * s},{y - 52 * s} '
            f'L{x + 17 * s},{y - 4 * s} L{x - 17 * s},{y - 4 * s} L{x - 9 * s},{y - 52 * s} Z" fill="{color}"/>'
            f'<rect x="{x - 6 * s}" y="{y - 5 * s}" width="{3.5 * s}" height="{5 * s}" fill="{color}"/>'
            f'<rect x="{x + 2.5 * s}" y="{y - 5 * s}" width="{3.5 * s}" height="{5 * s}" fill="{color}"/>'
        )
    if kind == "farmer":
        o.append(f'<ellipse cx="{hx}" cy="{hy - 4 * s}" rx="{15 * s}" ry="{3 * s}" fill="{color}"/>')
        o.append(f'<rect x="{hx - 7 * s}" y="{hy - 12 * s}" width="{14 * s}" height="{8 * s}" rx="{3 * s}" fill="{color}"/>')
    if kind == "woman_basket":
        o.append(f'<path d="M{hx - 9 * s},{hy - 3 * s} Q{hx},{hy - 14 * s} {hx + 9 * s},{hy - 3 * s} Z" fill="{color}"/>')
        o.append(f'<ellipse cx="{x + 18 * s}" cy="{y - 50 * s}" rx="{11 * s}" ry="{8 * s}" fill="{color}"/>')
        o.append(f'<path d="M{x + 8 * s},{y - 52 * s} Q{x + 18 * s},{y - 70 * s} {x + 28 * s},{y - 52 * s}" stroke="{color}" stroke-width="{2 * s}" fill="none"/>')
    if kind == "beater":
        o.append(
            f'<line x1="{x + 6 * s}" y1="{y - 70 * s}" x2="{x + 46 * s}" y2="{y - 150 * s}" stroke="{color}" stroke-width="{2.6 * s}" stroke-linecap="round"/>'
        )
    if kind == "woman":
        o.append(f'<ellipse cx="{hx + 4 * s}" cy="{hy + 2 * s}" rx="{6 * s}" ry="{9 * s}" fill="{color}"/>')
    return "".join(o)


def nets(x1, x2, y, color=C["olive_light"], opacity=.55):
    return (
        f'<path d="M{x1},{y} Q{(x1 + x2) / 2},{y + 18} {x2},{y} L{x2 + 20},{y + 26} '
        f'Q{(x1 + x2) / 2},{y + 46} {x1 - 20},{y + 26} Z" fill="{color}" opacity="{opacity}"/>'
    )


# --------------------------------------------------------------------------- #
# Szenen
# --------------------------------------------------------------------------- #
def scene_hero(w=1920, h=1080, seed=3):
    """Panorama: Olivenhain bei Sonnenuntergang, Villa auf dem Hügel."""
    rng = random.Random(seed)
    defs, body = sky(w, h)
    d2, b2 = sun(w * 0.56, h * 0.47, 46)
    defs += d2
    body += b2
    body += clouds(w, h * 0.3, rng, 8)
    body += ridge(w, h, h * 0.6, 40, random.Random(11), C["rose"], 3, .55)
    body += ridge(w, h, h * 0.66, 50, random.Random(12), C["wine"], 3, .55)
    # Mittelgrund mit Villa
    mid_seed, mid_base, mid_amp = 13, h * 0.74, 34
    body += ridge(w, h, mid_base, mid_amp, random.Random(mid_seed), C["plum"], 3, .9)
    vx = w * 0.7
    vy = ridge_y(w, mid_base, mid_amp, mid_seed, 3, vx + 90) + 6
    for cx in (vx - 30, vx + 250, vx + 275, vx + 300):
        body += cypress(cx, ridge_y(w, mid_base, mid_amp, mid_seed, 3, cx) + 4, rng.uniform(80, 120), C["night"])
    body += villa(vx, vy, 1.0, wall="#c98f6a", shade="#8f5a4a", roof="#6e3434")
    for i in range(22):
        tx = rng.uniform(0, w)
        ty = ridge_y(w, mid_base, mid_amp, mid_seed, 3, tx) + rng.uniform(8, 40)
        body += olive_tree(tx, ty, rng.uniform(.25, .4), rng, trunk=C["night"], dark=C["night"],
                           light=C["plum"], silhouette=True)
    # Vordergrund
    body += ridge(w, h, h * 0.9, 22, random.Random(14), C["night"], 3)
    for i in range(7):
        tx = -60 + i * (w + 120) / 6 + rng.uniform(-60, 60)
        body += olive_tree(tx, h * 0.92 + rng.uniform(-10, 30), rng.uniform(1.6, 2.3), rng,
                           trunk="#1d1520", dark="#22191f", light="#3b2b2e", rim=C["amber"], silhouette=False)
    body += person(w * 0.36, h * 0.93, 92, "#140e12", "beater")
    body += person(w * 0.4, h * 0.935, 84, "#140e12", "woman_basket")
    body += nets(w * 0.28, w * 0.46, h * 0.935, C["wine"], .5)
    return svg_doc(w, h, body, defs)


def scene_villa(w=1600, h=1100, seed=5):
    rng = random.Random(seed)
    defs, body = sky(w, h, stops=[(0, C["wine"]), (0.45, C["orange"]), (0.8, C["gold"]), (1, C["honey"])])
    d2, b2 = sun(w * 0.85, h * 0.42, 40)
    defs += d2
    body += b2
    body += clouds(w, h * 0.22, rng, 6, C["honey"], .3)
    body += ridge(w, h, h * 0.58, 30, random.Random(21), C["rose"], 3, .5)
    body += ridge(w, h, h * 0.75, 18, random.Random(22), C["olive"], 2)
    body += cypress(w * 0.2, h * 0.73, 260, C["olive_dark"])
    body += cypress(w * 0.24, h * 0.735, 220, C["olive_dark"])
    body += villa(w * 0.32, h * 0.74, 2.3, wall="#e3bf8c", shade="#b98a5e", roof="#a2482c")
    body += cypress(w * 0.86, h * 0.75, 300, C["olive_dark"])
    body += ridge(w, h, h * 0.86, 14, random.Random(23), C["olive_mid"], 2)
    for i in range(6):
        tx = i * w / 5 + rng.uniform(-50, 50)
        body += olive_tree(tx, h * 0.97 + rng.uniform(-10, 20), rng.uniform(1.5, 2.1), rng,
                           rim=C["gold"])
    body += ridge(w, h, h * 1.0, 12, random.Random(24), C["olive_dark"], 2)
    return svg_doc(w, h, body, defs)


def scene_panorama(w=1600, h=900, seed=8):
    """Blick vom Monte Pisano über die Ebene zum Meer, Pisa in der Ferne."""
    rng = random.Random(seed)
    defs, body = sky(w, h, stops=[(0, C["plum"]), (0.4, C["rose"]), (0.7, C["gold"]), (1, C["honey"])])
    d2, b2 = sun(w * 0.3, h * 0.5, 34)
    defs += d2
    body += b2
    # Meer
    body += f'<rect x="0" y="{h * 0.53}" width="{w}" height="{h * .1}" fill="{C["gold"]}" opacity=".55"/>'
    body += f'<rect x="{w * .22}" y="{h * 0.53}" width="{w * .16}" height="3" fill="#fff3cf" opacity=".8"/>'
    # Ebene
    body += f'<rect x="0" y="{h * 0.58}" width="{w}" height="{h * .42}" fill="{C["rose"]}" opacity=".8"/>'
    # Schiefer Turm + Dom in der Ferne
    px, py = w * 0.55, h * 0.6
    body += f'<g transform="rotate(4 {px} {py})"><rect x="{px}" y="{py - 46}" width="10" height="46" fill="{C["wine"]}" opacity=".8"/></g>'
    body += f'<path d="M{px - 60},{py} L{px - 60},{py - 16} L{px - 36},{py - 22} L{px - 12},{py - 16} L{px - 12},{py} Z" fill="{C["wine"]}" opacity=".7"/>'
    body += f'<ellipse cx="{px - 36}" cy="{py - 22}" rx="9" ry="7" fill="{C["wine"]}" opacity=".7"/>'
    # Hänge des Monte Pisano
    body += ridge(w, h, h * 0.72, 40, random.Random(31), C["olive_mid"], 3)
    body += ridge(w, h, h * 0.84, 30, random.Random(32), C["olive"], 3)
    for i in range(30):
        tx = rng.uniform(0, w)
        body += olive_tree(tx, h * 0.84 + rng.uniform(-10, 50), rng.uniform(.4, .7), rng, rim=C["gold"])
    body += ridge(w, h, h * 0.97, 14, random.Random(33), C["olive_dark"], 2)
    for i in range(4):
        body += olive_tree(i * w / 3 + rng.uniform(-60, 60), h * 1.02, rng.uniform(1.6, 2.0), rng, rim=C["gold"])
    return svg_doc(w, h, body, defs)


def scene_harvest(w=1600, h=1100, seed=9):
    rng = random.Random(seed)
    defs, body = sky(w, h, stops=[(0, "#c9b8a0"), (0.5, C["honey"]), (1, C["cream"])])
    body += ridge(w, h, h * 0.5, 24, random.Random(41), C["silver"], 3, .7)
    body += ridge(w, h, h * 0.62, 18, random.Random(42), C["olive_light"], 2)
    for i in range(8):
        body += olive_tree(rng.uniform(0, w), h * 0.62 + rng.uniform(0, 30), rng.uniform(.8, 1.1), rng)
    body += ridge(w, h, h * 0.8, 10, random.Random(43), C["olive_mid"], 2)
    # Großer Baum mit Netzen
    body += nets(w * 0.22, w * 0.82, h * 0.86, C["terracotta"], .65)
    body += olive_tree(w * 0.5, h * 0.88, 3.2, rng, rim=C["honey"])
    body += person(w * 0.3, h * 0.9, 210, C["olive_dark"], "beater")
    body += person(w * 0.7, h * 0.91, 190, C["olive_dark"], "woman_basket")
    body += person(w * 0.82, h * 0.9, 200, C["olive_dark"], "farmer")
    # Kisten mit Oliven
    for bx in (w * 0.08, w * 0.14):
        body += f'<rect x="{bx}" y="{h * 0.88}" width="70" height="44" fill="{C["terracotta"]}"/>'
        for k in range(8):
            body += f'<circle cx="{bx + 8 + k * 7.5}" cy="{h * 0.88 - 3 + (k % 2) * 3}" r="6" fill="{C["olive_dark"] if k % 3 else C["wine"]}"/>'
    return svg_doc(w, h, body, defs)


def scene_mill(w=1600, h=1100):
    """Alte Ölmühle: Mahlstein im Steinbecken, warmes Licht."""
    defs = rad_grad("glow", [(0, C["honey"], .95), (0.5, C["amber"], .5), (1, C["night"], 0)], .3, .25, .8)
    defs += lin_grad("wallg", [(0, "#5a3a2e"), (1, "#2b1f2e")])
    body = f'<rect width="{w}" height="{h}" fill="url(#wallg)"/>'
    # Steinwand
    rng = random.Random(4)
    for row in range(14):
        y = row * 70
        off = (row % 2) * 60
        for col in range(-1, 15):
            x = col * 120 + off + rng.uniform(-6, 6)
            body += f'<rect x="{x}" y="{y + 3}" width="{112 + rng.uniform(-10, 6)}" height="62" rx="10" fill="#6b4a38" opacity="{rng.uniform(.25, .5):.2f}"/>'
    # Fenster mit Licht
    body += f'<path d="M180,140 L180,420 L420,420 L420,140 A120,120 0 0 0 180,140 Z" fill="{C["gold"]}"/>'
    body += f'<rect width="{w}" height="{h}" fill="url(#glow)"/>'
    # Holzbalken
    body += f'<rect x="0" y="40" width="{w}" height="40" fill="#2b1f2e"/>'
    # Becken
    bx, by = w * 0.55, h * 0.72
    body += f'<ellipse cx="{bx}" cy="{by + 60}" rx="460" ry="120" fill="#3a2a2a"/>'
    body += f'<ellipse cx="{bx}" cy="{by}" rx="460" ry="120" fill="{C["stone_dark"]}"/>'
    body += f'<ellipse cx="{bx}" cy="{by}" rx="400" ry="96" fill="#7a5d40"/>'
    body += f'<ellipse cx="{bx - 30}" cy="{by + 5}" rx="300" ry="60" fill="{C["olive"]}" opacity=".85"/>'
    # Achse + Mühlstein
    body += f'<rect x="{bx - 14}" y="{h * 0.2}" width="28" height="{by - h * 0.2}" fill="#3b2a22"/>'
    body += f'<rect x="{bx - 300}" y="{by - 210}" width="300" height="22" fill="#3b2a22" transform="rotate(-6 {bx} {by - 200})"/>'
    body += f'<ellipse cx="{bx - 190}" cy="{by - 140}" rx="70" ry="160" fill="{C["stone"]}"/>'
    body += f'<rect x="{bx - 190}" y="{by - 300}" width="120" height="320" fill="{C["stone_dark"]}"/>'
    body += f'<ellipse cx="{bx - 70}" cy="{by - 140}" rx="70" ry="160" fill="{C["stone"]}"/>'
    body += f'<ellipse cx="{bx - 70}" cy="{by - 140}" rx="14" ry="30" fill="#3b2a22"/>'
    # Krüge (orci)
    for i, ox in enumerate((w * 0.12, w * 0.2, w * 0.88)):
        s = 1 if i < 2 else 1.2
        oy = h * 0.95
        body += f'<path d="M{ox - 40 * s},{oy - 170 * s} Q{ox - 110 * s},{oy - 90 * s} {ox - 50 * s},{oy} L{ox + 50 * s},{oy} Q{ox + 110 * s},{oy - 90 * s} {ox + 40 * s},{oy - 170 * s} Z" fill="{C["terracotta"]}"/>'
        body += f'<rect x="{ox - 44 * s}" y="{oy - 186 * s}" width="{88 * s}" height="18" rx="6" fill="{C["roof"]}"/>'
        body += f'<path d="M{ox - 30 * s},{oy - 150 * s} Q{ox - 80 * s},{oy - 90 * s} {ox - 40 * s},{oy - 20 * s}" stroke="{C["amber"]}" stroke-width="6" fill="none" opacity=".5"/>'
    body += f'<rect x="0" y="{h * 0.95}" width="{w}" height="{h * .05}" fill="#22181c"/>'
    return svg_doc(w, h, body, defs)


def scene_oil(w=1600, h=1100):
    """Goldgrüner Öltropfen über Oliven und Blättern."""
    defs = rad_grad("bg", [(0, C["honey"], 1), (0.55, C["amber"], 1), (1, C["wine"], 1)], .5, .35, .85)
    defs += lin_grad("drop", [(0, "#e8d36a"), (0.5, "#b9b335"), (1, "#6e7a1c")], 0, 0, 1, 1)
    defs += rad_grad("olive_g", [(0, "#8d9a4a", 1), (1, "#33391c", 1)], .35, .3, .75)
    defs += rad_grad("olive_b", [(0, "#6a4a5a", 1), (1, "#22161e", 1)], .35, .3, .75)
    body = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    rng = random.Random(12)
    # Bokeh
    for _ in range(26):
        body += f'<circle cx="{rng.uniform(0, w):.0f}" cy="{rng.uniform(0, h * .6):.0f}" r="{rng.uniform(20, 70):.0f}" fill="#fff3cf" opacity="{rng.uniform(.06, .22):.2f}"/>'
    # Ausgießstrahl
    body += f'<path d="M{w * .5 - 6},0 C{w * .5 - 4},{h * .2} {w * .5 + 4},{h * .3} {w * .5},{h * .38} L{w * .5 + 8},{h * .38} C{w * .5 + 10},{h * .3} {w * .5 + 8},{h * .2} {w * .5 + 10},0 Z" fill="url(#drop)" opacity=".9"/>'
    # Tropfen
    dx, dy = w * .5 + 4, h * .5
    body += f'<path d="M{dx},{dy - 120} C{dx + 40},{dy - 50} {dx + 80},{dy} {dx + 80},{dy + 50} A80,80 0 0 1 {dx - 80},{dy + 50} C{dx - 80},{dy} {dx - 40},{dy - 50} {dx},{dy - 120} Z" fill="url(#drop)"/>'
    body += f'<ellipse cx="{dx - 30}" cy="{dy + 30}" rx="16" ry="34" fill="#fffbe0" opacity=".55" transform="rotate(20 {dx - 30} {dy + 30})"/>'
    # Blätter
    for i in range(14):
        lx = rng.uniform(0, w)
        ly = h * .78 + rng.uniform(-60, 80)
        ang = rng.uniform(-60, 60)
        L = rng.uniform(140, 220)
        col = rng.choice([C["olive"], C["olive_mid"], C["silver"], C["olive_dark"]])
        body += f'<g transform="rotate({ang:.0f} {lx:.0f} {ly:.0f})"><path d="M{lx},{ly} Q{lx + L / 2},{ly - 26} {lx + L},{ly} Q{lx + L / 2},{ly + 26} {lx},{ly} Z" fill="{col}"/><line x1="{lx}" y1="{ly}" x2="{lx + L}" y2="{ly}" stroke="{C["silver"]}" stroke-width="2" opacity=".5"/></g>'
    # Oliven
    for i in range(16):
        ox = rng.uniform(w * .1, w * .9)
        oy = h * .86 + rng.uniform(-50, 70)
        g = "olive_g" if rng.random() < .65 else "olive_b"
        body += f'<ellipse cx="{ox:.0f}" cy="{oy:.0f}" rx="{rng.uniform(34, 44):.0f}" ry="{rng.uniform(46, 58):.0f}" fill="url(#{g})" transform="rotate({rng.uniform(-50, 50):.0f} {ox:.0f} {oy:.0f})"/>'
        body += f'<ellipse cx="{ox - 10:.0f}" cy="{oy - 16:.0f}" rx="8" ry="12" fill="#fff" opacity=".25"/>'
    return svg_doc(w, h, body, defs)


def scene_branch(w=1600, h=1100):
    """Olivenzweig mit Früchten vor Sonnenuntergang (Bokeh)."""
    defs, body = sky(w, h, stops=[(0, C["wine"]), (0.5, C["orange"]), (1, C["gold"])])
    defs += rad_grad("olive_g", [(0, "#a3ad5a", 1), (1, "#3a411c", 1)], .35, .3, .75)
    defs += rad_grad("olive_b", [(0, "#7a5068", 1), (1, "#24161f", 1)], .35, .3, .75)
    rng = random.Random(21)
    for _ in range(30):
        body += f'<circle cx="{rng.uniform(0, w):.0f}" cy="{rng.uniform(0, h):.0f}" r="{rng.uniform(30, 110):.0f}" fill="#fff0c4" opacity="{rng.uniform(.05, .2):.2f}" filter="url(#blur6)"/>'
    body += f'<path d="M-40,{h * .3} C{w * .3},{h * .38} {w * .6},{h * .5} {w + 40},{h * .7}" stroke="#3b2a22" stroke-width="16" fill="none" stroke-linecap="round"/>'
    for i in range(26):
        t = i / 25
        bx = -40 + (w + 80) * t
        by = h * .3 + (h * .4) * t ** 1.3
        for side in (-1, 1):
            ang = side * rng.uniform(25, 60) + (20 if side > 0 else -20)
            L = rng.uniform(140, 210)
            col = rng.choice([C["olive"], C["olive_mid"], C["olive_dark"]])
            body += (f'<g transform="rotate({ang:.0f} {bx:.0f} {by:.0f})">'
                     f'<path d="M{bx},{by} Q{bx + L / 2},{by - 22} {bx + L},{by} Q{bx + L / 2},{by + 22} {bx},{by} Z" fill="{col}"/>'
                     f'<path d="M{bx},{by} Q{bx + L / 2},{by - 22} {bx + L},{by}" fill="none" stroke="{C["silver"]}" stroke-width="3" opacity=".6"/></g>')
    for i in range(9):
        t = rng.uniform(.1, .9)
        bx = -40 + (w + 80) * t
        by = h * .3 + (h * .4) * t ** 1.3 + rng.uniform(40, 80)
        g = "olive_g" if i % 3 else "olive_b"
        body += f'<line x1="{bx}" y1="{by - 50}" x2="{bx}" y2="{by - 20}" stroke="#3b2a22" stroke-width="4"/>'
        body += f'<ellipse cx="{bx:.0f}" cy="{by:.0f}" rx="30" ry="42" fill="url(#{g})"/>'
        body += f'<ellipse cx="{bx - 9:.0f}" cy="{by - 14:.0f}" rx="7" ry="11" fill="#fff" opacity=".3"/>'
    return svg_doc(w, h, body, defs)


def scene_sharecroppers(w=1600, h=1000, seed=31):
    """Mezzadri-Familie auf dem Hügelkamm, Silhouetten gegen den Abendhimmel."""
    rng = random.Random(seed)
    defs, body = sky(w, h)
    d2, b2 = sun(w * .4, h * .62, 60)
    defs += d2
    body += b2
    body += clouds(w, h * .25, rng, 7)
    body += ridge(w, h, h * .7, 30, random.Random(51), C["wine"], 3, .7)
    body += ridge(w, h, h * .8, 20, random.Random(52), C["night"], 2)
    for i in range(5):
        body += olive_tree(rng.uniform(0, w), h * .8 + rng.uniform(-5, 10), rng.uniform(1.2, 1.7), rng,
                           trunk=C["night"], dark=C["night"], light=C["plum"], rim=C["amber"])
    base = h * .82
    body += person(w * .52, base, 170, C["night"], "farmer")
    body += person(w * .57, base, 158, C["night"], "woman_basket")
    body += person(w * .615, base, 100, C["night"], "man")
    body += person(w * .645, base, 80, C["night"], "woman")
    # Esel
    ex, ey = w * .72, base
    body += (f'<ellipse cx="{ex}" cy="{ey - 70}" rx="60" ry="30" fill="{C["night"]}"/>'
             f'<path d="M{ex + 45},{ey - 85} L{ex + 85},{ey - 120} L{ex + 100},{ey - 105} L{ex + 62},{ey - 70} Z" fill="{C["night"]}"/>'
             f'<path d="M{ex + 84},{ey - 120} l-6,-30 l10,26 Z M{ex + 92},{ey - 118} l2,-30 l4,30 Z" fill="{C["night"]}"/>'
             + "".join(f'<rect x="{ex + dx}" y="{ey - 50}" width="9" height="50" fill="{C["night"]}"/>' for dx in (-48, -30, 30, 44))
             + f'<rect x="{ex - 40}" y="{ey - 112}" width="70" height="30" rx="8" fill="{C["night"]}"/>')
    body += ridge(w, h, h * 1.0, 18, random.Random(53), C["night"], 2)
    body += f'<rect x="0" y="{base - 2}" width="{w}" height="{h - base + 2}" fill="{C["night"]}"/>'
    return svg_doc(w, h, body, defs)


def scene_couple(w=1600, h=1100, seed=61):
    """Platzhalter für das Foto von Ralph & Christina: Paar zwischen Olivenbäumen."""
    rng = random.Random(seed)
    defs, body = sky(w, h, stops=[(0, C["wine"]), (0.4, C["orange"]), (0.75, C["gold"]), (1, C["honey"])])
    d2, b2 = sun(w * .5, h * .58, 52)
    defs += d2
    body += b2
    body += ridge(w, h, h * .66, 26, random.Random(61), C["rose"], 3, .6)
    body += ridge(w, h, h * .78, 16, random.Random(62), C["plum"], 2)
    for i in range(6):
        body += olive_tree(rng.uniform(0, w), h * .78 + rng.uniform(0, 20), rng.uniform(.7, 1), rng,
                           trunk=C["plum"], dark=C["plum"], light=C["wine"], silhouette=True)
    body += f'<rect x="0" y="{h * .86}" width="{w}" height="{h * .14}" fill="{C["night"]}"/>'
    body += olive_tree(w * .14, h * .88, 2.8, rng, trunk="#1d1520", dark="#22191f", light="#3b2b2e", rim=C["amber"])
    body += olive_tree(w * .88, h * .9, 2.6, rng, trunk="#1d1520", dark="#22191f", light="#3b2b2e", rim=C["amber"])
    body += person(w * .47, h * .875, 230, C["night"], "man")
    body += person(w * .53, h * .875, 215, C["night"], "woman")
    # Hände
    body += f'<path d="M{w * .47 + 22},{h * .875 - 120} Q{w * .5},{h * .875 - 105} {w * .53 - 22},{h * .875 - 118}" stroke="{C["night"]}" stroke-width="8" fill="none"/>'
    # Hund
    dx, dy = w * .6, h * .875
    body += (f'<ellipse cx="{dx}" cy="{dy - 30}" rx="34" ry="14" fill="{C["night"]}"/>'
             f'<circle cx="{dx + 34}" cy="{dy - 44}" r="12" fill="{C["night"]}"/>'
             + "".join(f'<rect x="{dx + o}" y="{dy - 22}" width="6" height="22" fill="{C["night"]}"/>' for o in (-26, -14, 14, 24))
             + f'<path d="M{dx - 32},{dy - 34} q-18,-10 -22,-26" stroke="{C["night"]}" stroke-width="6" fill="none"/>')
    return svg_doc(w, h, body, defs)


# ---------------------------- Porträts ------------------------------------- #
def portrait(w, h, bg_stops, skin, garments, hair_svg, seed, extra=""):
    rng = random.Random(seed)
    defs = lin_grad("pbg", bg_stops)
    body = f'<rect width="{w}" height="{h}" fill="url(#pbg)"/>'
    # Unscharfe Olivenblätter im Hintergrund
    for _ in range(24):
        lx, ly = rng.uniform(0, w), rng.uniform(0, h * .7)
        L = rng.uniform(80, 160)
        body += (f'<g transform="rotate({rng.uniform(-80, 80):.0f} {lx:.0f} {ly:.0f})" filter="url(#blur6)" opacity="{rng.uniform(.25, .5):.2f}">'
                 f'<path d="M{lx},{ly} Q{lx + L / 2},{ly - 16} {lx + L},{ly} Q{lx + L / 2},{ly + 16} {lx},{ly} Z" fill="{rng.choice([C["olive"], C["olive_dark"], C["olive_mid"]])}"/></g>')
    body += f'<circle cx="{w * .72}" cy="{h * .3}" r="{w * .35}" fill="{C["honey"]}" opacity=".35" filter="url(#soft)"/>'
    cx = w / 2
    # Hals
    body += f'<path d="M{cx - 48},{h * .5} L{cx - 52},{h * .66} L{cx + 52},{h * .66} L{cx + 48},{h * .5} Z" fill="{skin[1]}"/>'
    # Kleidung (Schultern)
    body += garments
    # Kopf
    body += f'<ellipse cx="{cx}" cy="{h * .4}" rx="{w * .16}" ry="{h * .155}" fill="{skin[0]}"/>'
    body += f'<path d="M{cx + w * .03},{h * .3} C{cx + w * .17},{h * .32} {cx + w * .17},{h * .5} {cx + w * .02},{h * .555} C{cx + w * .14},{h * .48} {cx + w * .13},{h * .36} {cx + w * .03},{h * .3} Z" fill="{skin[1]}" opacity=".7"/>'
    # Ohr
    body += f'<ellipse cx="{cx - w * .158}" cy="{h * .41}" rx="{w * .022}" ry="{h * .032}" fill="{skin[1]}"/>'
    # Warmes Seitenlicht
    body += f'<path d="M{cx - w * .14},{h * .33} C{cx - w * .17},{h * .4} {cx - w * .15},{h * .48} {cx - w * .1},{h * .53}" stroke="{C["honey"]}" stroke-width="7" fill="none" opacity=".5" stroke-linecap="round"/>'
    body += hair_svg
    body += extra
    return svg_doc(w, h, body, defs)


def portraits():
    w, h = 900, 1100
    cx = w / 2
    res = {}

    def shoulders(color, collar=None, accent=None):
        s = f'<path d="M{cx - 330},{h} C{cx - 320},{h * .72} {cx - 200},{h * .64} {cx},{h * .63} C{cx + 200},{h * .64} {cx + 320},{h * .72} {cx + 330},{h} Z" fill="{color}"/>'
        if collar:
            s += collar
        if accent:
            s += accent
        return s

    # 1) Il Conte (1536) – Renaissance-Barett, roter Mantel, Pelzkragen
    fur = f'<path d="M{cx - 260},{h * .76} C{cx - 160},{h * .64} {cx - 60},{h * .7} {cx},{h * .78} C{cx + 60},{h * .7} {cx + 160},{h * .64} {cx + 260},{h * .76} L{cx + 290},{h * .86} C{cx + 150},{h * .74} {cx + 60},{h * .8} {cx},{h * .9} C{cx - 60},{h * .8} {cx - 150},{h * .74} {cx - 290},{h * .86} Z" fill="#6b4a3a"/>'
    chain = f'<path d="M{cx - 120},{h * .8} Q{cx},{h * .98} {cx + 120},{h * .8}" stroke="{C["gold"]}" stroke-width="9" fill="none" stroke-dasharray="14 6"/>'
    hair = (f'<path d="M{cx - w * .16},{h * .4} C{cx - w * .18},{h * .5} {cx - w * .12},{h * .55} {cx - w * .1},{h * .56} L{cx - w * .13},{h * .4} Z" fill="#3a2a22"/>'
            f'<path d="M{cx - w * .1},{h * .5} C{cx - w * .06},{h * .6} {cx + w * .08},{h * .6} {cx + w * .11},{h * .5} C{cx + w * .06},{h * .56} {cx - w * .05},{h * .56} {cx - w * .1},{h * .5} Z" fill="#3a2a22"/>'
            f'<ellipse cx="{cx}" cy="{h * .27}" rx="{w * .25}" ry="{h * .06}" fill="#1f1418" transform="rotate(-6 {cx} {h * .27})"/>'
            f'<ellipse cx="{cx + 10}" cy="{h * .24}" rx="{w * .17}" ry="{h * .06}" fill="#1f1418"/>')
    res["ritratto-conte"] = portrait(w, h, [(0, C["wine"]), (0.6, C["terracotta"]), (1, C["amber"])],
                                     ("#e0b48f", "#c08e6c"), shoulders("#8e2a2a", fur, chain), hair, 1)

    # 2) La Mezzadra – Kopftuch, Leinenbluse, Korb mit Oliven
    scarf = (f'<path d="M{cx - w * .19},{h * .44} C{cx - w * .22},{h * .2} {cx + w * .22},{h * .2} {cx + w * .19},{h * .44} '
             f'L{cx + w * .15},{h * .36} C{cx + w * .1},{h * .28} {cx - w * .1},{h * .28} {cx - w * .15},{h * .36} Z" fill="#b5603a"/>'
             f'<path d="M{cx - w * .19},{h * .44} L{cx - w * .24},{h * .58} L{cx - w * .12},{h * .5} Z" fill="#9c4a2f"/>')
    blouse = shoulders("#efe2c8",
                       f'<path d="M{cx - 70},{h * .64} L{cx},{h * .74} L{cx + 70},{h * .64}" stroke="#cdb898" stroke-width="10" fill="none"/>',
                       f'<path d="M{cx - 330},{h} C{cx - 300},{h * .86} {cx - 200},{h * .82} {cx - 120},{h * .84} L{cx - 90},{h} Z" fill="#6f7744"/>')
    basket = (f'<ellipse cx="{cx + 250}" cy="{h * .93}" rx="150" ry="60" fill="#8a6440"/>'
              + "".join(f'<circle cx="{cx + 150 + i * 22}" cy="{h * .9 - (i % 2) * 8}" r="14" fill="{C["olive_dark"] if i % 3 else C["plum"]}"/>' for i in range(10)))
    res["ritratto-mezzadra"] = portrait(w, h, [(0, C["rose"]), (0.6, C["gold"]), (1, C["honey"])],
                                        ("#d9a27c", "#b8805e"), blouse, scarf, 2, basket)

    # 3) Il Frantoiano – Schiebermütze, Schnurrbart, Schürze
    cap = (f'<path d="M{cx - w * .17},{h * .33} C{cx - w * .15},{h * .2} {cx + w * .17},{h * .2} {cx + w * .18},{h * .33} Z" fill="#4a4a3a"/>'
           f'<path d="M{cx + w * .05},{h * .32} L{cx + w * .27},{h * .345} L{cx + w * .17},{h * .3} Z" fill="#3b3b2e"/>'
           f'<path d="M{cx - w * .07},{h * .47} Q{cx},{h * .44} {cx + w * .08},{h * .47} Q{cx},{h * .495} {cx - w * .07},{h * .47} Z" fill="#d8d0c0"/>'
           f'<path d="M{cx - w * .16},{h * .36} L{cx - w * .16},{h * .43} L{cx - w * .13},{h * .36} Z" fill="#d8d0c0"/>')
    apron = shoulders("#5b6b7a",
                      f'<path d="M{cx - 150},{h} L{cx - 120},{h * .72} L{cx + 120},{h * .72} L{cx + 150},{h} Z" fill="#c9b796"/>',
                      f'<line x1="{cx - 120}" y1="{h * .72}" x2="{cx - 70}" y2="{h * .64}" stroke="#c9b796" stroke-width="10"/><line x1="{cx + 120}" y1="{h * .72}" x2="{cx + 70}" y2="{h * .64}" stroke="#c9b796" stroke-width="10"/>')
    res["ritratto-frantoiano"] = portrait(w, h, [(0, "#3b2a22"), (0.5, "#7a4a2e"), (1, C["amber"])],
                                          ("#c99068", "#a5704e"), apron, cap, 3)

    # 4) La Raccoglitrice – heute, Strohhut, Arbeitshemd, Olivenzweig
    hat = (f'<ellipse cx="{cx}" cy="{h * .29}" rx="{w * .32}" ry="{h * .05}" fill="#e2c27a"/>'
           f'<path d="M{cx - w * .15},{h * .29} C{cx - w * .14},{h * .16} {cx + w * .14},{h * .16} {cx + w * .15},{h * .29} Z" fill="#d7b468"/>'
           f'<rect x="{cx - w * .15}" y="{h * .255}" width="{w * .3}" height="{h * .025}" fill="{C["olive"]}"/>'
           f'<path d="M{cx + w * .13},{h * .33} C{cx + w * .2},{h * .45} {cx + w * .18},{h * .6} {cx + w * .26},{h * .66} C{cx + w * .13},{h * .64} {cx + w * .1},{h * .5} {cx + w * .1},{h * .35} Z" fill="#6b4a2e"/>')
    shirt = shoulders("#7c8a5a",
                      f'<path d="M{cx - 60},{h * .635} L{cx},{h * .72} L{cx + 60},{h * .635} L{cx + 40},{h * .7} L{cx},{h * .78} L{cx - 40},{h * .7} Z" fill="#6a774a"/>')
    twig = (f'<path d="M{cx - 300},{h * .98} Q{cx - 220},{h * .8} {cx - 120},{h * .74}" stroke="#3b2a22" stroke-width="6" fill="none"/>'
            + "".join(f'<ellipse cx="{cx - 300 + i * 40}" cy="{h * .95 - i * 44}" rx="36" ry="10" fill="{C["olive"]}" transform="rotate({-50 + i * 8} {cx - 300 + i * 40} {h * .95 - i * 44})"/>' for i in range(5))
            + f'<ellipse cx="{cx - 210}" cy="{h * .86}" rx="13" ry="17" fill="{C["olive_dark"]}"/>')
    res["ritratto-raccoglitrice"] = portrait(w, h, [(0, C["plum"]), (0.55, C["orange"]), (1, C["gold"])],
                                             ("#e8bf9c", "#c8987a"), shirt, hat, 4, twig)
    return res


def favicon():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
            '<rect width="64" height="64" rx="14" fill="#4a2c3f"/>'
            '<circle cx="40" cy="22" r="9" fill="#f2c46d"/>'
            '<path d="M10 50 C24 40 36 34 54 30" stroke="#f8efdf" stroke-width="3" fill="none" stroke-linecap="round"/>'
            '<path d="M22 43 q6 -12 16 -10 q-6 10 -16 10z" fill="#9aa36d"/>'
            '<path d="M34 37 q10 -2 14 6 q-10 2 -14 -6z" fill="#9aa36d"/>'
            '<ellipse cx="28" cy="52" rx="5" ry="6.5" fill="#d9822b"/>'
            "</svg>")


def og_image():
    """Social-Media-Vorschaubild 1200x630 (wird separat mit Text gerendert)."""
    hero = scene_hero(1200, 630, seed=3)
    text = ('<rect x="0" y="0" width="1200" height="630" fill="#2b1f2e" opacity=".25"/>'
            '<text x="80" y="250" font-family="Cormorant Garamond, Georgia, serif" font-size="96" fill="#f8efdf" font-weight="600">Villa Belvedere</text>'
            '<text x="84" y="320" font-family="Cormorant Garamond, Georgia, serif" font-style="italic" font-size="40" fill="#f7dc9c">Olio extravergine del Monte Pisano · dal 1536</text>')
    return hero.replace('<rect width="1200" height="630" filter="url(#grain)"', text + '<rect width="1200" height="630" filter="url(#grain)"')


SCENES = {
    "hero-oliveto-tramonto": scene_hero,
    "villa-belvedere": scene_villa,
    "monte-pisano-panorama": scene_panorama,
    "raccolta-olive": scene_harvest,
    "frantoio-antico": scene_mill,
    "olio-goccia": scene_oil,
    "ramo-olivo": scene_branch,
    "mezzadri-tramonto": scene_sharecroppers,
    "olivicoltori-ralph-christina": scene_couple,
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, fn in SCENES.items():
        with open(os.path.join(OUT, name + ".svg"), "w") as f:
            f.write(fn())
    for name, svg in portraits().items():
        with open(os.path.join(OUT, name + ".svg"), "w") as f:
            f.write(svg)
    with open(os.path.join(OUT, "og-villa-belvedere.svg"), "w") as f:
        f.write(og_image())
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(root, "favicon.svg"), "w") as f:
        f.write(favicon())
    print("SVGs geschrieben nach", OUT)


if __name__ == "__main__":
    main()
