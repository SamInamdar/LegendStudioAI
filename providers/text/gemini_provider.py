"""
Gemini Provider.
"""

from google import genai

from config.settings import Settings
from providers.base.text_provider import TextProvider
from providers.models import AIRequest, AIResponse


class GeminiProvider(TextProvider):
    """Google Gemini implementation."""

    MODEL = "gemini-2.0-flash"

    def __init__(self):

        settings = Settings()

        self.client = genai.Client(
            api_key=settings.gemini_api_key,
        )

    def generate(self, request: AIRequest) -> AIResponse:

        prompt = f"""
{request.system_prompt}

{request.user_prompt}
"""

        response = self.client.models.generate_content(
            model=self.MODEL,
            contents=prompt,
        )

        return AIResponse(
            text=response.text,
            provider="gemini",
            model=self.MODEL,
        )