# TutorChain: Multi-Agent Personalized AI Tutor

### Capstone Project — Google & Kaggle Agents Intensive (2025)

TutorChain is a **multi-agent AI tutoring prototype** designed around a personalized, mastery-oriented learning workflow. The project separates planning, tutoring, assessment, evaluation, and student-memory responsibilities into distinct modules.

> **Project status:** Capstone prototype / learning project. The repository demonstrates the architecture and orchestration of an AI tutoring system, while some LLM integrations and evaluation components remain placeholders or prototype implementations.

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

- A lesson-planning module
- A tutor module
- An assessment module
- An evaluation module
- Persistent student memory using SQLite-backed storage
- A mastery-session loop
- Rich console logging
- Basic session metrics
- A configurable LLM wrapper interface
- A Wikipedia-based knowledge lookup integration

The system is structured so that individual responsibilities can be developed and replaced independently.

---

## Architecture

Conceptually, the workflow is:

**Student Input → Planner → Tutor → Student Response → Assessor → Evaluator → Memory**

The mastery workflow can repeat the learning cycle until the configured target score is reached or the attempt limit is exhausted.

### Main Components

| Component | Responsibility |
|---|---|
| Planner | Produces a structured lesson plan |
| Tutor | Generates explanations and practice material |
| Assessor | Produces an answer score and feedback |
| Evaluator | Evaluates session-level tutoring signals |
| Memory Agent | Persists student profile, history, topics, attempts, scores, and weak areas |
| Metrics | Tracks basic session-level measurements |
| Logging | Provides structured console/event logging |
| LLM Wrapper | Provides the interface used by the agent modules to call an LLM |

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

The LLM wrapper currently defaults to a **local placeholder provider**. OpenAI and Gemini provider branches are defined as extension points but are not implemented in the current codebase.

Therefore, the repository should be viewed as an **agent-system prototype**, not as a production-ready Gemini/OpenAI application.

### Assessment

The current assessor uses normalized string similarity as a simple prototype scoring mechanism. It is **not equivalent to semantic correctness evaluation**.

### Session Evaluation

The evaluator is designed around structured JSON scoring, but fallback behavior exists when an LLM response cannot be parsed. These values should be treated as prototype fallback behavior rather than validated educational evaluation metrics.

These limitations are intentionally documented so the project description matches the current implementation.

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

### 4. Environment configuration

Copy `.env.example` to `.env` if you want to configure environment variables.

**Do not commit real API keys or secrets to the repository.**

---

## Running the Project

Start the interactive application with:

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

## Future Improvements

Potential next steps include:

- Implementing a real Gemini/OpenAI provider in the LLM wrapper
- Replacing string-similarity assessment with semantic/rubric-based answer evaluation
- Improving reference-answer handling
- Adding reliable automated tests
- Adding code execution for programming lessons
- Expanding tool integrations
- Adding a web UI
- Deploying the agent workflow
- Adding voice interaction

---

## Why This Project Matters

TutorChain was built as a capstone project to explore **multi-agent orchestration, tool integration, persistent learner state, evaluation, and mastery-oriented workflows**.

It is a foundation for experimenting with personalized AI learning systems rather than a claim of production readiness.

---

## License

MIT License
