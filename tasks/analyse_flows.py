# tasks/analyse_flows.py

from crewai import Knowledge,Task
from agents.flow_analyst import flow_agent

flow_analysis_task = Task(
    description="""
    Analyse the supplied Power Automate artifacts:

    - definition.json
    - connectionsMap.json
    - apisMap.json

    Knowledge:
    {knowledge}

    Reverse engineer the solution architecture.

    Identify:

    - SharePoint lists used
    - Entity relationships
    - Business rules
    - Data lifecycle
    - Synchronisation logic
    - Folder creation logic
    - Azure Function dependencies
    - Parser outputs

    Document how data moves from source
    documents into SharePoint.
    """,

    expected_output="""
    A markdown document containing:

    # Current Solution Architecture

    # Entity Inventory

    # Data Flow Diagram

    # Business Rules

    # SharePoint Dependencies

    # Power Automate Dependencies

    # Improvement Opportunities

    # Canonical Entity Candidates
    """,

    agent=flow_agent
)