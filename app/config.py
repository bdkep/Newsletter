"""Zentrale Konfiguration. Der API-Schlüssel kommt nur aus der Umgebung."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = Path(os.environ.get("NEWSLETTER_DATA_DIR", BASE_DIR / "data"))
DB_PATH = DATA_DIR / "newsletter.db"
FILES_DIR = DATA_DIR / "files"
DESIGN_DIR = BASE_DIR / "design"
STYLE_FILE = BASE_DIR / "style.md"

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")  # optional
ANTHROPIC_MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5-5")
IMAGE_BASE_URL = os.environ.get("IMAGE_BASE_URL", "https://example.invalid/bilder/")
TEXT_WORDS_MIN = int(os.environ.get("TEXT_WORDS_MIN", 40))
TEXT_WORDS_MAX = int(os.environ.get("TEXT_WORDS_MAX", 80))


def ensure_dirs() -> None:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
