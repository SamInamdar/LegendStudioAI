"""
Provider Registry.

Stores available AI providers.
"""

from providers.base import AIProvider


class ProviderRegistry:
    """Registers and retrieves AI providers."""

    def __init__(self) -> None:
        self._providers: dict[str, AIProvider] = {}

    def register(self, name: str, provider: AIProvider) -> None:
        """Register a provider."""
        self._providers[name] = provider

    def get(self, name: str) -> AIProvider:
        """Retrieve a provider by name."""
        return self._providers[name]