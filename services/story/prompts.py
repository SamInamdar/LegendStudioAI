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

IMPORTANT:
Return ONLY valid JSON.
Do NOT use markdown.
Do NOT write any explanation.
Do NOT add extra text before or after the JSON.

Return this EXACT JSON schema:

{{
    "title":"...",
    "hook":"...",
    "scenes":[
        {{
            "scene_number":1,
            "narration":"...",
            "emotion":"...",
            "duration":5
        }},
        {{
            "scene_number":2,
            "narration":"...",
            "emotion":"...",
            "duration":5
        }},
        {{
            "scene_number":3,
            "narration":"...",
            "emotion":"...",
            "duration":5
        }},
        {{
            "scene_number":4,
            "narration":"...",
            "emotion":"...",
            "duration":5
        }},
        {{
            "scene_number":5,
            "narration":"...",
            "emotion":"...",
            "duration":5
        }}
    ],
    "moral":"...",
    "cta":"Subscribe for more inspiring stories."
}}

Rules:

- Exactly 5 scenes.
- narration should be 2–4 sentences.
- Use simple, emotional English.
- Build the story from struggle to success.
- End with a powerful moral.
- Return ONLY valid JSON.
"""