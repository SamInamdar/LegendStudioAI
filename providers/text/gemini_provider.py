"""
Gemini Provider.
"""

from google import genai

from config.settings import Settings
from providers.base.text_provider import TextProvider
from providers.manager.provider_errors import (
    ProviderError,
    ProviderErrorType,
)
from providers.models import AIRequest, AIResponse


class GeminiProvider(TextProvider):
    """Google Gemini implementation."""

    def __init__(self) -> None:
        settings = Settings()

        self.model = settings.gemini_model

        self.client = genai.Client(
            api_key=settings.gemini_api_key,
        )

    def generate(self, request: AIRequest) -> AIResponse:
        """Generate text using Gemini."""

        prompt = f"""
{request.system_prompt}

{request.user_prompt}
"""

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )

        except Exception as exc:
            error_type = self._classify_error(exc)

            raise ProviderError(
                provider="gemini",
                error_type=error_type,
                message=str(exc),
                original_error=exc,
            ) from exc

        return AIResponse(
            text=response.text,
            provider="gemini",
            model=self.model,
        )

    @staticmethod
    def _classify_error(exc: Exception) -> ProviderErrorType:
        """Classify a Gemini API error."""

        message = str(exc).lower()

        if "resource_exhausted" in message:
            if "quota" in message:
                return ProviderErrorType.QUOTA_EXHAUSTED

            return ProviderErrorType.RATE_LIMITED

        if "429" in message:
            if "quota" in message:
                return ProviderErrorType.QUOTA_EXHAUSTED

            return ProviderErrorType.RATE_LIMITED

        if "unauthenticated" in message:
            return ProviderErrorType.AUTHENTICATION_ERROR

        if "invalid api key" in message:
            return ProviderErrorType.AUTHENTICATION_ERROR

        if "401" in message:
            return ProviderErrorType.AUTHENTICATION_ERROR

        if "not found" in message:
            return ProviderErrorType.MODEL_NOT_FOUND

        if "404" in message:
            return ProviderErrorType.MODEL_NOT_FOUND

        if "503" in message or "500" in message:
            return ProviderErrorType.SERVER_ERROR

        if "timeout" in message:
            return ProviderErrorType.TIMEOUT

        return ProviderErrorType.UNKNOWN