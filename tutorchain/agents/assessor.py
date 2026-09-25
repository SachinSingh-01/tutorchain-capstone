# tutorchain/agents/assessor.py
"""Assessor Agent.

Gemini mode uses rubric-based JSON evaluation.
Local mode uses a transparent text-similarity baseline.
"""

import difflib
import json

from tutorchain.llm_wrapper import LLM_PROVIDER, call_llm


def _baseline_score(student: str, reference: str) -> float:
    if not student:
        return 0.0
    return round(
        difflib.SequenceMatcher(None, student, reference).ratio() * 100,
        1,
    )


def grade_answer(student_answer: str, reference_answer: str) -> dict:
    """Grade a student answer against an actual reference answer."""

    student = student_answer.strip()
    reference = reference_answer.strip()

    if LLM_PROVIDER == "local":
        score = _baseline_score(student.lower(), reference.lower())
        return {
            "score": score,
            "feedback": (
                "Local baseline scoring uses text similarity. "
                "It is a prototype heuristic, not semantic correctness evaluation."
            ),
            "scoring_method": "text_similarity_baseline",
        }

    prompt = f"""
You are grading a beginner student's answer.

Reference answer:
{reference}

Student answer:
{student}

Use the reference as a rubric, but give credit for correct wording that differs
from the reference. Score from 0 to 100.

Return ONLY valid JSON:
{{
  "score": number,
  "feedback": "concise explanation"
}}
"""

    try:
        data = json.loads(call_llm(prompt))
        score = float(data["score"])
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100.")
        return {
            "score": round(score, 1),
            "feedback": str(data["feedback"]),
            "scoring_method": "gemini_rubric_evaluation",
        }
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        score = _baseline_score(student.lower(), reference.lower())
        return {
            "score": score,
            "feedback": (
                "LLM grading returned invalid structured output; "
                "a text-similarity baseline was used instead."
            ),
            "scoring_method": "text_similarity_fallback",
        }
