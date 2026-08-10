"""
Story Image Generator.
"""

from pathlib import Path

from services.image.image_engine import ImageEngine
from services.story.image_prompt_generator import ImagePromptGenerator


class StoryImageGenerator:
    """Generates cinematic shot images for every scene."""

    def __init__(self):

        self.engine = ImageEngine()

    def generate(self, story):

        print("\nGenerating Cinematic Images...\n")

        images = []

        image_dir = Path("workspace/assets/images")
        image_dir.mkdir(parents=True, exist_ok=True)

        for scene in story.scenes:

            # Backward compatibility:
            # If a scene has no planned shots, use the
            # original scene-level image generation.
            shots = scene.shots

            if not shots:

                prompt = ImagePromptGenerator.generate(scene)

                output_path = (
                    image_dir
                    / f"scene_{scene.scene_number:02d}.png"
                )

                print(
                    f"Generating Scene {scene.scene_number}..."
                )

                self.engine.generate(
                    prompt=prompt,
                    output_path=str(output_path),
                )

                images.append(output_path)

                print(f"Saved -> {output_path}")

                continue

            for shot in shots:

                output_path = (
                    image_dir
                    / (
                        f"scene_{scene.scene_number:02d}"
                        f"_shot_{shot.shot_number:02d}.png"
                    )
                )

                print(
                    f"Generating Scene {scene.scene_number} "
                    f"Shot {shot.shot_number}..."
                )

                self.engine.generate(
                    prompt=shot.prompt,
                    output_path=str(output_path),
                )

                images.append(output_path)

                print(f"Saved -> {output_path}")

        print(
            f"\nCinematic images generated: {len(images)}\n"
        )

        return images