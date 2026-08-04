"""
Tests for PathManager.
"""

from infrastructure.storage.path_manager import PathManager


def test_initialize_creates_workspace_directories():
    """
    Verify that PathManager creates all required directories.
    """

    manager = PathManager()
    manager.initialize()

    assert manager.get_workspace_path().exists()
    assert manager.get_assets_path().exists()
    assert manager.get_images_path().exists()
    assert manager.get_audio_path().exists()
    assert manager.get_music_path().exists()
    assert manager.get_videos_path().exists()
    assert manager.get_subtitles_path().exists()
    assert manager.get_cache_path().exists()
    assert manager.get_exports_path().exists()
    assert manager.get_metadata_path().exists()
    assert manager.get_projects_path().exists()
    assert manager.get_temp_path().exists()
    assert manager.get_logs_path().exists()