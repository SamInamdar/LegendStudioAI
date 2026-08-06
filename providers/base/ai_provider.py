"""
AI Provider Interface.
"""

from abc import ABC, abstractmethod

from providers.models import AIRequest, AIResponse


class AIProvider(ABC):
    """Base AI Provider."""

    @abstractmethod
    def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        """Generate AI response."""