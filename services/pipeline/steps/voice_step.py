"""
Voice Pipeline Step.
"""

from services.pipeline.pipeline_step import PipelineStep
from services.voice.story_voice_generator import StoryVoiceGenerator


class VoiceStep(PipelineStep):
    """Generates narration audio."""

    def __init__(self) -> None:
        self.generator = None

    def execute(self, context):

        if self.generator is None:
            self.generator = StoryVoiceGenerator(
                context.application_context.storage
            )

        context.audio_files = self.generator.generate(
            context.story
        )

        return context