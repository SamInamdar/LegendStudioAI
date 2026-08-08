from core import context
from services import story
from services.story.story_engine import StoryEngine
from services.asset.scene_asset_generator import SceneAssetGenerator
from core.bootstrap.bootstrap import Bootstrap


def main():

    engine = StoryEngine()

    story = engine.generate("Poor Boy Success Story")

    context = Bootstrap().run()
    image_generator = SceneAssetGenerator(context.storage)
    images = image_generator.generate(story)

    print()
    print(f"Images generated: {len(images)}")

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