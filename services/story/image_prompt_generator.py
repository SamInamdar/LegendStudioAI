"""
Image Prompt Generator.
"""


class ImagePromptGenerator:
    """Generates cinematic image prompts."""

    @staticmethod
    def generate(scene) -> str:
        """Generate a cinematic prompt from a story scene."""

        return f"""
{scene.narration}

Emotion:
{scene.emotion}

Visual Style:
Ultra realistic,
cinematic,
Hollywood movie,
8K,
masterpiece,
highly detailed,
volumetric lighting,
global illumination,
sharp focus,
dramatic composition,
professional color grading,
no text,
no watermark,
no logo
""".strip()