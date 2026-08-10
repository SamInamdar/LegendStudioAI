"""
Cinematic Shot Planner.
"""

from services.story.story_package import Scene, Shot


class ShotPlanner:
    """Creates visually distinct cinematic shots for story scenes."""

    SHOT_STYLES = [
        {
            "type": "establishing",
            "camera": "slow cinematic push-in",
            "angle": "wide",
            "instruction": (
                "Establish the complete environment and location. "
                "Show where the character is, what surrounds them, "
                "and the overall situation."
            ),
        },
        {
            "type": "action",
            "camera": "gentle cinematic tracking movement",
            "angle": "medium",
            "instruction": (
                "Show the character actively performing the key "
                "physical action described in the story."
            ),
        },
        {
            "type": "emotion",
            "camera": "slow cinematic push toward the face",
            "angle": "close-up",
            "instruction": (
                "Capture the strongest emotional moment through "
                "facial expression, eyes, posture, and body language."
            ),
        },
        {
            "type": "detail",
            "camera": "subtle cinematic handheld movement",
            "angle": "detail",
            "instruction": (
                "Focus on an important symbolic detail such as "
                "hands, tools, books, shoes, machinery, money, "
                "technology, or another object from the story."
            ),
        },
    ]

    @staticmethod
    def _extract_visual_moment(scene: Scene, shot_type: str) -> str:
        """Extract a useful visual moment from the narration."""

        sentences = [
            sentence.strip()
            for sentence in (
                scene.narration
                .replace("!", ".")
                .replace("?", ".")
                .split(".")
            )
            if sentence.strip()
        ]

        if not sentences:
            return scene.narration

        if shot_type == "establishing":
            return sentences[0]

        if shot_type == "action":
            return sentences[1] if len(sentences) > 1 else sentences[0]

        if shot_type == "emotion":
            return sentences[-1]

        if shot_type == "detail":
            return sentences[0]

        return scene.narration

    @classmethod
    def plan(cls, scene: Scene) -> list[Shot]:
        """Create cinematic shots for one scene."""

        word_count = len(scene.narration.split())

        if word_count < 40:
            shot_count = 3
        elif word_count < 65:
            shot_count = 4
        else:
            shot_count = 4

        shot_count = min(
            shot_count,
            len(cls.SHOT_STYLES),
        )

        duration = scene.duration / shot_count

        shots = []

        for index in range(shot_count):

            style = cls.SHOT_STYLES[index]

            visual_moment = cls._extract_visual_moment(
                scene,
                style["type"],
            )

            prompt = (
                f"VISUAL MOMENT:\n"
                f"{visual_moment}\n\n"

                f"SHOT TYPE:\n"
                f"{style['type']}\n\n"

                f"CAMERA DIRECTION:\n"
                f"{style['instruction']}\n\n"

                f"EMOTION:\n"
                f"{scene.emotion}\n\n"

                "CHARACTER CONSISTENCY:\n"
                "Maintain the same character identity throughout "
                "the entire story. Keep age, facial structure, "
                "hairstyle, skin tone, body proportions and clothing "
                "consistent with previous shots.\n\n"

                "VISUAL STYLE:\n"
                "Photorealistic cinematic photography, realistic "
                "human proportions, realistic environment, natural "
                "facial expressions, Hollywood film composition, "
                "dramatic depth of field, volumetric lighting, "
                "professional film color grading, highly detailed, "
                "sharp focus, realistic textures.\n\n"

                "QUALITY RESTRICTIONS:\n"
                "No text, no subtitles, no watermark, no logo, "
                "no captions, no distorted hands, no extra fingers, "
                "no duplicate people, no deformed faces."
            )

            shots.append(
                Shot(
                    shot_number=index + 1,
                    prompt=prompt,
                    duration=round(duration, 2),
                    camera_movement=style["camera"],
                    camera_angle=style["angle"],
                    transition="smooth cinematic dissolve",
                )
            )

        return shots