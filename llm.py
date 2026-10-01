# llm.py

from crewai import LLM

architect_llm = LLM(
    model="ollama/qwen3:14b",
    base_url="http://localhost:11434"
)

worker_llm = LLM(
    model="ollama/qwen3:14b",
    base_url="http://localhost:11434"
)

reviewer_llm = LLM(
    model="ollama/deepseek-r1:14b",
    base_url="http://localhost:11434"
)