from crewai import Task

from agents.python_dev import python_agent

from tasks.discovery_platform import discovery_task
from tasks.build_model import build_model_task
from tasks.build_sharepoint import sharepoint_task


build_parser_task = Task(
    description="""
    Analyse the current platform architecture and determine
    the extraction, transformation, normalisation and
    ingestion capabilities required to support the
    Academic Knowledge Platform.

    Repository Knowledge:

    {knowledge}

    Review findings from:

    - Discovery Analysis
    - Platform Architecture
    - SharePoint Architecture

    Evaluate information sources including:

    - TAS documents
    - LAP documents
    - Assessment Plans
    - Assessment Mapping Matrices
    - Validation Records
    - Industry Advisory Documentation
    - Student Feedback
    - Employer Feedback
    - Continuous Improvement Records
    - Standards Documentation
    - Compliance Requirements
    - Policies and Procedures
    - Training Package Information

    Determine:

    - what information must be extracted
    - where information originates
    - which entities are authoritative
    - how information should be normalised
    - how relationships should be created
    - how version history should be preserved
    - how evidence chains should be maintained

    Identify:

    - reusable extraction patterns
    - reusable normalisation rules
    - metadata requirements
    - entity mapping requirements
    - validation requirements
    - ingestion requirements
    - relationship generation requirements

    Design technical capabilities that support:

    - knowledge extraction
    - knowledge normalisation
    - knowledge enrichment
    - knowledge versioning
    - governance traceability
    - auditability
    - SharePoint integration
    - Canvas publishing
    - Knowledge Repository ingestion

    Preserve existing working implementations where
    possible and recommend extensions rather than
    complete replacement.

    Focus on practical implementation architecture
    rather than high-level concepts.
    """,

    expected_output="""
    A technical implementation specification containing:

    # Information Sources

    - Source Types
    - Ownership
    - Authority Levels

    # Extraction Architecture

    - Parser Types
    - Extraction Responsibilities
    - Supported Artefacts
    - Reusable Components

    # Entity Mapping Model

    For each source identify:

    - Extracted Entities
    - Entity Relationships
    - Authority Sources
    - Validation Rules

    # Normalisation Rules

    - Data Standardisation
    - Metadata Generation
    - Relationship Resolution
    - Versioning Strategy

    # Knowledge Repository Integration

    - Knowledge Objects
    - Metadata Requirements
    - Taxonomies
    - Classification Rules

    # SharePoint Integration

    - Target Lists
    - Content Types
    - Lookup Relationships

    # Validation and Quality Controls

    - Validation Rules
    - Error Handling
    - Data Quality Requirements

    # Technical Architecture

    - Python Modules
    - Parser Classes
    - Services
    - Azure Functions
    - API Requirements

    # Implementation Roadmap

    - Existing Components To Reuse
    - Required Enhancements
    - New Components Required

    Focus on implementation-ready guidance.
    """,

    context=[
        discovery_task,
        build_model_task,
        sharepoint_task
    ],

    agent=python_agent,

    output_file="outputs/implementation/parser_architecture.md"
)