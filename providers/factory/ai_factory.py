"""
AI Factory.

Creates AI providers based on configuration.
"""

from config.settings import Settings
from providers.registry import ProviderRegistry


class AIFactory:
    """Factory for AI providers."""

    @staticmethod
    def create():
        settings = Settings()

        provider_name = getattr(settings, "ai_provider", "gemini")

        registry = ProviderRegistry()

        return registry.get_provider(provider_name)