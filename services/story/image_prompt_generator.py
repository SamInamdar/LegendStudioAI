"""
Image Prompt Generator.
"""

from providers.factory import AIFactory


class ImagePromptGenerator:
    """Generate cinematic image prompts."""

    def __init__(self):
        self.provider = AIFactory.create()

    def generate(self, description: str) -> str:

        prompt = f"""
You are a Hollywood movie concept artist.

Convert the following scene into a cinematic AI image prompt.

Scene:
{description}

Rules:

- Ultra realistic
- Cinematic
- 8K
- Highly detailed
- Emotional
- Natural lighting
- DSLR photography
- Sharp focus
- Realistic human anatomy
- Professional color grading

Return ONLY the image prompt.
"""

        return self.provider.generate_text(prompt)