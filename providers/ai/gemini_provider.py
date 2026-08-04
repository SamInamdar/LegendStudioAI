"""
Gemini Provider.

Google Gemini implementation.
"""

from google import genai

from config.settings import Settings


class GeminiProvider:
    """Google Gemini Provider."""

    def __init__(self) -> None:
        settings = Settings()

        self.client = genai.Client(
            api_key=settings.gemini_api_key,
        )

    def generate_text(self, prompt: str) -> str:
        """
        Generate text using Gemini.
        """

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        return response.text