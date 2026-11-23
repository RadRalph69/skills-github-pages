"""Testi in italiano (lingua principale). Tutti i testi sono bozze da rivedere."""
from config import LEGAL as L, LEGAL_DATE, FORM_ENDPOINT, FORM_PROVIDER as FP
from lib import (fig, ph, link, section, split, h2, cards, portraits, facts, timeline, band,
                 table, note, calendar, btn, contact_form)

UI = {
    "skip": "Vai al contenuto",
    "menu": "Menu",
    "nav_label": "Navigazione principale",
    "lang_label": "Lingua",
    "breadcrumb": "Percorso",
    "nav": {"home": "Home", "conte": "L’Olio del Conte", "energia": "Olio, Energia della Vita",
            "olivicoltori": "Gli Olivicoltori", "contatti": "Contatti", "legal": "Note legali (Impressum)",
            "privacy": "Privacy", "sitemap": "Mappa del sito"},
    "footer_claim": "Olio extravergine d’oliva biologico dagli oliveti del Monte Pisano, dove si coltiva l’olivo dal 1536.",
    "vat": "P. IVA",
    "footer_nav": "Pagine",
    "footer_legal": "Informazioni legali",
    "info_only": "Questo sito ha esclusivamente scopo informativo. Tramite questo sito non si vendono prodotti "
                 "e non si concludono contratti.",
    "images_note": "Illustrazioni: immagini segnaposto create digitalmente",
    "og_alt": "Oliveto di Villa Belvedere sul Monte Pisano al tramonto",
    "nf_title": "Pagina non trovata",
    "nf_text": "La pagina che cerchi non esiste o è stata spostata.",
    "nf_link": "Torna alla home",
}

MORE = "Scopri di più"

# --------------------------------------------------------------------------- #
HOME = (
    section(split(
        h2("Un podere, cinque secoli, un olio", "intro", "Benvenuti a Villa Belvedere")
        + "<p>Sulle pendici del Monte Pisano, tra Pisa e Lucca, sorge Villa Belvedere: un’antica casa colonica "
          "con la sua colombaia, circondata da terrazze di olivi che guardano verso la pianura e, nelle giornate "
          "limpide, fino al mare.</p>"
          "<p>Dal 1536 queste terre appartenevano al frantoio e al palazzo del Conte di Pisa. Generazioni di mezzadri "
          "hanno potato, raccolto e portato le olive a valle. Oggi continuiamo quel lavoro con metodi biologici e con "
          "lo stesso rispetto per la collina.</p>"
          f"<p>{link('conte', 'Leggi la storia della Villa →')}</p>",
        fig("villa-belvedere", "La casa colonica di Villa Belvedere con la colombaia, tra cipressi e olivi, nella luce del tramonto",
            "La casa colonica con la sua colombaia")),
        "section--cream", label="intro")
    + '<section class="facts-band" aria-label="Villa Belvedere in cifre"><div class="wrap">'
    + facts([("1536", "anno di fondazione del podere"), (ph("N") + " olivi", "su terrazze in pietra a secco"),
             (ph("xxx") + " m", "di altitudine sul Monte Pisano"), ("Bio", "agricoltura biologica certificata")])
    + "</div></section>"
    + section(
        h2("Tre storie, un solo olio", "storie")
        + cards([
            ("conte", "frantoio-antico", "L’antica macina in pietra del frantoio del Conte", "L’Olio del Conte",
             "Cinquecento anni di storia: dalla casa colonica dei mezzadri al frantoio e al palazzo del Conte di Pisa."),
            ("energia", "olio-goccia", "Una goccia di olio verde-oro sopra olive e foglie", "Olio, Energia della Vita",
             "Che cosa rende speciale un extravergine biologico ricco di polifenoli – spiegato con semplicità."),
            ("olivicoltori", "olivicoltori-ralph-christina", "Due persone tra gli olivi al tramonto", "Gli Olivicoltori",
             "Ralph e Christina Striewski: dal 2024 a Belvedere, con le mani nella terra e lo sguardo sugli olivi."),
        ], MORE), label="storie")
    + section(
        h2("Le voci della collina", "voci", "Chi ha abitato questo colle")
        + '<p class="section-intro">Per cinque secoli il Monte Pisano è stato casa di conti e contadini, di frantoiani e '
          "raccoglitrici. Abbiamo immaginato i loro volti e le loro voci.</p>"
        + portraits([
            ("ritratto-conte", "Ritratto illustrato di un nobile rinascimentale con berretto nero e mantello rosso",
             "Il Conte", "1536 – il proprietario",
             "«Ho voluto queste terrazze perché il sole della sera è il più generoso con gli olivi.»"),
            ("ritratto-mezzadra", "Ritratto illustrato di una contadina con fazzoletto rosso e cesto di olive",
             "La mezzadra", "1700 – la famiglia del podere",
             "«Metà del raccolto al padrone, metà a noi. Ma la fatica, quella era tutta nostra.»"),
            ("ritratto-frantoiano", "Ritratto illustrato di un anziano frantoiano con berretto e grembiule",
             "Il frantoiano", "1900 – il mastro del frantoio",
             "«L’olio buono si sente in gola: se pizzica, è vivo.»"),
            ("ritratto-raccoglitrice", "Ritratto illustrato di una giovane raccoglitrice con cappello di paglia",
             "La raccoglitrice", "oggi – la raccolta",
             "«A ottobre la collina si riempie di voci, di reti e di risate.»"),
        ])
        + '<p class="fineprint">Personaggi immaginari. Illustrazioni create digitalmente a scopo evocativo.</p>',
        "section--dark", label="voci")
    + band("monte-pisano-panorama", "Vista dal Monte Pisano sulla pianura di Pisa e sul mare al tramonto",
           "Da quassù si vede la pianura che un tempo era palude, la torre di Pisa e, la sera, il mare che diventa d’oro.",
           "Villa Belvedere, Monte Pisano")
    + section(
        '<div class="cta-box">' + h2("Venite a conoscerci", "visita")
        + "<p>Avete domande sul nostro olio, sulla storia della Villa o sul lavoro nell’oliveto? Scriveteci: "
          "rispondiamo volentieri.</p>" + btn("contatti", "Scrivici") + "</div>",
        "section--cream", label="visita")
)

# --------------------------------------------------------------------------- #
CONTE = (
    section(split(
        h2("Una casa colonica sulle colline di Pisa", "origini", "Le origini")
        + "<p>Nel 1536 la pianura di Pisa era ancora in gran parte paludosa e, in certe stagioni, sommersa dalle acque. "
          "Per mettere a coltura le colline del Monte Pisano vennero chiamate famiglie di lavoratori poveri: "
          "ricevevano una casa e un pezzo di terra, in cambio del lavoro e di una parte del raccolto.</p>"
          "<p>Così nacque Belvedere: una casa colonica in pietra, con stalla, aia e la tipica colombaia, costruita "
          "dove lo sguardo si apre sulla valle – da qui il suo nome. Il podere apparteneva al frantoio e al palazzo "
          f"del Conte di Pisa, {ph('nome della famiglia comitale, da verificare')}.</p>",
        fig("monte-pisano-panorama", "Panorama dal Monte Pisano verso la pianura pisana e il mare", "La pianura di Pisa vista dal Monte Pisano")),
        label="origini")
    + section(
        h2("Cinque secoli in breve", "cronologia", "Cronologia")
        + timeline([
            ("1536", "La fondazione", "Il Conte di Pisa fa costruire la casa colonica e affida le terrazze a una famiglia di mezzadri. I primi olivi vengono piantati sui muri a secco."),
            ("XVI–XVII sec.", "Bonifica e olivi", "Mentre in pianura si scavano fossi e canali, sul monte crescono gli oliveti. L’olio viene portato a dorso d’asino al frantoio del Conte."),
            ("XVIII–XIX sec.", "Il tempo della mezzadria", "Il raccolto si divide a metà tra padrone e famiglia colonica. In casa vivono fino a tre generazioni, che conoscono ogni albero per nome."),
            ("1964", "La fine di un’epoca", "La legge vieta nuovi contratti di mezzadria. Molte famiglie lasciano le colline per la città; tanti oliveti restano senza cure."),
            (ph("anno"), "Anni di silenzio", f"{ph('Breve racconto degli ultimi decenni della Villa – proprietari, restauri, abbandono.')}"),
            ("2024", "Una nuova stagione", "Ralph e Christina Striewski arrivano a Belvedere e riprendono la cura degli olivi, secondo i principi dell’agricoltura biologica."),
        ]),
        "section--cream", label="cronologia")
    + section(split(
        h2("Il frantoio e il palazzo del Conte", "frantoio")
        + "<p>Le olive di Belvedere non venivano spremute in casa. Scendevano a valle nelle ceste, fino al frantoio "
          "del Conte: un grande ambiente in pietra, buio e caldo, dove una macina di granito mossa da un animale – e "
          "più tardi dall’acqua – riduceva i frutti in pasta. La pasta veniva stesa sui fiscoli e pressata; l’olio "
          "riposava negli orci di terracotta.</p>"
          "<p>Una parte dell’olio prendeva la strada del palazzo di città, a Pisa, dove illuminava le lampade, "
          "condiva la tavola del Conte e veniva scambiato con altre merci. Il resto restava alla famiglia del podere: "
          "per tutto l’anno era cibo, medicina e luce.</p>",
        fig("frantoio-antico", "Interno di un antico frantoio con macina in pietra e orci di terracotta", "Un antico frantoio: macina, vasca e orci"),
        rev=True), label="frantoio")
    + section(split(
        h2("La vita dei mezzadri", "mezzadri")
        + "<p>La giornata seguiva il sole. Si potava in primavera, si zappava d’estate, si raccoglieva in autunno "
          "battendo i rami con lunghe pertiche sopra teli stesi a terra. Le donne accudivano l’orto, gli animali e "
          "la casa; i bambini aiutavano a raccogliere le olive cadute, una per una.</p>"
          "<p>Il contratto di mezzadria legava famiglia e podere per generazioni. Era un patto duro, ma ha "
          "plasmato il paesaggio che vediamo ancora oggi: i muri a secco, le terrazze, i sentieri, gli olivi "
          "che qualcuno ha piantato pensando ai propri nipoti.</p>"
          f"<p>{link('olivicoltori', 'Chi si prende cura degli olivi oggi →')}</p>",
        fig("mezzadri-tramonto", "Silhouette di una famiglia di contadini con un asino sul crinale al tramonto", "Una famiglia di mezzadri al rientro dai campi")),
        "section--dark", label="mezzadri")
    + band("ramo-olivo", "Ramo di olivo con olive verdi e scure controluce",
           "Un olivo non appartiene a chi lo pianta, ma a chi verrà dopo.", "Detto contadino toscano")
    + section(note("<strong>Nota:</strong> il racconto storico è una bozza basata sulla tradizione orale e sulla storia "
                   f"generale del Monte Pisano. {ph('Fonti d’archivio, date e nomi da verificare e integrare.')}"),
              label=None)
)

# --------------------------------------------------------------------------- #
ENERGIA = (
    section(split(
        h2("Che cos’è un olio extravergine d’oliva", "evo", "Le basi")
        + "<p>L’olio extravergine d’oliva è il succo dell’oliva, ottenuto <strong>solo con mezzi meccanici</strong>: "
          "le olive vengono lavate, frante, gramolate e separate, senza solventi e senza raffinazione. È la "
          "categoria più alta prevista dalla normativa europea.</p>"
          "<p>Per potersi chiamare «extravergine», un olio deve rispettare parametri chimici precisi e superare "
          "l’esame di un panel di assaggiatori: deve avere un fruttato percepibile e <strong>nessun difetto</strong>.</p>",
        fig("olio-goccia", "Goccia di olio extravergine verde-oro sopra olive e foglie", "Il colore verde-oro dell’olio appena franto")),
        label="evo")
    + section(
        h2("I parametri di legge", "parametri")
        + table("Limiti per la categoria extravergine (Reg. delegato (UE) 2022/2104) e valori del nostro olio",
                ["Parametro", "Limite extravergine", "Il nostro olio " + ph("annata")],
                [["Acidità libera (acido oleico)", "≤ 0,80 %", ph("…")],
                 ["Numero di perossidi", "≤ 20 mEq O₂/kg", ph("…")],
                 ["K232", "≤ 2,50", ph("…")],
                 ["K270", "≤ 0,22", ph("…")],
                 ["Mediana dei difetti", "= 0", ph("…")],
                 ["Mediana del fruttato", "> 0", ph("…")],
                 ["Polifenoli totali", "nessun limite di legge", ph("… mg/kg")]],
                "Inserire i valori del certificato di analisi del laboratorio. Valori più bassi di acidità e perossidi indicano olive sane e una lavorazione rapida."),
        "section--cream", label="parametri")
    + section(split(
        h2("Polifenoli: la forza dell’olio", "polifenoli", "Il cuore della qualità")
        + "<p>I polifenoli sono sostanze naturali che l’olivo produce per proteggere i propri frutti. Nell’olio "
          "extravergine se ne trovano decine; i più noti sono <strong>idrossitirosolo</strong>, <strong>tirosolo</strong>, "
          "<strong>oleuropeina</strong> (nelle sue forme derivate), <strong>oleocantale</strong> e <strong>oleaceina</strong>.</p>"
          "<p>Sono loro a dare all’olio le note <strong>amare</strong> e <strong>piccanti</strong>: quel pizzicore in gola "
          "dopo l’assaggio è dovuto soprattutto all’oleocantale. Un olio ricco di polifenoli è anche più stabile: "
          "si ossida più lentamente e conserva più a lungo i suoi profumi.</p>"
          "<p>La quantità dipende dalla varietà, dal grado di maturazione, dal clima e soprattutto dalla "
          "lavorazione. Per questo raccogliamo presto e portiamo le olive al frantoio nel giro di poche ore.</p>",
        fig("ramo-olivo", "Ramo di olivo con olive verdi e invaiate", "Olive raccolte all’invaiatura: il momento dei polifenoli"),
        rev=True), label="polifenoli")
    + section(
        h2("Cosa dice la scienza – e cosa dice la legge", "claim")
        + note("<p><strong>Indicazione sulla salute autorizzata (Reg. (UE) n. 432/2012):</strong> «I polifenoli dell’olio "
               "d’oliva contribuiscono alla protezione dei lipidi ematici dallo stress ossidativo.» L’effetto benefico "
               "si ottiene con l’assunzione giornaliera di 20 g di olio d’oliva.</p>"
               "<p>L’indicazione può essere utilizzata solo per oli che contengono <strong>almeno 5 mg di idrossitirosolo "
               "e suoi derivati per 20 g</strong> di olio (pari a 250 mg/kg). "
               f"Il nostro olio: {ph('valore da analisi di laboratorio – usare il claim solo se il limite è raggiunto')}.</p>",
               "note note--claim")
        + "<p>L’olio extravergine d’oliva è un elemento centrale della dieta mediterranea. È composto in gran parte da "
          "<strong>acido oleico</strong>, un acido grasso monoinsaturo, e contiene naturalmente <strong>vitamina E</strong> "
          "(tocoferoli), <strong>squalene</strong> e <strong>pigmenti</strong> come clorofille e carotenoidi.</p>"
          + '<p class="fineprint">Le informazioni di questa pagina hanno carattere generale e non sostituiscono il parere '
            "di un medico o di un nutrizionista. Una dieta varia ed equilibrata e uno stile di vita sano sono importanti.</p>",
        "section--cream", label="claim")
    + section(split(
        h2("Biologico, dalla pianta all’olio", "bio", "Il nostro metodo")
        + "<ul class='ticks'>"
          "<li><strong>Agricoltura biologica</strong> secondo il Reg. (UE) 2018/848: niente diserbanti chimici né "
          "fertilizzanti di sintesi; inerbimento, sovescio e potature equilibrate.</li>"
          f"<li><strong>Organismo di controllo:</strong> {L['bio_body']} – codice {L['bio_code']}.</li>"
          "<li><strong>Raccolta precoce</strong> tra ottobre e inizio novembre, quando le olive iniziano a cambiare colore.</li>"
          "<li><strong>A mano o con agevolatori</strong>, su reti: nessuna oliva raccolta da terra.</li>"
          "<li><strong>Molitura entro poche ore</strong> in frantoio a ciclo continuo, con estrazione a freddo "
          "(temperatura inferiore a 27 °C).</li>"
          "<li><strong>Conservazione</strong> in contenitori di acciaio inox sotto gas inerte, al riparo da luce e calore.</li>"
          "</ul>"
          f"<p>Varietà del nostro oliveto: {ph('es. Frantoio, Leccino, Moraiolo, Pendolino')}.</p>",
        fig("raccolta-olive", "Raccolta delle olive su reti sotto un grande olivo", "La raccolta: reti, pertiche e cassette")),
        label="bio")
    + section(
        h2("Come riconoscere un grande olio", "assaggio", "L’assaggio")
        + '<div class="trio">'
          "<div><h3>Fruttato</h3><p>Profumo di oliva fresca, erba tagliata, carciofo, mandorla verde, pomodoro. "
          "Nel fruttato «verde» si riconosce la raccolta precoce.</p></div>"
          "<div><h3>Amaro</h3><p>Una nota amara sulla lingua è un pregio, non un difetto: indica olive sane e "
          "ricche di polifenoli.</p></div>"
          "<div><h3>Piccante</h3><p>Il pizzicore in gola, a volte con un piccolo colpo di tosse, è il segno "
          "dell’oleocantale. Più è intenso, più l’olio è giovane e vivo.</p></div>"
          "</div>"
          "<p><strong>Come conservarlo:</strong> lontano da luce e calore, tra 14 e 18 °C, ben chiuso. L’olio non "
          "migliora con il tempo: va gustato preferibilmente entro 12–18 mesi dalla molitura.</p>"
          "<p><strong>In cucina:</strong> a crudo su pane tostato, legumi, verdure e zuppe toscane; ma anche in "
          "cottura, perché grazie agli antiossidanti l’extravergine resiste bene al calore.</p>",
        "section--dark", label="assaggio")
)

# --------------------------------------------------------------------------- #
OLIVICOLTORI = (
    section(split(
        h2("Ralph e Christina Striewski", "noi", "Chi siamo")
        + "<p>Nel 2024 abbiamo lasciato " + ph("città/regione di provenienza") + " e ci siamo trasferiti a Belvedere. "
          "Ci ha conquistati la luce della sera sugli olivi, il silenzio delle terrazze e la sensazione di "
          "entrare in una storia molto più grande di noi.</p>"
          "<p>" + ph("Breve presentazione personale: professioni precedenti, cosa vi ha portato in Italia, cosa vi lega alla terra.") + "</p>"
          "<p>Non siamo nati contadini: abbiamo imparato – e impariamo ogni giorno – dai vicini, dai frantoiani e "
          "dagli alberi stessi. Con loro portiamo avanti un lavoro iniziato quasi cinquecento anni fa.</p>",
        fig("olivicoltori-ralph-christina", "Segnaposto: due persone e un cane tra gli olivi al tramonto",
            "Segnaposto per una foto di Ralph e Christina nell’oliveto")),
        label="noi")
    + section(
        h2("Cosa ci sta a cuore", "valori")
        + '<div class="trio">'
          "<div><h3>Rispetto per la collina</h3><p>Curiamo i muri a secco, lasciamo crescere l’erba tra i filari e "
          "proteggiamo api, insetti e uccelli che vivono nell’oliveto.</p></div>"
          "<div><h3>Qualità senza compromessi</h3><p>Raccolta precoce, molitura immediata, analisi di laboratorio: "
          "vogliamo sapere esattamente cosa c’è nel nostro olio.</p></div>"
          "<div><h3>Una storia condivisa</h3><p>Raccontiamo la storia di Belvedere e delle persone che l’hanno "
          "vissuta, perché il paesaggio è memoria.</p></div>"
          "</div>",
        "section--cream", label="valori")
    + section(
        h2("Un anno nell’oliveto", "anno", "Il calendario")
        + calendar([
            ("Gennaio – Marzo", "Potatura", "Alleggeriamo le chiome perché luce e aria entrino nella pianta."),
            ("Aprile – Maggio", "Fioritura", "Gli olivi si coprono di piccoli fiori bianchi: è il momento più delicato."),
            ("Giugno – Agosto", "Allegagione", "I frutti si formano e crescono; ci prendiamo cura del suolo e dei muri."),
            ("Settembre", "Attesa", "Controlliamo la maturazione e prepariamo reti, cassette e attrezzi."),
            ("Ottobre – Novembre", "Raccolta e molitura", "Raccogliamo all’invaiatura e portiamo le olive al frantoio in giornata."),
            ("Dicembre", "Riposo", "Gli alberi si riposano. Noi assaggiamo il nuovo olio e ringraziamo la collina."),
        ]),
        "section--dark", label="anno")
    + section(split(
        h2("Gli olivi di Belvedere", "olivi")
        + f"<p>Il nostro oliveto conta circa {ph('N')} piante su {ph('x')} ettari di terrazze, tra {ph('xxx')} e "
          f"{ph('xxx')} metri di altitudine. Alcuni alberi hanno {ph('età stimata')} anni: hanno visto passare "
          "generazioni di mezzadri e porteranno frutti per chi verrà dopo di noi.</p>"
          f"<p>{link('energia', 'Scopri le caratteristiche del nostro olio →')}</p>",
        fig("raccolta-olive", "Persone che raccolgono olive su reti sotto un olivo", "La raccolta con amici e vicini"),
        rev=True), label="olivi")
)

# --------------------------------------------------------------------------- #
FORM = {
    "name": "Nome e cognome", "email": "E-mail", "topic": "Argomento",
    "topics": ["Informazioni sull’olio", "Storia della Villa", "Visita all’oliveto", "Stampa e media", "Altro"],
    "message": "Messaggio", "privacy": "Ho letto l’{link} e acconsento al trattamento dei miei dati per rispondere alla mia richiesta.",
    "privacy_link": "informativa sulla privacy", "send": "Invia messaggio", "required": "Campi obbligatori",
    "ok": "Grazie! Il tuo messaggio è stato inviato. Ti risponderemo al più presto.",
    "err": "Si è verificato un errore. Riprova oppure scrivici direttamente via e-mail.",
    "sending": "Invio in corso…", "hp": "Non compilare questo campo",
}

CONTATTI = section(
    '<div class="contact-grid"><div class="prose">'
    + h2("Scriveteci", "scrivici")
    + "<p>Avete domande sul nostro olio, sulla storia di Villa Belvedere o sul lavoro nell’oliveto? Desiderate "
      "conoscerci di persona? Usate il modulo oppure scriveteci un’e-mail.</p>"
    + note("Il modulo serve esclusivamente per domande e informazioni. Tramite questo sito non si accettano "
           "ordini e non si concludono contratti.")
    + f"<h3>Contatto diretto</h3><address>{L['company']}<br>{L['street']}<br>{L['zip_city']}<br>{L['country']}<br>"
      f"Tel.: {L['phone']}<br>E-mail: {L['email']}</address>"
    + "<h3>Come raggiungerci</h3><p>Villa Belvedere si trova sulle pendici del Monte Pisano, "
    + ph("indicazioni stradali, es. a 15 minuti da Pisa, uscita …") + ". Per una visita vi preghiamo di "
      "contattarci prima: l’oliveto è un luogo di lavoro.</p>"
    + "</div>"
    + contact_form(FORM, "it")
    + "</div>", label="scrivici")

# --------------------------------------------------------------------------- #
LEGAL_PAGE = section(
    '<div class="prose legal">'
    + "<h2>Informazioni ai sensi del § 5 DDG (Germania) e dell’art. 2250 c.c. / art. 35 DPR 633/1972 (Italia)</h2>"
    + f"<p><strong>{L['company']}</strong><br>di {L['owner']}<br>{L['legal_form']}<br>{L['street']}<br>{L['zip_city']}<br>{L['country']}</p>"
    + f"<h3>Contatti</h3><p>Telefono: {L['phone']}<br>E-mail: {L['email']}<br>PEC: {L['pec']}</p>"
    + f"<h3>Dati fiscali e registro</h3><p>Partita IVA: {L['vat']}<br>Codice fiscale: {L['tax_code']}<br>"
      f"Iscrizione: {L['register']}, {L['rea']}</p>"
    + f"<h3>Controllo biologico</h3><p>Organismo di controllo: {L['bio_body']}<br>Codice: {L['bio_code']}</p>"
    + f"<h3>Responsabile dei contenuti</h3><p>{L['content_responsible']}, {L['street']}, {L['zip_city']} (§ 18 c. 2 MStV)</p>"
    + "<h3>Natura del sito</h3><p>Questo sito ha esclusivamente scopo informativo e di presentazione dell’azienda. "
      "Non offre prodotti in vendita, non indica prezzi e non consente di concludere contratti a distanza.</p>"
    + "<h3>Risoluzione delle controversie</h3><p>Non siamo obbligati né disponibili a partecipare a procedure di "
      "risoluzione delle controversie dinanzi a un organismo di conciliazione per i consumatori.</p>"
    + "<h3>Responsabilità per i contenuti</h3><p>I contenuti di questo sito sono stati redatti con la massima cura. "
      "Non possiamo tuttavia garantirne la completezza, l’esattezza e l’attualità. Le informazioni sulle "
      "proprietà dell’olio hanno carattere generale e non costituiscono consiglio medico.</p>"
    + "<h3>Responsabilità per i link</h3><p>Il sito contiene link a siti esterni, sui cui contenuti non abbiamo "
      "alcuna influenza. Al momento del collegamento non erano riconoscibili contenuti illeciti. In caso di "
      "segnalazione di violazioni, rimuoveremo immediatamente tali link.</p>"
    + "<h3>Diritto d’autore e immagini</h3><p>Testi, immagini e grafiche di questo sito sono protetti dal diritto "
      "d’autore. Ogni utilizzo al di fuori dei limiti di legge richiede il nostro consenso scritto.</p>"
      "<p>Le illustrazioni di persone e paesaggi sono immagini create digitalmente e, in parte, generate con "
      f"intelligenza artificiale; i personaggi raffigurati sono immaginari. {ph('Crediti fotografici, se presenti')}.</p>"
      "<p>Font: Cormorant Garamond (SIL Open Font License 1.1), ospitato localmente.</p>"
    + f"<p class='fineprint'>Aggiornamento: {LEGAL_DATE['it']}</p>"
    + "</div>", label=None)

PRIVACY_PAGE = section(
    '<div class="prose legal">'
    + "<h2>1. Titolare del trattamento</h2>"
    + f"<p>{L['company']}, {L['owner']}, {L['street']}, {L['zip_city']}, {L['country']} – E-mail: {L['email']}, "
      f"Tel.: {L['phone']}.</p>"
    + "<h2>2. In sintesi</h2><p>Questo sito non utilizza cookie, strumenti di analisi, pubblicità, social plugin, "
      "mappe o caratteri tipografici di terzi. I font sono ospitati sul nostro server. Trattiamo dati personali "
      "soltanto quando ciò è tecnicamente necessario per mostrare il sito o quando ci contattate.</p>"
    + "<h2>3. Hosting e file di log</h2><p>Il sito è ospitato da GitHub Pages, un servizio di GitHub, Inc., "
      "88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Quando visitate il sito, il server registra "
      "automaticamente dati tecnici (indirizzo IP, data e ora, pagina richiesta, browser, sistema operativo, "
      "sito di provenienza). Questi dati servono a garantire il funzionamento e la sicurezza del sito.</p>"
      "<p>Base giuridica: art. 6, par. 1, lett. f) GDPR (legittimo interesse a una presentazione sicura ed "
      "efficiente). GitHub può trattare dati negli USA; GitHub è certificata ai sensi dell’EU-U.S. Data Privacy "
      "Framework (art. 45 GDPR). Ulteriori informazioni: "
      "<a href='https://docs.github.com/it/site-policy/privacy-policies/github-general-privacy-statement' rel='noopener'>informativa privacy di GitHub</a>.</p>"
    + "<h2>4. Modulo di contatto</h2>"
    + f"<p>Se ci scrivete tramite il modulo di contatto, i dati inseriti (nome, e-mail, argomento, messaggio) "
      f"vengono trasmessi tramite il servizio {FP['name']}, {FP['address']}, che ce li inoltra via e-mail. "
      f"Il fornitore può trattare i dati in {FP['country']}; il trasferimento avviene sulla base "
      f"dell’EU-U.S. Data Privacy Framework o di clausole contrattuali standard (art. 46 GDPR). "
      f"Informativa del fornitore: <a href='{FP['privacy_url']}' rel='noopener'>{FP['privacy_url']}</a>.</p>"
      "<p>Base giuridica: art. 6, par. 1, lett. b) GDPR (misure precontrattuali su richiesta) e lett. f) "
      "(legittimo interesse a rispondere alle richieste). I dati vengono cancellati quando la richiesta è "
      "evasa, salvo obblighi di conservazione previsti dalla legge.</p>"
    + "<h2>5. Contatto via e-mail o telefono</h2><p>Se ci contattate via e-mail o telefono, trattiamo i vostri dati "
      "solo per rispondere alla richiesta (art. 6, par. 1, lett. b) e f) GDPR) e li cancelliamo quando non sono "
      "più necessari.</p>"
    + "<h2>6. Cookie e memorizzazione locale</h2><p>Questo sito non imposta cookie e non salva informazioni sul "
      "vostro dispositivo. Per questo non è necessario un banner per i cookie.</p>"
    + "<h2>7. I vostri diritti</h2><p>Avete diritto di accesso (art. 15), rettifica (art. 16), cancellazione "
      "(art. 17), limitazione (art. 18), portabilità (art. 20) e opposizione (art. 21 GDPR). Se il trattamento si "
      "basa sul consenso, potete revocarlo in qualsiasi momento con effetto per il futuro.</p>"
      "<p><strong>Diritto di opposizione:</strong> potete opporvi in qualsiasi momento, per motivi legati alla vostra "
      "situazione particolare, ai trattamenti basati sull’art. 6, par. 1, lett. f) GDPR.</p>"
    + f"<h2>8. Reclamo</h2><p>Avete il diritto di proporre reclamo a un’autorità di controllo, in particolare: "
      f"{L['authority_privacy']}.</p>"
    + "<h2>9. Sicurezza</h2><p>Il sito utilizza una connessione cifrata (HTTPS/TLS).</p>"
    + "<h2>10. Obbligo di fornire i dati</h2><p>Non siete obbligati a fornirci dati personali. Senza un indirizzo "
      "e-mail, però, non possiamo rispondere alla vostra richiesta.</p>"
    + f"<p class='fineprint'>Aggiornamento: {LEGAL_DATE['it']}</p>"
    + "</div>", label=None)

# --------------------------------------------------------------------------- #
PAGES = {
    "home": {
        "title": "Villa Belvedere – Olio extravergine d’oliva biologico del Monte Pisano",
        "description": "Villa Belvedere: antica casa colonica sul Monte Pisano dal 1536. Olio extravergine d’oliva "
                       "biologico ricco di polifenoli, storia, oliveto e olivicoltori.",
        "h1": "Villa Belvedere", "kicker": "Monte Pisano · dal 1536",
        "lead": "Olio extravergine d’oliva biologico, nato tra le terrazze di una casa colonica che guarda il tramonto.",
        "hero": "hero-oliveto-tramonto",
        "hero_alt": "Oliveto sul Monte Pisano al tramonto, con la casa colonica sulla collina e persone che raccolgono olive",
        "hero_cta": '<p class="hero-cta">' + btn("conte", "La storia della Villa") + btn("energia", "Il nostro olio", "btn btn--ghost") + "</p>",
        "images": ["hero-oliveto-tramonto", "villa-belvedere", "ritratto-conte", "ritratto-mezzadra",
                   "ritratto-frantoiano", "ritratto-raccoglitrice", "monte-pisano-panorama"],
        "body": HOME,
    },
    "conte": {
        "title": "L’Olio del Conte – 500 anni di storia di Villa Belvedere",
        "description": "Dal 1536 casa colonica dei mezzadri sul Monte Pisano, legata al frantoio e al palazzo del Conte "
                       "di Pisa: la storia di Villa Belvedere e del suo olio.",
        "h1": "L’Olio del Conte", "nav": "L’Olio del Conte", "kicker": "Cinque secoli di storia",
        "lead": "Da casa colonica dei mezzadri a oliveto biologico: la storia di Villa Belvedere, del frantoio e del palazzo del Conte di Pisa.",
        "hero": "mezzadri-tramonto", "hero_alt": "Famiglia di mezzadri con un asino sul crinale del Monte Pisano al tramonto",
        "schema": "Article",
        "images": ["mezzadri-tramonto", "monte-pisano-panorama", "frantoio-antico", "ramo-olivo"],
        "body": CONTE,
    },
    "energia": {
        "title": "Olio, Energia della Vita – extravergine bio e polifenoli",
        "description": "Cosa rende speciale un extravergine biologico ricco di polifenoli: parametri, oleocantale, "
                       "idrossitirosolo, raccolta precoce, assaggio e conservazione.",
        "h1": "Olio, Energia della Vita", "nav": "Olio, Energia della Vita", "kicker": "Extravergine biologico",
        "lead": "Amaro, piccante, profumato: tutto quello che c’è da sapere su un extravergine biologico ricco di polifenoli.",
        "hero": "olio-goccia", "hero_alt": "Goccia di olio extravergine verde-oro sopra olive e foglie di olivo",
        "schema": "Article",
        "images": ["olio-goccia", "ramo-olivo", "raccolta-olive"],
        "body": ENERGIA,
    },
    "olivicoltori": {
        "title": "Gli Olivicoltori – Ralph e Christina Striewski",
        "description": "Dal 2024 Ralph e Christina Striewski vivono a Villa Belvedere e curano l’oliveto secondo i "
                       "principi dell’agricoltura biologica. La nostra storia.",
        "h1": "Gli Olivicoltori", "nav": "Gli Olivicoltori", "kicker": "Dal 2024 a Belvedere",
        "lead": "Ralph e Christina Striewski: una nuova pagina in una storia lunga cinque secoli.",
        "hero": "olivicoltori-ralph-christina", "hero_alt": "Due persone e un cane tra gli olivi al tramonto",
        "schema": "AboutPage",
        "images": ["olivicoltori-ralph-christina", "raccolta-olive"],
        "body": OLIVICOLTORI,
    },
    "contatti": {
        "title": "Contatti – Villa Belvedere",
        "description": "Contattate Villa Belvedere sul Monte Pisano: domande sull’olio extravergine biologico, sulla "
                       "storia della Villa o sull’oliveto.",
        "h1": "Contatti", "nav": "Contatti", "kicker": "Scriveteci",
        "lead": "Siamo felici di rispondere alle vostre domande.",
        "hero": "villa-belvedere", "hero_alt": "La casa colonica di Villa Belvedere al tramonto",
        "schema": "ContactPage",
        "body": CONTATTI,
    },
    "legal": {
        "title": "Note legali (Impressum)", "description": "Note legali e Impressum di Azienda Agricola Villa Belvedere.",
        "h1": "Note legali", "nav": "Note legali", "body": LEGAL_PAGE,
    },
    "privacy": {
        "title": "Informativa sulla privacy", "description": "Informativa sul trattamento dei dati personali ai sensi del GDPR.",
        "h1": "Informativa sulla privacy", "nav": "Privacy", "body": PRIVACY_PAGE,
    },
    "sitemap": {
        "title": "Mappa del sito", "description": "Tutte le pagine del sito di Villa Belvedere in sintesi.",
        "h1": "Mappa del sito", "nav": "Mappa del sito", "body": "",
    },
}
