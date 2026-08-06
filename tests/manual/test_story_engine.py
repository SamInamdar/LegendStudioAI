from services.story.story_engine import StoryEngine


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
        print("-" * 60)
        print(f"Scene {scene.scene_number}")
        print(f"Narration : {scene.narration}")
        print(f"Image     : {scene.image_prompt}")
        print(f"Camera    : {scene.camera_angle}")
        print(f"Lighting  : {scene.lighting}")
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