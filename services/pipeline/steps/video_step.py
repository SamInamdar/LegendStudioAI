"""
Video Pipeline Step.
"""

from pathlib import Path

from services.pipeline.pipeline_step import PipelineStep
from services.video.video_engine import VideoEngine


class VideoStep(PipelineStep):
    """Creates the final video."""

    def __init__(self) -> None:
        self.engine = VideoEngine()

    def execute(self, context):

        output_path = (
            context.application_context.storage.get_videos_path()
            / "final_video.mp4"
        )

        self.engine.generate(
            story=context.story,
            output_path=str(output_path),
        )

        context.video_path = Path(output_path)

        return context