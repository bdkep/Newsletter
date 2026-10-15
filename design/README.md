# Designdateien (BdKEP)

Quelle: BdKEP Design System (claude.ai), gemeinsame Grundlage aller BdKEP-Dashboards (Hub, Sekretariat, Aufgaben, Finanzcockpit).

- `tokens.json` – Farben, Schrift, Abstände, Logo-Pfade, Fußtext (zentrale Werte für Export, Stufe 5)
- `colors.css`, `typography.css`, `spacing.css` – Original-Tokens des Design Systems
- `logo/` – Logos (kurz/voll, hell/invers); Regeln: nie auf weißem Feld, Mindesthöhe 24 px (kurz) bzw. 64 px (voll)
- `beispiel-newsletter-2026-09-30.html` – bisheriger Newsletter als Vorlage für `newsletter-template.html` (Stufe 5)

Die Oberfläche (`app/static/style.css`) nutzt dieselben Werte; Dunkelmodus folgt der Systemeinstellung.
Noch offen für Stufe 5: Vorlage mit Platzhaltern, Rechtspflichtangaben im Fuß, Bild-Hosting.
