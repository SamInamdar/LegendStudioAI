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
            "image_prompt":"...",
            "camera_angle":"Eye Level",
            "lighting":"Golden Hour",
            "emotion":"Hope",
            "duration":5
        }},
        {{
            "scene_number":2,
            "narration":"...",
            "image_prompt":"...",
            "camera_angle":"Wide Shot",
            "lighting":"Morning",
            "emotion":"Struggle",
            "duration":5
        }},
        {{
            "scene_number":3,
            "narration":"...",
            "image_prompt":"...",
            "camera_angle":"Close Up",
            "lighting":"Natural",
            "emotion":"Determination",
            "duration":5
        }},
        {{
            "scene_number":4,
            "narration":"...",
            "image_prompt":"...",
            "camera_angle":"Cinematic",
            "lighting":"Sunset",
            "emotion":"Success",
            "duration":5
        }},
        {{
            "scene_number":5,
            "narration":"...",
            "image_prompt":"...",
            "camera_angle":"Drone Shot",
            "lighting":"Golden Hour",
            "emotion":"Inspiration",
            "duration":5
        }}
    ],
    "moral":"...",
    "cta":"Subscribe for more inspiring stories."
}}

Rules:

- Exactly 5 scenes.
- Every scene must contain ALL fields.
- image_prompt must describe the image in cinematic detail.
- narration should be 2–4 sentences.
- Return ONLY JSON.
"""