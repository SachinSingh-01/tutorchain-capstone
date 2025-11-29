# tutorchain/metrics.py
"""
Simple Metrics System
Tracks:
- session duration
- total attempts
- average score
- tutor clarity average
"""

import time
from statistics import mean


class Metrics:
    def __init__(self):
        self.start_time = None
        self.scores = []
        self.tutor_clarity_scores = []
    
    def start(self):
        self.start_time = time.time()
    
    def end(self):
        if self.start_time is None:
            return 0
        return round(time.time() - self.start_time, 2)
    
    def add_score(self, score: float):
        self.scores.append(score)
    
    def get_avg_score(self):
        return round(mean(self.scores), 2) if self.scores else 0
    
    def add_tutor_clarity(self, score: float):
        self.tutor_clarity_scores.append(score)
    
    def get_avg_clarity(self):
        return round(mean(self.tutor_clarity_scores), 2) if self.tutor_clarity_scores else 0
