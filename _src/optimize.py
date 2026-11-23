#!/usr/bin/env python3
"""PNG (aus rasterize.js) -> responsive WebP-Varianten + JPG-Fallback in assets/img/."""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "png")
DST = os.path.join(HERE, "..", "assets", "img")
os.makedirs(DST, exist_ok=True)

for f in sorted(os.listdir(SRC)):
    name, ext = os.path.splitext(f)
    if ext.lower() not in (".png", ".jpg", ".jpeg"):
        continue
    im = Image.open(os.path.join(SRC, f)).convert("RGB")
    if name.startswith("og-"):
        im.save(os.path.join(DST, name + ".jpg"), "JPEG", quality=84, optimize=True, progressive=True)
        continue
    widths = [480, 900] if name.startswith("ritratto-") else [640, 1280, 1920]
    for w in widths:
        if w > im.width:
            w = im.width
        h = round(im.height * w / im.width)
        im.resize((w, h), Image.LANCZOS).save(os.path.join(DST, f"{name}-{w}.webp"), "WEBP", quality=78, method=6)
    # JPG-Fallback (mittlere Größe)
    w = widths[1] if len(widths) > 1 else widths[0]
    h = round(im.height * w / im.width)
    im.resize((w, h), Image.LANCZOS).save(os.path.join(DST, f"{name}-{w}.jpg"), "JPEG", quality=80, optimize=True, progressive=True)
    print(name, im.size)
