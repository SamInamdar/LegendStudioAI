"""
Image Prompt Generator.
"""


class ImagePromptGenerator:
    """Generates cinematic image prompts."""

    @staticmethod
    def generate(scene) -> str:

        return f"""
{scene.narration}

Emotion: {scene.emotion}

Style:
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
professional color grading
""".strip()