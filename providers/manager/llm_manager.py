"""
LLM Provider Manager.

Handles provider selection and automatic fallback.
"""

import logging

from config.settings import Settings
from providers.models import AIRequest, AIResponse
from providers.registry import ProviderRegistry


class LLMManager:
    """Manages LLM providers with priority-based fallback."""

    def __init__(self) -> None:
        self.settings = Settings()
        self.registry = ProviderRegistry()
        self.logger = logging.getLogger(__name__)

    def generate(self, request: AIRequest) -> AIResponse:
        """
        Generate a response using the first successful provider.

        Providers are attempted according to the configured priority.
        """

        errors: list[str] = []

        for provider_name in self.settings.llm_provider_priority:
            self.logger.info(
                "Trying LLM provider: %s",
                provider_name,
            )

            try:
                provider = self.registry.get_provider(provider_name)

                response = provider.generate(request)

                self.logger.info(
                    "LLM provider succeeded: %s",
                    provider_name,
                )

                return response

            except Exception as exc:
                error_message = (
                    f"{provider_name}: "
                    f"{type(exc).__name__}: {exc}"
                )

                errors.append(error_message)

                self.logger.warning(
                    "LLM provider failed: %s",
                    error_message,
                )

        error_details = "\n".join(errors)

        raise RuntimeError(
            "All configured LLM providers failed.\n"
            f"{error_details}"
        )