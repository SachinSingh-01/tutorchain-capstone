# tutorchain/tools/knowledge_tool.py
"""
Knowledge Lookup Tool (Custom Tool)
Fetches topic explanations from Wikipedia.
"""

import wikipedia

def lookup_topic(topic: str) -> str:
    try:
        summary = wikipedia.summary(topic, sentences=3, auto_suggest=True, redirect=True)
        return summary
    except Exception:
        return "Sorry, no reliable external information found."
