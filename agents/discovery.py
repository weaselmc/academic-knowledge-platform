# agents/discovery.py

from crewai import Agent
from llm import architect_llm

discovery_agent = Agent(
    role="Platform Discovery Analyst",

    goal="""
    Reverse engineer the existing platform
    using repository knowledge.
    """,

    backstory="""
    Expert in:

    - SharePoint
    - Power Automate
    - Python
    - Solution Architecture

    Analyse repository artifacts and
    identify:

    - entities
    - relationships
    - business rules
    - workflows
    """,

    llm=architect_llm,
    verbose=True
)