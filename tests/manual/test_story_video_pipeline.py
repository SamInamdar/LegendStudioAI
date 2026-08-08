from services.pipeline.story_video_pipeline import StoryVideoPipeline


def main():

    pipeline = StoryVideoPipeline()

    video_path = pipeline.generate(
        "Poor Boy Success Story"
    )

    print("=" * 80)
    print("COMPLETE VIDEO PIPELINE SUCCESS")
    print("=" * 80)
    print(f"Video: {video_path}")
    print("=" * 80)


if __name__ == "__main__":
    main()