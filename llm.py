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

# --------------------------------------------------
# Discovery, Compliance, Schema Synthesis
# --------------------------------------------------
# Responsible for:
# - Discovery
# - Compliance
# - Canonical Schema
#
# Strong reasoning
# Strong data modelling
# Lowest temperature
# --------------------------------------------------

architect_llm = LLM(
    model="ollama/qwen3:14b",
    base_url=OLLAMA_URL,
    temperature=0.0
)


# --------------------------------------------------
# Integration Analysis
# --------------------------------------------------
# Responsible for:
# - Flow Analysis
# - Integration Analysis
#
# Extract structure and relationships
# --------------------------------------------------

worker_llm = LLM(
    model="ollama/qwen3:14b",
    base_url=OLLAMA_URL,
    temperature=0.0
)


# --------------------------------------------------
# SharePoint Schema Generation
# Parser Generation
# Code Generation
#
# Strong preference for structured output
# --------------------------------------------------

coder_llm = LLM(
    model="ollama/qwen3-coder:30b",
    base_url=OLLAMA_URL,
    temperature=0.0
)


# --------------------------------------------------
# Validation / Review
# --------------------------------------------------

reviewer_llm = LLM(
    model="ollama/deepseek-r1:14b",
    base_url=OLLAMA_URL,
    temperature=0.1
)