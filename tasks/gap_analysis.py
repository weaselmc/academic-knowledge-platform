# tasks/gap_analysis.py

from crewai import Task

from agents.governance import governance_agent

from tasks.discovery_platform import discovery_task

gap_analysis_task = Task(
    description="""
    Using the discovered academic platform inventory:

    Determine whether the platform contains
    sufficient information to fully support:

    - TAS management
    - LAP management
    - Assessment management
    - Validation activities
    - Continuous improvement
    - Registration Standards 2025
    - TAC requirements
    - TIWA requirements

    Identify:

    1. Existing entities.
    2. Missing entities.
    3. Existing relationships.
    4. Missing relationships.
    5. Existing compliance evidence.
    6. Missing compliance evidence.
    7. Duplicated information.
    8. Information currently stored only
       inside documents.
    9. Information that should be
       represented as data.

    Recommend extensions to the model.

    Do not redesign the platform from
    scratch.

    Assume the current implementation
    represented by the parsers,
    Power Automate definitions and
    SharePoint schema is the baseline.
    """,

    context=[
        discovery_task
    ],

    expected_output="""
    Markdown report containing:

    # Current Platform Capability

    # TAS Coverage

    # LAP Coverage

    # Assessment Coverage

    # Compliance Coverage

    # Existing Entities

    # Missing Entities

    # Existing Relationships

    # Missing Relationships

    # Information Stored Only In Documents

    # Recommended Model Extensions

    # Priority Recommendations

    # Future State Architecture
    """,

    agent=governance_agent
)