"""
Pipeline Context.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class PipelineContext:
    """Stores data shared between pipeline steps."""

    application_context: Any

    topic: str

    story: Any = None

    images: list[Path] = field(default_factory=list)

    audio_files: list[Path] = field(default_factory=list)

    video_path: Path | None = None

    data: dict[str, Any] = field(default_factory=dict)