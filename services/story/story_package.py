"""
Story Package Models.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class Scene:
    """Single story scene."""

    scene_number: int

    narration: str

    emotion: str

    duration: int


@dataclass(slots=True)
class StoryPackage:
    """Complete story package."""

    title: str

    hook: str

    scenes: list[Scene] = field(default_factory=list)

    moral: str = ""

    cta: str = ""