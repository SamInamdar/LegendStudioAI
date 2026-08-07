from services.story.story_engine import StoryEngine
from services.image import StoryImageGenerator


def main():

    engine = StoryEngine()

    story = engine.generate("Poor Boy Success Story")

    image_generator = StoryImageGenerator()
    image_generator.generate(story)

    print("=" * 80)

    print("TITLE")
    print(story.title)

    print()

    print("HOOK")
    print(story.hook)

    print()

    print("SCENES")

    for scene in story.scenes:
        print("-" * 60)
        print(f"Scene {scene.scene_number}")
        print(f"Narration : {scene.narration}")
        print(f"Emotion   : {scene.emotion}")
        print(f"Duration  : {scene.duration}s")

    print()

    print("MORAL")
    print(story.moral)

    print()

    print("CTA")
    print(story.cta)

    print("=" * 80)


if __name__ == "__main__":
    main()