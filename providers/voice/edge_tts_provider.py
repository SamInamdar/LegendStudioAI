"""
Microsoft Edge TTS Provider.
"""

import asyncio

import edge_tts

from providers.voice import VoiceProvider


class EdgeTTSProvider(VoiceProvider):
    """Microsoft Edge Text-to-Speech Provider."""

    VOICE = "en-US-AndrewNeural"

    def generate(
        self,
        text: str,
        output_path: str,
    ) -> None:

        asyncio.run(
            self._generate(
                text=text,
                output_path=output_path,
            )
        )

    async def _generate(
        self,
        text: str,
        output_path: str,
    ) -> None:

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.VOICE,
        )

        await communicate.save(output_path)