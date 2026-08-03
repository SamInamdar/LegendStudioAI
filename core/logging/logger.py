from pathlib import Path
import logging
import logging.config
import yaml


class LoggerManager:
    """Initializes the application's logging configuration."""

    def __init__(self) -> None:
        config_path = Path("core/logging/logging.yaml")

        with config_path.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

        Path("logs").mkdir(exist_ok=True)

        logging.config.dictConfig(config)

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        return logging.getLogger(name)