"""
OpenAI Text Provider.
"""

from openai import OpenAI

from config.settings import Settings
from providers.base.text_provider import TextProvider
from providers.models import AIRequest, AIResponse


class OpenAIProvider(TextProvider):
    """Text generation provider using OpenAI."""

    def __init__(self) -> None:
        settings = Settings()

        self.api_key = settings.openai_api_key
        self.model = getattr(
            settings,
            "openai_model",
            "gpt-5-mini",
        )

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is not configured.")

        self.client = OpenAI(api_key=self.api_key)

    def generate(self, request: AIRequest) -> AIResponse:
        """Generate text using OpenAI."""

        response = self.client.responses.create(
            model=self.model,
            instructions=request.system_prompt,
            input=request.user_prompt,
            temperature=request.temperature,
            max_output_tokens=request.max_tokens,
        )

        return AIResponse(
            text=response.output_text,
            provider="openai",
            model=self.model,
        )