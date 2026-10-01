# agents/python_dev.py

from crewai import Agent
from llm import worker_llm

python_agent = Agent(
    role="Senior Python Developer",

    goal="""
    Build document extraction
    and normalization solutions.
    """,

    backstory="""
    Expert in:

    - Python
    - Document parsing
    - Azure Functions
    - APIs
    - Data modelling
    - ETL pipelines
    """,

    llm=worker_llm,
    verbose=True
)