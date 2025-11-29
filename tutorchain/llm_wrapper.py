# tutorchain/llm_wrapper.py
"""
Simple LLM wrapper with placeholder mode for local testing.
Replace the `call_llm` implementation with Gemini/ADK/OpenAI calls when ready.
Uses environment variable LLM_PROVIDER to switch mode.
"""
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Which provider to use: local | openai | gemini
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "local")

def call_llm(prompt: str, system: str = None, max_tokens: int = 256) -> str:
    """
    Wrapper to call LLM. For now 'local' provider returns a simple response.
    Actual LLM calls will be added later when you enable Gemini/OpenAI.
    """
    
    # ----------------------------------------------------
    # 1. Local mode (default): no internet, no API needed
    # ----------------------------------------------------
    if LLM_PROVIDER == "local":
        # Easy placeholder output for testing
        return f"[LLM-PLACEHOLDER] Prompt received: {prompt[:120]}..."
    
    # ----------------------------------------------------
    # 2. OpenAI provider (if you want to use it later)
    # ----------------------------------------------------
    elif LLM_PROVIDER == "openai":
        raise NotImplementedError("OpenAI provider not configured yet. Will add when you confirm.")
    
    # ----------------------------------------------------
    # 3. Gemini provider (ADK or Gemini API)
    # ----------------------------------------------------
    elif LLM_PROVIDER == "gemini":
        raise NotImplementedError("Gemini provider not configured yet. Will add when you confirm.")
    
    # ----------------------------------------------------
    # 4. Error case
    # ----------------------------------------------------
    else:
        raise ValueError(f"Unknown LLM_PROVIDER: {LLM_PROVIDER}")
