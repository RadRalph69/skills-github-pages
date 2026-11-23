# Bild-Prompts für KI-Bilder (Villa Belvedere)

Die Website enthält zurzeit **stilisierte Platzhalter-Illustrationen** (erzeugt mit `_src/images.py`).
Mit den folgenden Prompts können Sie in einem KI-Bildgenerator (z. B. Midjourney, DALL·E, Firefly,
Imagen) passende Bilder erzeugen. Die Dateinamen in der Tabelle entsprechen den Bildern auf der Website.

**Gemeinsamer Stil (an jeden Prompt anhängen):**
> golden hour, warm sunset light over Tuscan olive grove, palette of plum, wine red, terracotta, amber,
> honey gold and silvery olive green, soft film grain, natural, atmospheric, editorial photography,
> no text, no logos

| Datei (Name) | Format | Prompt |
|---|---|---|
| `hero-oliveto-tramonto` | 16:9, ≥1920 px | Wide panorama of terraced olive grove on the slopes of Monte Pisano at sunset, an old Tuscan stone farmhouse with a square dovecote tower on the hill, cypresses, two harvesters with long poles and nets under ancient twisted olive trees in backlight |
| `villa-belvedere` | 3:2 | Old Tuscan stone farmhouse (casa colonica) with dovecote tower and terracotta roof, arched loggia, cypresses, olive terraces in front, evening light |
| `monte-pisano-panorama` | 16:9 | View from Monte Pisano olive terraces over the plain of Pisa towards the sea at sunset, the leaning tower small in the far distance, haze |
| `frantoio-antico` | 3:2 | Interior of a 16th-century olive mill, large granite millstone in a stone basin, terracotta oil jars (orci), warm light from a small arched window, dust in the air |
| `olio-goccia` | 3:2 | Macro photo of a green-gold drop of fresh extra virgin olive oil falling onto green and dark olives with olive leaves, bokeh, warm backlight (keine Flasche, kein Etikett, kein Preis) |
| `ramo-olivo` | 3:2 | Close-up of an olive branch with silvery leaves and green and purple olives, sunset bokeh background |
| `raccolta-olive` | 3:2 | Olive harvest in Tuscany: people with poles and hand rakes, orange nets spread under a large old olive tree, crates of olives, soft late-morning light |
| `mezzadri-tramonto` | 16:10 | Silhouettes of a Renaissance-era Tuscan sharecropper family (man with hat, woman with basket, two children) and a donkey with baskets on a hill ridge at sunset among olive trees, painterly, historical |
| `ritratto-conte` | 9:11 Porträt | Painterly portrait of a fictional 16th-century Pisan count, black Renaissance beret, dark red velvet robe with fur collar, gold chain, olive leaves in background, in the style of a Renaissance oil portrait |
| `ritratto-mezzadra` | 9:11 | Painterly portrait of a fictional 18th-century Tuscan peasant woman, red headscarf, linen blouse, holding a basket of olives, warm evening light |
| `ritratto-frantoiano` | 9:11 | Portrait of a fictional elderly Tuscan olive miller around 1900, flat cap, white moustache, canvas apron, inside a stone mill, warm light |
| `ritratto-raccoglitrice` | 9:11 | Portrait of a fictional young woman harvesting olives today, straw hat, olive-green work shirt, holding an olive branch, sunset |
| `olivicoltori-ralph-christina` | 3:2 | **Hier bitte ein echtes Foto von Ralph und Christina verwenden** (kein KI-Bild realer Personen). |

## Bilder austauschen

1. Neues Bild (JPG/PNG, mindestens so groß wie oben angegeben) als
   `_src/png/<name>.jpg` (oder `.png`) speichern – z. B. `_src/png/villa-belvedere.jpg`.
   Die alte Platzhalterdatei gleichen Namens (`.png`) dabei löschen.
2. `python3 _src/optimize.py` ausführen → erzeugt WebP-Größen und JPG in `assets/img/`.
3. `python3 _src/build.py` ausführen (aktualisiert Breiten-/Höhenangaben in den Seiten).

Achtung: `images.py` + `rasterize.js` würden die Platzhalter neu rendern und eigene Bilder in
`_src/png/` überschreiben – danach also nur noch `optimize.py` und `build.py` verwenden.

## Rechtlicher Hinweis zu KI-Bildern

- KI-Bilder von **fiktiven** Personen sind auf der Website als „fiktive Figuren / digital erstellt“
  gekennzeichnet (Bildunterschrift auf der Startseite und Bildnachweis im Impressum). Das entspricht den
  Transparenzpflichten der EU-KI-Verordnung (Art. 50 AI Act) für realistisch wirkende KI-Inhalte.
- Keine KI-Bilder von **realen** Personen, Marken oder fremden Etiketten erzeugen.
- Nutzungsbedingungen des jeweiligen KI-Dienstes zur kommerziellen Nutzung prüfen.
