"""SQLite-Anbindung und Schema (Datenmodell nach Vorgabe, Abschnitt 6)."""
import sqlite3
from contextlib import contextmanager

from . import config

SCHEMA = """
CREATE TABLE IF NOT EXISTS source (
    id INTEGER PRIMARY KEY,
    typ TEXT NOT NULL CHECK (typ IN ('document','link','mail','note','image')),
    titel TEXT NOT NULL DEFAULT '',
    original_pfad TEXT,
    url TEXT,
    extrahierter_text TEXT NOT NULL DEFAULT '',
    metadaten TEXT NOT NULL DEFAULT '{}',
    erfasst_am TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS issue (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    versanddatum TEXT,
    status TEXT NOT NULL DEFAULT 'Planung'
        CHECK (status IN ('Planung','In Redaktion','Fertig','Versendet')),
    einleitung TEXT NOT NULL DEFAULT '',
    notiz TEXT NOT NULL DEFAULT '',
    archiviert INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS topic (
    id INTEGER PRIMARY KEY,
    titel TEXT NOT NULL,
    beschreibung TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'Idee'
        CHECK (status IN ('Idee','Text in Arbeit','Text fertig','Freigegeben')),
    issue_id INTEGER REFERENCES issue(id) ON DELETE SET NULL,
    position INTEGER NOT NULL DEFAULT 0,
    layout TEXT NOT NULL DEFAULT 'bild_oben'
        CHECK (layout IN ('bild_oben','bild_links','ohne_bild')),
    weiterlesen_url TEXT,
    notizen TEXT NOT NULL DEFAULT ''
);
CREATE TABLE IF NOT EXISTS topic_source (
    topic_id INTEGER NOT NULL REFERENCES topic(id) ON DELETE CASCADE,
    source_id INTEGER NOT NULL REFERENCES source(id) ON DELETE CASCADE,
    PRIMARY KEY (topic_id, source_id)
);
CREATE TABLE IF NOT EXISTS topic_image (
    id INTEGER PRIMARY KEY,
    topic_id INTEGER NOT NULL REFERENCES topic(id) ON DELETE CASCADE,
    pfad TEXT NOT NULL,
    alt_text TEXT NOT NULL DEFAULT '',
    bildunterschrift TEXT NOT NULL DEFAULT '',
    position INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS tag (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS topic_tag (
    topic_id INTEGER NOT NULL REFERENCES topic(id) ON DELETE CASCADE,
    tag_id INTEGER NOT NULL REFERENCES tag(id) ON DELETE CASCADE,
    PRIMARY KEY (topic_id, tag_id)
);
CREATE TABLE IF NOT EXISTS text_block (
    id INTEGER PRIMARY KEY,
    topic_id INTEGER NOT NULL REFERENCES topic(id) ON DELETE CASCADE,
    version INTEGER NOT NULL,
    ueberschrift TEXT NOT NULL DEFAULT '',
    kurztext TEXT NOT NULL DEFAULT '',
    link_text TEXT NOT NULL DEFAULT '',
    erzeugt_durch TEXT NOT NULL DEFAULT 'manuell' CHECK (erzeugt_durch IN ('manuell','api')),
    erstellt_am TEXT NOT NULL DEFAULT (datetime('now')),
    ist_aktuell INTEGER NOT NULL DEFAULT 1,
    UNIQUE (topic_id, version)
);
CREATE INDEX IF NOT EXISTS idx_topic_issue ON topic(issue_id, position);
"""


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(config.DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


@contextmanager
def session():
    conn = connect()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db() -> None:
    config.ensure_dirs()
    with session() as conn:
        conn.executescript(SCHEMA)
