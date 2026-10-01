# tasks/build_sharepoint.py

from crewai import Knowledge,Task
from agents.sharepoint import sharepoint_agent
from tasks.discovery_platform import discovery_task
from tasks.build_model import build_model_task

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
    context=[
        discovery_task,
        build_model_task
    ],

    agent=sharepoint_agent
)