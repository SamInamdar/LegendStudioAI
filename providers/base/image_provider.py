"""
Image Provider Interface.
"""

from abc import ABC, abstractmethod


class ImageProvider(ABC):
    """Base Image Provider."""

    @abstractmethod
    def generate_image(
        self,
        prompt: str,
        output_path: str,
    ) -> None:
        """
        Generate an image and save it to output_path.
        """
        pass