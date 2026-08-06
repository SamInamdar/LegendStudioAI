"""
Story Engine.
"""

from providers.factory.ai_factory import AIFactory
from providers.models import AIRequest

from services.story.prompts import StoryPrompts
from services.story.story_mapper import StoryMapper
from utils.json_parser import JsonParser


class StoryEngine:
    """Generates structured motivational stories."""

    def __init__(self):

        self.provider = AIFactory.create()

    def generate(self, topic: str):

        request = AIRequest(
            system_prompt="You are a world-class motivational storyteller.",
            user_prompt=StoryPrompts.motivational(topic),
        )

        response = self.provider.generate(request)

        data = JsonParser.parse(response.text)

        return StoryMapper.from_dict(data)