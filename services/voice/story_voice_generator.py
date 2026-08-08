"""
Story Voice Generator.
"""

from pathlib import Path

from services.story.story_package import StoryPackage
from services.voice.voice_engine import VoiceEngine


class StoryVoiceGenerator:
    """Generates voice audio for every story scene."""

    def __init__(self, storage) -> None:
        self.storage = storage
        self.voice_engine = VoiceEngine()

    def generate(self, story: StoryPackage) -> list[Path]:
        """Generate one audio file for each story scene."""

        audio_files = []

        audio_path = self.storage.get_audio_path()

        for scene in story.scenes:

            output_path = (
                audio_path
                / f"scene_{scene.scene_number:02d}.mp3"
            )

            self.voice_engine.generate(
                text=scene.narration,
                output_path=str(output_path),
            )

            audio_files.append(output_path)

        return audio_files