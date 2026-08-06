"""
Image Prompt Builder.
"""

from services.story.prompt_enhancer import PromptEnhancer
from services.story.story_package import Scene


class ImagePrompts:
    """Builds high-quality cinematic image prompts."""

    @staticmethod
    def build(scene: Scene) -> str:

        enhanced_prompt = PromptEnhancer.enhance(scene.image_prompt)

        return f"""
Create an image with the following description.

{enhanced_prompt}

Camera Angle:
{scene.camera_angle}

Lighting:
{scene.lighting}

Emotion:
{scene.emotion}

Requirements:

- Cinematic composition
- Movie quality
- Hyper realistic
- Professional photography
- No text
- No watermark
- No logo
"""