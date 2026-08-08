from core.bootstrap.bootstrap import Bootstrap
from services.story.story_engine import StoryEngine
from services.voice.story_voice_generator import StoryVoiceGenerator


def main():

    context = Bootstrap().run()

    story_engine = StoryEngine()
    story = story_engine.generate("Poor Boy Success Story")

    voice_generator = StoryVoiceGenerator(context.storage)

    audio_files = voice_generator.generate(story)

    print("=" * 80)
    print(f"Audio files generated: {len(audio_files)}")

    for audio_file in audio_files:
        print(audio_file)

    print("=" * 80)


if __name__ == "__main__":
    main()