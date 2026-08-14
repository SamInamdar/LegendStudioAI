"""
Cinematic Scene Asset Generator.
"""

from pathlib import Path

from services.image.image_engine import ImageEngine
from services.story.image_prompt_generator import ImagePromptGenerator
from services.story.shot_planner import ShotPlanner
from services.story.story_package import StoryPackage


class SceneAssetGenerator:
    """Generates cinematic shot images for story scenes."""

    def __init__(self, storage) -> None:
        self.storage = storage
        self.image_engine = ImageEngine()

    def generate(self, story: StoryPackage) -> list[Path]:
        """Generate images for every cinematic shot."""

        images = []

        images_path = self.storage.get_images_path()

        for scene in story.scenes:

            # Create cinematic shots for the scene.
            if not scene.shots:
                scene.shots = ShotPlanner.plan(scene)

            print(
                f"\nScene {scene.scene_number}: "
                f"{len(scene.shots)} shots"
            )

            for shot in scene.shots:

                # Generate the shot-specific prompt.
                base_prompt = ImagePromptGenerator.generate(scene)

                prompt = (
                    f"{base_prompt}\n\n"
                    f"CINEMATIC SHOT:\n"
                    f"{shot.prompt}\n\n"
                    f"CAMERA ANGLE:\n"
                    f"{shot.camera_angle}\n\n"
                    f"CAMERA MOVEMENT:\n"
                    f"{shot.camera_movement}\n\n"
                    "SHOT QUALITY:\n"
                    "Photorealistic cinematic film frame, "
                    "realistic human anatomy, natural skin texture, "
                    "realistic lighting, cinematic depth of field, "
                    "professional color grading, "
                    "high production value."
                )

                output_path = (
                    images_path
                    / (
                        f"scene_{scene.scene_number:02d}"
                        f"_shot_{shot.shot_number:02d}.png"
                    )
                )

                print(
                    f"Generating Shot "
                    f"{scene.scene_number}.{shot.shot_number}..."
                )

                self.image_engine.generate(
                    prompt=prompt,
                    output_path=str(output_path),
                )

                print(
                    f"Saved -> {output_path}"
                )

                images.append(output_path)

        return images