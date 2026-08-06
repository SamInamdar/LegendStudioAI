"""
Image Engine.
"""

import os

from providers.factory.image_factory import ImageFactory


class ImageEngine:
    """Generates images from prompts."""

    def __init__(self):

        self.provider = ImageFactory.create()

    def generate(
        self,
        prompt: str,
        output_path: str,
    ):

        folder = os.path.dirname(output_path)

        os.makedirs(folder, exist_ok=True)

        self.provider.generate_image(
            prompt=prompt,
            output_path=output_path,
        )