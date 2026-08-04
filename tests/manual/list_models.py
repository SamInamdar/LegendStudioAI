"""
List all available Gemini models.
"""

from google import genai
from config.settings import Settings


def main() -> None:
    settings = Settings()

    client = genai.Client(api_key=settings.gemini_api_key)

    print("\nAvailable Models:\n")
    print("-" * 80)

    for model in client.models.list():
        print(model.name)


if __name__ == "__main__":
    main()