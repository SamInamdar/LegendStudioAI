"""
Provider Registry.
"""

from providers.text.gemini_provider import GeminiProvider
from providers.text.groq_provider import GroqProvider
from providers.text.openrouter_provider import OpenRouterProvider
from providers.text.openai_provider import OpenAIProvider


class ProviderRegistry:
    """Registry of AI providers."""

    def get_provider(self, name: str):

        name = name.lower()

        if name == "gemini":
            return GeminiProvider()

        if name == "groq":
            return GroqProvider()

        if name == "openrouter":
            return OpenRouterProvider()

        if name == "openai":
            return OpenAIProvider()

        raise ValueError(f"Unknown provider: {name}")