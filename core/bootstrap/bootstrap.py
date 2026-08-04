"""
Bootstrap module.

Responsible for initializing the application infrastructure.
"""

from config.settings import Settings
from core.context.application_context import ApplicationContext
from core.logging import LoggerManager
from infrastructure.storage import StorageManager


class Bootstrap:
    """Initializes Legend Studio AI."""

    def run(self) -> ApplicationContext:
        """
        Initialize the application.

        Returns:
            ApplicationContext: Fully initialized application context.
        """

        # Initialize logger
        logger = LoggerManager.initialize()
        logger.info("Starting Legend Studio AI...")

        # Load settings
        settings = Settings()
        logger.info("Configuration loaded.")

        # Initialize storage
        storage = StorageManager()
        storage.initialize()
        logger.info("Storage initialized.")

        # Build application context
        context = ApplicationContext(
            settings=settings,
            logger=logger,
            storage=storage,
        )

        logger.info("Bootstrap completed successfully.")

        return context