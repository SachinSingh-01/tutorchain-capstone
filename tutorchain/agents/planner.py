# tutorchain/agents/planner.py
"""
Planner Agent (Structured JSON Version):
Yeh agent student ke profile + topic ke base par 
ek structured lesson plan banata hai.
"""

from tutorchain.llm_wrapper import call_llm
import json


def plan_lesson(student_profile: dict, topic: str, target_level: str = "beginner") -> dict:
    """
    Returns a structured JSON lesson plan:
    {
      "topic": "...",
      "objectives": [...],
      "explanation": "...",
      "practice_exercise": "..."
    }
    """

    profile_summary = f"Student Level: {student_profile.get('level', 'beginner')}, Goals: {student_profile.get('goals', [])}"

    prompt = f"""
You are an expert teacher.

Create a structured lesson plan in JSON format for the topic: "{topic}"
for a student with profile: {profile_summary}.

The JSON MUST have exactly these keys:

- topic: string
- objectives: list of strings
- explanation: string
- practice_exercise: string

Example format:
{{
  "topic": "for loops",
  "objectives": ["Understand iteration", "Use for loop"],
  "explanation": "Simple explanation here...",
  "practice_exercise": "Write a for loop that prints numbers 1 to 5."
}}

Return ONLY the JSON. No extra text.
"""

    llm_response = call_llm(prompt)

    # Safe parse: agar JSON parse nahi hota toh fallback
    try:
        plan = json.loads(llm_response)
    except:
        plan = {
            "topic": topic,
            "objectives": ["Understand basics"],
            "explanation": llm_response,     # fallback raw text
            "practice_exercise": "Write one example related to the topic."
        }

    return plan
