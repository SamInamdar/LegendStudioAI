"""
Story Pipeline Step.
"""

from services.pipeline.pipeline_step import PipelineStep
from services.story.story_engine import StoryEngine


class StoryStep(PipelineStep):
    """Generates the story."""

    def __init__(self) -> None:
        self.engine = StoryEngine()

    def execute(self, context):

        context.story = self.engine.generate(context.topic)

        return context