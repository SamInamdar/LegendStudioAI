"""
Base AI Provider interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class AIProvider(ABC):
    """Abstract base class for all AI providers."""

    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        """
        Generate text from a prompt.

        Args:
            prompt: Input prompt.

        Returns:
            Generated text.
        """
        raise NotImplementedError