"""
Story Package Models.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class Shot:
    """Single cinematic shot inside a scene."""

    shot_number: int

    prompt: str

    duration: float

    camera_movement: str = ""

    camera_angle: str = ""

    transition: str = ""


@dataclass(slots=True)
class Scene:
    """Single story scene."""

    scene_number: int

    narration: str

    emotion: str

    duration: int

    image_prompt: str = ""
    camera_angle: str = ""
    lighting: str = ""

    shots: list[Shot] = field(default_factory=list)


@dataclass(slots=True)
class StoryPackage:
    """Complete story package."""

    title: str

    hook: str

    scenes: list[Scene] = field(default_factory=list)

    moral: str = ""

    cta: str = ""