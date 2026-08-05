"""
Story Engine.

Responsible for generating stories.
"""

from providers.factory import AIFactory


class StoryEngine:
    """Story generation engine."""

    def __init__(self) -> None:
        self.provider = AIFactory.create()

    def generate(self, topic: str) -> str:
        """
        Generate a story from a topic.
        """

        prompt = f"""
You are a professional YouTube storyteller.

Write a highly emotional motivational story.

Topic:
{topic}

Requirements:
- Around 250 words
- Strong hook
- Clear ending
- Suitable for YouTube Shorts narration
"""

        return self.provider.generate_text(prompt)