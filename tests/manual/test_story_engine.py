from services.story import StoryEngine


def main():

    engine = StoryEngine()

    story = engine.generate(
        "A poor boy who became successful through hard work"
    )

    print("\n")
    print("=" * 80)
    print(story)
    print("=" * 80)


if __name__ == "__main__":
    main()