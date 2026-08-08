"""
LLM Provider Manager.

Handles provider selection, fallback, and provider cooldowns.
"""

import logging
import time

from config.settings import Settings
from providers.manager.provider_errors import (
    ProviderError,
    ProviderErrorType,
)
from providers.models import AIRequest, AIResponse
from providers.registry import ProviderRegistry


class LLMManager:
    """Manages LLM providers with priority-based fallback."""

    DEFAULT_COOLDOWN_SECONDS = 60

    def __init__(self) -> None:
        self.settings = Settings()
        self.registry = ProviderRegistry()
        self.logger = logging.getLogger(__name__)

        self._cooldowns: dict[str, float] = {}

    def generate(self, request: AIRequest) -> AIResponse:
        """
        Generate a response using the first available provider.

        Providers are attempted according to configured priority.
        Failed providers may be placed into a temporary cooldown.
        """

        errors: list[str] = []

        for provider_name in self.settings.llm_provider_priority:

            if self._is_on_cooldown(provider_name):
                self.logger.info(
                    "Skipping provider '%s' because it is on cooldown.",
                    provider_name,
                )

                errors.append(
                    f"{provider_name}: cooldown"
                )

                continue

            self.logger.info(
                "Trying LLM provider: %s",
                provider_name,
            )

            try:
                provider = self.registry.get_provider(
                    provider_name
                )

                response = provider.generate(request)

                self.logger.info(
                    "LLM provider succeeded: %s",
                    provider_name,
                )

                self._clear_cooldown(provider_name)

                return response

            except ProviderError as exc:

                self.logger.warning(
                    "LLM provider failed: %s | type=%s",
                    provider_name,
                    exc.error_type.value,
                )

                errors.append(
                    f"{provider_name}: "
                    f"{exc.error_type.value}"
                )

                self._apply_cooldown(
                    provider_name,
                    exc.error_type,
                )

            except Exception as exc:

                self.logger.exception(
                    "Unexpected error from provider: %s",
                    provider_name,
                )

                errors.append(
                    f"{provider_name}: "
                    f"{type(exc).__name__}"
                )

                self._apply_cooldown(
                    provider_name,
                    ProviderErrorType.UNKNOWN,
                )

        error_details = "\n".join(errors)

        raise RuntimeError(
            "All configured LLM providers failed.\n"
            f"{error_details}"
        )

    def _apply_cooldown(
        self,
        provider_name: str,
        error_type: ProviderErrorType,
    ) -> None:
        """Apply a temporary cooldown to a failed provider."""

        cooldown = self.DEFAULT_COOLDOWN_SECONDS

        if error_type == ProviderErrorType.QUOTA_EXHAUSTED:
            cooldown = 300

        elif error_type == ProviderErrorType.RATE_LIMITED:
            cooldown = 60

        elif error_type == ProviderErrorType.AUTHENTICATION_ERROR:
            cooldown = 600

        elif error_type == ProviderErrorType.MODEL_NOT_FOUND:
            cooldown = 600

        elif error_type == ProviderErrorType.SERVER_ERROR:
            cooldown = 60

        elif error_type == ProviderErrorType.TIMEOUT:
            cooldown = 30

        self._cooldowns[provider_name] = (
            time.time() + cooldown
        )

        self.logger.info(
            "Provider '%s' cooldown applied for %s seconds.",
            provider_name,
            cooldown,
        )

    def _is_on_cooldown(
        self,
        provider_name: str,
    ) -> bool:
        """Check whether a provider is currently on cooldown."""

        cooldown_until = self._cooldowns.get(provider_name)

        if cooldown_until is None:
            return False

        if time.time() >= cooldown_until:
            del self._cooldowns[provider_name]

            self.logger.info(
                "Provider '%s' cooldown expired.",
                provider_name,
            )

            return False

        return True

    def _clear_cooldown(
        self,
        provider_name: str,
    ) -> None:
        """Clear cooldown after successful provider usage."""

        self._cooldowns.pop(
            provider_name,
            None,
        )