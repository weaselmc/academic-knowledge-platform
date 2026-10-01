# tasks/build_model.py

from crewai import Knowledge, Task
from agents.architect import architect
from tasks.discovery_platform import discovery_task
from tasks.gap_analysis import gap_analysis_task

build_model_task = Task(
    description="""
    Design canonical academic data model"

    Knowledge:
    {knowledge}""",

    context=[
        discovery_task,
        gap_analysis_task
    ],

    expected_output="""
    Entity relationship model,
    JSON schema,
    implementation roadmap,
    and normalization strategy.
    """,

    agent=architect
)