# Newsletter-Dashboard BdKEP

Dashboard zum Sammeln von Quellen, Verteilen auf Ausgaben, Schreiben von Kurztexten und Zusammensetzen des HTML-Newsletters im BdKEP-Design. Fachliche Vorgabe: `newsletter-dashboard-vorgabe.md`.

**Live:** <https://claude.ai/artifact/SpfH3AWEaBy4SDy7thYrD5> (privat; Freigabe über das Teilen-Menü der Seite)

## Aufbau

Wie Hub, Sekretariat und Aufgaben: eine Artifact-Seite mit Artifact-Datenbank. `dashboard/newsletter.html` ist die Quelle der Seite (Logos als Platzhalter, die Veröffentlichung setzt sie aus `design/logo/` ein). Design: `design/` (Tokens, Logos, Beispiel-Newsletter), Stilvorgaben für Texte: `style.md`.

Datenbank-Sammlungen (Artifact-DB):
- `quellen`: typ (`mail|note|link|document|image`), titel, text, url, mailBetreff, mailAbsender, mailDatum, quelle (`mail|hand`), erfasstAm, erfasstVon
- `wuensche`: Wünsche zum Dashboard (text, von, status `offen|ausgearbeitet|geprueft|erledigt|geschlossen`, story, kriterien, erfolgsmass, pruefung, vorgabe, bewaehrt, kommentare, neuFuer, verlauf)
- folgen mit den nächsten Stufen: `themen`, `ausgaben`, `textbausteine`

## Wünsche

Reiter „Wünsche“ neben dem Eingangskorb, Logik wie im Sekretariat-Dashboard: Wunsch eintragen, Ausarbeitung (User Story, 2 bis 4 Kriterien, Erfolgsmaß; Vorschlag per Claude nur zum Prüfen, gespeichert wird erst nach Bestätigung), „Einbau prüfen“ (Abgleich mit den Abläufen des Dashboards und anderen Wünschen, Rückfragen, Vorgabe für Claude Code), Erledigt erst nach gespeicherter Einbauprüfung, danach „Bewährt?“ durch den Autor, Schließen und Wieder öffnen, Kommentare, Historie, „Neu für dich“. Beim Öffnen wählt jede Person „Ich bin …“ (Andreas, Mario, Ina), das ist keine Anmeldung. Prüfen und Schließen dürfen Autor, Andreas und Mario. Die Abläufe für die Einbauprüfung stehen als Text im Dashboard (`ABLAEUFE`) und müssen bei Änderungen der Abläufe nachgezogen werden. Die Änderungsübersicht des Sekretariats ist hier nicht enthalten.

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
