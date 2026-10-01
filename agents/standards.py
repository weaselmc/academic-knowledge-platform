# agents/standards.py

from crewai import Agent
from llm import architect_llm

standards_agent = Agent(
    role="RTO Compliance Domain Analyst",

    goal="""
    Identify every information element
    required across:

    - Standards 2025
    - TAC guidance
    - TIWA policy
    - Training Package requirements
    """,

    backstory="""
    Expert in:

    - Outcome Standards
    - Compliance Standards
    - Credential Policy
    - TAC guidance
    - TIWA requirements

    Extract information requirements.
    Do not audit documents.
    Build information models.
    """,

    llm=architect_llm,
    verbose=True
)