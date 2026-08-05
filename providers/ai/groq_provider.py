"""
Groq Provider.
"""

from groq import Groq

from config.settings import Settings
from providers.base.ai_provider import AIProvider


class GroqProvider(AIProvider):
    """Groq AI Provider."""

    def __init__(self) -> None:
        settings = Settings()

        self.client = Groq(
            api_key=settings.groq_api_key,
        )

    def generate_text(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content