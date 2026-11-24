"""English texts. All texts are drafts and can be edited freely."""
from config import LEGAL as L, LEGAL_DATE, FORM_PROVIDER as FP
from lib import (photo, credits_list, fig, ph, link, section, split, h2, cards, portraits, facts, timeline, band,
                 table, note, calendar, btn, contact_form)

UI = {
    "skip": "Skip to content",
    "menu": "Menu",
    "nav_label": "Main navigation",
    "lang_label": "Language",
    "breadcrumb": "Breadcrumb",
    "nav": {"home": "Home", "conte": "The Count’s Oil", "energia": "Oil, Energy of Life",
            "olivicoltori": "The Olive Growers", "contatti": "Contact", "legal": "Legal notice",
            "privacy": "Privacy policy", "sitemap": "Site map"},
    "footer_claim": "Organic extra virgin olive oil from the groves of Monte Pisano, where the mezzadri planted olive trees from 1735. From harvest to bottle, everything on our estate.",
    "vat": "VAT no. (P. IVA)",
    "footer_nav": "Pages",
    "footer_legal": "Legal",
    "info_only": "This website is for information purposes only. No products are sold and no contracts are "
                 "concluded through this website.",
    "images_note": "Illustrations: digitally created placeholder images",
    "og_alt": "Olive grove of Villa Belvedere on Monte Pisano at sunset",
    "nf_title": "Page not found",
    "nf_text": "The page you are looking for does not exist or has been moved.",
    "nf_link": "Back to the home page",
}

MORE = "Read more"

HOME = (
    section(split(
        h2("One farm, five centuries, one oil", "intro", "Welcome to Villa Belvedere")
        + "<p>On the slopes of Monte Pisano, between Pisa and Lucca, stands Villa Belvedere: an old Tuscan farmhouse "
          "with a dovecote tower, surrounded by olive terraces that look out over the plain and, on clear days, all "
          "the way to the sea.</p>"
          "<p>From 1536 the house was part of the estates of the Counts Agostini Fantini Venerosi della Seta. Around 1735 "
          "the sharecroppers – the <em>mezzadri</em> – began clearing the forest and planting olive trees, each one "
          "protected by a crescent-shaped stone wall, the “lunetta”. Some of those trees are now around 300 years old.</p>"
          "<p>Today we farm the grove organically and press in our own olive mill: from harvest to bottle, everything "
          "happens here, with the same respect for the hill.</p>"
          f"<p>{link('conte', 'Read the story of the Villa →')}</p>",
        fig("villa-belvedere", "The Villa Belvedere farmhouse with its dovecote tower between cypresses and olive trees in the evening light",
            "The farmhouse and its dovecote tower")),
        "section--cream", label="intro")
    + '<section class="facts-band" aria-label="Villa Belvedere in numbers"><div class="wrap">'
    + facts([("1536", "year the farm was founded"), ("2,320 olive trees", "on dry-stone terraces"),
             ("135 m", "above sea level on Monte Pisano"), ("Organic", "certified organic farming")])
    + "</div></section>"
    + section(
        h2("Three stories, one oil", "storie")
        + cards([
            ("conte", "frantoio-antico", "The old millstone in the Count’s olive mill", "The Count’s Oil",
             "Almost five hundred years of history: the Counts della Seta, the mezzadri, the lunette and the Villa’s rebirth."),
            ("energia", "olio-goccia", "A green-gold drop of oil above olives and leaves", "Oil, Energy of Life",
             "What makes an organic, polyphenol-rich extra virgin olive oil special – explained simply."),
            ("olivicoltori", "olivicoltori-ralph-christina", "Two people among olive trees at sunset", "The Olive Growers",
             "Ralph and Christina Striewski: at Belvedere since 2024, with their hands in the soil and their eyes on the trees."),
        ], MORE), label="storie")
    + section(
        h2("Voices of the hill", "voci", "Who lived on this hill")
        + '<p class="section-intro">For five centuries Monte Pisano was home to counts and farmers, millers and '
          "harvesters. We have imagined their faces and their voices.</p>"
        + portraits([
            ("ritratto-conte", "Illustrated portrait of a Renaissance nobleman with a black beret and red cloak",
             "The Count", "1536 – the landowner",
             "“I wanted this house to look out over the valley – that is why it is called Belvedere.”"),
            ("ritratto-mezzadra", "Illustrated portrait of a peasant woman with a red headscarf and a basket of olives",
             "The sharecropper", "1735 – the farm family",
             "“We won this hill from the forest, stone by stone, lunetta by lunetta.”"),
            ("ritratto-frantoiano", "Illustrated portrait of an elderly miller with a cap and apron",
             "The miller", "1900 – master of the mill",
             "“You feel good oil in your throat: if it tickles, it’s alive.”"),
            ("ritratto-raccoglitrice", "Illustrated portrait of a young harvester with a straw hat",
             "The harvester", "today – the harvest",
             "“In October the hill fills with voices, nets and laughter.”"),
        ])
        + '<p class="fineprint">Fictional characters. Digitally created illustrations for evocative purposes.</p>',
        "section--dark", label="voci")
    + band("monte-pisano-panorama", "View from Monte Pisano over the plain of Pisa and the sea at sunset",
           "From up here you see the plain that was once marshland, the tower of Pisa – and, in the evening, the sea turning to gold.",
           "Villa Belvedere, Monte Pisano")
    + section(
        '<div class="cta-box">' + h2("Get to know us", "visita")
        + "<p>Do you have questions about our oil, the history of the Villa or life in the olive grove? Write to us – "
          "we are happy to answer.</p>" + btn("contatti", "Write to us") + "</div>",
        "section--cream", label="visita")
)

CONTE = (
    section(split(
        h2("A farmhouse in the hills of Pisa", "origini", "The beginnings")
        + "<p>In 1536 the plain of Pisa was still largely marshland and, in some seasons, under water. To settle the "
          "hills of Monte Pisano, poor labouring families were called in: they received a house and a plot of land in "
          "exchange for their work and a share of the harvest.</p>"
          "<p>That is how Belvedere came to be: a stone farmhouse with a stable, a threshing floor and the typical "
          "dovecote tower, built where the view opens onto the valley – hence its name, “beautiful view”. The farm was "
          "part of the estates of the Counts Agostini Fantini Venerosi della Seta, a noble family of Pisa. At that time "
          "the hill was still covered in forest.</p>",
        fig("monte-pisano-panorama", "Panorama from Monte Pisano over the plain of Pisa to the sea", "The plain of Pisa seen from Monte Pisano")),
        label="origini")
    + section(
        h2("Five centuries at a glance", "cronologia", "Timeline")
        + timeline([
            ("1536", "The settlement", "Sharecropping families settle on the slopes of Monte Pisano. The Belvedere farmhouse is built as part of the estates of the Counts Agostini Fantini Venerosi della Seta."),
            ("c. 1735", "From forest to olive grove", "The mezzadri begin clearing the forest and planting olive trees, most of them supported by small crescent-shaped dry-stone walls, the “lunette”. Some of those trees still grow today."),
            ("18th–20th c.", "The age of sharecropping", "The harvest is split in half between landowner and farming family. Up to three generations live in the house, knowing every tree by name."),
            ("1964", "The end of an era", "The lands of Count Agostini Fantini Venerosi della Seta pass to a Sardinian building contractor – except for Villa di Corliano at the foot of Monte Pisano, directly below Belvedere. The mezzadri leave the Villa."),
            ("1964 – 1987", "Uncertain years", "Years of unclear ownership follow, during which the olive grove is no longer tended as it once was."),
            ("1987", "Rebirth", "Munich entrepreneur Rolf Freitag buys the Villa and renovates it completely over several years. The olive grove, too, is turned back into a productive grove."),
            ("2024", "A new chapter", "Ralph and Christina Striewski buy the Villa and the olive grove, together with the Azienda Agricola Villa Belvedere di Corliano, its organic certification and its own olive mill."),
        ]),
        "section--cream", label="cronologia")
    + section(split(
        h2("The lunette: olive trees won from the forest", "lunette")
        + "<p>Around 1735 the mezzadri began to transform the hill. They cleared the forest by hand, pulled the stones "
          "from the soil and used those very stones to build a small crescent-shaped wall around each young olive tree: "
          "the <em>lunetta</em> (half-moon). It holds soil and rainwater on the steep slope and protects the roots.</p>"
          "<p>Most of our olive trees still stand inside their lunetta today. Some are around 300 years old: those "
          "sharecroppers planted them, thinking of their grandchildren.</p>"
          "<p>The day followed the sun. Trees were pruned in spring, the soil hoed in summer, and in autumn the harvest "
          "came – long poles beating the branches above cloths spread on the ground. The women looked after the garden, "
          "the animals and the house; the children gathered fallen olives, one by one. Half the harvest belonged to the "
          "Count.</p>",
        fig("mezzadri-tramonto", "Silhouette of a farming family with a donkey on the ridge at sunset", "A sharecropping family heading home")),
        "section--dark", label="lunette")
    + section(split(
        h2("From the Count’s mill to our own mill", "frantoio")
        + "<p>For centuries Belvedere’s olives went down to the valley in baskets, to the Count’s mill at Corliano: a large stone "
          "room where a granite millstone crushed the fruit into a paste that was then pressed on mats. The oil rested "
          "in terracotta jars; part of it went to the Count, the rest stayed with the farm family – all year round it "
          "was food, medicine and light.</p>"
          "<p>In 1964 sharecropping ended and the mezzadri left the Villa. After years of unclear ownership, Rolf "
          "Freitag bought the estate in 1987, restored it carefully and brought the olive grove back into production. "
          "In 2024 we took over from him not only the Villa and the grove, but also the Azienda Agricola Villa Belvedere "
          "di Corliano, with its organic certification and <strong>its own olive mill</strong>.</p>"
          "<p>That is why today the whole process – from harvest to bottle – takes place right here on our estate.</p>"
          f"<p>{link('olivicoltori', 'Who looks after the trees today →')}</p>",
        photo("corliano-frantoio-1901", "Historic photograph of the Corliano olive mill in 1901", "The Corliano olive mill in 1901 – open to visitors today"),
        rev=True), label="frantoio")
    + section(split(
        h2("Villa di Corliano", "corliano", "At the foot of Monte Pisano")
        + "<p>Directly below Belvedere, at the foot of Monte Pisano, stands Villa di Corliano, seat of the Counts "
          "Agostini Fantini Venerosi della Seta. In 1964 it was the only part of their estates that did not pass to "
          "the Sardinian building contractor.</p>"
          "<p>The villa also includes the Count’s old olive mill, where the olives of the hill – Belvedere’s among "
          "them – were pressed for centuries. It can still be visited today.</p>",
        photo("corliano-facciata", "Façade of Villa di Corliano at the foot of Monte Pisano", "Villa di Corliano")),
        "section--cream", label="corliano")
    + band("ramo-olivo", "Olive branch with green and dark olives against the light",
           "An olive tree does not belong to the one who plants it, but to those who come after.", "Tuscan farmers’ saying")
)

ENERGIA = (
    section(split(
        h2("What is extra virgin olive oil?", "evo", "The basics")
        + "<p>Extra virgin olive oil is the juice of the olive, obtained <strong>solely by mechanical means</strong>: "
          "the olives are washed, crushed, malaxed and separated – without solvents and without refining. It is the "
          "highest grade defined by EU law.</p>"
          "<p>To be called “extra virgin”, an oil must meet precise chemical limits and pass the judgement of a "
          "tasting panel: it needs a perceptible fruitiness and <strong>no defects at all</strong>.</p>",
        fig("olio-goccia", "Green-gold drop of extra virgin olive oil above olives and leaves", "The green-gold colour of freshly pressed oil")),
        label="evo")
    + section(
        h2("The legal parameters", "parametri")
        + table("Limits for the extra virgin category (Delegated Regulation (EU) 2022/2104) and values of our oil",
                ["Parameter", "Extra virgin limit", "Our oil 2026"],
                [["Free acidity (oleic acid)", "≤ 0.80 %", "0.35 %"],
                 ["Peroxide value", "≤ 20 mEq O₂/kg", "7.6 mEq O₂/kg"],
                 ["K232", "≤ 2.50", "<span class=\"pending\">to follow</span>"],
                 ["K270", "≤ 0.22", "<span class=\"pending\">to follow</span>"],
                 ["Median of defects", "= 0", "<span class=\"pending\">to follow</span>"],
                 ["Median of fruitiness", "> 0", "<span class=\"pending\">to follow</span>"],
                 ["Total polyphenols", "no legal limit", "<strong>378 mg/kg</strong>"]],
                "Test report no. 2026-7563 of 23 October 2026, Enolab Service S.r.l., Capannoli (PI); sample from the harvest of 3 October 2026. Total polyphenols expressed as gallic acid. The missing values will follow with the next analyses."),
        "section--cream", label="parametri")
    + section(split(
        h2("Polyphenols: the strength of the oil", "polifenoli", "The heart of quality")
        + "<p>Polyphenols are natural substances the olive tree produces to protect its fruit. Extra virgin olive oil "
          "contains dozens of them; the best known are <strong>hydroxytyrosol</strong>, <strong>tyrosol</strong>, "
          "<strong>oleuropein</strong> (in its derived forms), <strong>oleocanthal</strong> and <strong>oleacein</strong>.</p>"
          "<p>They give the oil its <strong>bitter</strong> and <strong>pungent</strong> notes: the peppery tickle in the "
          "throat after tasting is mainly due to oleocanthal. A polyphenol-rich oil is also more stable – it oxidises "
          "more slowly and keeps its aromas for longer.</p>"
          "<p>The amount depends on the variety, ripeness, climate and above all on processing. That is why we harvest "
          "early and process the olives within a few hours in our own mill, just steps from the grove.</p>",
        fig("ramo-olivo", "Olive branch with green and turning olives", "Olives as they turn colour: the moment of polyphenols"),
        rev=True), label="polifenoli")
    + section(
        h2("What science says – and what the law allows", "claim")
        + note("<p><strong>Authorised health claim (Regulation (EU) No 432/2012):</strong> “Olive oil polyphenols "
               "contribute to the protection of blood lipids from oxidative stress.” The beneficial effect is obtained "
               "with a daily intake of 20 g of olive oil.</p>"
               "<p>The claim may only be used for olive oil containing <strong>at least 5 mg of hydroxytyrosol and its "
               "derivatives per 20 g</strong> of oil (equivalent to 250 mg/kg). "
               f"Our oil contains 378 mg/kg of total polyphenols. What counts for this claim, however, is the content of hydroxytyrosol and its derivatives, which requires a specific analysis. It is under way – until the result is available, we do not apply this claim to our oil.</p>",
               "note note--claim")
        + "<p>Extra virgin olive oil is a cornerstone of the Mediterranean diet. It consists mostly of <strong>oleic "
          "acid</strong>, a monounsaturated fatty acid, and naturally contains <strong>vitamin E</strong> (tocopherols), "
          "<strong>squalene</strong> and <strong>pigments</strong> such as chlorophylls and carotenoids.</p>"
          + '<p class="fineprint">The information on this page is general in nature and does not replace advice from a '
            "doctor or nutritionist. A varied, balanced diet and a healthy lifestyle are important.</p>",
        "section--cream", label="claim")
    + section(split(
        h2("Organic, from tree to oil", "bio", "How we work")
        + "<ul class='ticks'>"
          "<li><strong>Organic farming</strong> under Regulation (EU) 2018/848: no chemical herbicides, no synthetic "
          "fertilisers; ground cover, green manure and careful pruning.</li>"
          f"<li><strong>Control body:</strong> {L['bio_body']} – code {L['bio_code']}, origin: {L['bio_origin']}.</li>"
          "<li><strong>Early harvest</strong> between October and early November, as the olives begin to change colour.</li>"
          "<li><strong>By hand or with harvesting rakes</strong>, onto nets: no olive is picked up from the ground.</li>"
          "<li><strong>Milling within a few hours in our own estate mill</strong>, with cold extraction (below 27 °C): from harvest to bottle, everything on our estate.</li>"
          "<li><strong>Storage</strong> in stainless steel tanks under inert gas, protected from light and heat.</li>"
          "</ul>"
          f"<p>Varieties in our grove: {ph('e.g. Frantoio, Leccino, Moraiolo, Pendolino')}.</p>",
        fig("raccolta-olive", "Olive harvest onto nets beneath a large olive tree", "The harvest: nets, poles and crates")),
        label="bio")
    + section(
        h2("How to recognise a great oil", "assaggio", "Tasting")
        + '<div class="trio">'
          "<div><h3>Fruity</h3><p>Aromas of fresh olive, cut grass, artichoke, green almond, tomato. A “green” "
          "fruitiness reveals an early harvest.</p></div>"
          "<div><h3>Bitter</h3><p>A bitter note on the tongue is a mark of quality, not a defect: it shows healthy, "
          "polyphenol-rich olives.</p></div>"
          "<div><h3>Pungent</h3><p>The peppery tickle in the throat, sometimes with a little cough, is the sign of "
          "oleocanthal. The more intense, the younger and livelier the oil.</p></div>"
          "</div>"
          "<p><strong>Storage:</strong> away from light and heat, at 14–18 °C, tightly closed. Olive oil does not improve "
          "with age: it is best enjoyed within 12–18 months of milling.</p>"
          "<p><strong>In the kitchen:</strong> raw on toasted bread, pulses, vegetables and Tuscan soups – but also for "
          "cooking, as its antioxidants help extra virgin olive oil withstand heat well.</p>",
        "section--dark", label="assaggio")
)

OLIVICOLTORI = (
    section(split(
        h2("Ralph and Christina Striewski", "noi", "Who we are")
        + "<p>Becoming olive growers was never our plan. Ralph flew for 41 years – from 1981 to 2022 as a Lufthansa "
          "pilot, finally as captain of the Airbus A350. Christina is a fashion designer: from 2013 to 2021 we ran our "
          "own fashion label together, Arcanum Fashion, which produced shimmering, glossy fashion "
          "(<a href='https://www.instagram.com/vanilla.pearl/' rel='noopener'>Christina on Instagram</a>).</p>"
          "<p>But it seems the olive trees called us. After the first conversation and the first visit to Villa "
          "Belvedere, we knew at once that this would become our place. Everything else was organisation – and since "
          "buying it in 2024, a great deal of work and a whole new subject to learn.</p>"
          "<p>We were not born farmers: we have learned – and learn every day – from our neighbours, from those who "
          "tended the grove before us and from the trees themselves. With them, we carry on work that began almost three "
          "hundred years ago, when the mezzadri planted the first olive trees.</p>",
        fig("olivicoltori-ralph-christina", "Placeholder: two people and a dog among olive trees at sunset",
            "Placeholder for a photo of Ralph and Christina in the olive grove")),
        label="noi")
    + section(
        h2("What matters to us", "valori")
        + '<div class="trio">'
          "<div><h3>Respect for the hill</h3><p>We look after the dry-stone walls, let grass grow between the rows and "
          "protect the bees, insects and birds that live in the grove.</p></div>"
          "<div><h3>Uncompromising quality</h3><p>Early harvest, immediate milling in our own mill, laboratory analysis: we want to "
          "know exactly what is in our oil.</p></div>"
          "<div><h3>A shared story</h3><p>We tell the story of Belvedere and the people who lived here – because a "
          "landscape is memory.</p></div>"
          "</div>",
        "section--cream", label="valori")
    + section(
        h2("A year in the olive grove", "anno", "The calendar")
        + calendar([
            ("January – March", "Pruning", "We thin the crowns so that light and air can reach inside the tree."),
            ("April – May", "Flowering", "The trees are covered in tiny white flowers – the most delicate moment."),
            ("June – August", "Fruit set", "The fruit forms and grows; we tend the soil and the walls."),
            ("September", "Waiting", "We watch the olives ripen and prepare nets, crates and tools."),
            ("October – November", "Harvest and milling", "We pick as the olives turn colour and press them the same day in our own mill."),
            ("December", "Rest", "The trees rest. We taste the new oil and give thanks to the hill."),
        ]),
        "section--dark", label="anno")
    + section(split(
        h2("The olive trees of Belvedere", "olivi")
        + f"<p>Our grove has around 2,300 trees on approx. 7.5 hectares of terraces, between 100 and "
          f"160 metres above sea level. Some trees are around 300 years old: the mezzadri planted them "
          "in their lunette, and they will bear fruit long after we are gone.</p>"
          "<p>When we bought the Villa and the grove in 2024, there was – and still is – a good deal of work to do before "
          "every tree can be harvested again. Together with the Azienda Agricola Villa Belvedere di Corliano we took over "
          "the organic certification and the estate’s own olive mill, so the whole process, from harvest to bottle, "
          "takes place here on our land.</p>"
          f"<p>{link('energia', 'Discover the qualities of our oil →')}</p>",
        fig("raccolta-olive", "People harvesting olives onto nets under an olive tree", "Harvesting with friends and neighbours"),
        rev=True), label="olivi")
)

FORM = {
    "name": "Full name", "email": "Email", "topic": "Subject",
    "topics": ["About the oil", "History of the Villa", "Visiting the olive grove", "Press and media", "Other"],
    "message": "Message", "privacy": "I have read the {link} and agree to my data being processed to answer my enquiry.",
    "privacy_link": "privacy policy", "send": "Send message", "required": "Required fields",
    "ok": "Thank you! Your message has been sent. We will get back to you as soon as possible.",
    "err": "Something went wrong. Please try again or write to us directly by email.",
    "sending": "Sending…", "hp": "Please leave this field empty",
}

CONTATTI = section(
    '<div class="contact-grid"><div class="prose">'
    + h2("Write to us", "scrivici")
    + "<p>Do you have questions about our oil, the history of Villa Belvedere or work in the olive grove? Would you "
      "like to meet us in person? Use the form or send us an email.</p>"
    + note("This form is for questions and information only. No orders are accepted and no contracts are "
           "concluded through this website.")
    + f"<h3>Direct contact</h3><address>{L['company']}<br>{L['street']}<br>{L['zip_city']}<br>Italy<br>"
      f"Phone: {L['phone']}<br>Email: {L['email']}</address>"
    + "<h3>How to find us</h3><p>Villa Belvedere lies on the slopes of Monte Pisano near San Giuliano Terme, "
      "not far from Pisa. We will gladly send you directions on request. If you would like to visit, please get in "
      "touch first: the olive grove is a working farm.</p>"
    + "</div>"
    + contact_form(FORM, "en")
    + "</div>", label="scrivici")

LEGAL_PAGE = section(
    '<div class="prose legal">'
    + "<h2>Information pursuant to § 5 DDG (Germany) and Italian law</h2>"
    + f"<p><strong>{L['company']}</strong><br>Owner: {L['owner']}<br>Legal form: {L['legal_form']} (sole proprietorship)<br>{L['street']}<br>{L['zip_city']}<br>Italy</p>"
    + f"<h3>Contact</h3><p>Phone: {L['phone']}<br>Email: {L['email']}<br>PEC (certified email): {L['pec']}</p>"
    + f"<h3>Tax and registration</h3><p>VAT number (Partita IVA): {L['vat']}<br>Tax code (Codice fiscale): {L['tax_code']}<br>"
      f"Registered with: {L['register']}, {L['rea']}</p>"
    + f"<h3>Organic control body</h3><p>{L['bio_body']}<br>Code: {L['bio_code']}<br>Origin: {L['bio_origin']}</p>"
    + f"<h3>Responsible for content</h3><p>{L['content_responsible']}, {L['street']}, {L['zip_city']}, Italy</p>"
    + "<h3>Nature of this website</h3><p>This website is purely informational and presents our farm. No products are "
      "offered for sale, no prices are shown and no distance contracts are concluded.</p>"
    + "<h3>Consumer dispute resolution</h3><p>We are neither willing nor obliged to take part in dispute resolution "
      "proceedings before a consumer arbitration board.</p>"
    + "<h3>Liability for content</h3><p>The content of this website has been prepared with great care. However, we "
      "cannot guarantee that it is complete, accurate or up to date. Information on the properties of olive oil is "
      "general in nature and does not constitute medical advice.</p>"
    + "<h3>Liability for links</h3><p>This website contains links to external third-party websites over whose content "
      "we have no control. No legal violations were apparent at the time of linking. If we become aware of any, we "
      "will remove such links immediately.</p>"
    + "<h3>Photo credits</h3>" + credits_list() + "<h3>Copyright and image credits</h3><p>The texts, images and graphics on this website are protected by "
      "copyright. Any use beyond the limits of copyright law requires our written consent.</p>"
      "<p>The illustrations of people and landscapes are digitally created and partly generated with artificial "
      f"intelligence; the people depicted are fictional.</p>"
      "<p>Font: Cormorant Garamond (SIL Open Font License 1.1), hosted locally.</p>"
    + f"<p class='fineprint'>Last updated: {LEGAL_DATE['en']}</p>"
    + "</div>")

PRIVACY_PAGE = section(
    '<div class="prose legal">'
    + "<h2>1. Controller</h2>"
    + f"<p>{L['company']}, {L['owner']}, {L['street']}, {L['zip_city']}, Italy – Email: {L['email']}, Phone: {L['phone']}.</p>"
    + "<h2>2. At a glance</h2><p>This website uses no cookies, no analytics or tracking tools, no advertising, no "
      "social media plugins, no maps and no third-party fonts. Fonts are served from our own server. We only process "
      "personal data where technically necessary to provide the website, or when you contact us.</p>"
    + "<h2>3. Hosting and server log files</h2><p>This website is hosted on GitHub Pages, a service of GitHub, Inc., "
      "88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. When you visit the website, technical data is "
      "recorded automatically (IP address, date and time, page requested, browser, operating system, referrer URL). "
      "This data is used to operate the website securely and reliably.</p>"
      "<p>Legal basis: Art. 6(1)(f) GDPR (legitimate interest in secure and efficient provision). GitHub may process "
      "data in the USA; GitHub is certified under the EU-U.S. Data Privacy Framework (adequacy decision, Art. 45 "
      "GDPR). More information: "
      "<a href='https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement' rel='noopener'>GitHub privacy statement</a>.</p>"
    + "<h2>4. Contact form</h2>"
    + f"<p>If you write to us using the contact form, your details (name, email address, subject, message) are "
      f"forwarded to us by email via the service {FP['name']} (USA). The provider may process data in "
      f"the {FP['country']}; transfers are based on the EU-U.S. Data Privacy Framework or EU standard contractual "
      f"clauses (Art. 46 GDPR). Provider’s privacy policy: <a href='{FP['privacy_url']}' rel='noopener'>{FP['privacy_url']}</a>.</p>"
      "<p>Legal basis: Art. 6(1)(b) GDPR (steps taken at your request) and Art. 6(1)(f) GDPR (legitimate interest in "
      "answering enquiries). The data is deleted once your enquiry has been dealt with, unless statutory retention "
      "obligations apply.</p>"
    + "<h2>5. Contact by email or phone</h2><p>If you contact us by email or phone, we process your details only to "
      "handle your enquiry (Art. 6(1)(b) and (f) GDPR) and delete them when they are no longer needed.</p>"
    + "<h2>6. Cookies and local storage</h2><p>This website sets no cookies and stores no information on your device. "
      "A cookie banner is therefore not required.</p>"
    + "<h2>7. Your rights</h2><p>You have the right of access (Art. 15), rectification (Art. 16), erasure (Art. 17), "
      "restriction of processing (Art. 18), data portability (Art. 20) and to object (Art. 21 GDPR). You may withdraw "
      "any consent at any time with effect for the future.</p>"
      "<p><strong>Right to object:</strong> you may object at any time, on grounds relating to your particular "
      "situation, to processing based on Art. 6(1)(f) GDPR.</p>"
    + f"<h2>8. Right to lodge a complaint</h2><p>You have the right to lodge a complaint with a data protection "
      f"supervisory authority, in particular in the member state of your residence. Our competent authority is: "
      f"{L['authority_privacy']}.</p>"
    + "<h2>9. Security</h2><p>This website uses SSL/TLS encryption (HTTPS).</p>"
    + "<h2>10. Obligation to provide data</h2><p>You are not obliged to provide us with personal data. Without an email "
      "address, however, we cannot reply to your enquiry.</p>"
    + f"<p class='fineprint'>Last updated: {LEGAL_DATE['en']}</p>"
    + "</div>")

PAGES = {
    "home": {
        "title": "Villa Belvedere – Organic Extra Virgin Olive Oil from Monte Pisano",
        "description": "Villa Belvedere: an old farmhouse on Monte Pisano since 1536. Organic extra virgin olive oil rich "
                       "in polyphenols – history, olive grove and olive growers.",
        "h1": "Villa Belvedere", "kicker": "Monte Pisano · since 1536",
        "lead": "Organic extra virgin olive oil from the terraces of a farmhouse that faces the sunset.",
        "hero": "vista-belvedere-sera",
        "hero_alt": "Evening view from the terrace of Villa Belvedere over the plain below Monte Pisano, with roses and olive trees in the foreground and the lights of the valley on the horizon",
        "hero_cta": '<p class="hero-cta">' + btn("conte", "The story of the Villa") + btn("energia", "Our oil", "btn btn--ghost") + "</p>",
        "images": ["vista-belvedere-sera", "villa-belvedere", "ritratto-conte", "ritratto-mezzadra",
                   "ritratto-frantoiano", "ritratto-raccoglitrice", "monte-pisano-panorama"],
        "body": HOME,
    },
    "conte": {
        "title": "The Count’s Oil – 500 Years of Villa Belvedere",
        "description": "A sharecroppers’ farmhouse on Monte Pisano since 1536, an olive grove on lunette since 1735: the "
                       "story of Villa Belvedere, the Counts della Seta and its oil.",
        "h1": "The Count’s Oil", "nav": "The Count’s Oil", "kicker": "Five centuries of history",
        "lead": "From sharecroppers’ farmhouse to organic olive grove with its own mill: the story of Villa Belvedere.",
        "hero": "mezzadri-tramonto", "hero_alt": "Sharecropping family with a donkey on the ridge of Monte Pisano at sunset",
        "schema": "Article",
        "images": ["mezzadri-tramonto", "monte-pisano-panorama", "corliano-frantoio-1901", "corliano-facciata", "ramo-olivo"],
        "body": CONTE,
    },
    "energia": {
        "title": "Oil, Energy of Life – Organic Olive Oil and Polyphenols",
        "description": "What makes an organic extra virgin olive oil rich in polyphenols: legal parameters, oleocanthal, "
                       "hydroxytyrosol, early harvest, tasting and storage.",
        "h1": "Oil, Energy of Life", "nav": "Oil, Energy of Life", "kicker": "Organic extra virgin",
        "lead": "Bitter, pungent, fragrant: everything worth knowing about an organic, polyphenol-rich extra virgin olive oil.",
        "hero": "olio-goccia", "hero_alt": "Green-gold drop of olive oil above olives and olive leaves",
        "schema": "Article",
        "images": ["olio-goccia", "ramo-olivo", "raccolta-olive"],
        "body": ENERGIA,
    },
    "olivicoltori": {
        "title": "The Olive Growers – Ralph and Christina Striewski",
        "description": "Since 2024 Ralph and Christina Striewski have lived at Villa Belvedere, tending the olive grove "
                       "according to the principles of organic farming. Our story.",
        "h1": "The Olive Growers", "nav": "The Olive Growers", "kicker": "At Belvedere since 2024",
        "lead": "Ralph and Christina Striewski: a new chapter in a story five centuries long.",
        "hero": "olivicoltori-ralph-christina", "hero_alt": "Two people and a dog among olive trees at sunset",
        "schema": "AboutPage",
        "images": ["olivicoltori-ralph-christina", "raccolta-olive"],
        "body": OLIVICOLTORI,
    },
    "contatti": {
        "title": "Contact – Villa Belvedere",
        "description": "Contact Villa Belvedere on Monte Pisano: questions about our organic extra virgin olive oil, the "
                       "history of the Villa or the olive grove.",
        "h1": "Contact", "nav": "Contact", "kicker": "Write to us",
        "lead": "We look forward to your questions.",
        "hero": "villa-belvedere", "hero_alt": "The Villa Belvedere farmhouse at sunset",
        "schema": "ContactPage",
        "body": CONTATTI,
    },
    "legal": {
        "title": "Legal notice", "description": "Legal notice (Impressum) of Azienda Agricola Villa Belvedere.",
        "h1": "Legal notice", "nav": "Legal notice", "body": LEGAL_PAGE,
    },
    "privacy": {
        "title": "Privacy policy", "description": "Privacy policy under the GDPR of Azienda Agricola Villa Belvedere.",
        "h1": "Privacy policy", "nav": "Privacy policy", "body": PRIVACY_PAGE,
    },
    "sitemap": {
        "title": "Site map", "description": "All pages of the Villa Belvedere website at a glance.",
        "h1": "Site map", "nav": "Site map", "body": "",
    },
}
