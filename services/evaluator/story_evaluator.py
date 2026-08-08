"""
Story Evaluator.
"""

from services.story.story_package import StoryPackage


class StoryEvaluator:
    """Validates generated stories."""

    MIN_SCENES = 5
    MAX_SCENES = 5

    def evaluate(self, story: StoryPackage) -> tuple[bool, list[str]]:
        """Evaluate a StoryPackage."""

        errors: list[str] = []

        if not story.title.strip():
            errors.append("Title is empty.")

        if not story.hook.strip():
            errors.append("Hook is empty.")

        if not story.moral.strip():
            errors.append("Moral is empty.")

        if not story.cta.strip():
            errors.append("CTA is empty.")

        scene_count = len(story.scenes)

        if scene_count < self.MIN_SCENES:
            errors.append(
                f"Too few scenes: {scene_count}."
            )

        if scene_count > self.MAX_SCENES:
            errors.append(
                f"Too many scenes: {scene_count}."
            )

        for scene in story.scenes:

            if not scene.narration.strip():
                errors.append(
                    f"Scene {scene.scene_number}: narration is empty."
                )

            if not scene.emotion.strip():
                errors.append(
                    f"Scene {scene.scene_number}: emotion is empty."
                )

            if scene.duration <= 0:
                errors.append(
                    f"Scene {scene.scene_number}: invalid duration."
                )

        return len(errors) == 0, errors