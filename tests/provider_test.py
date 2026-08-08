import os
import time

from dotenv import load_dotenv
from google import genai
from openai import OpenAI
from groq import Groq
from elevenlabs.client import ElevenLabs


load_dotenv()


def test_gemini():
    print("=" * 60)
    print("Gemini Provider Test")
    print("=" * 60)

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("❌ GEMINI_API_KEY not found")
        return False

    try:
        client = genai.Client(api_key=api_key)

        start = time.perf_counter()

        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
            contents="Reply with exactly: Gemini connection successful."
        )

        elapsed = time.perf_counter() - start

        print("Status        : ✅ PASS")
        print(f"Response time : {elapsed:.2f}s")
        print(f"Response      : {response.text}")

        return True

    except Exception as exc:
        print("Status        : ❌ FAIL")
        print(f"Error         : {exc}")
        return False


def test_openai():
    print()
    print("=" * 60)
    print("OpenAI Provider Test")
    print("=" * 60)

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("❌ OPENAI_API_KEY not found")
        return False

    try:
        client = OpenAI(api_key=api_key)

        start = time.perf_counter()

        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-5-mini"),
            input="Reply with exactly: OpenAI connection successful."
        )

        elapsed = time.perf_counter() - start

        print("Status        : ✅ PASS")
        print(f"Response time : {elapsed:.2f}s")
        print(f"Response      : {response.output_text}")

        return True

    except Exception as exc:
        print("Status        : ❌ FAIL")
        print(f"Error         : {exc}")
        return False

def test_openrouter():
    print()
    print("=" * 60)
    print("OpenRouter Provider Test")
    print("=" * 60)

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        print("❌ OPENROUTER_API_KEY not found")
        return False

    try:
        import requests

        start = time.perf_counter()

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "openrouter/free",
                "messages": [
                    {
                        "role": "user",
                        "content": "Reply with exactly: OpenRouter connection successful."
                    }
                ],
            },
            timeout=60,
        )

        elapsed = time.perf_counter() - start

        if response.status_code == 200:
            data = response.json()
            message = data["choices"][0]["message"]["content"]

            print("Status        : ✅ PASS")
            print(f"Response time : {elapsed:.2f}s")
            print(f"Response      : {message}")

            return True

        print("Status        : ❌ FAIL")
        print(f"HTTP status   : {response.status_code}")
        print(f"Error         : {response.text}")

        return False

    except Exception as exc:
        print("Status        : ❌ FAIL")
        print(f"Error         : {exc}")
        return False

def test_groq():
    print()
    print("=" * 60)
    print("Groq Provider Test")
    print("=" * 60)

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        print("❌ GROQ_API_KEY not found")
        return False

    try:
        client = Groq(api_key=api_key)

        start = time.perf_counter()

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": "Reply with exactly: Groq connection successful."
                }
            ],
            temperature=0,
        )

        elapsed = time.perf_counter() - start

        print("Status        : ✅ PASS")
        print(f"Response time : {elapsed:.2f}s")
        print(f"Response      : {response.choices[0].message.content}")

        return True

    except Exception as exc:
        print("Status        : ❌ FAIL")
        print(f"Error         : {exc}")
        return False

def test_elevenlabs():
    print()
    print("=" * 60)
    print("ElevenLabs Provider Test")
    print("=" * 60)

    api_key = os.getenv("ELEVENLABS_API_KEY")

    if not api_key:
        print("❌ ELEVENLABS_API_KEY not found")
        return False

    try:
        client = ElevenLabs(api_key=api_key)

        start = time.perf_counter()

        audio = client.text_to_speech.convert(
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            text="LegendStudioAI voice connection successful."
        )

        # Consume the returned audio stream so the request is actually completed.
        audio_bytes = b"".join(audio)

        elapsed = time.perf_counter() - start

        print("Status        : ✅ PASS")
        print(f"Response time : {elapsed:.2f}s")
        print(f"Audio size    : {len(audio_bytes):,} bytes")

        return True

    except Exception as exc:
        print("Status        : ❌ FAIL")
        print(f"Error         : {exc}")
        return False

      
if __name__ == "__main__":

    gemini_ok = test_gemini()
    openai_ok = test_openai()
    openrouter_ok = test_openrouter()
    groq_ok = test_groq()
    elevenlabs_ok = test_elevenlabs()

    print()
    print("=" * 60)
    print("Provider Test Summary")
    print("=" * 60)

    print(f"Gemini       : {'✅ PASS' if gemini_ok else '❌ FAIL'}")
    print(f"OpenAI       : {'✅ PASS' if openai_ok else '❌ FAIL'}")
    print(f"OpenRouter   : {'✅ PASS' if openrouter_ok else '❌ FAIL'}")
    print(f"Groq         : {'✅ PASS' if groq_ok else '❌ FAIL'}")
    print(f"ElevenLabs  : {'✅ PASS' if elevenlabs_ok else '❌ FAIL'}")

    print("=" * 60)