"""
Prompt Enhancer.
"""


class PromptEnhancer:
    """Enhances image prompts."""

    @staticmethod
    def enhance(prompt: str) -> str:

        return (
            f"{prompt}, "
            "cinematic, "
            "ultra realistic, "
            "masterpiece, "
            "8k, "
            "highly detailed, "
            "photorealistic, "
            "dramatic lighting, "
            "volumetric light, "
            "sharp focus, "
            "film photography, "
            "Kodak Vision3, "
            "85mm lens"
        )