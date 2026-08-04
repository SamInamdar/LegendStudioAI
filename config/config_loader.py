"""
Configuration loader.

Loads environment variables from the .env file.
"""

from pathlib import Path

from dotenv import load_dotenv


class ConfigLoader:
    """Loads application configuration."""

    @staticmethod
    def load() -> None:
        """Load environment variables from .env."""

        env_path = Path(".env")

        if env_path.exists():
            load_dotenv(env_path)