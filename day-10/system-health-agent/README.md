## AI Log Analysis Agent | Python, Ollama, Agentic Framework
### ⭐ STAR Method
#### 🟡 Situation (IDEA)

During earlier days of the bootcamp (Day 04–Day 06), I built a manual Log Analyzer using:
- File handling
- OOP structure
- CLI-based execution

By Day 09, I had even exposed automation via a FastAPI service.

However, traditional log parsing relied on rigid string matching and predefined logic.
I wanted to explore how AI Agents can augment DevOps troubleshooting by analyzing logs more intelligently while maintaining control and guardrails.

#### 🔵 Task (Theme)

Build an AI-powered Log Analysis Agent that:

Reads a real .log file

Detects and counts INFO / WARNING / ERROR occurrences

Identifies repeated production issues

Operates with strict DevOps guardrails (no hallucination, no production actions)

Uses an LLM locally (Ollama + Llama 3.2)

Maintains simplicity while demonstrating automation maturity

The goal was not to replace logic — but to elevate abstraction.

#### 🟢 Action (Actual Implementation)

Built a Python-based Log Analysis Agent using the Strands Agentic Framework

Integrated Ollama (Llama 3.2) running locally for secure inference

Designed a strict SYSTEM_PROMPT:

DevOps mindset focused, No hallucination rules, No production-level changes, Suggestion-based outputs only.

Enabled file tool access to read app.log dynamically

Processed repeated and duplicated production-style log entries to test robustness

Executed analysis using a single agent instruction:

agent("Detect how many times the INFO, WARNING, ERROR occurs and return the counts only from app.log file")

Project Structure:
system-health-agent/
├── app.log
├── logs_agent.py
└── requirements.txt

#### 🔴 Result

Reduced 100+ lines of manual parsing logic into an intelligent agent workflow

Demonstrated evolution from Script → OOP → CLI → API → AI Agent

Improved abstraction level of automation

Showcased practical AI integration in DevOps use cases

Built a foundation for AI-assisted troubleshooting systems