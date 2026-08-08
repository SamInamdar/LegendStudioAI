"""
OpenAI Text Provider.
"""

from openai import OpenAI

from config.settings import Settings
from providers.base.text_provider import TextProvider
from providers.manager.provider_errors import (
    ProviderError,
    ProviderErrorType,
)
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
            raise ProviderError(
                provider="openai",
                error_type=ProviderErrorType.AUTHENTICATION_ERROR,
                message="OPENAI_API_KEY is not configured.",
            )

        self.client = OpenAI(
            api_key=self.api_key,
        )

    def generate(self, request: AIRequest) -> AIResponse:
        """Generate text using OpenAI."""

        try:
            response = self.client.responses.create(
                model=self.model,
                instructions=request.system_prompt,
                input=request.user_prompt,
                temperature=request.temperature,
                max_output_tokens=request.max_tokens,
            )

        except Exception as exc:
            error_type = self._classify_error(exc)

            raise ProviderError(
                provider="openai",
                error_type=error_type,
                message=str(exc),
                original_error=exc,
            ) from exc

        text = response.output_text

        if not text:
            raise ProviderError(
                provider="openai",
                error_type=ProviderErrorType.UNKNOWN,
                message="OpenAI returned an empty response.",
            )

        return AIResponse(
            text=text,
            provider="openai",
            model=self.model,
        )

    @staticmethod
    def _classify_error(exc: Exception) -> ProviderErrorType:
        """Classify an OpenAI API error."""

        message = str(exc).lower()

        if "insufficient_quota" in message:
            return ProviderErrorType.QUOTA_EXHAUSTED

        if "quota" in message:
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

        if "500" in message or "503" in message:
            return ProviderErrorType.SERVER_ERROR

        return ProviderErrorType.UNKNOWN