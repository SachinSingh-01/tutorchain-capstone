# TutorChain: Multi-Agent Personalized AI Tutor  
### Capstone Project – Google & Kaggle Agents Intensive (2025)

TutorChain is a multi-agent AI tutoring system designed to deliver personalized, adaptive, and mastery-based learning. It uses a structured pipeline of agents—planner, tutor, assessor, evaluator, and memory agent—to create a complete learning loop. The system integrates external tools, long-term memory, observability, and AI-based evaluation.

This repository contains the full implementation used for the Capstone Project submission.

---

## 1. Problem Statement

Students learning technical topics face challenges such as:

- Lack of personalized learning  
- No memory of past weak areas  
- No automated feedback or scoring  
- No evaluation of tutoring quality  
- Static explanations that do not adapt  

These gaps slow down improvement and reduce mastery.

---

## 2. Solution: TutorChain

TutorChain provides a complete AI-powered tutoring workflow:

- Generates structured lesson plans  
- Uses external knowledge (Wikipedia)  
- Teaches with step-by-step explanations  
- Generates practice questions  
- Scores answers  
- Evaluates tutoring quality using LLM-as-a-Judge  
- Stores long-term learning data  
- Repeats teaching until mastery is reached (Mastery Mode)  
- Logs all events for observability  

The system behaves like a real tutor that remembers, evaluates, and adapts over time.

---

## 3. Features Included (Capstone Requirements)

### Multi-Agent Architecture
- Lesson Planner Agent  
- Tutor Agent  
- Assessor Agent  
- Evaluator Agent  
- Memory Agent  
- Mastery Learning Orchestrator  

### Tools
- Wikipedia search tool  
- LLM wrapper (Gemini-ready placeholder)  

### Memory & State
- Student profile  
- Session history  
- Weak areas  
- Attempts tracking  
- Last score  

### Observability
- Rich logs  
- Event tables  
- Session metrics  

### Agent Evaluation
- LLM-as-a-Judge scoring  
- Structured JSON evaluation  

---

## 4. System Architecture

Student Input → Planner Agent → Tutor Agent → Student Response
↓ ↓
Memory Agent ← Assessor Agent ← Evaluator Agent (LLM-a-a-Judge)
↓
Mastery Mode Loop


---

## 5. Project Structure

tutorchain/
│── main.py
│── llm_wrapper.py
│── planner.py
│── tutor.py
│── assessor.py
│── evaluator.py
│── logging_utils.py
│── metrics.py
│── knowledge_tool.py
│── memory_agent.py
│── requirements.txt


---

## 6. Installation

### Step 1: Clone the repo
git clone https://github.com/your-username/tutorchain.git
cd tutorchain


### Step 2: Create virtual environment
python -m venv .venv
.venv\Scripts\activate # Windows
source .venv/bin/activate # Mac/Linux


### Step 3: Install dependencies
pip install -r requirements.txt


### Step 4 (Optional): Add Gemini API Key
Create a `.env` file:
GEMINI_API_KEY=your-key-here


---

## 7. How to Run

### Normal tutoring session:
python main.py


### Mastery Learning Mode (notebook version):
mastery_session("student1", "while loops in C", target_score=80)


---

## 8. Component Overview

### Lesson Planner Agent  
Creates structured JSON-based lesson plans.

### Tutor Agent  
Uses:
- lesson plan  
- Wikipedia knowledge  
- LLM explanation  

### Assessor Agent  
Scores answers and provides feedback.

### Evaluator Agent  
Grades the full session using JSON scoring.

### Memory Agent  
Stores:
- topics learned  
- weak areas  
- attempts  
- last score  

### Metrics  
Tracks:
- average score  
- average clarity  
- session duration  

---

## 9. Future Enhancements

- Replace placeholder LLM wrapper with Gemini models  
- Add MCP tool support  
- Add code execution for programming lessons  
- Deploy with Vertex AI Agent Engine  
- Add UI (Streamlit / Flutter)  
- Add voice input + speech output  

---

## 10. Conclusion

TutorChain demonstrates the core principles taught in the Agents Intensive workshop:

- Multi-agent system design  
- Tool integration  
- LLM-based evaluation  
- Long-term memory management  
- Observability and metrics  
- Mastery-based learning  

It serves as a strong foundation for personalized AI learning systems.

---

## 11. License  
MIT License
