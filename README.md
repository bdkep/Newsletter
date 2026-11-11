# Newsletter-Dashboard BdKEP

Dashboard zum Sammeln von Quellen, Verteilen auf Ausgaben, Schreiben von Kurztexten und Zusammensetzen des HTML-Newsletters im BdKEP-Design. Fachliche Vorgabe: `newsletter-dashboard-vorgabe.md`.

**Live:** <https://claude.ai/artifact/SpfH3AWEaBy4SDy7thYrD5> (privat; Freigabe über das Teilen-Menü der Seite)

## Aufbau

Wie Hub, Sekretariat und Aufgaben: eine Artifact-Seite mit Artifact-Datenbank. `dashboard/newsletter.html` ist die Quelle der Seite (Logos als Platzhalter, die Veröffentlichung setzt sie aus `design/logo/` ein). Design: `design/` (Tokens, Logos, Beispiel-Newsletter), Stilvorgaben für Texte: `style.md`.

Datenbank-Sammlungen (Artifact-DB):
- `quellen`: typ (`mail|note|link|document|image`), titel, text, url, mailBetreff, mailAbsender, mailDatum, quelle (`mail|hand`), erfasstAm, erfasstVon
- `wuensche`: Wünsche zum Dashboard (text, von, status `offen|ausgearbeitet|geprueft|erledigt|geschlossen`, story, kriterien, erfolgsmass, pruefung, vorgabe, bewaehrt, kommentare, neuFuer, verlauf)
- `ausgaben`: name, versanddatum (JJJJ-MM-TT), versandzeit (optional), notiz, status (`planung|versendet`), reihenfolge, phase (`themen|einzeltexte|gesamttext|design|gegenlesen|test1|korrektur|test2`), freigabe `{von,am}`, gesamt `{intro, abschnitte[{id,ueberschrift,text,linkText,url,kategorie}]}`, termine `[{titel,von,bis,ort,url}]`
- `archiv`: bereits versendete Newsletter: name, versanddatum, titel, einleitung, abschnitte (ueberschrift, text, linkText, url), html (versendeter HTML-Code), termine, abbinder, stilvorbild, notiz, quelle (`import|hand|ausgabe`)
- Textbausteine liegen im Dokument der Quelle (`tb`, `tbVersionen`); je Thema außerdem `zeichen` (Zielumfang), `ergaenzung` (ergänzende Angaben), `rueckfragen` (offene Fragen von Claude)

## Versandplan und Archiv

Reiter „Versandplan“: Versandtermine neuer Ausgaben anlegen (Name, Datum, optional Uhrzeit, Notiz), ändern und löschen (nur ohne Themen). Jede neue Ausgabe braucht einen Termin, auch beim Anlegen im Eingangskorb. Der Termin ist im Versandplan und direkt in der Ausgabe änderbar. Die Ausgaben stehen nach Termin aufsteigend (spätester zuletzt), Bestand ohne Termin am Ende und markiert, überschrittene Termine rot. „Als versendet ins Archiv“ verlangt den versendeten HTML-Code aus dem Newsletterprogramm, legt ihn mit den Artikeln im Archiv ab und nimmt die Ausgabe aus Planung und Zuordnung.

Reiter „Archiv“: bereits versendete Newsletter zum Nachschlagen, Durchsuchen und Kopieren. Neue Newsletter lassen sich als Text oder aus einer HTML-Datei einlesen (je `h2` ein Abschnitt). Einzelne Abschnitte gehen per „Als Entwurf übernehmen“ in eine geplante Ausgabe, nie freigegeben und mit Hinweis zur Aktualitätsprüfung. Newsletter mit „Stilvorbild“ gehen mit höchstens 3 Newslettern und je 2 Abschnitten als Beispiele in den Claude-Vorschlag (steht in der Sendevorschau). Die Kennzahl „Üblicher Aufbau“ zeigt Abschnitte je Newsletter, Wörter je Abschnitt und Wörter je Überschrift. Eingelesen ist der Newsletter vom 30.09.2026 (`design/beispiel-newsletter-2026-09-30.html`).

## Textvorschlag je Thema

Jedes Thema hat den Bereich „Newsletter-Text“ (im Eingangskorb und in der Ausgabe über „Text schreiben“ bzw. „Text bearbeiten“; der Text gehört zur Quelle und wandert mit ihr). Dort wird der Umfang in Zeichen eingestellt (Eingabefeld oder 300/500/800, Standard 450, Toleranz ±10 %); die Anzeige unter dem Kurztext zählt Zeichen gegen das Ziel. Der Vorschlag orientiert sich an den Newslettern im Archiv (Stilvorbilder, sonst die drei jüngsten; je Newsletter die zwei Abschnitte mit der Länge nächst dem Ziel). Reichen die Angaben der Quelle nicht, schreibt Claude keinen Text, sondern stellt bis zu 5 Rückfragen. Antworten kommen in das Feld „Ergänzende Angaben“, danach „Erneut vorschlagen“. Gespeichert und freigegeben wird nur nach Bestätigung durch die Person.

## Duplizieren und Zuklappen

- Ausgaben im Eingangskorb-Reiter lassen sich über die Kopfzeile zuklappen (nur Ansicht, im Browser gemerkt, ändert keine Daten).
- „Duplizieren“ am Thema im Eingangskorb legt eine Kopie im Eingangskorb an. In einer Ausgabe wählt „Thema duplizieren nach“ die Zielausgabe (Vorauswahl: die nächste nach Versandtermin) oder den Eingangskorb.
- Die Kopie ist eine neue Quelle (`h-…`, `quelle: kopie`, `dupliziertVon`) mit Quelldaten und Text. Der Text bleibt Entwurf (nie freigegeben), Versionen und Rückfragen werden nicht kopiert, ein Hinweis zur Aktualitätsprüfung wird gesetzt. Das Original bleibt unverändert.
- Abhängigkeiten geprüft: Mailabruf (Ids `m-…`, Doppelte, „Letzter Abruf“) bleibt unberührt, „Als versendet ins Archiv“ nimmt nur freigegebene Texte, Löschen einer Ausgabe geht nur ohne Themen (Kopien zählen mit).

## Wünsche

Reiter „Wünsche“ neben dem Eingangskorb, Logik wie im Sekretariat-Dashboard: Wunsch eintragen, Ausarbeitung (User Story, 2 bis 4 Kriterien, Erfolgsmaß; Vorschlag per Claude nur zum Prüfen, gespeichert wird erst nach Bestätigung), „Einbau prüfen“ (Abgleich mit den Abläufen des Dashboards und anderen Wünschen, Rückfragen, Vorgabe für Claude Code), Erledigt erst nach gespeicherter Einbauprüfung, danach „Bewährt?“ durch den Autor, Schließen und Wieder öffnen, Kommentare, Historie, „Neu für dich“. Ein schwebender Knopf „Wunsch“ rechts unten (auf dem Handy „+“) steht in jedem Reiter und öffnet direkt das Formular „Wunsch eintragen“. Beim Öffnen wählt jede Person „Ich bin …“ (Andreas, Moritz), das ist keine Anmeldung. Prüfen und Schließen dürfen Autor, Andreas und Moritz. Die Abläufe für die Einbauprüfung stehen als Text im Dashboard (`ABLAEUFE`) und müssen bei Änderungen der Abläufe nachgezogen werden. 

Über den Wünschen steht „Änderungen am Dashboard“: kurze, freigegebene Texte zu dem, was sich an Oberfläche und Grafik geändert hat, je mit Nachsätzen. Was seit „Als gesehen markieren“ der Person dazukam, steht unter „Neu“, der Rest zugeklappt unter „Frühere Änderungen“. Entwürfe werden im Dashboard angepasst und freigegeben (Sammlungen `aenderungen`, `besuche`).

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

## Ablauf einer Ausgabe

Sammeln und Sichten im Eingangskorb laufen unabhängig von Ausgaben. Der Status einer Ausgabe beginnt mit dem ersten zugeordneten Thema und wird in der Ausgabe per „Weiter zu …“ geschaltet (mit Voraussetzungsprüfung):

1. Themen → 2. Einzeltexte (je Thema ein Textbaustein, dazu eine Kategorie für das Badge) → 3. Gesamttext (Intro, „Auf einen Blick“, bearbeitbare Abschnitte) → 4. Design (HTML im BdKEP-Layout nach `design/newsletter-designvorlage.dc.html`, Vorschau Desktop/Mobil, Kopieren und Herunterladen) → 5. Gegenlesen und Freigabe (Name und Datum werden gespeichert) → 6. Testversand 1 → 7. Korrektur → 8. Testversand 2 → 9. Versendet.

Die Terminliste (KEP-Branchentermine) gehört je Ausgabe dazu und wird aus der vorherigen Ausgabe oder dem Archiv fortgeschrieben; Termine vor dem Versanddatum fallen weg. „Versendet“ verlangt den versendeten HTML-Code und legt die Ausgabe im Archiv ab. Dort lassen sich die Fassung ansehen, kopieren und herunterladen sowie einzelne Artikel als Text oder HTML-Block kopieren und als Entwurf in eine neue Ausgabe übernehmen. Der Abmeldelink im HTML ist der Platzhalter `{{ unsubscribe }}` (Schreibweise von Brevo), Kontakt und Impressum stehen in `NL_FUSS` im Code.
