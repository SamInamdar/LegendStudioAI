"""
Logger Manager.

Creates and configures the application logger.
"""

import logging
from pathlib import Path


class LoggerManager:
    """Creates and configures the application logger."""

    LOG_FILE = Path("workspace/logs/application.log")

    @classmethod
    def initialize(cls) -> logging.Logger:
        """
        Configure and return the application logger.
        """

        cls.LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

        logger = logging.getLogger("LegendStudioAI")

        if logger.handlers:
            return logger

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler(
            cls.LOG_FILE,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger