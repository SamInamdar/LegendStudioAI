"""
Path Manager.

Responsible for managing all workspace paths.
"""

from pathlib import Path


class PathManager:
    """Manages workspace directories."""

    def __init__(self) -> None:
        self._workspace = Path("workspace")

        self._assets = self._workspace / "assets"
        self._images = self._assets / "images"
        self._audio = self._assets / "audio"
        self._music = self._assets / "music"
        self._videos = self._assets / "videos"
        self._subtitles = self._assets / "subtitles"

        self._cache = self._workspace / "cache"
        self._exports = self._workspace / "exports"
        self._metadata = self._workspace / "metadata"
        self._projects = self._workspace / "projects"
        self._temp = self._workspace / "temp"
        self._logs = self._workspace / "logs"

    def initialize(self) -> None:
        """Create all required workspace directories."""
        directories = [
            self._workspace,
            self._assets,
            self._images,
            self._audio,
            self._music,
            self._videos,
            self._subtitles,
            self._cache,
            self._exports,
            self._metadata,
            self._projects,
            self._temp,
            self._logs,
        ]

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)

    def get_workspace_path(self) -> Path:
        return self._workspace

    def get_assets_path(self) -> Path:
        return self._assets

    def get_images_path(self) -> Path:
        return self._images

    def get_audio_path(self) -> Path:
        return self._audio

    def get_music_path(self) -> Path:
        return self._music

    def get_videos_path(self) -> Path:
        return self._videos

    def get_subtitles_path(self) -> Path:
        return self._subtitles

    def get_cache_path(self) -> Path:
        return self._cache

    def get_exports_path(self) -> Path:
        return self._exports

    def get_metadata_path(self) -> Path:
        return self._metadata

    def get_projects_path(self) -> Path:
        return self._projects

    def get_temp_path(self) -> Path:
        return self._temp

    def get_logs_path(self) -> Path:
        return self._logs