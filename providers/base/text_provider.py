"""
Text Provider Interface.
"""

from abc import ABC, abstractmethod

from providers.models import AIRequest, AIResponse


class TextProvider(ABC):
    """Base Text Provider."""

    @abstractmethod
    def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """Generate text response."""
        pass