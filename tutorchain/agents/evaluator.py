# tutorchain/agents/evaluator.py
"""Session Evaluation Agent."""

import json

from tutorchain.llm_wrapper import LLM_PROVIDER, call_llm


def evaluate_session(
    topic: str,
    explanation: str,
    exercise: str,
    student_answer: str,
    score: float,
) -> dict:
    """Evaluate a session when an actual LLM provider is configured.

    Local mode explicitly reports that LLM evaluation is unavailable instead
    of returning fabricated scores.
    """

    if LLM_PROVIDER == "local":
        return {
            "available": False,
            "tutor_clarity": None,
            "exercise_quality": None,
            "understanding": None,
            "summary": "LLM-based session evaluation is unavailable in local mode.",
        }

    prompt = f"""
You are an AI evaluator using rubric-based scoring.

Evaluate this tutoring session:

Topic: {topic}

Tutor Explanation:
{explanation}

Exercise:
{exercise}

Student Answer:
{student_answer}

Baseline Assessor Score:
{score}

Return ONLY valid JSON:
{{
  "tutor_clarity": number,
  "exercise_quality": number,
  "understanding": number,
  "summary": "string"
}}
"""

    try:
        data = json.loads(call_llm(prompt))
        for key in ("tutor_clarity", "exercise_quality", "understanding", "summary"):
            if key not in data:
                raise ValueError(f"Missing evaluation field: {key}")
        data["available"] = True
        return data
    except (json.JSONDecodeError, TypeError, ValueError):
        return {
            "available": False,
            "tutor_clarity": None,
            "exercise_quality": None,
            "understanding": None,
            "summary": "LLM evaluation returned invalid structured output.",
        }
