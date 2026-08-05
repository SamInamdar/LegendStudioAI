"""
Provider Registry.
"""


class ProviderRegistry:
    """Registry of AI providers."""

    def get_provider(self, name: str):

        name = name.lower()

        if name == "gemini":
            from providers.ai.gemini_provider import GeminiProvider
            return GeminiProvider()

        if name == "groq":
            from providers.ai.groq_provider import GroqProvider
            return GroqProvider()

        raise ValueError(f"Unknown provider: {name}")