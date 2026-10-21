# llm.py

from crewai import LLM


OLLAMA_URL = "http://localhost:11434"


# Discovery, Architecture, Governance and Standards
# Need strong reasoning and information synthesis

# architect_llm = LLM(
#     model="ollama/qwen3:32b",
#     base_url=OLLAMA_URL,
#     temperature=0.1
# )


# Implementation-focused tasks
# Prefer speed and consistency

# worker_llm = LLM(
#     model="ollama/qwen3:14b",
#     base_url=OLLAMA_URL,
#     temperature=0.0
# )

# coder_llm = LLM(
#     model="ollama/qwen3-coder:30b",
#     base_url=OLLAMA_URL,
#     temperature=0.0
# )

# Aggressive reviewer / critic

# reviewer_llm = LLM(
#     model="ollama/deepseek-r1:32b",
#     base_url=OLLAMA_URL,
#     temperature=0.2
# )

architect_llm = LLM(
    model="ollama/qwen3:14b",
    base_url=OLLAMA_URL,
    temperature=0.0
)

worker_llm = LLM(
    model="ollama/qwen3:14b",
    base_url=OLLAMA_URL,
    temperature=0.0
)

coder_llm = LLM(
    model="ollama/qwen2.5-coder:14b",
    base_url=OLLAMA_URL,
    temperature=0.0
)

reviewer_llm = LLM(
    model="ollama/deepseek-r1:14b",
    base_url=OLLAMA_URL,
    temperature=0.1
)