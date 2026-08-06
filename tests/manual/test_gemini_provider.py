from providers.ai.gemini_provider import GeminiProvider
from providers.models import AIRequest


def main():

    provider = GeminiProvider()

    request = AIRequest(
        system_prompt="You are a helpful assistant.",
        user_prompt="Say hello in one sentence.",
    )

    response = provider.generate(request)

    print("=" * 80)

    print(response.provider)

    print(response.model)

    print()

    print(response.text)


if __name__ == "__main__":
    main()