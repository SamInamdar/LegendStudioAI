"""
Storage Manager.

High-level interface for all storage operations.
"""

from pathlib import Path
from typing import Any

from infrastructure.storage.file_manager import FileManager
from infrastructure.storage.path_manager import PathManager


class StorageManager:
    """
    Central storage service.

    Combines PathManager and FileManager into one API.
    """

    def __init__(self) -> None:
        self.paths = PathManager()
        self.files = FileManager()

    def initialize(self) -> None:
        """Initialize storage."""
        self.paths.initialize()

    def get_images_path(self) -> Path:
        return self.paths.get_images_path()

    def get_audio_path(self) -> Path:
        return self.paths.get_audio_path()

    def get_music_path(self) -> Path:
        return self.paths.get_music_path()

    def get_videos_path(self) -> Path:
        return self.paths.get_videos_path()

    def get_cache_path(self) -> Path:
        return self.paths.get_cache_path()

    def write_json(self, path: Path, data: dict[str, Any]) -> None:
        self.files.write_json(path, data)

    def read_json(self, path: Path) -> dict[str, Any]:
        return self.files.read_json(path)

    def exists(self, path: Path) -> bool:
        return self.files.exists(path)

    def delete(self, path: Path) -> None:
        self.files.delete(path)