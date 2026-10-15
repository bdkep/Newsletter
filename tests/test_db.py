import sqlite3

import pytest
from fastapi.testclient import TestClient


@pytest.fixture()
def env(tmp_path, monkeypatch):
    monkeypatch.setenv("NEWSLETTER_DATA_DIR", str(tmp_path))
    import importlib
    from app import config, db
    importlib.reload(config)
    importlib.reload(db)
    db.init_db()
    return db


def test_schema_tables(env):
    with env.session() as c:
        names = {r[0] for r in c.execute("select name from sqlite_master where type='table'")}
    assert {"source", "topic", "topic_source", "topic_image", "tag", "topic_tag", "issue", "text_block"} <= names


def test_status_constraint(env):
    with env.session() as c:
        with pytest.raises(sqlite3.IntegrityError):
            c.execute("insert into topic (titel, status) values ('x', 'Unsinn')")


def test_issue_delete_releases_topic(env):
    with env.session() as c:
        c.execute("insert into issue (id, name) values (1, 'November 2026')")
        c.execute("insert into topic (id, titel, issue_id) values (1, 'T', 1)")
        c.execute("delete from issue where id=1")
        assert c.execute("select issue_id from topic where id=1").fetchone()[0] is None


def test_status_endpoint(env):
    from app import main
    import importlib
    importlib.reload(main)
    with TestClient(main.app) as client:
        r = client.get("/api/status")
    assert r.status_code == 200 and r.json()["ok"] is True
