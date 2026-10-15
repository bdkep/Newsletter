# Newsletter-Dashboard BdKEP

Lokale Web-Anwendung: Inhalte sammeln, auf Ausgaben verteilen, Kurztexte erstellen und einen HTML-Newsletter im BdKEP-Design zusammensetzen. Arbeitsgrundlage ist die Vorgabe `newsletter-dashboard-vorgabe.md`. Kein Versand aus dem Dashboard.

## Stand

| Stufe | Inhalt | Status |
|---|---|---|
| 1 | Gerüst, Datenmodell, Start-Skript, README | fertig |
| 2 | Inbox (alle Quelltypen) inkl. täglichem Mailabruf 23:45 (Abschnitt 3.1a der Vorgabe) | offen |
| 3 | Themenkarten und Board | offen |
| 4 | Textbausteine, API-Erzeugung | offen |
| 5 | Design und Export | offen (Designdateien nötig) |
| 6 | Prüfung | offen |

## Technikwahl

Python mit FastAPI und SQLite (Standardbibliothek `sqlite3`, kein ORM), Frontend als statische Seiten ohne Build-System. Wenige Abhängigkeiten, ein Befehl zum Start, alle Daten in einem Ordner.

## Installation und Start

Voraussetzung: Python 3.10 oder neuer.

```
./start.sh
```

Das Skript legt beim ersten Start `.venv` an, installiert die Pakete und startet den Server unter <http://127.0.0.1:8000>. Anderer Port: `PORT=8080 ./start.sh`.

## Konfiguration (Umgebungsvariablen)

| Variable | Bedeutung | Standard |
|---|---|---|
| `ANTHROPIC_API_KEY` | Schlüssel für die Texterzeugung (optional, nie in Dateien ablegen) | nicht gesetzt |
| `ANTHROPIC_MODEL` | Modell für Textbausteine | `claude-sonnet-5-5` |
| `NEWSLETTER_DATA_DIR` | Datenordner | `./data` |
| `IMAGE_BASE_URL` | Basis-Pfad für Bild-URLs im Export | Platzhalter |
| `TEXT_WORDS_MIN` / `TEXT_WORDS_MAX` | Richtwert Kurztext | 40 / 80 |

Ohne API-Schlüssel startet die Anwendung vollständig; alle Texte werden dann manuell geschrieben. Stilvorgaben für die Erzeugung stehen in `style.md`.

## Daten und Sicherung

Alles liegt unter `data/` (`newsletter.db` und `files/` mit den Originaldateien). Sicherung: Anwendung beenden und den Ordner `data/` kopieren oder als ZIP ablegen. `data/` ist nicht im Git-Repository.

## Design

Designdateien gehören nach `design/` (siehe `design/README.md`). Sie fehlen noch und werden vor Stufe 5 benötigt.

## Tests

```
.venv/bin/pytest
```
