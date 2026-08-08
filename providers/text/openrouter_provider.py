"""
OpenRouter Text Provider.
"""

import requests

from config.settings import Settings
from providers.base.text_provider import TextProvider
from providers.manager.provider_errors import (
    ProviderError,
    ProviderErrorType,
)
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
            raise ProviderError(
                provider="openrouter",
                error_type=ProviderErrorType.AUTHENTICATION_ERROR,
                message="OPENROUTER_API_KEY is not configured.",
            )

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

        try:
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

        except requests.Timeout as exc:
            raise ProviderError(
                provider="openrouter",
                error_type=ProviderErrorType.TIMEOUT,
                message=str(exc),
                original_error=exc,
            ) from exc

        except requests.HTTPError as exc:
            status_code = (
                exc.response.status_code
                if exc.response is not None
                else None
            )

            if status_code == 401:
                error_type = ProviderErrorType.AUTHENTICATION_ERROR

            elif status_code == 404:
                error_type = ProviderErrorType.MODEL_NOT_FOUND

            elif status_code == 429:
                error_type = ProviderErrorType.RATE_LIMITED

            elif status_code is not None and status_code >= 500:
                error_type = ProviderErrorType.SERVER_ERROR

            else:
                error_type = ProviderErrorType.UNKNOWN

            raise ProviderError(
                provider="openrouter",
                error_type=error_type,
                message=str(exc),
                original_error=exc,
            ) from exc

        except requests.RequestException as exc:
            raise ProviderError(
                provider="openrouter",
                error_type=ProviderErrorType.UNKNOWN,
                message=str(exc),
                original_error=exc,
            ) from exc

        choices = data.get("choices", [])

        if not choices:
            raise ProviderError(
                provider="openrouter",
                error_type=ProviderErrorType.UNKNOWN,
                message="OpenRouter returned no choices.",
            )

        message = choices[0].get("message", {})

        text = message.get("content")

        if text is None:
            text = choices[0].get("text")

        if not text:
            raise ProviderError(
                provider="openrouter",
                error_type=ProviderErrorType.UNKNOWN,
                message=(
                    "OpenRouter returned an empty response. "
                    f"Response data: {data}"
                ),
            )

        return AIResponse(
            text=str(text),
            provider="openrouter",
            model=self.model,
        )