"""
Story Engine.
"""

from providers.manager.llm_manager import LLMManager
from providers.models import AIRequest
from services.story.image_prompt_generator import ImagePromptGenerator
from services.evaluator.story_evaluator import StoryEvaluator
from services.story.prompts import StoryPrompts
from services.story.story_mapper import StoryMapper
from utils.json_parser import JsonParser


class StoryEngine:
    """Generates and validates structured motivational stories."""

    def __init__(self) -> None:
        self.provider = LLMManager()
        self.evaluator = StoryEvaluator()

    def generate(self, topic: str):
        """Generate and validate a motivational story."""

        request = AIRequest(
            system_prompt="You are a world-class motivational storyteller.",
            user_prompt=StoryPrompts.motivational(topic),
        )
       
        response = self.provider.generate(request)

        print("=" * 80)
        print("Response text:")
        print(repr(response.text))
        print("=" * 80)

        data = JsonParser.parse(response.text)

        story = StoryMapper.from_dict(data)

        for scene in story.scenes:
            scene.image_prompt = ImagePromptGenerator.generate(scene)

        is_valid, errors = self.evaluator.evaluate(story)

        if not is_valid:
            error_details = "\n".join(
                f"- {error}"
                for error in errors
            )

            raise ValueError(
                "Generated story failed validation:\n"
                f"{error_details}"
            )

        return story