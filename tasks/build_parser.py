# tasks/build_parser.py

from crewai import Knowledge,Task
from agents.python_dev import python_agent

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

    agent=python_agent
)