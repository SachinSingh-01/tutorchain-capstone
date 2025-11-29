# tutorchain/agents/evaluator.py
"""
Evaluation Agent (LLM-as-a-Judge)
Yeh agent tutor + assessor ke output ko evaluate karta hai.
"""

from tutorchain.llm_wrapper import call_llm


def evaluate_session(topic: str, explanation: str, exercise: str, student_answer: str, score: float) -> dict:
    """
    LLM-as-a-Judge style evaluation.
    """

    prompt = f"""
You are an AI evaluator using rubric-based scoring.

Evaluate the following tutoring session:

Topic: {topic}

Tutor Explanation:
{explanation}

Exercise Given:
{exercise}

Student Answer:
{student_answer}

Assessor Score: {score}

Now provide:
1. Tutor Clarity Score (0–10)
2. Exercise Quality Score (0–10)
3. Student Understanding Score (0–10)
4. One-line summary evaluation
Return the result in this exact JSON format:

{{
  "tutor_clarity": number,
  "exercise_quality": number,
  "understanding": number,
  "summary": "string"
}}
"""

    raw = call_llm(prompt)

    # Parsing fallback
    try:
        import json
        data = json.loads(raw)
    except:
        data = {
            "tutor_clarity": 7,
            "exercise_quality": 7,
            "understanding": 7,
            "summary": raw
        }

    return data
