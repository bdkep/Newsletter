# Mailabruf: Antworten auf den Newsletter

Erweiterung des bestehenden Mailabrufs („Newsletter: Mail-Abruf in die Inbox (23:45)“, täglich 23:45 Uhr Europe/Berlin). Es bleibt bei **einer** Adresse, `aschumann.bdkep+news@gmail.com`, und beim normalen Rhythmus. Der Abruf sortiert die Mails nur zusätzlich: Antworten auf den Newsletter gehen in die Sammlung `emails` (Reiter „E-Mails“), alles andere wie bisher in `quellen`.

## Voraussetzungen

- Im Versandtool ist Reply-To bereits die Adresse `aschumann.bdkep+news@gmail.com` (oder wird darauf gesetzt). Mit einem Testversand prüfen, wohin Abwesenheitsnotizen tatsächlich gehen (je nach Mailserver Reply-To, Return-Path oder From).
- Gmail wird nur gelesen: nichts senden, löschen, verschieben, labeln oder als gelesen markieren. Auch Antworten werden nie versendet; Antwortentwürfe entstehen nur als Text im Dashboard.
- Der Betreff des Newsletters ändert sich mit jedem Versand, es gibt kein festes Muster. Antworten werden über den Betreff-Rest erkannt (siehe Ablauf, Schritt 3).
- Reply-To im Versandtool steht bisher auf `support@bdkep.de` (Ticketsystem). Auf `aschumann.bdkep+news@gmail.com` umstellen, sonst landen Abwesenheitsnotizen weiter im Ticketsystem.

## Ablauf

1. Suche wie bisher (`deliveredto:aschumann.bdkep+news@gmail.com`).
2. Je Mail zuerst prüfen, ob das Dokument schon existiert (`quellen/m-<ID>` oder `emails/e-<ID>`), dann überspringen. Vorhandene Dokumente nie überschreiben, dort stehen Aufgaben und Status.
3. Mail einsortieren:
   - **in `emails`**: Zustellfehler, Abwesenheitsnotizen und automatische Antworten (Header, Absender oder Betreff siehe unten). Außerdem Mails, die auf den Newsletter antworten:
     - Betreff-Rest bilden: Präfixe wie „Automatische Antwort:“, „Out of Office:“, „Abwesenheit:“, „Re:“, „AW:“, „Antwort:“, „WG:“ (auch mehrfach, auch englisch) vorn abschneiden, Groß- und Kleinschreibung und Leerzeichen ignorieren.
     - Ein Betreff-Rest, der bei Abwesenheitsnotizen oder Zustellfehlern der letzten 14 Tage am häufigsten vorkommt (bei 100 bis 200 Rückläufern je Versand eindeutig), ist der Betreff des Newsletters. Jede Mail mit diesem Betreff-Rest gehört in `emails`, auch eine persönliche Antwort mit „Re:“.
     - Zusätzlich: Mails mit „Re:“, „AW:“ oder „Antwort:“ im Betreff, die innerhalb von 14 Tagen nach einem Versandtermin (`ausgaben`, `versanddatum`) eingehen, gehören in `emails`.
     - Im Zweifel ebenfalls in `emails`, damit keine Antwort im Eingangskorb der Themen untergeht.
   - **in `quellen`**: alles andere (weitergeleitete Meldungen, Hinweise, Links), unverändert wie bisher.
4. Ist die Mail einer Ausgabe zuzuordnen (jüngster Versandtermin in `ausgaben` vor dem Maildatum), deren Namen in `ausgabe` eintragen.
5. Der Zeitraum der Suche muss mindestens 14 Tage zurückreichen, damit ein ausgefallener Lauf nachgeholt wird. Das Dashboard löscht automatisch geschlossene Mails frühestens nach 30 Tagen, sie werden also nie erneut angelegt.

## Den versendeten Newsletter einlesen (Archiv)

Geht der Newsletter automatisch auch an `aschumann.bdkep+news@gmail.com` (Adresse als Empfänger im Versandtool eintragen), liegt eine Kopie im Postfach. Der Abruf legt sie im Archiv ab und kennt damit den echten Betreff.

- **Erkennen:** Absender ist die Absenderadresse des Newsletters (Platzhalter `<Absenderadresse des Newsletters>`, bitte festlegen) und die Mail ist kein Auto-Reply (kein `Auto-Submitted`, kein „Automatische Antwort“ im Betreff). Diese Mail ist weder Quelle noch Antwort.
- **Ablegen:** Dokument in `archiv`, Felder: `name` (Betreff), `betreff` (Original), `gmailId`, `versanddatum` (Datum der Mail, `JJJJ-MM-TT`), `abschnitte` (je `h2` ein Abschnitt, wie beim HTML-Import: ueberschrift, text, linkText, url), `einleitung`, `abbinder`, `stilvorbild` `false`, `quelle` `mail`, `erfasstAm`.
- **Keine Doppelten, in dieser Reihenfolge prüfen, beim ersten Treffer nichts neu anlegen:**
  1. Es gibt in `archiv` schon ein Dokument mit derselben `gmailId`.
  2. Es gibt ein Dokument mit demselben `betreff` (ohne Beachtung von Groß- und Kleinschreibung und Leerzeichen) und demselben `versanddatum`.
  3. Die Mail gehört zu einer Ausgabe: `ausgaben` mit `status` `planung` und `versanddatum` am Tag der Mail (oder Vortag/Folgetag, wenn es nur eine Ausgabe gibt). Dann gilt die Dokument-ID `archiv/v-<Ausgabe-ID>` (dieselbe wie bei „Als versendet ins Archiv“). Existiert sie schon (von Hand abgelegt), wird sie nur um `betreff` und `gmailId` ergänzt, die vorhandenen Abschnitte bleiben. Existiert sie nicht, wird sie neu angelegt, mit `ausgabeId`, und die Ausgabe auf `status` `versendet`, `versendetAm` gesetzt.
  4. Sonst: neues Dokument `archiv/n-<Gmail-ID>`.
- Das Dashboard schützt zusätzlich: „Als versendet ins Archiv“ legt nichts an, wenn für die Ausgabe schon ein Archiv-Eintrag existiert, und nimmt sie nur aus dem Versandplan.
- **Betreff für die Antwort-Erkennung:** Der Betreff-Rest einer Mail (siehe Ablauf, Schritt 3) wird zuerst mit dem `betreff` des jüngsten Archiv-Eintrags verglichen. Das Zählen der häufigsten Rest-Betreffe bleibt nur als Rückfall, falls noch kein Newsletter eingelesen wurde.
- Reihenfolge im Lauf: zuerst Newsletter-Kopien einlesen, dann Antworten einstufen.

## Einstufung

| `art` | Erkennung | `status` |
|---|---|---|
| `zustellfehler` | Absender `MAILER-DAEMON` oder `postmaster`, Betreff „Undeliverable“, „Delivery Status Notification“, „Zustellung fehlgeschlagen“ | `offen` |
| `abwesenheit` | Header `Auto-Submitted` (nicht `no`), `X-Autoreply`, `X-Autorespond`, `Precedence: auto_reply` oder `bulk`, oder Betreff „Abwesenheit“, „Automatische Antwort“, „Out of Office“, „Auto-Reply“ | siehe unten |
| `antwort` | alles andere in `emails` | `offen` |

Abwesenheit, Entscheidung über `status`:

- **`auto`** nur, wenn alle drei Punkte gelten: Es ist eine Abwesenheitsnotiz, im Text steht ein eindeutiges Rückkehrdatum (alle Schreibweisen, auch „bis Montag, den 3. November“, „back on Nov 3rd“; ohne Jahr gilt das nächste passende Datum), und im Text steht nichts Besonderes. Als Rückkehrdatum gilt der erste Tag, an dem die Person wieder da ist. Steht dort „ab 26.10.2026 wieder erreichbar“, ist es der 26.10.2026; steht nur „bis 25.10. im Urlaub“, ist es der 26.10. Zweisprachige Texte sind normal, nur ein Datum muss sich eindeutig ergeben. Ein Hinweis auf eine Vertretung (Name, Adresse, Telefon, „wenden Sie sich an …“) ist **kein** Sondertext, solange ein Rückkehrdatum dabei steht.
- **`offen`**, wenn eines gilt: kein Rückkehrdatum, Datum nicht eindeutig, Rückkehr mehr als 180 Tage in der Zukunft, oder ein Sondertext wie „nicht mehr im Unternehmen“, „ausgeschieden“, „im Ruhestand“, „Mail wird nicht weitergeleitet“, „Nachfolger“, „Elternzeit“ ohne Ende, ein Hinweis auf eine dauerhaft zuständige andere Person ohne Rückkehrdatum, eine persönliche Nachricht zusätzlich zur Abwesenheit.

Beispiel (Abwesenheit, wird `auto`): Betreff „Automatische Antwort: <Newsletter-Betreff>“, Text „ich befinde mich bis 25.10. im Urlaub … Meine Vertretung ist … Ab 26.10.2026 stehe ich wieder zur Verfügung“, dazu ein englischer Absatz „currently not available, please contact your project manager“. Ergebnis: `art` `abwesenheit`, `rueckkehr` `2026-10-26`, `status` `auto`.
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
