# Newsletter-Dashboard BdKEP

Dashboard zum Sammeln von Quellen, Verteilen auf Ausgaben, Schreiben von Kurztexten und Zusammensetzen des HTML-Newsletters im BdKEP-Design. Fachliche Vorgabe: `newsletter-dashboard-vorgabe.md`.

**Live:** <https://claude.ai/artifact/SpfH3AWEaBy4SDy7thYrD5> (privat; Freigabe über das Teilen-Menü der Seite)

## Aufbau

Wie Hub, Sekretariat und Aufgaben: eine Artifact-Seite mit Artifact-Datenbank. `dashboard/newsletter.html` ist die Quelle der Seite (Logos als Platzhalter, die Veröffentlichung setzt sie aus `design/logo/` ein). Design: `design/` (Tokens, Logos, Beispiel-Newsletter), Stilvorgaben für Texte: `style.md`.

Datenbank-Sammlungen (Artifact-DB):
- `quellen`: typ (`mail|note|link|document|image`), titel, text, url, mailBetreff, mailAbsender, mailDatum, quelle (`mail|hand`), erfasstAm, erfasstVon
- `wuensche`: Wünsche zum Dashboard (text, von, status `offen|ausgearbeitet|geprueft|erledigt|geschlossen`, story, kriterien, erfolgsmass, pruefung, vorgabe, bewaehrt, kommentare, neuFuer, verlauf)
- `ausgaben`: name, versanddatum (JJJJ-MM-TT), versandzeit (optional), notiz, status (`planung|versendet`), reihenfolge
- `archiv`: bereits versendete Newsletter: name, versanddatum, titel, einleitung, abschnitte (ueberschrift, text, linkText, url), abbinder, stilvorbild, notiz, quelle (`import|hand|ausgabe`)
- Textbausteine liegen im Dokument der Quelle (`tb`, `tbVersionen`); je Thema außerdem `zeichen` (Zielumfang), `ergaenzung` (ergänzende Angaben), `rueckfragen` (offene Fragen von Claude)

## Versandplan und Archiv

Reiter „Versandplan“: Versandtermine neuer Ausgaben anlegen (Name, Datum, optional Uhrzeit, Notiz), ändern und löschen (nur ohne Themen). Jede neue Ausgabe braucht einen Termin, auch beim Anlegen im Eingangskorb. Der Termin ist im Versandplan und direkt in der Ausgabe änderbar. Die Ausgaben stehen nach Termin aufsteigend (spätester zuletzt), Bestand ohne Termin am Ende und markiert, überschrittene Termine rot. „Als versendet ins Archiv“ legt die freigegebenen Texte als Newsletter im Archiv ab und nimmt die Ausgabe aus Planung und Zuordnung.

Reiter „Archiv“: bereits versendete Newsletter zum Nachschlagen, Durchsuchen und Kopieren. Neue Newsletter lassen sich als Text oder aus einer HTML-Datei einlesen (je `h2` ein Abschnitt). Einzelne Abschnitte gehen per „Als Entwurf übernehmen“ in eine geplante Ausgabe, nie freigegeben und mit Hinweis zur Aktualitätsprüfung. Newsletter mit „Stilvorbild“ gehen mit höchstens 3 Newslettern und je 2 Abschnitten als Beispiele in den Claude-Vorschlag (steht in der Sendevorschau). Die Kennzahl „Üblicher Aufbau“ zeigt Abschnitte je Newsletter, Wörter je Abschnitt und Wörter je Überschrift. Eingelesen ist der Newsletter vom 30.09.2026 (`design/beispiel-newsletter-2026-09-30.html`).

## Textvorschlag je Thema

Jedes Thema hat den Bereich „Newsletter-Text“ (im Eingangskorb und in der Ausgabe über „Text schreiben“ bzw. „Text bearbeiten“; der Text gehört zur Quelle und wandert mit ihr). Dort wird der Umfang in Zeichen eingestellt (Eingabefeld oder 300/500/800, Standard 450, Toleranz ±10 %); die Anzeige unter dem Kurztext zählt Zeichen gegen das Ziel. Der Vorschlag orientiert sich an den Newslettern im Archiv (Stilvorbilder, sonst die drei jüngsten; je Newsletter die zwei Abschnitte mit der Länge nächst dem Ziel). Reichen die Angaben der Quelle nicht, schreibt Claude keinen Text, sondern stellt bis zu 5 Rückfragen. Antworten kommen in das Feld „Ergänzende Angaben“, danach „Erneut vorschlagen“. Gespeichert und freigegeben wird nur nach Bestätigung durch die Person.

## Wünsche

Reiter „Wünsche“ neben dem Eingangskorb, Logik wie im Sekretariat-Dashboard: Wunsch eintragen, Ausarbeitung (User Story, 2 bis 4 Kriterien, Erfolgsmaß; Vorschlag per Claude nur zum Prüfen, gespeichert wird erst nach Bestätigung), „Einbau prüfen“ (Abgleich mit den Abläufen des Dashboards und anderen Wünschen, Rückfragen, Vorgabe für Claude Code), Erledigt erst nach gespeicherter Einbauprüfung, danach „Bewährt?“ durch den Autor, Schließen und Wieder öffnen, Kommentare, Historie, „Neu für dich“. Beim Öffnen wählt jede Person „Ich bin …“ (Andreas, Moritz), das ist keine Anmeldung. Prüfen und Schließen dürfen Autor, Andreas und Moritz. Die Abläufe für die Einbauprüfung stehen als Text im Dashboard (`ABLAEUFE`) und müssen bei Änderungen der Abläufe nachgezogen werden. 

Über den Wünschen steht „Änderungen am Dashboard“: kurze, freigegebene Texte zu dem, was sich an Oberfläche und Grafik geändert hat, je mit Nachsätzen. Was seit „Als gesehen markieren“ der Person dazukam, steht unter „Neu“, der Rest zugeklappt unter „Frühere Änderungen“. Entwürfe werden im Dashboard angepasst und freigegeben (Sammlungen `aenderungen`, `besuche`).

## Mailabruf

Geplante Aufgabe „Newsletter: Mail-Abruf in die Inbox (23:45)“, täglich 23:45 Uhr Europe/Berlin. Sie liest über den Gmail-Connector Mails an `aschumann.bdkep+news@gmail.com` (nur lesen) und legt sie als `quellen/m-<Gmail-ID>` ab. Doppelte Abrufe sind ausgeschlossen.

## E-Mails: Antworten auf den Newsletter

Reiter „E-Mails“ für die Antworten auf den Newsletter, damit sie nicht im Ticketsystem landen. Reply-To des Newsletters ist die Abrufadresse `aschumann.bdkep+news@gmail.com`. Der bestehende Mailabruf (täglich 23:45 Uhr, nur lesend) sortiert Antworten, Abwesenheitsnotizen und Zustellfehler zusätzlich in `emails/e-<Gmail-ID>`, alles andere bleibt in `quellen` (Vorgabe: `mailabruf-antworten.md`):

- **Abwesenheit mit eindeutigem Rückkehrdatum** (nicht mehr als 180 Tage voraus): schließt sich selbst (`status` `auto`), ohne gespeicherten Mailtext. Sichtbar unter „Automatisch geschlossen“ mit „Wieder öffnen“. Das Dashboard prüft die Einstufung selbst nach: ein `auto` ohne gültiges Datum zeigt es als offen. Über „Älter als 30 Tage löschen“ lassen sie sich bereinigen.
- **Abwesenheit ohne Datum oder mit Sondertext** (ausgeschieden, Ruhestand, Nachfolger …), **echte Antworten** und **Zustellfehler**: bleiben offen, mit Einstufungsgrund und Mailtext.
- Aufgabenlogik wie im Aufgaben-Dashboard: an jede E-Mail lassen sich Aufgaben anhängen (Titel, Zuständiger, Frist, Status offen, in Arbeit, wartend, erledigt, verworfen; offen nur ohne, in Arbeit nur mit Zuständigem). „Erledigt“ ist erst möglich, wenn keine Aufgabe mehr offen ist. Wird eine Aufgabe jemand anderem zugewiesen, steht die E-Mail bei ihm unter „Neu für mich“. Historie je E-Mail.
- **Antwortentwurf**: bei offenen Antworten schreibt Claude auf Knopfdruck einen Antworttext (nach „Jetzt senden“ mit Vorschau, was an Claude geht: Betreff und Mailtext, keine Absenderadresse) oder die Person schreibt ihn von Hand. Der Entwurf wird gespeichert und lässt sich kopieren, das Dashboard versendet nie etwas.

Datenbank-Sammlung `emails`: betreff, absender, datum, text (nur offene), art (`abwesenheit|antwort|zustellfehler`), rueckkehr, grund, status (`auto|offen|erledigt`), ausgabe, erfasstAm, aufgaben, antwortEntwurf, neuFuer, verlauf.

## Stand

| Stufe | Inhalt | Status |
|---|---|---|
| 1 | Gerüst, Datenmodell | fertig |
| 2 | Inbox: Notiz, Link, Mail, Textdatei (.txt, .md, .eml), Mailabruf | fertig, offen: docx, pdf, msg, Bilder, Link-Abruf |
| 3 | Eingangskorb mit Status und Hinweis, Ausgaben, Zuordnung per Knopf, Reihenfolge | fertig (Vorlage "Newsletter-Dashboard"), offen: Drag-and-Drop, Schlagwörter, Bilder |
| 4 | Textbausteine: Vorschlag per Claude mit Sendevorschau, Bearbeiten, Versionen, Freigabe, Text der Ausgabe kopieren | fertig |
| 5 | Export | offen |
| 6 | Prüfung | offen |
