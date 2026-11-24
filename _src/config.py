"""
ZENTRALE EINSTELLUNGEN – hier zuerst anpassen, dann `python3 _src/build.py` ausführen.

Alles in eckigen Klammern [ ... ] ist ein Platzhalter und erscheint auf der Website
gelb markiert, bis er ersetzt ist.
"""

# Öffentliche Adresse der Website OHNE abschließenden Schrägstrich.
# Solange keine eigene Domain verbunden ist, ist das die GitHub-Pages-Adresse.
# Mit eigener Domain z. B.:  SITE_URL = "https://www.villabelvedere.xyz"
SITE_URL = "https://belvedere-oliveoil.com"

# Kontaktformular: statische Seiten (GitHub Pages) können keine E-Mails versenden.
# Das Formular wird an einen Formular-Dienst geschickt, z. B. Formspree
# (https://formspree.io → neues Formular anlegen → Endpoint hier eintragen).
FORM_ENDPOINT = "https://formspree.io/f/DEIN-FORMULAR-ID"
FORM_PROVIDER = {
    "name": "Formspree, Inc.",
    "address": "[Anschrift des Formular-Anbieters laut dessen Datenschutzerklärung]",
    "privacy_url": "https://formspree.io/legal/privacy-policy",
    "country": "USA",
}

# Angaben für Impressum / Note legali / Datenschutz
LEGAL = {
    "company": "Azienda Agricola Villa Belvedere di Corliano",
    "owner": "[Vor- und Nachname Inhaber/in]",
    "legal_form": "[Rechtsform, z. B. impresa individuale / società agricola semplice]",
    "street": "[Via ..., Nr.]",
    "zip_city": "[CAP] [Comune] (PI)",
    "country": "Italia",
    "phone": "[+39 ...]",
    "email": "[info@ihre-domain.it]",
    "pec": "[PEC-Adresse]",
    "vat": "[Partita IVA]",
    "tax_code": "[Codice Fiscale]",
    "rea": "[REA PI-......]",
    "register": "Registro delle Imprese – CCIAA Toscana Nord-Ovest / Pisa",
    "content_responsible": "Ralph Striewski",
    "bio_body": "[Name der Bio-Kontrollstelle]",
    "bio_code": "[IT-BIO-...]",
    "authority_privacy": "Garante per la protezione dei dati personali, Piazza Venezia 11, 00187 Roma – www.garanteprivacy.it",
}

# Datum, an dem Impressum/Datenschutz zuletzt geprüft wurden
LEGAL_DATE = {"it": "novembre 2026", "de": "November 2026", "en": "November 2026"}

BRAND = "Villa Belvedere"
