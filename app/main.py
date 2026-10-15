"""Einstiegspunkt der Anwendung (FastAPI)."""
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import config, db


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()
    yield


app = FastAPI(title="Newsletter-Dashboard BdKEP", lifespan=lifespan)


@app.get("/api/status")
def status():
    return {
        "ok": True,
        "api_schluessel_vorhanden": bool(config.ANTHROPIC_API_KEY),
        "modell": config.ANTHROPIC_MODEL,
    }


app.mount("/", StaticFiles(directory=Path(__file__).parent / "static", html=True), name="static")
