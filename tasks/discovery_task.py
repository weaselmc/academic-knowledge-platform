

from crewai import Knowledge,Task
from agents.discovery import discovery_agent


discovery_task = Task(
    description="""
    Analyse the supplied repository.

    Repository Contents:

    {knowledge}

    Identify:

    - parser outputs
    - SharePoint entities
    - business rules
    - Power Automate flows
    - relationships

    Reverse engineer the current platform.
    """,

    expected_output="""
    JSON inventory containing:

    entities
    relationships
    business_rules
    workflows
    """,

    agent=discovery_agent
)