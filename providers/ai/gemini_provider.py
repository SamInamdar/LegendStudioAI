"""
Gemini Provider.
"""

from google import genai

from config.settings import Settings
from providers.base.ai_provider import AIProvider
from providers.models import AIRequest, AIResponse


class GeminiProvider(AIProvider):
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
            provider="Gemini",
            model=self.MODEL,
        )