"""
AI Response Model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class AIResponse:
    """Standard AI response."""

    text: str

    provider: str

    model: str