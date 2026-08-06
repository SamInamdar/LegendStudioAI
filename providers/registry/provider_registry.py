"""
Provider Registry.
"""

from providers.text.gemini_provider import GeminiProvider
from providers.text.groq_provider import GroqProvider


class ProviderRegistry:
    """Registry of AI providers."""

    def get_provider(self, name: str):

        name = name.lower()

        if name == "gemini":
            return GeminiProvider()

        if name == "groq":
            return GroqProvider()

        raise ValueError(f"Unknown provider: {name}")