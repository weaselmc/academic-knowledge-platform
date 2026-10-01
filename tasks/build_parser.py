# tasks/build_parser.py

from crewai import Knowledge,Task
from agents.python_dev import python_agent
from tasks.discovery_platform import discovery_task
from tasks.build_model import build_model_task
from tasks.build_sharepoint import sharepoint_task

build_parser_task = Task(
    description="""
    Design parsing architecture for:

    Knowledge:
    {knowledge}

    - TAS
    - LAP
    - Standards
    - Policies
    """,

    expected_output="""
    Python module structure,
    parser classes,
    extraction workflow,
    normalization workflow.
    """,

    context=[
        discovery_task,
        build_model_task,
        sharepoint_task
    ],

    agent=python_agent
)