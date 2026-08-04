"""
Application Context.

Stores shared services used across the application.
"""

from dataclasses import dataclass
from logging import Logger
from typing import Optional

from config.settings import Settings


@dataclass(slots=True)
class ApplicationContext:
    """
    Shared application context.

    This object is created once during startup and passed to all
    modules requiring access to shared services.
    """

    settings: Settings

    logger: Optional[Logger] = None

    storage: Optional["StorageManager"] = None

    cache: Optional["CacheManager"] = None

    providers: Optional["ProviderRegistry"] = None