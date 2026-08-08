from core.bootstrap.bootstrap import Bootstrap
from services.story.story_engine import StoryEngine
from services.asset.scene_asset_generator import SceneAssetGenerator
from services.voice.story_voice_generator import StoryVoiceGenerator
from services.video.video_engine import VideoEngine


def main():

    context = Bootstrap().run()

    story_engine = StoryEngine()
    story = story_engine.generate("Poor Boy Success Story")

    image_generator = SceneAssetGenerator(context.storage)
    images = image_generator.generate(story)

    voice_generator = StoryVoiceGenerator(context.storage)
    audio_files = voice_generator.generate(story)

    print(f"Images generated: {len(images)}")
    print(f"Audio files generated: {len(audio_files)}")

    video_engine = VideoEngine()

    output_path = (
        context.storage.get_videos_path()
        / "test_story.mp4"
    )

    video_engine.generate(
        story=story,
        output_path=str(output_path),
    )

    print("=" * 80)
    print("Video generated successfully.")
    print(output_path)
    print("=" * 80)


if __name__ == "__main__":
    main()