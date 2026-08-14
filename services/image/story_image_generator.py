"""
Story Image Generator.
"""

from pathlib import Path

from services.image.image_engine import ImageEngine
from services.story.image_prompt_generator import ImagePromptGenerator
from services.story.shot_planner import ShotPlanner


class StoryImageGenerator:
    """Generates cinematic images for every story shot."""

    def __init__(self):
        self.engine = ImageEngine()

    def generate(self, story):

        print("\nGenerating Cinematic Shot Images...\n")

        total_images = 0

        for scene in story.scenes:

            print("=" * 70)
            print(f"SCENE {scene.scene_number}")
            print("=" * 70)

            # Create cinematic shot plan
            scene.shots = ShotPlanner.plan(scene)

            print(f"Shots planned: {len(scene.shots)}")

            for shot in scene.shots:

                prompt = ImagePromptGenerator.generate(
                    scene=scene,
                    shot=shot,
                )

                output_path = Path(
                    "workspace/assets/images"
                ) / (
                    f"scene_{scene.scene_number:02d}"
                    f"_shot_{shot.shot_number:02d}.png"
                )

                print(
                    f"Generating Scene {scene.scene_number} "
                    f"| Shot {shot.shot_number} "
                    f"| {shot.camera_angle}"
                )

                self.engine.generate(
                    prompt=prompt,
                    output_path=str(output_path),
                )

                print(f"Saved -> {output_path}")

                total_images += 1

        print("\n" + "=" * 70)
        print(f"Total cinematic images generated: {total_images}")
        print("=" * 70)