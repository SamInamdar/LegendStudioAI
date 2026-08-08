"""
OpenRouter Text Provider.
"""

import requests

from config.settings import Settings
from providers.base.text_provider import TextProvider
from providers.models import AIRequest, AIResponse


class OpenRouterProvider(TextProvider):
    """Text generation provider using OpenRouter."""

    BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

    def __init__(self) -> None:
        settings = Settings()
        self.api_key = settings.openrouter_api_key
        self.model = getattr(
            settings,
            "openrouter_model",
            "openrouter/free",
        )

    def generate(self, request: AIRequest) -> AIResponse:
        """Generate text using OpenRouter."""

        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY is not configured.")

        messages = [
            {
                "role": "system",
                "content": request.system_prompt,
            },
            {
                "role": "user",
                "content": request.user_prompt,
            },
        ]

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": request.temperature,
            "max_tokens": request.max_tokens,
        }

        response = requests.post(
            self.BASE_URL,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=60,
        )

        response.raise_for_status()

        data = response.json()

        text = data["choices"][0]["message"]["content"]

        return AIResponse(
            text=text,
            provider="openrouter",
            model=self.model,
        )