# Mailabruf: Antworten auf den Newsletter

Erweiterung des bestehenden Mailabrufs („Newsletter: Mail-Abruf in die Inbox (23:45)“, täglich 23:45 Uhr Europe/Berlin). Es bleibt bei **einer** Adresse, `aschumann.bdkep+news@gmail.com`, und beim normalen Rhythmus. Der Abruf sortiert die Mails nur zusätzlich: Antworten auf den Newsletter gehen in die Sammlung `emails` (Reiter „E-Mails“), alles andere wie bisher in `quellen`.

## Voraussetzungen

- Im Versandtool ist Reply-To bereits die Adresse `aschumann.bdkep+news@gmail.com` (oder wird darauf gesetzt). Mit einem Testversand prüfen, wohin Abwesenheitsnotizen tatsächlich gehen (je nach Mailserver Reply-To, Return-Path oder From).
- Gmail wird nur gelesen: nichts senden, löschen, verschieben, labeln oder als gelesen markieren. Auch Antworten werden nie versendet; Antwortentwürfe entstehen nur als Text im Dashboard.
- **Betreff-Muster des Newsletters** festlegen (Platzhalter `<Betreff-Muster>`, zum Beispiel der feste Teil des Betreffs). Es dient dazu, Antworten auf den Newsletter von weitergeleiteten Quellen zu unterscheiden.

## Ablauf

1. Suche wie bisher (`deliveredto:aschumann.bdkep+news@gmail.com`).
2. Je Mail zuerst prüfen, ob das Dokument schon existiert (`quellen/m-<ID>` oder `emails/e-<ID>`), dann überspringen. Vorhandene Dokumente nie überschreiben, dort stehen Aufgaben und Status.
3. Mail einsortieren:
   - **in `emails`**: Zustellfehler, Abwesenheitsnotizen und automatische Antworten (Header, Absender oder Betreff siehe unten), außerdem Mails, deren Betreff mit „Re:“, „AW:“ oder „Antwort:“ beginnt und das `<Betreff-Muster>` enthält. Im Zweifel ebenfalls in `emails`, damit keine Antwort im Eingangskorb der Themen untergeht.
   - **in `quellen`**: alles andere (weitergeleitete Meldungen, Hinweise, Links), unverändert wie bisher.
4. Ist die Mail einer Ausgabe zuzuordnen (jüngster Versandtermin in `ausgaben` vor dem Maildatum), deren Namen in `ausgabe` eintragen.
5. Der Zeitraum der Suche muss mindestens 14 Tage zurückreichen, damit ein ausgefallener Lauf nachgeholt wird. Das Dashboard löscht automatisch geschlossene Mails frühestens nach 30 Tagen, sie werden also nie erneut angelegt.

## Einstufung

| `art` | Erkennung | `status` |
|---|---|---|
| `zustellfehler` | Absender `MAILER-DAEMON` oder `postmaster`, Betreff „Undeliverable“, „Delivery Status Notification“, „Zustellung fehlgeschlagen“ | `offen` |
| `abwesenheit` | Header `Auto-Submitted` (nicht `no`), `X-Autoreply`, `X-Autorespond`, `Precedence: auto_reply` oder `bulk`, oder Betreff „Abwesenheit“, „Automatische Antwort“, „Out of Office“, „Auto-Reply“ | siehe unten |
| `antwort` | alles andere in `emails` | `offen` |

Abwesenheit, Entscheidung über `status`:

- **`auto`** nur, wenn alle drei Punkte gelten: Es ist eine Abwesenheitsnotiz, im Text steht ein eindeutiges Rückkehrdatum (alle Schreibweisen, auch „bis Montag, den 3. November“, „back on Nov 3rd“; ohne Jahr gilt das nächste passende Datum), und im Text steht nichts Besonderes.
- **`offen`**, wenn eines gilt: kein Rückkehrdatum, Datum nicht eindeutig, Rückkehr mehr als 180 Tage in der Zukunft, oder ein Sondertext wie „nicht mehr im Unternehmen“, „ausgeschieden“, „im Ruhestand“, „Mail wird nicht weitergeleitet“, „Nachfolger“, „bitte wenden Sie sich an …“, „Elternzeit“ ohne Ende, eine persönliche Nachricht zusätzlich zur Abwesenheit.
- Im Zweifel `offen`. Das Dashboard prüft zusätzlich selbst: Ein `auto` ohne gültiges `rueckkehr` oder mit Rückkehr nach mehr als 180 Tagen zeigt es als offen.

## Felder in `emails/e-<Gmail-Nachrichten-ID>`

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
