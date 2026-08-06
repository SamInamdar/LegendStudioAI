from services.story.story_engine import StoryEngine
from services.image.image_engine import ImageEngine


def main():

    story_engine = StoryEngine()
    image_engine = ImageEngine()

    story = story_engine.generate("Poor Boy Success Story")

    images = image_engine.generate(story)

    print("=" * 80)

    print("GENERATED IMAGE PROMPTS")

    print("=" * 80)

    for image in images:

        print("-" * 80)

        print(image.image_path)

        print()

        print(image.prompt)

        print()

    print("=" * 80)


if __name__ == "__main__":
    main()