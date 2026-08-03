"""
Configuration Loader
"""

from pathlib import Path
from typing import Any

import yaml


class Settings:
    """
    Loads configuration from YAML.
    """

    def __init__(self, config_file: str = "config/config.yaml") -> None:
        self._config_path = Path(config_file)

        if not self._config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self._config_path}"
            )

        with open(self._config_path, "r", encoding="utf-8") as file:
            self.data: dict[str, Any] = yaml.safe_load(file)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Access nested configuration using dot notation.

        Example:
            settings.get("video.width")
        """

        value: Any = self.data

        for part in key.split("."):
            if isinstance(value, dict):
                value = value.get(part)
            else:
                return default

            if value is None:
                return default

        return value


settings = Settings()