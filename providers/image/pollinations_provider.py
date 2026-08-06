"""
Pollinations Image Provider.
"""

import requests

from providers.base.image_provider import ImageProvider


class PollinationsProvider(ImageProvider):
    """Free image generation using Pollinations AI."""

    def generate_image(
        self,
        prompt: str,
        output_path: str,
    ) -> None:

        prompt = prompt.replace(" ", "%20")

        url = f"https://image.pollinations.ai/prompt/{prompt}"

        response = requests.get(url, timeout=120)

        response.raise_for_status()

        with open(output_path, "wb") as file:
            file.write(response.content)