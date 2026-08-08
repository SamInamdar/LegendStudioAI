"""
Story Video Pipeline.
"""

from pathlib import Path

from core.bootstrap.bootstrap import Bootstrap
from services.pipeline.pipeline import Pipeline
from services.pipeline.pipeline_context import PipelineContext
from services.pipeline.steps import (
    ImageStep,
    StoryStep,
    VideoStep,
    VoiceStep,
)


class StoryVideoPipeline:
    """Runs the complete story-to-video pipeline."""

    def __init__(self) -> None:
        self.application_context = Bootstrap().run()

        self.pipeline = (
            Pipeline()
            .add_step(StoryStep())
            .add_step(ImageStep())
            .add_step(VoiceStep())
            .add_step(VideoStep())
        )

    def generate(self, topic: str) -> Path:
        """Generate a complete video from a story topic."""

        context = PipelineContext(
            application_context=self.application_context,
            topic=topic,
        )

        context = self.pipeline.execute(context)

        if context.video_path is None:
            raise RuntimeError(
                "Pipeline completed without generating a video."
            )

        return context.video_path