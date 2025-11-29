# tutorchain/agents/memory_agent.py
"""
MemoryAgent (Upgraded Version)
Long-term student memory:
- profile
- history
- last_score
- topics_learned
- weak_areas
- attempt_count
"""

from sqlitedict import SqliteDict
from typing import Dict, Any, List

DB_PATH = "memory.db"


class MemoryAgent:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.store = SqliteDict(self.db_path, autocommit=True)

    # -------------------------------
    # Profile Management
    # -------------------------------
    def get_profile(self, student_id: str) -> Dict[str, Any]:
        return self.store.get(f"profile:{student_id}", {})

    def save_profile(self, student_id: str, profile: Dict[str, Any]):
        self.store[f"profile:{student_id}"] = profile

    # -------------------------------
    # History Append
    # -------------------------------
    def append_history(self, student_id: str, event: Dict[str, Any]):
        key = f"history:{student_id}"
        history = self.store.get(key, [])
        history.append(event)
        self.store[key] = history

    def get_history(self, student_id: str):
        return self.store.get(f"history:{student_id}", [])

    # -------------------------------
    # NEW: Track topics learned
    # -------------------------------
    def add_topic(self, student_id: str, topic: str):
        key = f"topics:{student_id}"
        topics = self.store.get(key, [])
        if topic not in topics:
            topics.append(topic)
        self.store[key] = topics

    def get_topics(self, student_id: str) -> List[str]:
        return self.store.get(f"topics:{student_id}", [])

    # -------------------------------
    # NEW: Track scores
    # -------------------------------
    def update_last_score(self, student_id: str, score: float):
        self.store[f"last_score:{student_id}"] = score

    def get_last_score(self, student_id: str):
        return self.store.get(f"last_score:{student_id}", None)

    # -------------------------------
    # NEW: Track weak areas
    # -------------------------------
    def update_weak_areas(self, student_id: str, topic: str, score: float):
        key = f"weak:{student_id}"
        weak = self.store.get(key, [])

        # If score < 60 → consider weak
        if score < 60 and topic not in weak:
            weak.append(topic)

        self.store[key] = weak

    def get_weak_areas(self, student_id: str) -> List[str]:
        return self.store.get(f"weak:{student_id}", [])

    # -------------------------------
    # NEW: Attempt Counter
    # -------------------------------
    def increment_attempts(self, student_id: str):
        key = f"attempts:{student_id}"
        count = self.store.get(key, 0)
        count += 1
        self.store[key] = count
        return count

    def get_attempts(self, student_id: str):
        return self.store.get(f"attempts:{student_id}", 0)
   
