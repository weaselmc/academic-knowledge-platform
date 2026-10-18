from crewai import Task
from agents.flow_analyst import flow_agent

flow_analysis_task = Task(
    description="""
    Analyse the supplied Power Automate solution artefacts:

    - definition.json
    - connectionsMap.json
    - apisMap.json

    Repository Knowledge:

    {knowledge}

    Reverse engineer the existing automation architecture.

    Treat the supplied artefacts as evidence of the
    current production implementation.

    Identify:

    - flows
    - triggers
    - actions
    - SharePoint dependencies
    - Azure Function dependencies
    - external integrations
    - data transformations
    - entity relationships
    - business rules
    - information ownership
    - source-of-truth systems
    - automation boundaries
    - lifecycle events

    Determine:

    - how information enters the platform
    - how information moves through the platform
    - how information is transformed
    - how information is published
    - which systems consume information
    - which systems produce information
    - where duplication occurs
    - where governance controls exist
    - where governance controls are missing

    Identify change propagation paths:

    For example:

    Qualification
        -> Cluster
            -> Unit
                -> TAS
                    -> LAP
                        -> Canvas

    Trace automation dependencies and document
    potential downstream impacts.

    Support all findings with evidence identified
    in the supplied artefacts.

    Classify findings as:

    - Confirmed
    - Strong Evidence
    - Inferred
    - Unknown

    Do not redesign the solution.
    Focus on documenting and understanding
    the current implementation.
    """,

    expected_output="""
    A structured automation analysis containing:

    # Automation Inventory

    - Flows
    - Triggers
    - Actions
    - Integrations

    # Entity Usage Analysis

    - Entities
    - Relationships
    - Ownership
    - Source Systems

    # Automation Architecture

    - Data Movement
    - Transformation Logic
    - Synchronisation Logic
    - Publishing Logic

    # Business Rules

    - Explicit Rules
    - Derived Rules
    - Validation Rules

    # Dependencies

    - SharePoint Dependencies
    - Azure Function Dependencies
    - Integration Dependencies
    - Canvas Dependencies

    # Change Propagation Analysis

    - Upstream Dependencies
    - Downstream Dependencies
    - Impact Chains

    # Governance Assessment

    - Governance Controls
    - Missing Controls
    - Ownership Boundaries

    # Risks and Technical Debt

    - Duplicate Logic
    - Single Points of Failure
    - Maintenance Risks

    # Recommended Follow-up Analysis

    Areas requiring additional investigation.
    """,

    agent=flow_agent,

    output_file="outputs/platform/automation_analysis.md"
)