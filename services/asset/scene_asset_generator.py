"""
Scene Asset Generator.
"""

from pathlib import Path

from services.image.image_engine import ImageEngine
from services.story.story_package import StoryPackage
from services.story.image_prompt_generator import ImagePromptGenerator


class SceneAssetGenerator:
    """Generates image assets for story scenes."""

    def __init__(self, storage) -> None:
        self.storage = storage
        self.image_engine = ImageEngine()

    def generate(self, story: StoryPackage) -> list[Path]:
        """Generate one image for each story scene."""

        images = []

        images_path = self.storage.get_images_path()

        for scene in story.scenes:
            if not scene.image_prompt:
                scene.image_prompt = ImagePromptGenerator.generate(scene)

            output_path = (
                images_path
                / f"scene_{scene.scene_number:02d}.png"
            )

            self.image_engine.generate(
                prompt=scene.image_prompt,
                output_path=str(output_path),
            )

            images.append(output_path)

        return images