# tutorchain/agents/tutor.py
"""
Tutor Agent (Enhanced Version)
Uses:
- Structured JSON lesson plan
- Knowledge lookup tool (Wikipedia)
- LLM-based explanation + custom exercise
"""

from tutorchain.llm_wrapper import call_llm
from tutorchain.tools.knowledge_tool import lookup_topic


def teach(plan: dict) -> dict:
    """
    Uses structured lesson plan + external tool to create better explanations.
    plan example:
    {
      'topic': 'loops',
      'objectives': [...],
      'explanation': '...',
      'practice_exercise': '...'
    }
    """

    # Fetch external verified info (wikipedia)
    external_info = lookup_topic(plan["topic"])

    # ---------- MAIN EXPLANATION ----------
    prompt_exp = f"""
You are an expert teacher.

Teach the topic below using:
1. Simple language
2. Step-by-step approach
3. Real-life analogy
4. 1 coding or academic example
5. Bullet points

Topic: {plan['topic']}
Objectives: {plan['objectives']}
External Info (use if helpful): {external_info}
Base Lesson Info: {plan['explanation']}

Now produce the BEST educational explanation for a beginner.
"""

    explanation = call_llm(prompt_exp)

    # ---------- EXERCISE GENERATION ----------
    prompt_ex = f"""
Create ONE high-quality practice question for topic: {plan['topic']}

Rules:
- Must match beginner level
- Should relate to skills in objectives
- No answer included in the question
- Keep it short and clear
"""

    exercise = call_llm(prompt_ex)

    return {
        "explanation": explanation,
        "exercise": exercise
    }
