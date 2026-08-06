"""
AI Request Model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class AIRequest:
    """Standard request for every AI provider."""

    system_prompt: str

    user_prompt: str

    temperature: float = 0.7

    max_tokens: int = 4096