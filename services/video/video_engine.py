"""
Cinematic Video Engine.
"""

from pathlib import Path

from moviepy import (
    AudioFileClip,
    ImageClip,
    concatenate_videoclips,
)


class VideoEngine:
    """Creates a cinematic video from shot images and scene narration."""

    IMAGE_DIR = Path("workspace/assets/images")
    AUDIO_DIR = Path("workspace/assets/audio")

    def generate(
        self,
        story,
        output_path: str,
    ) -> None:

        final_scene_clips = []

        for scene in story.scenes:

            print("=" * 70)
            print(f"Rendering Scene {scene.scene_number}")
            print("=" * 70)

            audio_path = (
                self.AUDIO_DIR
                / f"scene_{scene.scene_number:02d}.mp3"
            )

            if not audio_path.exists():
                raise FileNotFoundError(
                    f"Audio not found: {audio_path}"
                )

            scene_audio = AudioFileClip(str(audio_path))

            # Make sure shot planning exists.
            shots = getattr(scene, "shots", [])

            if not shots:
                raise ValueError(
                    f"Scene {scene.scene_number} has no shots."
                )

            shot_clips = []

            for shot in shots:

                image_path = (
                    self.IMAGE_DIR
                    / (
                        f"scene_{scene.scene_number:02d}"
                        f"_shot_{shot.shot_number:02d}.png"
                    )
                )

                if not image_path.exists():
                    raise FileNotFoundError(
                        f"Image not found: {image_path}"
                    )

                print(
                    f"Shot {shot.shot_number}: "
                    f"{shot.camera_angle} | "
                    f"{shot.camera_movement} | "
                    f"{shot.duration}s"
                )

                clip = (
                    ImageClip(str(image_path))
                    .with_duration(shot.duration)
                    .resized(
                        lambda t: (
                            1
                            + (
                                0.08
                                * t
                                / max(shot.duration, 0.01)
                            )
                        )
                    )
                )

                shot_clips.append(clip)

            # Combine all shots belonging to this scene.
            scene_video = concatenate_videoclips(
                shot_clips,
                method="compose",
            )

            # Attach the original scene narration.
            scene_video = scene_video.with_audio(
                scene_audio
            )

            final_scene_clips.append(scene_video)

        # Combine all scenes.
        final_video = concatenate_videoclips(
            final_scene_clips,
            method="compose",
        )

        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        print("\nRendering final video...\n")

        final_video.write_videofile(
            output_path,
            fps=30,
            codec="libx264",
            audio_codec="aac",
        )

        # Close resources.
        for clip in final_scene_clips:
            if clip.audio:
                clip.audio.close()

        final_video.close()

        print("\nVideo generated successfully.")
        print(output_path)