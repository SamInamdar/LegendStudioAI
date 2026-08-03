"""
Legend Studio AI
Global Project Constants
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ASSETS_DIR = PROJECT_ROOT / "assets"
CACHE_DIR = PROJECT_ROOT / "storage" / "cache"
DATABASE_DIR = PROJECT_ROOT / "storage" / "database"
PROJECTS_DIR = PROJECT_ROOT / "projects"
LOGS_DIR = PROJECT_ROOT / "logs"

APP_NAME = "Legend Studio AI"
APP_VERSION = "0.1.0"