"""
Manual test for Gemini Provider.
"""

from providers.ai.gemini_provider import GeminiProvider


def main() -> None:
    """Manual test."""

    provider = GeminiProvider()

    prompt = "Write a motivational story in exactly 100 words."

    print("=" * 60)
    print("Testing Gemini Provider")
    print("=" * 60)

    try:
        result = provider.generate_text(prompt)

        print("\n✅ SUCCESS\n")
        print(result)

    except Exception as ex:
        print("\n❌ FAILED\n")
        print(type(ex).__name__)
        print(ex)


if __name__ == "__main__":
    main()