# tutorchain/llm_wrapper.py
"""Provider-agnostic LLM wrapper.

Local mode is deterministic and requires no API key.
Gemini mode uses Google's current GenAI Python SDK.
"""

import os

from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "local").strip().lower()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")


def call_llm(prompt: str, system: str = None, max_tokens: int = 256) -> str:
    """Return generated text from the configured provider."""

    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    if LLM_PROVIDER == "local":
        return (
            "Local mode is active. Configure LLM_PROVIDER=gemini and "
            "GEMINI_API_KEY to enable model-generated responses."
        )

    if LLM_PROVIDER == "gemini":
        from google import genai
        from google.genai import types

        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is required when LLM_PROVIDER=gemini.")

        client = genai.Client(api_key=api_key)
        config_kwargs = {"max_output_tokens": max_tokens}

        if system:
            config_kwargs["system_instruction"] = system

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(**config_kwargs),
        )

        if not response.text:
            raise RuntimeError("Gemini returned an empty response.")

        return response.text.strip()

    if LLM_PROVIDER == "openai":
        raise NotImplementedError(
            "OpenAI provider is not implemented yet. "
            "Use LLM_PROVIDER=gemini or local."
        )

    raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")
