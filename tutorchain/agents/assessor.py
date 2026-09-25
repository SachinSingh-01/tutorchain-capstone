# tutorchain/agents/assessor.py
"""Assessor Agent.

The current implementation provides a transparent lexical baseline score.
It is not a semantic correctness model.
"""

import difflib

from tutorchain.llm_wrapper import LLM_PROVIDER, call_llm


def grade_answer(student_answer: str, reference_answer: str) -> dict:
    """Grade a student answer against an actual reference answer."""

    student = student_answer.strip().lower()
    reference = reference_answer.strip().lower()

    if not student:
        score = 0.0
    else:
        score = round(
            difflib.SequenceMatcher(None, student, reference).ratio() * 100,
            1,
        )

    feedback = (
        "Baseline similarity scoring is being used. "
        "A higher score means the response is more textually similar "
        "to the reference answer."
    )

    if LLM_PROVIDER != "local":
        feedback = call_llm(
            "Review the student's answer against the reference answer. "
            "Give concise feedback on what is correct and what should improve.\n\n"
            f"Student Answer: {student_answer}\n"
            f"Reference Answer: {reference_answer}\n"
        )

    return {
        "score": score,
        "feedback": feedback,
        "scoring_method": "text_similarity_baseline",
    }
