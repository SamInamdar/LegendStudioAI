"""
Image Models.
"""

from dataclasses import dataclass


@dataclass
class ImageRequest:
    """Request for generating an image."""

    prompt: str
    output_name: str


@dataclass
class ImageResult:
    """Generated image."""

    prompt: str
    image_path: str