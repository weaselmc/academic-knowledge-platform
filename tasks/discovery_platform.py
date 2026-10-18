from crewai import Task

from agents.discovery import discovery_agent


discovery_task = Task(
    description="""
    Analyse the supplied repository and all available
    knowledge artefacts.

    Repository Knowledge:

    {knowledge}

    Treat the repository as evidence of the current
    Academic Knowledge Platform implementation.

    Analyse:

    - Parser outputs
    - SharePoint structures
    - Lists
    - Libraries
    - Metadata
    - Content Types
    - Power Automate flows
    - Azure Function integrations
    - Python services
    - Knowledge repository assets
    - TAS artefacts
    - LAP artefacts
    - Assessment artefacts
    - Validation artefacts
    - Governance artefacts
    - Continuous improvement artefacts
    - Industry engagement artefacts
    - Canvas-related artefacts

    Discover and document:

    - entities
    - relationships
    - business rules
    - workflows
    - integrations
    - governance controls
    - authority sources
    - knowledge assets
    - taxonomies
    - metadata structures
    - reusable information domains
    - business capabilities

    Determine:

    - what exists
    - where it exists
    - who owns it
    - what consumes it
    - what depends upon it
    - what systems it integrates with

    Identify:

    - source-of-truth systems
    - duplicated information
    - conflicting information
    - upstream dependencies
    - downstream dependencies
    - change propagation paths

    For each significant discovery identify:

    - source system
    - source artefact
    - ownership
    - authority level
    - consuming systems

    Classify findings as:

    - Confirmed
    - Strong Evidence
    - Inferred
    - Unknown

    Focus exclusively on understanding and
    documenting the current implementation.

    Do not propose future-state solutions,
    implementation recommendations or redesigns.
    """,

    expected_output="""
    Structured discovery inventory containing:

    # Platform Capability Inventory

    - Existing capabilities
    - Existing systems
    - Existing integrations

    # Entity Inventory

    For each entity:

    - Purpose
    - Ownership
    - Authority Level
    - Related Entities

    # Relationship Inventory

    - Parent-child relationships
    - Reference relationships
    - Governance relationships

    # Authority Model

    - Source-of-truth systems
    - Derived information sources
    - Consuming systems

    # Workflow Inventory

    - Business Processes
    - Automation Processes
    - Knowledge Flows

    # Integration Inventory

    - SharePoint
    - Power Automate
    - Azure Functions
    - Canvas
    - External Systems

    # Governance Inventory

    - Governance Controls
    - Approval Points
    - Evidence Sources

    # Knowledge Inventory

    - Knowledge Objects
    - Taxonomies
    - Metadata Structures
    - Information Domains

    # Dependency Analysis

    - Upstream Dependencies
    - Downstream Dependencies
    - Change Propagation Chains

    # Confidence Assessment

    - Confirmed Findings
    - Strong Evidence Findings
    - Inferred Findings
    - Unknown Areas
    """,

    agent=discovery_agent,

    output_file="outputs/platform/discovery_inventory.md"
)