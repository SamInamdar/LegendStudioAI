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

    # API Keys
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")

    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")

    openrouter_api_key: str = os.getenv("OPENROUTER_API_KEY", "")

    groq_api_key: str = os.getenv("GROQ_API_KEY", "")

    elevenlabs_api_key: str = os.getenv("ELEVENLABS_API_KEY", "")

    # Provider Models
    gemini_model: str = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.0-flash",
    )

    openai_model: str = os.getenv(
        "OPENAI_MODEL",
        "gpt-5-mini",
    )

    openrouter_model: str = os.getenv(
        "OPENROUTER_MODEL",
        "openrouter/free",
    )

    groq_model: str = os.getenv(
        "GROQ_MODEL",
        "llama-3.3-70b-versatile",
    )

    # YouTube
    youtube_client_id: str = os.getenv(
        "YOUTUBE_CLIENT_ID",
        "",
    )

    youtube_client_secret: str = os.getenv(
        "YOUTUBE_CLIENT_SECRET",
        "",
    )

    # AI Provider Configuration
    ai_provider: str = os.getenv(
        "AI_PROVIDER",
        "gemini",
    )

    llm_provider_priority: tuple[str, ...] = (
        "gemini",
        "openrouter",
        "groq",
        "openai",
    )

    default_llm_model: str = os.getenv(
        "DEFAULT_LLM_MODEL",
        "",
    )