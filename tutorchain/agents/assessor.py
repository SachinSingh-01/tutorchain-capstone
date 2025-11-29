# tutorchain/agents/assessor.py
"""
Assessor Agent:
Yeh agent student ke jawab ko grade karta hai.
2 cheezen karta hai:
1. Similarity score nikalta hai (0–100)
2. LLM se feedback deta hai (placeholder abhi)
"""

from tutorchain.llm_wrapper import call_llm
import difflib


def grade_answer(student_answer: str, reference_answer: str) -> dict:
    """
    Returns:
    {
        'score': float,
        'feedback': str
    }
    """

    # ----------------------------
    # Step 1: Similarity score
    # ----------------------------
    ratio = difflib.SequenceMatcher(
        None,
        student_answer.strip().lower(),
        reference_answer.strip().lower()
    ).ratio()

    score = round(ratio * 100, 1)

    # ----------------------------
    # Step 2: LLM feedback
    # ----------------------------
    prompt = (
        "Grade the student's answer. "
        "Tell what is good and what should be improved.\n\n"
        f"Student Answer: {student_answer}\n"
        f"Reference Answer: {reference_answer}\n"
    )

    feedback = call_llm(prompt)

    return {
        "score": score,
        "feedback": feedback
    }
