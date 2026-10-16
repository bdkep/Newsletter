# Newsletter-Dashboard BdKEP

Dashboard zum Sammeln von Quellen, Verteilen auf Ausgaben, Schreiben von Kurztexten und Zusammensetzen des HTML-Newsletters im BdKEP-Design. Fachliche Vorgabe: `newsletter-dashboard-vorgabe.md`.

**Live:** <https://claude.ai/artifact/SpfH3AWEaBy4SDy7thYrD5> (privat; Freigabe über das Teilen-Menü der Seite)

## Aufbau

Wie Hub, Sekretariat und Aufgaben: eine Artifact-Seite mit Artifact-Datenbank. `dashboard/newsletter.html` ist die Quelle der Seite (Logos als Platzhalter, die Veröffentlichung setzt sie aus `design/logo/` ein). Design: `design/` (Tokens, Logos, Beispiel-Newsletter), Stilvorgaben für Texte: `style.md`.

Datenbank-Sammlungen (Artifact-DB):
- `quellen`: typ (`mail|note|link|document|image`), titel, text, url, mailBetreff, mailAbsender, mailDatum, quelle (`mail|hand`), erfasstAm, erfasstVon
- folgen mit den nächsten Stufen: `themen`, `ausgaben`, `textbausteine`

## Mailabruf

Geplante Aufgabe „Newsletter: Mail-Abruf in die Inbox (23:45)“, täglich 23:45 Uhr Europe/Berlin. Sie liest über den Gmail-Connector Mails an `aschumann.bdkep+news@gmail.com` (nur lesen) und legt sie als `quellen/m-<Gmail-ID>` ab. Doppelte Abrufe sind ausgeschlossen.

## Stand

| Stufe | Inhalt | Status |
|---|---|---|
| 1 | Gerüst, Datenmodell | fertig |
| 2 | Inbox: Notiz, Link, Mail, Textdatei (.txt, .md, .eml), Mailabruf | fertig, offen: docx, pdf, msg, Bilder, Link-Abruf |
| 3 | Eingangskorb mit Status und Hinweis, Ausgaben, Zuordnung per Knopf, Reihenfolge | fertig (Vorlage "Newsletter-Dashboard"), offen: Drag-and-Drop, Schlagwörter, Bilder |
| 4 | Textbausteine: Vorschlag per Claude mit Sendevorschau, Bearbeiten, Versionen, Freigabe, Text der Ausgabe kopieren | fertig |
| 5 | Export | offen |
| 6 | Prüfung | offen |
