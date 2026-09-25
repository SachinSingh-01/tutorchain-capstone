# main.py
"""TutorChain application entry point."""

from tutorchain.agents.memory_agent import MemoryAgent
from tutorchain.agents.planner import plan_lesson
from tutorchain.agents.tutor import teach
from tutorchain.agents.assessor import grade_answer
from tutorchain.agents.evaluator import evaluate_session
from tutorchain.logging_utils import log_info, log_event, log_error
from tutorchain.metrics import Metrics


def demo_session(student_id: str, topic: str):
    mem = MemoryAgent()
    metrics = Metrics()
    metrics.start()

    print("\n==========================")
    print("     TutorChain Session")
    print("==========================\n")

    try:
        profile = mem.get_profile(student_id) or {
            "name": student_id,
            "level": "beginner",
            "goals": ["learn basics"],
        }
        mem.save_profile(student_id, profile)
        log_info(f"Loaded profile for {student_id}")
    except Exception as e:
        log_error(f"Profile load error: {e}")
        return

    print("👤 Student Profile:", profile)

    try:
        plan = plan_lesson(profile, topic)
        log_event("LessonPlanGenerated", {"topic": topic})
    except Exception as e:
        log_error(f"Planner error: {e}")
        return

    print("\n📚 Lesson Plan:")
    print("Topic:", plan["topic"])
    print("Objectives:", plan["objectives"])
    print("\nExplanation (base):", plan["explanation"])
    print("\nPractice (base):", plan["practice_exercise"])

    try:
        tutor_resp = teach(plan)
        log_event("TutorExplanation", {"topic": topic})
    except Exception as e:
        log_error(f"Tutor error: {e}")
        return

    print("\n🧑‍🏫 Final Explanation:\n", tutor_resp["explanation"])
    print("\n📝 Practice Question:\n", tutor_resp["exercise"])

    student_answer = input("\n✏ Enter your answer: ").strip()
    reference_answer = tutor_resp["reference_answer"]

    try:
        assessment = grade_answer(student_answer, reference_answer)
        metrics.add_score(assessment["score"])
        log_event(
            "AssessmentCompleted",
            {
                "score": assessment["score"],
                "method": assessment["scoring_method"],
            },
        )
    except Exception as e:
        log_error(f"Assessment error: {e}")
        return

    print("\n📊 Assessment Result:")
    print("Score:", assessment["score"])
    print("Scoring method:", assessment["scoring_method"])
    print("Feedback:", assessment["feedback"])

    try:
        eval_data = evaluate_session(
            topic,
            tutor_resp["explanation"],
            tutor_resp["exercise"],
            student_answer,
            assessment["score"],
        )
        clarity = eval_data.get("tutor_clarity")
        if isinstance(clarity, (int, float)):
            metrics.add_tutor_clarity(clarity)
        log_event("EvaluationCompleted", eval_data)
    except Exception as e:
        eval_data = {
            "available": False,
            "summary": f"Evaluation failed: {e}",
        }
        log_error(f"Evaluation error: {e}")

    print("\n🤖 Session Evaluation:")
    print(eval_data)

    try:
        mem.append_history(
            student_id,
            {
                "topic": topic,
                "answer": student_answer,
                "assessment": assessment,
                "evaluation": eval_data,
            },
        )
        mem.add_topic(student_id, topic)
        mem.update_last_score(student_id, assessment["score"])
        mem.update_weak_areas(student_id, topic, assessment["score"])
        attempts = mem.increment_attempts(student_id)
        log_event("MemoryUpdated", {"attempts": attempts})
    except Exception as e:
        log_error(f"Memory error: {e}")
        return

    duration = metrics.end()

    print("\n📈 Performance Summary")
    print("Topics Learned:", mem.get_topics(student_id))
    print("Weak Areas:", mem.get_weak_areas(student_id))
    print("Last Score:", mem.get_last_score(student_id))
    print("Attempts:", mem.get_attempts(student_id))
    print("Session Time:", duration, "seconds")
    print("Avg Score:", metrics.get_avg_score())
    print("Avg Tutor Clarity:", metrics.get_avg_clarity())
    print("\n🎉 Session Finished")


def mastery_session(student_id: str, topic: str, target_score: int = 80):
    print("\n🔁 Mastery Mode Activated")
    attempt = 1

    while True:
        print(f"\n==== Attempt #{attempt} ====")
        demo_session(student_id, topic)

        mem = MemoryAgent()
        score = mem.get_last_score(student_id)

        if score is not None and score >= target_score:
            print(f"\n🏆 Mastered! Final Score = {score}")
            break

        if attempt >= 5:
            print("\n⚠ Maximum attempts reached. Suggest reviewing easier material.")
            break

        print(f"\nScore {score} < {target_score}. Retrying...\n")
        attempt += 1


if __name__ == "__main__":
    print("===================================")
    print("  Welcome to TutorChain AI Tutor")
    print("===================================\n")

    sid = input("Enter Student ID: ").strip() or "student1"
    topic = input("Enter Topic: ").strip() or "for loops in python"

    print("\nModes Available:")
    print("1️⃣ Normal Single Session")
    print("2️⃣ Mastery Auto-Learning Mode")

    mode = input("Choose mode (1 or 2): ").strip()

    if mode == "2":
        mastery_session(sid, topic)
    else:
        demo_session(sid, topic)
