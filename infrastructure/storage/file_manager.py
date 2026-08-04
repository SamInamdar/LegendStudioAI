"""
File Manager.

Handles reading and writing files.
"""

import json
from pathlib import Path
from typing import Any


class FileManager:
    """Provides common file operations."""

    @staticmethod
    def write_json(path: Path, data: dict[str, Any]) -> None:
        """
        Write JSON data to a file.

        Args:
            path: Destination file path.
            data: Dictionary to write.
        """
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def read_json(path: Path) -> dict[str, Any]:
        """
        Read JSON from a file.

        Args:
            path: JSON file path.

        Returns:
            Dictionary containing JSON data.
        """
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def exists(path: Path) -> bool:
        """Check whether a file exists."""
        return path.exists()

    @staticmethod
    def delete(path: Path) -> None:
        """Delete a file if it exists."""
        if path.exists():
            path.unlink()