"""
Groq Provider.
"""

from groq import Groq

from config.settings import Settings
from providers.base.text_provider import TextProvider
from providers.manager.provider_errors import (
    ProviderError,
    ProviderErrorType,
)
from providers.models import AIRequest, AIResponse


class GroqProvider(TextProvider):
    """Groq AI Provider."""

    def __init__(self) -> None:
        settings = Settings()

        self.api_key = settings.groq_api_key
        self.model = getattr(
            settings,
            "groq_model",
            "llama-3.3-70b-versatile",
        )

        if not self.api_key:
            raise ProviderError(
                provider="groq",
                error_type=ProviderErrorType.AUTHENTICATION_ERROR,
                message="GROQ_API_KEY is not configured.",
            )

        self.client = Groq(
            api_key=self.api_key,
        )

    def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """Generate text using Groq."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
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
                max_tokens=request.max_tokens,
            )

        except Exception as exc:
            error_type = self._classify_error(exc)

            raise ProviderError(
                provider="groq",
                error_type=error_type,
                message=str(exc),
                original_error=exc,
            ) from exc

        if not response.choices:
            raise ProviderError(
                provider="groq",
                error_type=ProviderErrorType.UNKNOWN,
                message="Groq returned no choices.",
            )

        text = response.choices[0].message.content

        if not text:
            raise ProviderError(
                provider="groq",
                error_type=ProviderErrorType.UNKNOWN,
                message="Groq returned an empty response.",
            )

        return AIResponse(
            text=text,
            provider="groq",
            model=self.model,
        )

    @staticmethod
    def _classify_error(
        exc: Exception,
    ) -> ProviderErrorType:
        """Classify a Groq API error."""

        message = str(exc).lower()

        if "quota" in message:
            return ProviderErrorType.QUOTA_EXHAUSTED

        if "insufficient" in message and "credit" in message:
            return ProviderErrorType.QUOTA_EXHAUSTED

        if "rate limit" in message:
            return ProviderErrorType.RATE_LIMITED

        if "429" in message:
            return ProviderErrorType.RATE_LIMITED

        if "authentication" in message:
            return ProviderErrorType.AUTHENTICATION_ERROR

        if "invalid api key" in message:
            return ProviderErrorType.AUTHENTICATION_ERROR

        if "401" in message:
            return ProviderErrorType.AUTHENTICATION_ERROR

        if "model" in message and "not found" in message:
            return ProviderErrorType.MODEL_NOT_FOUND

        if "404" in message:
            return ProviderErrorType.MODEL_NOT_FOUND

        if "timeout" in message:
            return ProviderErrorType.TIMEOUT

        if "500" in message or "502" in message:
            return ProviderErrorType.SERVER_ERROR

        if "503" in message:
            return ProviderErrorType.SERVER_ERROR

        return ProviderErrorType.UNKNOWN