"""
Manual test for Gemini Provider.

Run this file after adding a valid Gemini API key.
"""

from providers.ai.gemini_provider import GeminiProvider


def main() -> None:
    """Run a manual Gemini test."""

    provider = GeminiProvider()

    prompt = """
Write a motivational YouTube Shorts script.

Topic: Never Give Up

Requirements:
- Maximum 120 words
- Powerful hook
- Emotional ending
"""

    print("\nGenerating response...\n")

    result = provider.generate_text(prompt)

    print("=" * 60)
    print(result)
    print("=" * 60)


if __name__ == "__main__":
    main()