"""
Story Image Generator.
"""

from services.image.image_engine import ImageEngine
from services.story.image_prompt_generator import ImagePromptGenerator


class StoryImageGenerator:
    """Generates images for every scene."""

    def __init__(self):

        self.engine = ImageEngine()

    def generate(self, story):

        print("\nGenerating Images...\n")

        for scene in story.scenes:

            prompt = ImagePromptGenerator.generate(scene)

            output_path = (
                f"workspace/assets/images/"
                f"scene_{scene.scene_number:02d}.png"
            )

            print(f"Generating Scene {scene.scene_number}...")

            self.engine.generate(
                prompt=prompt,
                output_path=output_path,
            )

            print(f"✓ Saved -> {output_path}")

        print("\nAll images generated successfully!\n")