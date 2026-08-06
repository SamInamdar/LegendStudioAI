"""
OpenAI Image Provider.
"""

from openai import OpenAI

from config.settings import Settings
from providers.base.image_provider import ImageProvider


class OpenAIImageProvider(ImageProvider):
    """OpenAI Image Provider."""

    MODEL = "gpt-image-1"

    def __init__(self):

        settings = Settings()

        self.client = OpenAI(
            api_key=settings.openai_api_key,
        )

    def generate_image(
        self,
        prompt: str,
        output_path: str,
    ) -> None:

        response = self.client.images.generate(
            model=self.MODEL,
            prompt=prompt,
            size="1024x1024",
        )

        image_base64 = response.data[0].b64_json

        import base64

        with open(output_path, "wb") as file:
            file.write(base64.b64decode(image_base64))