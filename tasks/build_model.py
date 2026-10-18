from crewai import Task

from agents.architect import architect

from tasks.discovery_platform import discovery_task
from tasks.gap_analysis import gap_analysis_task
from tasks.analyse_flows import flow_analysis_task


build_model_task = Task(
    description="""
    Build the target architecture model for the Academic Knowledge Platform.

    Use findings from:

    - Discovery Analysis
    - Governance Analysis
    - Standards Analysis
    - Gap Analysis
    - Flow Analysis

    Treat existing repository artefacts, SharePoint structures,
    Power Automate solutions, governance assets and knowledge
    repositories as evidence of the current implementation.

    The objective is not to redesign the platform from scratch.

    Determine:

    - What already exists
    - What must be retained
    - What must be extended
    - What is duplicated
    - What is missing
    - What relationships are required
    - What governance controls are required
    - What knowledge structures are required

    Define the target platform architecture required to support:

    - Qualifications
    - Courses
    - Clusters
    - Units
    - TASs
    - LAPs
    - Assessment Mapping Matrices
    - Assessment Plans
    - Validation Activities
    - Industry Advisory Meetings
    - Student Feedback
    - Employer Feedback
    - Recommendations
    - Continuous Improvement
    - Change Requests
    - Approvals
    - Governance Records
    - Knowledge Assets
    - Canvas Publishing
    - Power Automate Integrations
    - SharePoint Structures
    - Auditor Evidence Chains

    Identify:

    - authoritative entities
    - source-of-truth locations
    - ownership boundaries
    - governance responsibilities
    - integration requirements
    - audit requirements
    - retention requirements
    - change propagation paths

    Ensure:

    - information is captured once
    - information is reused where possible
    - duplication is minimised
    - relationships are explicit
    - governance requirements are supported
    - solutions are auditable
    - solutions are version controlled

    No information should be physically deleted.

    All platform information should support:

    - traceability
    - historical reconstruction
    - auditability
    - governance
    - compliance
    - automation
    - knowledge retrieval

    Produce an architecture that supports long-term platform
    evolution while preserving existing working solutions.
    """,

    expected_output="""
    A comprehensive Academic Knowledge Platform
    architecture model containing:

    # Current State Summary

    - Existing Platform Capabilities
    - Existing Entities
    - Existing Relationships

    # Target Architecture

    - Platform Domains
    - Major Information Areas
    - Source-of-Truth Systems

    # Canonical Entity Model

    For each entity define:

    - Purpose
    - Ownership
    - Authority Level
    - Related Entities
    - Lifecycle

    # Relationship Model

    Document:

    - Parent-child relationships
    - Reference relationships
    - Governance relationships
    - Knowledge relationships

    # Governance Model

    Define:

    - Ownership
    - Approval Responsibilities
    - Audit Responsibilities
    - Versioning Requirements

    # Knowledge Model

    Define:

    - Knowledge Objects
    - Taxonomies
    - Metadata Requirements
    - Retrieval Requirements

    # Change Propagation Model

    Define:

    - Upstream Dependencies
    - Downstream Dependencies
    - Impact Chains

    # Integration Model

    Define:

    - SharePoint Integration
    - Power Automate Integration
    - Canvas Integration
    - Parser Integration

    # Architectural Decisions

    Include key architectural principles,
    constraints and assumptions.

    Focus on implementation-ready architecture
    rather than theoretical design.
    """,

    context=[
        discovery_task,
        gap_analysis_task,
        flow_analysis_task
    ],

    agent=architect,

    output_file="outputs/architecture/platform_architecture.md"
)