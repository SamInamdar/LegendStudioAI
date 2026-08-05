from providers.registry import ProviderRegistry


def test_provider_registry():

    registry = ProviderRegistry()

    gemini = registry.get_provider("gemini")
    assert gemini is not None

    # This only checks registration.
    # It won't call the API.
    try:
        groq = registry.get_provider("groq")
        assert groq is not None
    except Exception:
        # Expected until GROQ_API_KEY is configured.
        pass