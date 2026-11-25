"""Deutsche Texte. Alle Texte sind Entwürfe und können frei angepasst werden."""
from config import LEGAL as L, LEGAL_DATE, FORM_PROVIDER as FP
from lib import (photo, credits_list, fig, ph, link, section, split, h2, cards, portraits, facts, timeline, band,
                 table, note, calendar, btn, contact_form)

UI = {
    "skip": "Zum Inhalt springen",
    "menu": "Menü",
    "nav_label": "Hauptnavigation",
    "lang_label": "Sprache",
    "breadcrumb": "Brotkrümelnavigation",
    "nav": {"home": "Home", "conte": "Öl des Grafen", "energia": "Öl, Energie des Lebens",
            "olivicoltori": "Die Ölbauern", "contatti": "Kontakt", "legal": "Impressum",
            "privacy": "Datenschutz", "sitemap": "Sitemap"},
    "footer_claim": "Biologisches Olivenöl extra vergine aus den Olivenhainen des Monte Pisano, wo die Mezzadri seit 1735 Olivenbäume pflanzten. Von der Ernte bis in die Flasche – alles auf unserem Hof.",
    "vat": "USt-IdNr. (P. IVA)",
    "footer_nav": "Seiten",
    "footer_legal": "Rechtliches",
    "info_only": "Diese Website dient ausschließlich der Information. Über diese Website werden keine Waren "
                 "verkauft und keine Verträge geschlossen.",
    "images_note": "Illustrationen: digital erstellte Platzhalterbilder",
    "og_alt": "Olivenhain der Villa Belvedere am Monte Pisano bei Sonnenuntergang",
    "nf_title": "Seite nicht gefunden",
    "nf_text": "Die gesuchte Seite existiert nicht oder wurde verschoben.",
    "nf_link": "Zur Startseite",
}

MORE = "Weiterlesen"

HOME = (
    section(split(
        h2("Ein Hof, fünf Jahrhunderte, ein Öl", "intro", "Willkommen in der Villa Belvedere")
        + "<p>An den Hängen des Monte Pisano, zwischen Pisa und Lucca, liegt die Villa Belvedere: ein altes "
          "toskanisches Bauernhaus aus Stein, umgeben von Oliventerrassen, die auf die Ebene und an klaren "
          "Tagen bis zum Meer blicken.</p>"
          "<p>Seit 1536 gehörte das Haus zu den Besitzungen der Grafen Agostini Fantini Venerosi della Seta. Um 1735 "
          "begannen die Halbpächter – die <em>mezzadri</em> – den Wald zu roden und Olivenbäume zu pflanzen, jeden "
          "geschützt von einem halbmondförmigen Steinmäuerchen, der „Lunetta“. Manche dieser Bäume sind heute rund "
          "300 Jahre alt.</p>"
          "<p>Heute pflegen wir den Olivenhain biologisch und pressen in unserer eigenen Ölmühle: Von der Ernte bis in "
          "die Flasche geschieht alles hier – mit demselben Respekt vor dem Hügel.</p>"
          f"<p>{link('conte', 'Die Geschichte der Villa lesen →')}</p>",
        fig("villa-belvedere", "Das Bauernhaus der Villa Belvedere zwischen Zypressen und Olivenbäumen im Abendlicht",
            "Das Bauernhaus der Villa Belvedere")),
        "section--cream", label="intro")
    + '<section class="facts-band" aria-label="Villa Belvedere in Zahlen"><div class="wrap">'
    + facts([("1536", "Gründungsjahr des Hofes"), ("2.320 Olivenbäume", "auf Trockenmauer-Terrassen"),
             ("135 m", "Höhe am Monte Pisano"), ("Bio", "zertifizierter ökologischer Anbau")])
    + "</div></section>"
    + section(
        h2("Drei Geschichten, ein Öl", "storie")
        + cards([
            ("conte", "frantoio-antico", "Der alte Mühlstein in der Ölmühle des Grafen", "Öl des Grafen",
             "Fast 500 Jahre Geschichte: die Grafen della Seta, die Mezzadri, die Lunette und die Wiedergeburt der Villa."),
            ("energia", "olio-goccia", "Ein grüngoldener Öltropfen über Oliven und Blättern", "Öl, Energie des Lebens",
             "Was ein biologisches Olivenöl extra vergine mit vielen Polyphenolen besonders macht – einfach erklärt."),
            ("olivicoltori", "olivicoltori-ralph-christina", "Zwei Menschen zwischen Olivenbäumen im Sonnenuntergang", "Die Ölbauern",
             "Ralph und Christina Striewski: seit 2024 in Belvedere, mit den Händen in der Erde und dem Blick auf die Bäume."),
        ], MORE), label="storie")
    + section(
        h2("Die Stimmen des Hügels", "voci", "Wer auf diesem Hügel lebte")
        + '<p class="section-intro">Fünf Jahrhunderte lang war der Monte Pisano Heimat von Grafen und Bauern, von '
          "Ölmüllern und Erntehelferinnen. Wir haben uns ihre Gesichter und Stimmen vorgestellt.</p>"
        + portraits([
            ("ritratto-conte", "Illustriertes Porträt eines Renaissance-Adligen mit schwarzem Barett und rotem Mantel",
             "Der Graf", "1536 – der Grundherr",
             "„Ich wollte, dass dieses Haus ins Tal blickt – darum heißt es Belvedere.“"),
            ("ritratto-mezzadra", "Illustriertes Porträt einer Bäuerin mit rotem Kopftuch und Olivenkorb",
             "Die Halbpächterin", "1735 – die Familie auf dem Hof",
             "„Wir haben dem Hügel den Wald abgerungen, Stein auf Stein, Lunetta um Lunetta.“"),
            ("ritratto-frantoiano", "Illustriertes Porträt eines älteren Ölmüllers mit Mütze und Schürze",
             "Der Ölmüller", "1900 – der Meister der Mühle",
             "„Gutes Öl spürt man im Hals: Wenn es kratzt, lebt es.“"),
            ("ritratto-raccoglitrice", "Illustriertes Porträt einer jungen Erntehelferin mit Strohhut",
             "Die Erntehelferin", "heute – die Ernte",
             "„Im Oktober füllt sich der Hügel mit Stimmen, Netzen und Lachen.“"),
        ])
        + '<p class="fineprint">Fiktive Figuren. Digital erstellte Illustrationen zur Veranschaulichung.</p>',
        "section--dark", label="voci")
    + band("monte-pisano-panorama", "Blick vom Monte Pisano auf die Ebene von Pisa und das Meer bei Sonnenuntergang",
           "Von hier oben sieht man die Ebene, die einst Sumpf war, den Turm von Pisa – und am Abend das Meer, das golden wird.",
           "Villa Belvedere, Monte Pisano")
    + section(
        '<div class="cta-box">' + h2("Lernen Sie uns kennen", "visita")
        + "<p>Sie haben Fragen zu unserem Öl, zur Geschichte der Villa oder zur Arbeit im Olivenhain? Schreiben Sie "
          "uns – wir antworten gern.</p>" + btn("contatti", "Schreiben Sie uns") + "</div>",
        "section--cream", label="visita")
)

CONTE = (
    section(split(
        h2("Ein Bauernhaus auf den Hügeln von Pisa", "origini", "Die Anfänge")
        + "<p>Im Jahr 1536 war die Ebene von Pisa noch weitgehend sumpfig und stand zu manchen Jahreszeiten unter "
          "Wasser. Um die Hügel des Monte Pisano zu besiedeln, holte man arme Arbeiterfamilien: Sie bekamen ein Haus "
          "und ein Stück Land – im Gegenzug für ihre Arbeit und einen Teil der Ernte.</p>"
          "<p>So entstand Belvedere: ein steinernes Bauernhaus mit Stall und Tenne, "
          "errichtet dort, wo sich der Blick ins Tal öffnet – daher sein Name, „schöne Aussicht“. Der Hof gehörte zu "
          "den Besitzungen der Grafen Agostini Fantini Venerosi della Seta, einer Pisaner Adelsfamilie. Damals war "
          "der Hügel noch von Wald bedeckt.</p>",
        fig("monte-pisano-panorama", "Panorama vom Monte Pisano über die Ebene von Pisa bis zum Meer", "Die Ebene von Pisa vom Monte Pisano aus")),
        label="origini")
    + section(
        h2("Fünf Jahrhunderte im Überblick", "cronologia", "Zeitleiste")
        + timeline([
            ("1536", "Die Besiedlung", "An den Hängen des Monte Pisano werden Halbpächterfamilien angesiedelt. Es entsteht das Bauernhaus Belvedere, Teil der Besitzungen der Grafen Agostini Fantini Venerosi della Seta."),
            ("um 1735", "Vom Wald zum Olivenhain", "Die Mezzadri beginnen, den Wald zu roden und Olivenbäume zu pflanzen – die meisten gestützt von kleinen halbmondförmigen Steinmäuerchen, den „Lunette“. Einige dieser Bäume wachsen noch heute."),
            ("18.–20. Jh.", "Die Zeit der Halbpacht", "Die Ernte wird zur Hälfte zwischen Grundherr und Bauernfamilie geteilt. Im Haus leben bis zu drei Generationen, die jeden Baum beim Namen kennen."),
            ("1964", "Das Ende einer Epoche", "Die Ländereien des Grafen Agostini Fantini Venerosi della Seta fallen an einen sardischen Bauunternehmer – ausgenommen die Villa di Corliano am Fuß des Monte Pisano, direkt unterhalb von Belvedere. Die Mezzadri verlassen die Villa."),
            ("1964 – 1987", "Unklare Jahre", "Es folgen Jahre mit ungeklärten Besitzverhältnissen, in denen der Olivenhain nicht mehr wie früher gepflegt wird."),
            ("1987", "Die Wiedergeburt", "Der Münchner Unternehmer Rolf Freitag kauft die Villa und renoviert sie über mehrere Jahre komplett. Auch der Olivenhain wird wieder zu einem produktiven Olivenhain."),
            ("2024", "Ein neues Kapitel", "Ralph und Christina Striewski kaufen Villa und Olivenhain – zusammen mit der Azienda Agricola Villa Belvedere di Corliano, der Bio-Zertifizierung und der eigenen Ölmühle."),
        ]),
        "section--cream", label="cronologia")
    + section(split(
        h2("Die Lunette: Olivenbäume, dem Wald abgerungen", "lunette")
        + "<p>Um 1735 begannen die Mezzadri, den Hügel zu verwandeln. Sie rodeten den Wald von Hand, lasen die Steine "
          "aus dem Boden und bauten mit genau diesen Steinen um jeden jungen Olivenbaum ein kleines halbmondförmiges "
          "Mäuerchen: die <em>Lunetta</em> (Halbmond). Sie hält Erde und Regenwasser am steilen Hang und schützt die "
          "Wurzeln.</p>"
          "<p>Die meisten unserer Olivenbäume stehen bis heute in ihrer Lunetta. Manche sind rund 300 Jahre alt: "
          "Diese Halbpächter haben sie gepflanzt – mit dem Gedanken an ihre Enkel.</p>"
          "<p>Der Tag folgte der Sonne. Im Frühjahr wurde geschnitten, im Sommer gehackt, im Herbst geerntet – mit "
          "langen Stangen schlug man die Zweige über ausgebreiteten Tüchern. Die Frauen versorgten Garten, Tiere und "
          "Haus; die Kinder sammelten die heruntergefallenen Oliven auf, eine nach der anderen. Die Hälfte der Ernte "
          "gehörte dem Grafen.</p>",
        fig("mezzadri-tramonto", "Silhouette einer Bauernfamilie mit Esel auf dem Hügelkamm im Sonnenuntergang", "Eine Halbpächterfamilie auf dem Heimweg")),
        "section--dark", label="lunette")
    + section(split(
        h2("Von der Ölmühle des Grafen zur eigenen Ölmühle", "frantoio")
        + "<p>Jahrhundertelang wanderten die Oliven aus Belvedere in Körben ins Tal, zur Ölmühle des Grafen in Corliano: ein "
          "großer Raum aus Stein, in dem ein Mühlstein aus Granit die Früchte zu Brei zermahlte, der dann auf Matten "
          "gepresst wurde. Das Öl ruhte in Tonkrügen; ein Teil ging an den Grafen, der Rest blieb der Familie auf dem "
          "Hof – das ganze Jahr über Nahrung, Medizin und Licht.</p>"
          "<p>1964 endete die Halbpacht, und die Mezzadri verließen die Villa. Nach Jahren mit unklaren "
          "Besitzverhältnissen kaufte Rolf Freitag 1987 das Anwesen, restaurierte es sorgfältig und machte den "
          "Olivenhain wieder produktiv. Von ihm haben wir 2024 nicht nur Villa und Olivenhain übernommen, sondern auch "
          "die Azienda Agricola Villa Belvedere di Corliano mit Bio-Zertifizierung und <strong>eigener Ölmühle</strong>.</p>"
          "<p>Deshalb findet heute der gesamte Weg – von der Ernte bis in die Flasche – bei uns auf dem Grundstück statt.</p>"
          f"<p>{link('olivicoltori', 'Wer sich heute um die Bäume kümmert →')}</p>",
        photo("corliano-frantoio-1901", "Historisches Foto der Ölmühle von Corliano aus dem Jahr 1901", "Die Ölmühle von Corliano im Jahr 1901 – heute zu besichtigen"),
        rev=True), label="frantoio")
    + section(split(
        h2("Die Villa di Corliano", "corliano", "Am Fuß des Monte Pisano")
        + "<p>Direkt unterhalb von Belvedere, am Fuß des Monte Pisano, liegt die Villa di Corliano, der Sitz der "
          "Grafen Agostini Fantini Venerosi della Seta. 1964 war sie der einzige Teil ihrer Besitzungen, der nicht an "
          "den sardischen Bauunternehmer ging.</p>"
          "<p>Zur Villa gehört auch die alte Ölmühle des Grafen, in der jahrhundertelang die Oliven des Hügels gepresst "
          "wurden – auch die aus Belvedere. Sie kann noch heute besichtigt werden.</p>",
        photo("corliano-facciata", "Fassade der Villa di Corliano am Fuß des Monte Pisano", "Die Villa di Corliano")),
        "section--cream", label="corliano")
    + band("ramo-olivo", "Olivenzweig mit grünen und dunklen Oliven im Gegenlicht",
           "Ein Olivenbaum gehört nicht dem, der ihn pflanzt, sondern denen, die nach ihm kommen.", "Toskanisches Bauernsprichwort")
)

ENERGIA = (
    section(split(
        h2("Was ist ein Olivenöl extra vergine?", "evo", "Die Grundlagen")
        + "<p>Olivenöl extra vergine – auf Deutsch „nativ extra“ – ist der Saft der Olive, gewonnen <strong>ausschließlich "
          "mit mechanischen Verfahren</strong>: Die Oliven werden gewaschen, gemahlen, gerührt und getrennt – ohne "
          "Lösungsmittel und ohne Raffination. Es ist die höchste Güteklasse, die das EU-Recht kennt.</p>"
          "<p>Um „extra vergine“ heißen zu dürfen, muss ein Öl genaue chemische Grenzwerte einhalten und die Prüfung "
          "durch ein Verkostungspanel bestehen: Es braucht eine wahrnehmbare Fruchtigkeit und <strong>keinerlei "
          "Fehler</strong>.</p>",
        fig("olio-goccia", "Grüngoldener Tropfen Olivenöl extra vergine über Oliven und Blättern", "Die grüngoldene Farbe frisch gepressten Öls")),
        label="evo")
    + section(
        h2("Die gesetzlichen Kennwerte", "parametri")
        + table("Grenzwerte für die Kategorie extra vergine (Delegierte Verordnung (EU) 2022/2104) und Werte unseres Öls",
                ["Parameter", "Grenzwert extra vergine", "Unser Öl 2026"],
                [["Freie Säure (Ölsäure)", "≤ 0,80 %", "0,35 %"],
                 ["Peroxidzahl", "≤ 20 mEq O₂/kg", "7,6 mEq O₂/kg"],
                 ["K232", "≤ 2,50", "<span class=\"pending\">folgt</span>"],
                 ["K270", "≤ 0,22", "<span class=\"pending\">folgt</span>"],
                 ["Median der Fehler", "= 0", "<span class=\"pending\">folgt</span>"],
                 ["Median der Fruchtigkeit", "> 0", "<span class=\"pending\">folgt</span>"],
                 ["Polyphenole gesamt", "kein gesetzlicher Grenzwert", "<strong>378 mg/kg</strong>"]],
                "Prüfbericht Nr. 2026-7563 vom 23.10.2026, Enolab Service S.r.l., Capannoli (PI); Probe aus der Ernte vom 3. Oktober 2026. Polyphenole gesamt angegeben als Gallussäure. Die fehlenden Werte folgen mit den nächsten Analysen."),
        "section--cream", label="parametri")
    + section(split(
        h2("Polyphenole: die Kraft des Öls", "polifenoli", "Das Herz der Qualität")
        + "<p>Polyphenole sind natürliche Stoffe, die der Olivenbaum bildet, um seine Früchte zu schützen. Im Olivenöl "
          "extra vergine finden sich Dutzende davon; die bekanntesten sind <strong>Hydroxytyrosol</strong>, "
          "<strong>Tyrosol</strong>, <strong>Oleuropein</strong> (in seinen Abbauformen), <strong>Oleocanthal</strong> "
          "und <strong>Oleacein</strong>.</p>"
          "<p>Sie geben dem Öl seine <strong>bitteren</strong> und <strong>scharfen</strong> Noten: Das Kratzen im Hals "
          "nach dem Probieren geht vor allem auf das Oleocanthal zurück. Ein polyphenolreiches Öl ist außerdem "
          "stabiler: Es oxidiert langsamer und bewahrt seine Aromen länger.</p>"
          "<p>Wie viele Polyphenole ein Öl enthält, hängt von Sorte, Reifegrad, Klima und vor allem von der "
          "Verarbeitung ab. Deshalb ernten wir früh und verarbeiten die Oliven innerhalb weniger Stunden in unserer eigenen Ölmühle, nur wenige Schritte vom Hain entfernt.</p>",
        fig("ramo-olivo", "Olivenzweig mit grünen und sich färbenden Oliven", "Oliven bei der Farbumstellung: der Moment der Polyphenole"),
        rev=True), label="polifenoli")
    + section(
        h2("Was die Wissenschaft sagt – und was das Gesetz erlaubt", "claim")
        + note("<p><strong>Zugelassene gesundheitsbezogene Angabe (Verordnung (EU) Nr. 432/2012):</strong> „Olivenöl-"
               "Polyphenole tragen dazu bei, die Blutfette vor oxidativem Stress zu schützen.“ Die positive Wirkung "
               "stellt sich bei einer täglichen Aufnahme von 20 g Olivenöl ein.</p>"
               "<p>Die Angabe darf nur für Olivenöl verwendet werden, das <strong>mindestens 5 mg Hydroxytyrosol und "
               "dessen Derivate je 20 g</strong> Öl enthält (entspricht 250 mg/kg). "
               f"Unser Öl enthält 378 mg/kg Polyphenole gesamt. Maßgeblich für diese Angabe ist jedoch der Gehalt an Hydroxytyrosol und dessen Derivaten, der eine eigene Analyse erfordert. Sie ist in Arbeit – bis das Ergebnis vorliegt, nehmen wir diese Angabe für unser Öl nicht in Anspruch.</p>",
               "note note--claim")
        + "<p>Olivenöl extra vergine ist ein zentraler Bestandteil der Mittelmeerküche. Es besteht zum größten Teil aus "
          "<strong>Ölsäure</strong>, einer einfach ungesättigten Fettsäure, und enthält von Natur aus <strong>Vitamin E</strong> "
          "(Tocopherole), <strong>Squalen</strong> sowie <strong>Farbstoffe</strong> wie Chlorophylle und Carotinoide.</p>"
          + '<p class="fineprint">Die Informationen auf dieser Seite sind allgemeiner Natur und ersetzen keine ärztliche '
            "oder ernährungswissenschaftliche Beratung. Eine abwechslungsreiche, ausgewogene Ernährung und eine gesunde "
            "Lebensweise sind wichtig.</p>",
        "section--cream", label="claim")
    + section(split(
        h2("Bio – vom Baum bis ins Öl", "bio", "Unsere Arbeitsweise")
        + "<ul class='ticks'>"
          "<li><strong>Ökologischer Landbau</strong> nach Verordnung (EU) 2018/848: keine chemischen Herbizide, keine "
          "synthetischen Dünger; Begrünung, Gründüngung und behutsamer Schnitt.</li>"
          f"<li><strong>Kontrollstelle:</strong> {L['bio_body']} – Code {L['bio_code']}, Herkunft: {L['bio_origin']}.</li>"
          "<li><strong>Frühe Ernte</strong> zwischen Oktober und Anfang November, wenn die Oliven beginnen, ihre Farbe zu wechseln.</li>"
          "<li><strong>Von Hand oder mit Erntekämmen</strong>, auf Netzen: Keine Olive wird vom Boden aufgelesen.</li>"
          "<li><strong>Verarbeitung innerhalb weniger Stunden in unserer hofeigenen Ölmühle</strong> mit Kaltextraktion "
          "(unter 27 °C): von der Ernte bis in die Flasche alles auf unserem Hof.</li>"
          "<li><strong>Lagerung</strong> in Edelstahltanks unter Schutzgas, geschützt vor Licht und Wärme.</li>"
          "</ul>"
          "<p>Sorten in unserem Hain: vor allem <strong>Frantoio</strong> und <strong>Leccino</strong>, dazu einige <strong>Moraiolo</strong> – die klassischen Sorten der Toskana.</p>",
        fig("raccolta-olive", "Olivenernte auf Netzen unter einem großen Olivenbaum", "Die Ernte: Netze, Stangen und Kisten")),
        label="bio")
    + section(
        h2("Woran man ein großes Öl erkennt", "assaggio", "Die Verkostung")
        + '<div class="trio">'
          "<div><h3>Fruchtig</h3><p>Duft nach frischer Olive, geschnittenem Gras, Artischocke, grüner Mandel, Tomate. "
          "Am „grünen“ Fruchtton erkennt man die frühe Ernte.</p></div>"
          "<div><h3>Bitter</h3><p>Eine bittere Note auf der Zunge ist ein Qualitätsmerkmal, kein Fehler: Sie zeigt "
          "gesunde, polyphenolreiche Oliven.</p></div>"
          "<div><h3>Scharf</h3><p>Das Kratzen im Hals, manchmal mit einem kleinen Hustenreiz, ist das Zeichen des "
          "Oleocanthals. Je intensiver, desto jünger und lebendiger das Öl.</p></div>"
          "</div>"
          "<p><strong>Aufbewahrung:</strong> dunkel, kühl (14–18 °C) und gut verschlossen. Olivenöl wird mit der Zeit "
          "nicht besser: Am besten genießt man es innerhalb von 12–18 Monaten nach der Pressung.</p>"
          "<p><strong>In der Küche:</strong> roh auf geröstetem Brot, Hülsenfrüchten, Gemüse und toskanischen Suppen – "
          "aber auch zum Kochen, denn dank seiner Antioxidantien verträgt Olivenöl extra vergine Hitze gut.</p>",
        "section--dark", label="assaggio")
)

OLIVICOLTORI = (
    section(split(
        h2("Ralph und Christina Striewski", "noi", "Wer wir sind")
        + "<p>Olivenbauern zu werden, war nie unser Plan. Ralph ist 41 Jahre lang geflogen – von 1981 bis 2022 als "
          "Pilot bei der Lufthansa, zuletzt als Kapitän auf dem Airbus A350. Christina ist Modedesignerin: Von 2013 bis "
          "2021 haben wir gemeinsam unsere Modefirma Arcanum Fashion geführt, die glänzende Mode produzierte "
          "(<a href='https://www.instagram.com/vanilla.pearl/' rel='noopener'>Christina auf Instagram</a>).</p>"
          "<p>Doch anscheinend haben uns die Olivenbäume gerufen. Nach dem ersten Gespräch und dem ersten Besuch auf "
          "der Villa Belvedere war uns sofort klar, dass dies unser Ort werden würde. Alles Weitere war Organisation – "
          "und seit dem Kauf 2024 jede Menge Arbeit und eine ganz neue Materie, die wir lernen.</p>"
          "<p>Wir sind keine geborenen Landwirte: Wir haben gelernt – und lernen jeden Tag – von den Nachbarn, von denen, "
          "die den Hain vor uns gepflegt haben, und von den Bäumen selbst. Mit ihnen führen wir eine Arbeit fort, die vor "
          "fast 300 Jahren begann, als die Mezzadri die ersten Olivenbäume pflanzten.</p>",
        fig("olivicoltori-ralph-christina", "Platzhalter: zwei Menschen und ein Hund zwischen Olivenbäumen im Sonnenuntergang",
            "Platzhalter für ein Foto von Ralph und Christina im Olivenhain")),
        label="noi")
    + section(
        h2("Was uns am Herzen liegt", "valori")
        + '<div class="trio">'
          "<div><h3>Respekt vor dem Hügel</h3><p>Wir pflegen die Trockenmauern, lassen Gras zwischen den Reihen wachsen "
          "und schützen Bienen, Insekten und Vögel, die im Olivenhain leben.</p></div>"
          "<div><h3>Qualität ohne Kompromisse</h3><p>Frühe Ernte, sofortige Verarbeitung in der eigenen Mühle, Laboranalysen: Wir wollen "
          "genau wissen, was in unserem Öl steckt.</p></div>"
          "<div><h3>Eine gemeinsame Geschichte</h3><p>Wir erzählen die Geschichte von Belvedere und der Menschen, die "
          "hier gelebt haben – denn Landschaft ist Erinnerung.</p></div>"
          "</div>",
        "section--cream", label="valori")
    + section(
        h2("Ein Jahr im Olivenhain", "anno", "Der Kalender")
        + calendar([
            ("Januar – März", "Schnitt", "Wir lichten die Kronen aus, damit Licht und Luft in den Baum gelangen."),
            ("April – Mai", "Blüte", "Die Bäume bedecken sich mit kleinen weißen Blüten – die empfindlichste Zeit."),
            ("Juni – August", "Fruchtansatz", "Die Früchte bilden sich und wachsen; wir kümmern uns um Boden und Mauern."),
            ("September", "Warten", "Wir beobachten die Reife und bereiten Netze, Kisten und Werkzeug vor."),
            ("Oktober – November", "Ernte und Pressung", "Wir ernten bei der Farbumstellung und pressen die Oliven noch am selben Tag in unserer eigenen Ölmühle."),
            ("Dezember", "Ruhe", "Die Bäume ruhen. Wir probieren das neue Öl und danken dem Hügel."),
        ]),
        "section--dark", label="anno")
    + section(split(
        h2("Die Olivenbäume von Belvedere", "olivi")
        + f"<p>Unser Olivenhain umfasst rund 2.300 Bäume auf ca. 7,5 Hektar Terrassen, zwischen 100 und "
          f"160 Metern Höhe. Manche Bäume sind ca. 300 Jahre alt: Die Mezzadri haben sie in "
          "ihre Lunette gepflanzt, und sie werden noch Früchte tragen, wenn wir längst nicht mehr hier sind.</p>"
          "<p>Als wir 2024 Villa und Olivenhain kauften, war – und ist immer noch – einiges zu tun, damit wir alle Bäume "
          "wieder abernten können. Mit der Azienda Agricola Villa Belvedere di Corliano haben wir auch die "
          "Bio-Zertifizierung und die eigene Ölmühle übernommen. Deshalb findet der gesamte Prozess – vom Ernten bis in "
          "die Flasche – bei uns auf dem Grundstück statt.</p>"
          f"<p>{link('energia', 'Die Eigenschaften unseres Öls entdecken →')}</p>",
        fig("raccolta-olive", "Menschen ernten Oliven auf Netzen unter einem Olivenbaum", "Die Ernte mit Freunden und Nachbarn"),
        rev=True), label="olivi")
)

FORM = {
    "name": "Vor- und Nachname", "email": "E-Mail", "topic": "Thema",
    "topics": ["Informationen zum Öl", "Geschichte der Villa", "Besuch im Olivenhain", "Presse und Medien", "Sonstiges"],
    "message": "Nachricht", "privacy": "Ich habe die {link} gelesen und bin einverstanden, dass meine Angaben zur Beantwortung meiner Anfrage verarbeitet werden.",
    "privacy_link": "Datenschutzerklärung", "send": "Nachricht senden", "required": "Pflichtfelder",
    "ok": "Vielen Dank! Ihre Nachricht wurde gesendet. Wir melden uns so bald wie möglich.",
    "err": "Leider ist ein Fehler aufgetreten. Bitte versuchen Sie es erneut oder schreiben Sie uns direkt per E-Mail.",
    "sending": "Wird gesendet …", "hp": "Dieses Feld bitte leer lassen",
}

CONTATTI = section(
    '<div class="contact-grid"><div class="prose">'
    + h2("Schreiben Sie uns", "scrivici")
    + "<p>Sie haben Fragen zu unserem Öl, zur Geschichte der Villa Belvedere oder zur Arbeit im Olivenhain? Sie "
      "möchten uns persönlich kennenlernen? Nutzen Sie das Formular oder schreiben Sie uns eine E-Mail.</p>"
    + note("Das Formular dient ausschließlich für Fragen und Informationen. Über diese Website werden keine "
           "Bestellungen angenommen und keine Verträge geschlossen.")
    + f"<h3>Direkter Kontakt</h3><address>{L['company']}<br>{L['street']}<br>{L['zip_city']}<br>Italien<br>"
      f"Tel.: {L['phone']}<br>E-Mail: {L['email']}</address>"
    + "<h3>Anfahrt</h3><p>Die Villa Belvedere liegt an den Hängen des Monte Pisano bei San Giuliano Terme, "
      "unweit von Pisa. Eine Wegbeschreibung schicken wir Ihnen gern auf Anfrage. Bitte melden Sie sich vor einem "
      "Besuch bei uns: Der Olivenhain ist ein Arbeitsort.</p>"
    + "</div>"
    + contact_form(FORM, "de")
    + "</div>", label="scrivici")

LEGAL_PAGE = section(
    '<div class="prose legal">'
    + "<h2>Angaben gemäß § 5 DDG</h2>"
    + f"<p><strong>{L['company']}</strong><br>Inhaber: {L['owner']}<br>Rechtsform: {L['legal_form']} (Einzelunternehmen)<br>{L['street']}<br>{L['zip_city']}<br>Italien</p>"
    + f"<h3>Kontakt</h3><p>Telefon: {L['phone']}<br>E-Mail: {L['email']}<br>PEC (zertifizierte E-Mail): {L['pec']}</p>"
    + f"<h3>Steuer- und Registerangaben</h3><p>Umsatzsteuer-Identifikationsnummer (Partita IVA): {L['vat']}<br>"
      f"Steuernummer (Codice fiscale): {L['tax_code']}<br>Registereintrag: {L['register']}, {L['rea']}</p>"
    + f"<h3>Öko-Kontrollstelle</h3><p>{L['bio_body']}<br>Code: {L['bio_code']}<br>Herkunftsangabe: {L['bio_origin']}</p>"
    + f"<h3>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h3><p>{L['content_responsible']}, {L['street']}, {L['zip_city']}, Italien</p>"
    + "<h3>Charakter dieser Website</h3><p>Diese Website dient ausschließlich der Information und der Vorstellung "
      "unseres Betriebs. Es werden keine Waren angeboten, keine Preise genannt und keine Fernabsatzverträge "
      "geschlossen.</p>"
    + "<h3>Verbraucherstreitbeilegung</h3><p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren "
      "vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>"
    + "<h3>Haftung für Inhalte</h3><p>Die Inhalte dieser Website wurden mit größter Sorgfalt erstellt. Für die "
      "Richtigkeit, Vollständigkeit und Aktualität können wir jedoch keine Gewähr übernehmen. Als Diensteanbieter "
      "sind wir gemäß § 7 Abs. 1 DDG für eigene Inhalte nach den allgemeinen Gesetzen verantwortlich. Die "
      "Informationen zu den Eigenschaften von Olivenöl sind allgemeiner Natur und stellen keine medizinische "
      "Beratung dar.</p>"
    + "<h3>Haftung für Links</h3><p>Diese Website enthält Links zu externen Websites Dritter, auf deren Inhalte "
      "wir keinen Einfluss haben. Für diese fremden Inhalte ist stets der jeweilige Anbieter verantwortlich. Zum "
      "Zeitpunkt der Verlinkung waren keine Rechtsverstöße erkennbar. Bei Bekanntwerden von Rechtsverletzungen "
      "entfernen wir derartige Links umgehend.</p>"
    + "<h3>Fotonachweise</h3>" + credits_list() + "<h3>Urheberrecht und Bildnachweis</h3><p>Die Texte, Bilder und Grafiken dieser Website unterliegen dem "
      "Urheberrecht. Jede Verwertung außerhalb der Grenzen des Urheberrechts bedarf unserer schriftlichen "
      "Zustimmung.</p>"
      "<p>Die Illustrationen von Personen und Landschaften sind digital erstellt und teilweise mit künstlicher "
      f"Intelligenz erzeugt; die dargestellten Personen sind fiktiv.</p>"
      "<p>Schrift: Cormorant Garamond (SIL Open Font License 1.1), lokal eingebunden.</p>"
    + f"<p class='fineprint'>Stand: {LEGAL_DATE['de']}</p>"
    + "</div>")

PRIVACY_PAGE = section(
    '<div class="prose legal">'
    + "<h2>1. Verantwortlicher</h2>"
    + f"<p>{L['company']}, {L['owner']}, {L['street']}, {L['zip_city']}, Italien – E-Mail: {L['email']}, "
      f"Telefon: {L['phone']}.</p>"
    + "<h2>2. Auf einen Blick</h2><p>Diese Website verwendet keine Cookies, keine Analyse- oder Tracking-Werkzeuge, "
      "keine Werbung, keine Social-Media-Plugins, keine Karten und keine Schriftarten von Drittanbietern. Die "
      "Schriften werden von unserem eigenen Server geladen. Personenbezogene Daten verarbeiten wir nur, soweit "
      "dies für die Bereitstellung der Website technisch nötig ist oder wenn Sie uns kontaktieren.</p>"
    + "<h2>3. Hosting und Server-Logfiles</h2><p>Diese Website wird bei GitHub Pages gehostet, einem Dienst der "
      "GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Beim Aufruf der Website "
      "werden automatisch technische Daten erfasst (IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Browser, "
      "Betriebssystem, Referrer-URL). Diese Daten dienen dem sicheren und stabilen Betrieb der Website.</p>"
      "<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an einer sicheren und "
      "effizienten Bereitstellung). GitHub kann Daten in den USA verarbeiten; GitHub ist nach dem EU-U.S. Data "
      "Privacy Framework zertifiziert (Angemessenheitsbeschluss, Art. 45 DSGVO). Weitere Informationen: "
      "<a href='https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement' rel='noopener'>Datenschutzerklärung von GitHub</a>.</p>"
    + "<h2>4. Kontaktformular</h2>"
    + f"<p>Wenn Sie uns über das Kontaktformular schreiben, werden Ihre Angaben (Name, E-Mail-Adresse, Thema, "
      f"Nachricht) über den Dienst {FP['name']} (USA) an uns per E-Mail weitergeleitet. Der Anbieter "
      f"kann Daten in den {FP['country']} verarbeiten; die Übermittlung erfolgt auf Grundlage des EU-U.S. Data "
      f"Privacy Framework bzw. von EU-Standardvertragsklauseln (Art. 46 DSGVO). Datenschutzhinweise des Anbieters: "
      f"<a href='{FP['privacy_url']}' rel='noopener'>{FP['privacy_url']}</a>.</p>"
      "<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO (vorvertragliche Maßnahmen auf Ihre Anfrage) sowie "
      "lit. f DSGVO (berechtigtes Interesse an der Beantwortung von Anfragen). Die Daten werden gelöscht, sobald "
      "Ihre Anfrage erledigt ist, sofern keine gesetzlichen Aufbewahrungspflichten bestehen.</p>"
    + "<h2>5. Kontakt per E-Mail oder Telefon</h2><p>Wenn Sie uns per E-Mail oder Telefon kontaktieren, verarbeiten "
      "wir Ihre Angaben nur zur Bearbeitung Ihrer Anfrage (Art. 6 Abs. 1 lit. b und f DSGVO) und löschen sie, "
      "sobald sie nicht mehr erforderlich sind.</p>"
    + "<h2>6. Cookies und lokale Speicherung</h2><p>Diese Website setzt keine Cookies und speichert keine "
      "Informationen auf Ihrem Endgerät (§ 25 TDDDG). Ein Cookie-Banner ist daher nicht erforderlich.</p>"
    + "<h2>7. Ihre Rechte</h2><p>Sie haben das Recht auf Auskunft (Art. 15), Berichtigung (Art. 16), Löschung "
      "(Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch "
      "(Art. 21 DSGVO). Eine erteilte Einwilligung können Sie jederzeit mit Wirkung für die Zukunft widerrufen.</p>"
      "<p><strong>Widerspruchsrecht:</strong> Sie können der Verarbeitung Ihrer Daten, die auf Art. 6 Abs. 1 lit. f "
      "DSGVO beruht, aus Gründen, die sich aus Ihrer besonderen Situation ergeben, jederzeit widersprechen.</p>"
    + f"<h2>8. Beschwerderecht</h2><p>Sie haben das Recht, sich bei einer Datenschutz-Aufsichtsbehörde zu beschweren, "
      f"insbesondere in dem Mitgliedstaat Ihres Aufenthaltsorts. Für uns zuständig ist: {L['authority_privacy']}.</p>"
    + "<h2>9. Sicherheit</h2><p>Diese Website nutzt aus Sicherheitsgründen eine SSL-/TLS-Verschlüsselung (HTTPS).</p>"
    + "<h2>10. Pflicht zur Bereitstellung</h2><p>Sie sind nicht verpflichtet, uns personenbezogene Daten zu "
      "überlassen. Ohne E-Mail-Adresse können wir Ihre Anfrage jedoch nicht beantworten.</p>"
    + f"<p class='fineprint'>Stand: {LEGAL_DATE['de']}</p>"
    + "</div>")

PAGES = {
    "home": {
        "title": "Villa Belvedere – Bio-Olivenöl extra vergine vom Monte Pisano",
        "description": "Villa Belvedere: altes Bauernhaus am Monte Pisano seit 1536. Biologisches Olivenöl extra "
                       "vergine mit vielen Polyphenolen – Geschichte, Olivenhain und Ölbauern.",
        "h1": "Villa Belvedere", "kicker": "Monte Pisano · seit 1536",
        "lead": "Biologisches Olivenöl extra vergine von den Terrassen eines Bauernhauses, das in den Sonnenuntergang blickt.",
        "hero": "vista-belvedere-sera",
        "hero_alt": "Abendlicher Blick von der Terrasse der Villa Belvedere über die Ebene unterhalb des Monte Pisano, mit Rosen und Olivenbäumen im Vordergrund und den Lichtern des Tals am Horizont",
        "hero_cta": '<p class="hero-cta">' + btn("conte", "Die Geschichte der Villa") + btn("energia", "Unser Öl", "btn btn--ghost") + "</p>",
        "images": ["vista-belvedere-sera", "villa-belvedere", "ritratto-conte", "ritratto-mezzadra",
                   "ritratto-frantoiano", "ritratto-raccoglitrice", "monte-pisano-panorama"],
        "body": HOME,
    },
    "conte": {
        "title": "Öl des Grafen – 500 Jahre Geschichte der Villa Belvedere",
        "description": "Seit 1536 Bauernhaus der Halbpächter am Monte Pisano, seit 1735 Olivenhain auf Lunette: die "
                       "Geschichte der Villa Belvedere, der Grafen della Seta und ihres Öls.",
        "h1": "Öl des Grafen", "nav": "Öl des Grafen", "kicker": "Fünf Jahrhunderte Geschichte",
        "lead": "Vom Bauernhaus der Halbpächter zum Bio-Olivenhain mit eigener Ölmühle: die Geschichte der Villa Belvedere.",
        "hero": "mezzadri-tramonto", "hero_alt": "Halbpächterfamilie mit Esel auf dem Kamm des Monte Pisano im Sonnenuntergang",
        "schema": "Article",
        "images": ["mezzadri-tramonto", "monte-pisano-panorama", "corliano-frantoio-1901", "corliano-facciata", "ramo-olivo"],
        "body": CONTE,
    },
    "energia": {
        "title": "Öl, Energie des Lebens – Bio-Olivenöl und Polyphenole",
        "description": "Was ein biologisches Olivenöl extra vergine mit hohem Polyphenolgehalt ausmacht: Kennwerte, "
                       "Oleocanthal, Hydroxytyrosol, frühe Ernte, Verkostung und Lagerung.",
        "h1": "Öl, Energie des Lebens", "nav": "Öl, Energie des Lebens", "kicker": "Bio extra vergine",
        "lead": "Bitter, scharf, duftend: alles Wissenswerte über ein biologisches Olivenöl extra vergine mit vielen Polyphenolen.",
        "hero": "olio-goccia", "hero_alt": "Grüngoldener Tropfen Olivenöl über Oliven und Olivenblättern",
        "schema": "Article",
        "images": ["olio-goccia", "ramo-olivo", "raccolta-olive"],
        "body": ENERGIA,
    },
    "olivicoltori": {
        "title": "Die Ölbauern – Ralph und Christina Striewski",
        "description": "Seit 2024 leben Ralph und Christina Striewski in der Villa Belvedere und bewirtschaften den "
                       "Olivenhain ökologisch. Unsere Geschichte.",
        "h1": "Die Ölbauern", "nav": "Die Ölbauern", "kicker": "Seit 2024 in Belvedere",
        "lead": "Ralph und Christina Striewski: ein neues Kapitel in einer Geschichte, die fünf Jahrhunderte zurückreicht.",
        "hero": "olivicoltori-ralph-christina", "hero_alt": "Zwei Menschen und ein Hund zwischen Olivenbäumen im Sonnenuntergang",
        "schema": "AboutPage",
        "images": ["olivicoltori-ralph-christina", "raccolta-olive"],
        "body": OLIVICOLTORI,
    },
    "contatti": {
        "title": "Kontakt – Villa Belvedere",
        "description": "Kontakt zur Villa Belvedere am Monte Pisano: Fragen zum biologischen Olivenöl extra vergine, "
                       "zur Geschichte der Villa oder zum Olivenhain.",
        "h1": "Kontakt", "nav": "Kontakt", "kicker": "Schreiben Sie uns",
        "lead": "Wir freuen uns auf Ihre Fragen.",
        "hero": "villa-belvedere", "hero_alt": "Das Bauernhaus der Villa Belvedere im Sonnenuntergang",
        "schema": "ContactPage",
        "body": CONTATTI,
    },
    "legal": {
        "title": "Impressum", "description": "Impressum der Azienda Agricola Villa Belvedere am Monte Pisano (Toskana).",
        "h1": "Impressum", "nav": "Impressum", "body": LEGAL_PAGE,
    },
    "privacy": {
        "title": "Datenschutzerklärung", "description": "Datenschutzerklärung nach DSGVO der Azienda Agricola Villa Belvedere.",
        "h1": "Datenschutzerklärung", "nav": "Datenschutz", "body": PRIVACY_PAGE,
    },
    "sitemap": {
        "title": "Sitemap", "description": "Alle Seiten der Website der Villa Belvedere im Überblick.",
        "h1": "Sitemap", "nav": "Sitemap", "body": "",
    },
}
