"""
Cinematic Image Prompt Generator.
"""

from services.story.story_package import Scene, Shot


class ImagePromptGenerator:
    """Generates cinematic prompts for individual story shots."""

    @staticmethod
    def generate(scene: Scene, shot: Shot | None = None) -> str:
        """
        Generate an image prompt.

        If a shot is provided, the prompt is built specifically
        for that shot. Otherwise, it falls back to scene-level
        generation for backward compatibility.
        """

        if shot is None:
            return ImagePromptGenerator._scene_prompt(scene)

        return ImagePromptGenerator._shot_prompt(scene, shot)

    @staticmethod
    def _scene_prompt(scene: Scene) -> str:

        return f"""
STORY MOMENT:
{scene.narration}

EMOTION:
{scene.emotion}

CHARACTER CONTINUITY:
Maintain the same main character identity throughout the entire story.
Keep age, facial structure, hairstyle, skin tone, body proportions,
and clothing consistent.

VISUAL STYLE:
Photorealistic cinematic photography,
Hollywood feature film quality,
realistic human proportions,
realistic environment,
natural facial expressions,
dramatic depth of field,
volumetric lighting,
realistic textures,
professional cinematic color grading,
sharp focus.

QUALITY:
No text,
no subtitles,
no watermark,
no logo,
no captions,
no distorted hands,
no extra fingers,
no duplicate people,
no deformed faces.
""".strip()

    @staticmethod
    def _shot_prompt(scene: Scene, shot: Shot) -> str:

        return f"""
CINEMATIC STORY FRAME

STORY MOMENT:
{scene.narration}

SHOT PURPOSE:
{shot.camera_angle}

SHOT VISUAL DIRECTION:
{shot.prompt}

CAMERA ANGLE:
{shot.camera_angle}

CAMERA MOVEMENT:
{shot.camera_movement}

EMOTION:
{scene.emotion}

CHARACTER CONTINUITY:
Maintain the exact same main character identity established
for this story.

Keep consistent:
- age
- facial structure
- hairstyle
- skin tone
- body proportions
- clothing
- accessories
- overall appearance

The character must look like the same person across every scene,
even when the character ages throughout the story.

VISUAL STORYTELLING:
The frame must visually communicate the specific story moment.

Do not simply create a generic portrait.

Show the character actually performing the action described
in the shot.

Use meaningful environmental details that support the story.

The environment should change naturally according to the story:
poverty, childhood streets, workshop, technology laboratory,
startup office, rural village, awards stage, or modern city.

COMPOSITION:
Use cinematic composition appropriate for the shot.

Create clear foreground, middle ground, and background separation.

Use realistic depth of field.

Make the primary storytelling subject visually dominant.

LIGHTING:
Cinematic natural lighting appropriate to the scene.

Use realistic shadows, highlights, reflections, and atmospheric depth.

VISUAL STYLE:
Photorealistic cinematic photography,
Hollywood feature film,
ultra realistic,
highly detailed,
realistic skin texture,
realistic clothing texture,
realistic environment,
dramatic depth of field,
volumetric lighting,
global illumination,
professional film color grading,
sharp focus,
cinematic atmosphere.

QUALITY RESTRICTIONS:
No text,
no subtitles,
no watermark,
no logo,
no captions,
no distorted hands,
no extra fingers,
no missing fingers,
no duplicate people,
no duplicated objects,
no deformed face,
no unrealistic anatomy,
no cartoon,
no illustration,
no plastic-looking skin.
""".strip()