"""
Content Plan Models.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class ContentItem:
    day: str
    format: str
    category: str
    topic: str
    priority: int


@dataclass(slots=True)
class ContentPlan:
    items: list[ContentItem] = field(default_factory=list)