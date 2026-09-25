# tutorchain/agents/tutor.py
"""Tutor Agent.

Combines a lesson plan with optional external knowledge and an LLM provider.
Local mode remains runnable without an API key.
"""

import json

from tutorchain.llm_wrapper import LLM_PROVIDER, call_llm
from tutorchain.tools.knowledge_tool import lookup_topic


def teach(plan: dict) -> dict:
    """Generate an explanation, exercise, and reference answer."""

    external_info = lookup_topic(plan["topic"])

    if LLM_PROVIDER == "local":
        explanation = plan["explanation"]
        if external_info:
            explanation = f"{explanation}\n\nAdditional reference information:\n{external_info}"

        return {
            "explanation": explanation,
            "exercise": plan["practice_exercise"],
            "reference_answer": plan["reference_answer"],
        }

    explanation_prompt = f"""
You are an expert teacher.

Teach the topic below using:
1. Simple language
2. Step-by-step approach
3. A real-life analogy
4. One coding or academic example
5. Bullet points

Topic: {plan['topic']}
Objectives: {plan['objectives']}
External Info: {external_info}
Base Lesson Info: {plan['explanation']}

Produce a beginner-friendly explanation.
"""

    explanation = call_llm(explanation_prompt)

    exercise_prompt = f"""
Create ONE high-quality beginner practice question for: {plan['topic']}.

Return ONLY valid JSON:
{{
  "exercise": "question",
  "reference_answer": "correct concise answer"
}}

The reference_answer must answer the exercise.
"""

    try:
        exercise_data = json.loads(call_llm(exercise_prompt))
        exercise = exercise_data["exercise"]
        reference_answer = exercise_data["reference_answer"]
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        exercise = plan["practice_exercise"]
        reference_answer = plan["reference_answer"]

    return {
        "explanation": explanation,
        "exercise": exercise,
        "reference_answer": reference_answer,
    }
