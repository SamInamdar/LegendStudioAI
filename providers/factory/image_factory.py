"""
Image Factory.
"""

from providers.image.pollinations_provider import PollinationsProvider


class ImageFactory:
    """Creates image providers."""

    @staticmethod
    def create():

        # Later this can come from config:
        # image_provider = Settings().image_provider

        return PollinationsProvider()