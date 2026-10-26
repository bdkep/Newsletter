# Mailabruf Antworten auf den Newsletter

Arbeitsgrundlage für die geplante Aufgabe, die Antworten auf den Newsletter in die Sammlung `emails` des Dashboards schreibt (Reiter „E-Mails“). Eigene Aufgabe, getrennt vom Quellen-Abruf (23:45 Uhr), damit Antworten nie im Eingangskorb der Themen landen.

## Voraussetzungen

- Im Versandtool Reply-To (und, wenn einstellbar, Return-Path) auf eine eigene Antwortadresse setzen, zum Beispiel `aschumann.bdkep+antworten@gmail.com`. Nicht die Adresse des Quellen-Abrufs (`+news`) verwenden.
- Mit einem Testversand prüfen, wohin Abwesenheitsnotizen tatsächlich gehen (je nach Mailserver Reply-To, Return-Path oder From).
- Gmail wird nur gelesen: nichts senden, löschen, verschieben, labeln oder als gelesen markieren.

## Ablauf der Aufgabe

1. Suche: `deliveredto:<Antwortadresse> newer_than:14d`. Der Zeitraum von 14 Tagen fängt einen ausgefallenen Lauf ab. Das Dashboard löscht automatisch geschlossene Mails frühestens nach 30 Tagen, sie werden also nie erneut angelegt.
2. Je Mail das Dokument `emails/e-<Gmail-Nachrichten-ID>` anlegen. Gibt es das Dokument schon, überspringen (keine Doppelten, vorhandene Dokumente nie überschreiben, weil dort Aufgaben und Status stehen).
3. Mail einstufen (siehe unten) und schreiben.
4. Ist die Mail einer Ausgabe zuzuordnen (Versanddatum liegt vor dem Maildatum, jüngster Versand in `ausgaben`), deren Namen in `ausgabe` eintragen.

## Einstufung

| `art` | Erkennung | `status` |
|---|---|---|
| `zustellfehler` | Absender `MAILER-DAEMON` oder `postmaster`, Betreff „Undeliverable“, „Delivery Status Notification“, „Zustellung fehlgeschlagen“ | `offen` |
| `abwesenheit` | Header `Auto-Submitted` (nicht `no`), `X-Autoreply`, `X-Autorespond`, `Precedence: auto_reply` oder `bulk`, oder Betreff „Abwesenheit“, „Automatische Antwort“, „Out of Office“, „Auto-Reply“ | siehe unten |
| `antwort` | alles andere, auch bei Zweifel | `offen` |

Abwesenheit, Entscheidung über `status`:

- **`auto`** nur, wenn alle drei Punkte gelten: Es ist eine Abwesenheitsnotiz, im Text steht ein eindeutiges Rückkehrdatum (alle Schreibweisen, auch „bis Montag, den 3. November“, „back on Nov 3rd“; ohne Jahr gilt das nächste passende Datum), und im Text steht nichts Besonderes.
- **`offen`**, wenn eines gilt: kein Rückkehrdatum, Datum nicht eindeutig, Rückkehr mehr als 180 Tage in der Zukunft, oder ein Sondertext wie „nicht mehr im Unternehmen“, „ausgeschieden“, „im Ruhestand“, „Mail wird nicht weitergeleitet“, „Nachfolger“, „bitte wenden Sie sich an …“, „Elternzeit“ ohne Ende, eine persönliche Nachricht zusätzlich zur Abwesenheit.
- Im Zweifel `offen`. Das Dashboard prüft zusätzlich selbst: Ein `auto` ohne gültiges `rueckkehr` oder mit Rückkehr nach mehr als 180 Tagen zeigt es als offen.

## Felder

| Feld | Inhalt |
|---|---|
| `betreff`, `absender`, `datum` (ISO) | aus der Mail |
| `art` | `abwesenheit`, `antwort`, `zustellfehler` |
| `rueckkehr` | `JJJJ-MM-TT`, nur bei Abwesenheit mit Datum, sonst `''` |
| `grund` | ein kurzer Satz, warum so eingestuft, zum Beispiel „Rückkehr am 03.11.2026“ oder „kein Datum, Hinweis auf Ausscheiden“ |
| `status` | `auto` oder `offen` |
| `text` | **nur bei `offen`**: Mailtext ohne Signatur und zitierten Verlauf, höchstens 3000 Zeichen. Bei `auto` leer lassen (Datensparsamkeit). |
| `ausgabe` | Name der Ausgabe, optional |
| `erfasstAm` | Zeitpunkt des Abrufs (ISO) |
| `aufgaben`, `verlauf` | beim Anlegen leer (`[]`), pflegt das Dashboard |

## Häufigkeit

Täglich, in den 48 Stunden nach einem Versandtermin (Sammlung `ausgaben`, `versanddatum`) stündlich.
