"""
Story Models.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class Scene:
    """Represents one scene."""

    number: int

    description: str

    image_prompt: str = ""


@dataclass(slots=True)
class Story:
    """Story model."""

    title: str

    hook: str

    story: str

    moral: str

    cta: str

    scenes: list[Scene] = field(default_factory=list)