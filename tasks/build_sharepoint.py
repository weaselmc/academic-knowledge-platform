# tasks/build_sharepoint.py

from crewai import Knowledge,Task
from agents.sharepoint import sharepoint_agent

sharepoint_task = Task(
    description="""
    Create SharePoint solution based
    on the canonical academic data model.

    Knowledge:
    {knowledge}

    Design:
    - Lists
    - Libraries
    - Content Types
    - Metadata
    - Views
    - Relationships
    """,

    expected_output="""
    A complete SharePoint architecture document
    including:

    - Lists
    - Libraries
    - Content Types
    - Lookup Relationships
    - Deployment Recommendations
    """,

    agent=sharepoint_agent
)