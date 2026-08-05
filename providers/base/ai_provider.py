"""
Base AI Provider Interface.
"""

from abc import ABC, abstractmethod


class AIProvider(ABC):
    """Base interface for all AI providers."""

    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        """
        Generate text from a prompt.
        """
        raise NotImplementedError