"""
Image Pipeline Step.
"""

from services.asset.scene_asset_generator import SceneAssetGenerator
from services.pipeline.pipeline_step import PipelineStep


class ImageStep(PipelineStep):
    """Generates scene images."""

    def __init__(self) -> None:
        self.generator = None

    def execute(self, context):

        if self.generator is None:
            self.generator = SceneAssetGenerator(
                context.application_context.storage
            )

        context.images = self.generator.generate(
            context.story
        )

        return context