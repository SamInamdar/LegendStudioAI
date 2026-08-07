"""
Voice Factory.
"""

from providers.voice.edge_tts_provider import EdgeTTSProvider


class VoiceFactory:
    """Factory for voice providers."""

    @staticmethod
    def create():
        return EdgeTTSProvider()