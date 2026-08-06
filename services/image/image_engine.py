"""
Image Engine.
"""

from providers.factory.ai_factory import AIFactory
from providers.models import AIRequest

from services.image.image_prompts import ImagePrompts
from services.image.models import ImageRequest, ImageResult
from services.story.story_package import StoryPackage


class ImageEngine:
    """Generates images for story scenes."""

    def __init__(self):
        self.provider = AIFactory.create()

    def generate(self, story: StoryPackage) -> list[ImageResult]:

        images = []

        for scene in story.scenes:

            prompt = ImagePrompts.build(scene)

            request = AIRequest(
                system_prompt="You are an expert cinematic image prompt engineer.",
                user_prompt=prompt,
            )

            # Temporary placeholder.
            # In the next sprint this will call an actual image model.
            self.provider.generate(request)

            images.append(
                ImageResult(
                    prompt=prompt,
                    image_path=f"workspace/assets/images/scene_{scene.scene_number:03}.png",
                )
            )

        return images