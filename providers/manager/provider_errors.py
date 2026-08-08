"""
Provider error definitions.

Provides standardized error categories for LLM providers.
"""

from enum import Enum


class ProviderErrorType(str, Enum):
    """Standard provider error categories."""

    RATE_LIMITED = "rate_limited"

    QUOTA_EXHAUSTED = "quota_exhausted"

    AUTHENTICATION_ERROR = "authentication_error"

    MODEL_NOT_FOUND = "model_not_found"

    SERVER_ERROR = "server_error"

    TIMEOUT = "timeout"

    UNKNOWN = "unknown"


class ProviderError(Exception):
    """Standardized provider exception."""

    def __init__(
        self,
        provider: str,
        error_type: ProviderErrorType,
        message: str,
        original_error: Exception | None = None,
    ) -> None:
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error

        super().__init__(message)