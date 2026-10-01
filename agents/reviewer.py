# agents/reviewer.py

from crewai import Agent
from llm import reviewer_llm

reviewer = Agent(
    role="Technical Reviewer",

    goal="""
    Identify weaknesses in
    architecture and implementation.
    """,

    backstory="""
    Expert reviewer.

    Challenge:
    - assumptions
    - architecture
    - security
    - maintainability

    Seek flaws.
    """,

    llm=reviewer_llm,
    verbose=True
)
