"""
Groq Provider.
"""

from groq import Groq

from config.settings import Settings
from providers.base.ai_provider import AIProvider
from providers.models import AIRequest, AIResponse


class GroqProvider(AIProvider):
    """Groq AI Provider."""

    def __init__(self) -> None:
        settings = Settings()

        self.client = Groq(
            api_key=settings.groq_api_key,
        )

    def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """Generate text using Groq."""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": request.system_prompt,
                },
                {
                    "role": "user",
                    "content": request.user_prompt,
                },
            ],
            temperature=request.temperature,
        )

        return AIResponse(
            text=response.choices[0].message.content,
            provider="groq",
            model="llama-3.3-70b-versatile",
        )