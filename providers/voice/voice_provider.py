"""
Voice Provider Interface.
"""

from abc import ABC, abstractmethod


class VoiceProvider(ABC):
    """Base Voice Provider."""

    @abstractmethod
    def generate(
        self,
        text: str,
        output_path: str,
    ) -> None:
        """Generate voice from text."""