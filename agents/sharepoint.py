# agents/sharepoint.py

from crewai import Agent
from llm import worker_llm

sharepoint_agent = Agent(
    role="SharePoint Solution Architect",

    goal="""
    Design SharePoint Online storage
    structures for the central model.
    """,

    backstory="""
    Expert in:

    - SharePoint Online
    - Graph API
    - Power Automate
    - Metadata
    - Content Types
    - Information Architecture
    """,

    llm=worker_llm,
    verbose=True
)