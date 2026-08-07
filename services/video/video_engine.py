"""
Video Engine.
"""

from pathlib import Path

from moviepy import (
    AudioFileClip,
    ImageClip,
    concatenate_videoclips,
)


class VideoEngine:
    """Creates a video from images and narration."""

    def generate(
        self,
        story,
        output_path: str,
    ) -> None:

        clips = []

        image_dir = Path("workspace/assets/images")
        audio_dir = Path("workspace/assets/audio")

        for scene in story.scenes:

            image_path = image_dir / f"scene_{scene.scene_number:02}.png"
            audio_path = audio_dir / f"scene_{scene.scene_number:02}.mp3"

            audio = AudioFileClip(str(audio_path))

            clip = (
                ImageClip(str(image_path))
                .with_duration(audio.duration)
                .resized(lambda t: 1 + (0.08 * t / audio.duration))
                .with_audio(audio)
            )

            clips.append(clip)

        final_video = concatenate_videoclips(
            clips,
            method="compose",
        )

        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        final_video.write_videofile(
            output_path,
            fps=30,
            codec="libx264",
            audio_codec="aac",
        )

        final_video.close()