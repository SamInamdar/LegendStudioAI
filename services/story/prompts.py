"""
Story Prompt Builder.
"""


class StoryPrompts:
    """Collection of Story prompts."""

    @staticmethod
    def motivational(topic: str) -> str:

        return f"""
You are an expert YouTube storyteller.

Create an ORIGINAL motivational story.

TOPIC:
{topic}

Return ONLY valid JSON.

Do NOT write markdown.

JSON FORMAT:

Return ONLY valid JSON.

{{
    "title":"...",
    "hook":"...",
    "story":"...",
    "scenes":[
        {{
            "number":1,
            "description":"..."
        }},
        {{
            "number":2,
            "description":"..."
        }},
        {{
            "number":3,
            "description":"..."
        }},
        {{
            "number":4,
            "description":"..."
        }},
        {{
            "number":5,
            "description":"..."
        }}
    ],
    "moral":"...",
    "cta":"Subscribe for more inspiring stories."
}}

Requirements:

- Story around 250 words
- Emotional
- Strong hook
- Happy ending
- Simple English
- Generate exactly 5 scenes.
"""