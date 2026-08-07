from services.voice import VoiceEngine


def main():

    engine = VoiceEngine()

    engine.generate(
        text="Hello Sameer, welcome to Legend Studio AI.",
        output_path="workspace/assets/audio/test.mp3",
    )

    print("Voice generated successfully!")


if __name__ == "__main__":
    main()