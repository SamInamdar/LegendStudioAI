from services.story import StoryEngine


def main():

    engine = StoryEngine()

    story = engine.generate("Poor Boy Success Story")

    print("=" * 80)

    print("TITLE")
    print(story.title)

    print()

    print("HOOK")
    print(story.hook)

    print()

    print("SCENES")

    for scene in story.scenes:

        print(f"{scene.scene_number}. {scene.narration}")

    print()

    print("MORAL")
    print(story.moral)

    print()

    print("CTA")
    print(story.cta)

    print("=" * 80)


if __name__ == "__main__":
    main()