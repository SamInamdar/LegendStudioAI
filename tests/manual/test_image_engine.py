from services.image import ImageEngine


def main():

    engine = ImageEngine()

    prompt = """
A poor boy studying under a street light,
cinematic,
golden hour,
ultra realistic,
8k,
highly detailed,
emotional,
Hollywood lighting
"""

    output = "workspace/assets/images/test.png"

    engine.generate(
        prompt=prompt,
        output_path=output,
    )

    print("=" * 80)
    print("Image generated successfully!")
    print(output)
    print("=" * 80)


if __name__ == "__main__":
    main()