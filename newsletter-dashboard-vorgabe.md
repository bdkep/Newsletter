# Vorgabe: Newsletter-Dashboard BdKEP

Arbeitsgrundlage für Claude Code. Ziel ist eine lokal lauffähige Web-Anwendung, mit der Inhalte für Newsletter gesammelt, auf Ausgaben verteilt, in Kurztexte gefasst und zu einem HTML-Newsletter im BdKEP-Design zusammengesetzt werden.

## 1. Ausgangslage

- Auftraggeber: Bundesverband der Kurier-Express-Paket-Dienste (BdKEP), Berlin.
- Inhalte für Newsletter liegen verteilt vor: Dokumente, Links, E-Mails, Notizen, Bilder.
- Es gibt keine fertige Software, die Themenpool, Zuordnung zu künftigen Ausgaben, Textbausteine und ein festes Corporate Design in einem Ablauf verbindet. Klassische Newsletter-Tools decken Gestaltung, Versand und Auswertung ab, Content-Tools wie Feedly oder Curated decken Sammeln bzw. Linklisten ab.
- Das Dashboard ersetzt kein Versandtool. Es erzeugt den fertigen Newsletter als HTML, der in ein Versandtool mit HTML-Editor übernommen wird (z. B. Brevo, das den Import eigener HTML-Vorlagen unterstützt).

## 2. Ablauf aus Nutzersicht

1. Quellen erfassen (Dokument, Link, E-Mail, Notiz, Bild) in einer **Inbox**.
2. Aus einer Quelle entsteht eine **Themenkarte**.
3. Themenkarten werden einer **Ausgabe** zugeordnet und zwischen Ausgaben verschoben (Drag-and-Drop).
4. Je Themenkarte entsteht ein **Textbaustein** (Kurztext), erzeugt per Claude-API oder manuell geschrieben, immer editierbar.
5. Aus den freigegebenen Textbausteinen einer Ausgabe wird der **Newsletter** im BdKEP-Design zusammengesetzt, mit Vorschau und HTML-Export.

## 3. Funktionsumfang (Version 1)

### 3.1 Quellen-Inbox
- Upload von Dokumenten: `.docx`, `.pdf`, `.txt`, `.md`.
- E-Mails: Upload von `.eml` und `.msg` sowie Einfügen von Mailtext per Copy-and-paste. Betreff, Absender, Datum und Text werden ausgelesen.
- Links: URL eingeben; Titel, Beschreibung, Vorschaubild und Haupttext werden automatisch abgerufen. Bei Fehlschlag bleibt die Karte mit URL erhalten und lässt sich manuell ergänzen.
- Freitext-Notiz.
- Bilder: Upload `.jpg`, `.png`, `.webp`; Zuordnung zu einer Themenkarte.
- Extrahierter Quelltext wird gespeichert, das Original bleibt unverändert in einer Dateiablage.
- Eine Quelle kann mehreren Themenkarten zugeordnet werden, eine Themenkarte mehreren Quellen.

### 3.1a Automatischer Mailabruf (Ergänzung des Auftraggebers)
- Mails, die an `aschumann.bdkep+news@gmail.com` gehen, werden täglich um 23:45 Uhr (Europe/Berlin) abgerufen und als Quelle vom Typ `mail` in der Inbox abgelegt.
- Abruf per IMAP; Zugangsdaten nur über Umgebungsvariablen (`MAIL_IMAP_USER`, `MAIL_IMAP_PASSWORD`, bei Gmail ein App-Passwort), nie im Repository.
- Gmail liefert Mails an die Plus-Adresse im Postfach `aschumann.bdkep@gmail.com` aus; gefiltert wird auf den Empfänger `+news`.
- Bereits abgerufene Mails werden nicht doppelt angelegt (Message-ID wird gespeichert).
- Zeitplan über den Scheduler der Anwendung oder alternativ als Cron-Befehl; Abruf ist auch manuell per Schaltfläche möglich.
- Umsetzung in Stufe 2 zusammen mit der Inbox.

### 3.2 Themenkarten
Felder: Titel, Kurzbeschreibung, Quellen (1..n), Schlagwörter, Status (`Idee`, `Text in Arbeit`, `Text fertig`, `Freigegeben`), zugeordnete Ausgabe (oder keine), Position innerhalb der Ausgabe, Bilder (0..n, je mit Alt-Text und optionaler Bildunterschrift), Notizen (intern, nie im Newsletter), optionaler Link „Weiterlesen“.

### 3.3 Ausgaben und Board
- Ausgabe: Name (z. B. „November 2026“), geplantes Versanddatum, Status (`Planung`, `In Redaktion`, `Fertig`, `Versendet`), interne Notiz.
- Board-Ansicht: Spalte „Inbox/Ohne Ausgabe“ plus eine Spalte je Ausgabe.
- Karten per Drag-and-Drop zwischen Spalten verschieben und innerhalb einer Spalte umsortieren. Die Reihenfolge innerhalb einer Ausgabe bestimmt die Reihenfolge im Newsletter.
- Ausgaben anlegen, umbenennen, verschieben (Datum), archivieren. Versendete Ausgaben sind schreibgeschützt und bleiben als Archiv einsehbar.
- Filter nach Schlagwort, Status, Quelle; Volltextsuche über Titel, Quelltext und Textbausteine.

### 3.4 Textbausteine
- Pro Themenkarte ein Textbaustein: Überschrift, Kurztext (Richtwert 40–80 Wörter, einstellbar), optionaler Link-Text.
- Erzeugung per Schaltfläche über die Anthropic-API aus dem gespeicherten Quelltext und den Karten-Notizen. Der Entwurf wird nie automatisch freigegeben.
- Manuelle Bearbeitung jederzeit; frühere Fassungen bleiben als Versionen abrufbar.
- Stilvorgaben für die Erzeugung (als bearbeitbare Konfiguration `style.md`, wird in den Prompt eingebunden):
  - sachlich, neutral, dauerhaft gültige Formulierungen,
  - keine Werbesprache und keine wertenden Zusätze,
  - keine rhetorischen Fragen,
  - keine typischen KI-Formulierungen,
  - Angaben ausschließlich aus den hinterlegten Quellen; fehlende Angaben werden nicht ergänzt, sondern als Lücke markiert (`[Angabe fehlt]`).
- Jeder erzeugte Text zeigt die verwendeten Quellen an, damit die Redaktion Aussagen prüfen kann.
- Die Erzeugung ist optional. Ohne API-Schlüssel funktioniert die Anwendung vollständig mit manuellen Texten.

### 3.5 Newsletter-Zusammenbau und Export
- Aus allen Themenkarten einer Ausgabe mit Status `Freigegeben` wird der Newsletter in der festgelegten Reihenfolge erzeugt.
- Feste Bestandteile aus der Vorlage: Kopf mit Logo, optionaler Einleitungstext je Ausgabe, Themenblöcke (Bild + Überschrift + Kurztext + Link), Abbinder mit Absender-/Impressumsangaben, Abmeldehinweis als Platzhalter des Versandtools.
- Layout-Varianten je Themenblock: Bild oben, Bild links, ohne Bild.
- Live-Vorschau in Desktop- und Mobilbreite.
- Export:
  - `newsletter.html` (E-Mail-tauglich: Tabellenlayout, Inline-CSS, Breite 600 px, Alt-Texte, Textalternativen für Bilder),
  - `newsletter.txt` (Nur-Text-Fassung),
  - ZIP mit HTML und Bildordner (Bilder auf Breite 1200 px für Retina skaliert, Anzeige 600 px).
- Bilder müssen im Versandtool gehostet werden. Das Dashboard weist beim Export darauf hin und erzeugt Bild-URLs über einen konfigurierbaren Basis-Pfad.
- Kein Versand aus dem Dashboard in Version 1.

## 4. BdKEP-Design

- **Die Designvorlage liegt nicht in dieser Vorgabe vor.** Claude Code erfindet kein Design. Der Nutzer legt im Ordner `design/` ab: Logo (SVG/PNG), Farbwerte, Schriftarten bzw. E-Mail-sichere Ersatzschriften, vorhandene HTML-Vorlage oder Word-Vorlage, Beispiel eines früheren Newsletters.
- Vor der Umsetzung des Exports prüft Claude Code, welche Dateien in `design/` vorhanden sind, und fragt fehlende Angaben beim Nutzer ab.
- Design-Werte (Farben, Abstände, Schriften, Logo-Pfad, Fußtexte) liegen zentral in `design/tokens.json` und in einer HTML-Vorlage `design/newsletter-template.html` mit Platzhaltern. Änderungen am Design erfordern keine Änderung am Anwendungscode.
- Der Export muss in gängigen E-Mail-Clients (Outlook-Desktop, Gmail, Apple Mail, mobile Clients) lesbar bleiben. Outlook-spezifische Besonderheiten (z. B. fehlende Unterstützung moderner CSS-Eigenschaften) werden beim Aufbau der Vorlage berücksichtigt.

## 5. Technische Rahmenbedingungen

- Lokal lauffähig, ein Nutzer, kein Cloud-Zwang. Start mit einem einzigen Befehl, Anleitung in `README.md`.
- Datenhaltung: SQLite plus Dateiablage im Projektordner (`data/`). Export/Backup als ZIP.
- Technologiewahl liegt bei Claude Code; bevorzugt wird ein schlanker Aufbau mit wenigen Abhängigkeiten (Vorschlag: Python mit FastAPI und SQLite, Frontend ohne aufwendiges Build-System). Die Wahl wird in der README kurz begründet.
- Textextraktion: `python-docx`, `pypdf`, `extract-msg` und die Standardbibliothek `email` oder gleichwertige Pakete.
- Anthropic-API: Schlüssel ausschließlich über Umgebungsvariable `ANTHROPIC_API_KEY`, nie in Dateien oder im Repository. Modellname konfigurierbar.
- Datenschutz: E-Mails und Dokumente können vertrauliche oder personenbezogene Inhalte enthalten. Beim Erzeugen eines Textbausteins wird vorab angezeigt, welche Quellen an die API gesendet werden; Senden erfolgt nur nach Klick. E-Mail-Absender und -Adressen werden standardmäßig nicht an die API übergeben.
- Sprache der Oberfläche und der erzeugten Texte: Deutsch.
- Barrierefreiheit: Alt-Texte sind Pflichtfeld für Bilder im Newsletter; Export prüft Kontrast der Designfarben und warnt bei Unterschreitung.

## 6. Datenmodell (Richtwert)

- `source`: id, typ (`document|link|mail|note|image`), titel, original_pfad, url, extrahierter_text, metadaten (JSON), erfasst_am
- `topic`: id, titel, beschreibung, status, issue_id (nullable), position, notizen
- `topic_source`: topic_id, source_id
- `topic_image`: id, topic_id, pfad, alt_text, bildunterschrift, position
- `tag` und `topic_tag`
- `issue`: id, name, versanddatum, status, einleitung, notiz
- `text_block`: id, topic_id, version, ueberschrift, kurztext, link_text, erzeugt_durch (`manuell|api`), erstellt_am, ist_aktuell

## 7. Nicht Bestandteil von Version 1

- Versand, Abonnentenverwaltung, Öffnungs- und Klickstatistik, A/B-Tests.
- Direktanbindung an weitere Postfächer oder Cloud-Speicher (SharePoint u. Ä.); der Abruf des Newsletter-Postfachs nach 3.1a ist davon ausgenommen und Teil von Version 1. Weitere Anbindungen sind als spätere Erweiterung vorgesehen; die Quellenerfassung wird so gebaut, dass weitere Quelltypen als Module ergänzt werden können.
- Mehrbenutzerbetrieb und Rechteverwaltung.

## 8. Vorgehen in Stufen

Nach jeder Stufe lauffähiger Stand und kurze Rückmeldung an den Nutzer, bevor die nächste beginnt.

1. **Gerüst und Datenmodell:** Projektstruktur, Datenbank, Start-Skript, README.
2. **Inbox:** Erfassung aller Quelltypen mit Textextraktion, Anzeige und Löschen.
3. **Themenkarten und Board:** Karten anlegen, Ausgaben, Drag-and-Drop, Sortierung, Filter, Suche.
4. **Textbausteine:** manuelle Bearbeitung, Versionen, danach API-Erzeugung mit Quellenanzeige.
5. **Design und Export:** Klärung der Designdateien, Vorlage, Vorschau, HTML-/Text-/ZIP-Export.
6. **Prüfung:** Tests mit Beispieldaten, Export-Test in mindestens zwei E-Mail-Clients bzw. Testdiensten, Aktualisierung der README.

## 9. Abnahmekriterien

- Eine Quelle jedes Typs lässt sich erfassen; der Text ist im Dashboard lesbar.
- Eine Themenkarte lässt sich per Drag-and-Drop in eine andere Ausgabe verschieben; Reihenfolge bleibt nach Neustart erhalten.
- Ein Textbaustein lässt sich erzeugen, bearbeiten, auf frühere Version zurücksetzen und freigeben.
- Der exportierte Newsletter enthält ausschließlich freigegebene Bausteine in der Reihenfolge des Boards, nutzt die Werte aus `design/` und zeigt Text- und Bildelemente korrekt in Desktop- und Mobilvorschau.
- Der Export enthält keine internen Notizen und keine Quelldaten.
- Ohne API-Schlüssel startet die Anwendung und alle manuellen Funktionen arbeiten.
- Die README beschreibt Installation, Start, Konfiguration und Sicherung der Daten.

## 10. Offene Punkte (vor Stufe 5 zu klären)

- BdKEP-Designdateien (siehe Abschnitt 4).
- Zielsystem für den Versand (Hosting der Bilder, Platzhalter für Abmeldelink und Impressum).
- Erscheinungsrhythmus und übliche Anzahl der Themenblöcke je Ausgabe.
- Rechtliche Pflichtangaben im Newsletter-Fuß (Impressum, Datenschutzhinweis).
- Gewünschtes Claude-Modell für die Textbausteine.
