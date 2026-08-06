"""
Story Mapper.
"""

from services.story.story_package import StoryPackage, Scene


class StoryMapper:
    """Maps AI JSON into StoryPackage."""

    @staticmethod
    def from_dict(data: dict) -> StoryPackage:

        scenes = []

        for item in data["scenes"]:

            scenes.append(
                Scene(
                    scene_number=item["scene_number"],
                    narration=item["narration"],
                    image_prompt=item["image_prompt"],
                    camera_angle=item["camera_angle"],
                    lighting=item["lighting"],
                    emotion=item["emotion"],
                    duration=item["duration"],
                )
            )

        return StoryPackage(
            title=data["title"],
            hook=data["hook"],
            scenes=scenes,
            moral=data["moral"],
            cta=data["cta"],
        )