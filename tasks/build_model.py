# tasks/build_model.py

from crewai import Knowledge, Task
from agents.architect import architect
from tasks import discovery_task

build_model_task = Task(
    description="""
    Design canonical academic data model"

    Knowledge:
    {knowledge}""",

    context=[
        discovery_task
    ],

    expected_output="""
    Entity relationship model,
    JSON schema,
    implementation roadmap,
    and normalization strategy.
    """,

    agent=architect
)