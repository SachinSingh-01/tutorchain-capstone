# tutorchain/agents/planner.py
"""Lesson Planner Agent."""

import json

from tutorchain.llm_wrapper import LLM_PROVIDER, call_llm


def _fallback_plan(topic: str) -> dict:
    """Return a usable local lesson plan when no LLM provider is configured."""
    return {
        "topic": topic,
        "objectives": [
            f"Understand the core concept of {topic}",
            f"Explain the main idea of {topic} in your own words",
            f"Apply {topic} in a simple example",
        ],
        "explanation": (
            f"{topic} is the subject of this lesson. Start by identifying its "
            "core definition, understand how it works, and then apply it in a "
            "small example."
        ),
        "practice_exercise": (
            f"Explain the main concept of {topic} in your own words and give "
            "one simple example."
        ),
        "reference_answer": (
            f"A strong answer should define {topic} clearly, explain its main "
            "idea, and provide a relevant example."
        ),
    }


def plan_lesson(student_profile: dict, topic: str, target_level: str = "beginner") -> dict:
    """Create a structured lesson plan with a reference answer for assessment."""

    profile_summary = (
        f"Student Level: {student_profile.get('level', target_level)}, "
        f"Goals: {student_profile.get('goals', [])}"
    )

    prompt = f"""
You are an expert teacher.

Create a structured lesson plan in JSON format for the topic: "{topic}"
for a student with profile: {profile_summary}.

The JSON MUST have exactly these keys:
- topic: string
- objectives: list of strings
- explanation: string
- practice_exercise: string
- reference_answer: string

The reference_answer must answer the practice_exercise, not repeat the question.

Return ONLY valid JSON.
"""

    if LLM_PROVIDER == "local":
        return _fallback_plan(topic)

    try:
        plan = json.loads(call_llm(prompt))
        required = {
            "topic",
            "objectives",
            "explanation",
            "practice_exercise",
            "reference_answer",
        }
        if not required.issubset(plan):
            return _fallback_plan(topic)
        return plan
    except (json.JSONDecodeError, TypeError, ValueError):
        return _fallback_plan(topic)
