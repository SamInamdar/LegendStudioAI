"""
Application Settings.
"""

from dataclasses import dataclass
import os

from config.config_loader import ConfigLoader


ConfigLoader.load()


@dataclass(slots=True)
class Settings:
    """Application settings loaded from environment."""

    app_env: str = os.getenv("APP_ENV", "development")

    log_level: str = os.getenv("LOG_LEVEL", "INFO")

    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")

    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")

    groq_api_key: str = os.getenv("GROQ_API_KEY", "")

    elevenlabs_api_key: str = os.getenv("ELEVENLABS_API_KEY", "")

    youtube_client_id: str = os.getenv("YOUTUBE_CLIENT_ID", "")

    youtube_client_secret: str = os.getenv("YOUTUBE_CLIENT_SECRET", "")