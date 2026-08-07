"""
Voice Engine.
"""

from providers.factory.voice_factory import VoiceFactory


class VoiceEngine:
    """Voice generation engine."""

    def __init__(self):

        self.provider = VoiceFactory.create()

    def generate(
        self,
        text: str,
        output_path: str,
    ) -> None:

        self.provider.generate(
            text=text,
            output_path=output_path,
        )