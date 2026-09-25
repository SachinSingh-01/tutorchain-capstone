# TutorChain: Multi-Agent Personalized AI Tutor

### Capstone Project — Google & Kaggle Agents Intensive (2025)

TutorChain is a **multi-agent AI tutoring prototype** designed around a personalized, mastery-oriented learning workflow. The project separates planning, tutoring, assessment, evaluation, and student-memory responsibilities into distinct modules.

> **Project status:** Capstone prototype / learning project. Gemini is supported as the real LLM provider; local mode remains available for offline development. The assessment and evaluation systems are still prototype components and should not be treated as validated educational measurement.

---

## Problem Statement

Technical learners can struggle with:

- Generic explanations that do not account for learning context
- Losing track of previous topics and weak areas
- Limited automated feedback
- Repeating the same material without a mastery loop
- Difficulty evaluating the quality of a tutoring session

TutorChain explores how a modular agent workflow can address these problems.

---

## What TutorChain Implements

The current codebase includes:

- Structured lesson planning
- Tutor-generated explanations and exercises
- Wikipedia-based external knowledge lookup
- Gemini-powered generation when configured
- Rubric-based Gemini answer assessment
- A transparent local text-similarity assessment baseline
- Persistent student memory using SQLite-backed storage
- A mastery-session loop
- Rich console logging
- Basic session metrics
- Structured session evaluation
- Explicit evaluation-unavailable handling instead of fabricated scores

The system is structured so that individual responsibilities can be developed and replaced independently.

---

## Architecture

Conceptually, the workflow is:

**Student Input → Planner → Tutor → Student Response → Assessor → Evaluator → Memory**

The mastery workflow can repeat the learning cycle until the configured target score is reached or the attempt limit is exhausted.

### Main Components

| Component | Responsibility |
|---|---|
| Planner | Produces a structured lesson plan and reference answer |
| Tutor | Generates explanations and practice material |
| Assessor | Scores the student's answer against an actual reference answer |
| Evaluator | Evaluates session-level tutoring signals when Gemini is enabled |
| Memory Agent | Persists student profile, history, topics, attempts, scores, and weak areas |
| Metrics | Tracks basic session-level measurements |
| Logging | Provides structured console/event logging |
| LLM Wrapper | Connects the application to the configured LLM provider |

---

## Repository Structure

The repository uses a Python package structure:

```text
tutorchain-capstone/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── tutorchain/
    ├── __init__.py
    ├── agents/
    │   ├── planner.py
    │   ├── tutor.py
    │   ├── assessor.py
    │   ├── evaluator.py
    │   └── memory_agent.py
    ├── llm_wrapper.py
    ├── logging_utils.py
    └── metrics.py
```

---

## Current Implementation Status

### LLM Integration

The default provider is **local**, which requires no API key and keeps the project runnable as a prototype.

For real model-generated tutoring, set:

```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your-key-here
GEMINI_MODEL=gemini-3.8-flash
```

The Gemini integration uses Google's GenAI Python SDK. citeturn0search1turn0search3

### Assessment

With Gemini enabled, the assessor uses a rubric-based JSON response and scores the student's answer against an actual reference answer.

In local mode, TutorChain uses a transparent text-similarity baseline. This is a prototype heuristic and **not semantic correctness evaluation**.

### Session Evaluation

With Gemini enabled, the evaluator requests structured session-level scores for tutor clarity, exercise quality, and student understanding.

If an LLM response is unavailable or invalid, TutorChain reports evaluation as unavailable rather than inserting hardcoded scores.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/SachinSingh-01/tutorchain-capstone.git
cd tutorchain-capstone
```

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\\Scripts\\activate
```

**macOS/Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini

Copy `.env.example` to `.env`.

For real LLM operation:

```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your-key-here
GEMINI_MODEL=gemini-3.8-flash
```

**Never commit the real API key to GitHub.**

---

## Running the Project

Start the interactive application:

```bash
python main.py
```

The application asks for a student identifier, learning topic, and session mode.

---

## Memory

TutorChain stores persistent student state using SQLite-backed storage, including:

- Student profile
- Session history
- Topics
- Attempts
- Last score
- Weak areas

This is a lightweight prototype memory mechanism rather than a production knowledge/memory system.

---

## Observability and Metrics

The project includes:

- Rich console logging
- Event-oriented logging helpers
- Session duration tracking
- Average score tracking
- Basic tutor-clarity tracking

These metrics are intended for prototype observability and experimentation.

---

## Limitations

TutorChain is a capstone prototype, not a production educational platform.

Known limitations include:

- OpenAI is not currently implemented as a provider.
- Local answer scoring is a text-similarity baseline.
- Gemini assessment depends on valid model output.
- Session evaluation is only available when a real LLM provider is configured.
- No automated test suite is currently included.

---

## Future Improvements

- Add an OpenAI provider
- Add automated unit/integration tests
- Improve semantic answer assessment
- Add code execution for programming lessons
- Expand tool integrations
- Add a web UI
- Deploy the agent workflow
- Add voice interaction

---

## Why This Project Matters

TutorChain was built as a capstone project to explore **multi-agent orchestration, tool integration, persistent learner state, LLM-based evaluation, and mastery-oriented workflows**.

It is a foundation for experimenting with personalized AI learning systems rather than a claim of production readiness.

---

## License

MIT License
