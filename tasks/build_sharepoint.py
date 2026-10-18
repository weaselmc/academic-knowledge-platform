from crewai import Task

from agents.sharepoint import sharepoint_agent

from tasks.discovery_platform import discovery_task
from tasks.build_model import build_model_task


sharepoint_task = Task(
    description="""
    Analyse the existing SharePoint implementation and
    determine the SharePoint architecture required to
    support the Academic Knowledge Platform.

    Repository Knowledge:

    {knowledge}

    Use findings from:

    - Discovery Analysis
    - Platform Architecture Model

    Treat existing SharePoint structures as evidence
    of the current implementation.

    Review and analyse:

    - Lists
    - Libraries
    - Site Columns
    - Content Types
    - Views
    - Metadata Structures
    - Lookup Relationships
    - Permissions
    - Search Structures
    - Automation Dependencies

    Determine:

    - what SharePoint structures currently exist
    - which structures are authoritative
    - which structures are duplicated
    - which relationships already exist
    - which governance controls exist
    - what changes are required
    - what new structures are required

    Ensure SharePoint can support:

    - Qualifications
    - Courses
    - Clusters
    - Units
    - TASs
    - LAPs
    - Assessments
    - Assessment Mapping Matrices
    - Validation Activities
    - Industry Advisory Records
    - Student Feedback
    - Employer Feedback
    - Continuous Improvement
    - Change Requests
    - Approvals
    - Governance Records
    - Knowledge Assets
    - Canvas Publishing
    - Power Automate Automation
    - Audit Evidence

    Identify:

    - source-of-truth locations
    - ownership boundaries
    - lookup requirements
    - metadata requirements
    - governance requirements
    - retention requirements
    - security boundaries
    - integration dependencies

    Preserve existing structures wherever possible.

    Recommend extensions and enhancements rather
    than complete redesign unless clearly justified.

    Focus on implementation-ready SharePoint architecture.
    """,

    expected_output="""
    A SharePoint implementation architecture containing:

    # Current SharePoint Assessment

    - Existing Lists
    - Existing Libraries
    - Existing Relationships
    - Existing Governance Controls

    # Information Architecture

    - Site Structure
    - Logical Domains
    - Ownership Model

    # List Architecture

    For each list define:

    - Purpose
    - Ownership
    - Authority Level
    - Key Metadata
    - Related Lists

    # Content Type Architecture

    - Content Types
    - Site Columns
    - Managed Metadata
    - Reusable Components

    # Relationship Model

    - Lookup Relationships
    - Hierarchical Relationships
    - Governance Relationships

    # Security and Governance Model

    - Permissions
    - Ownership
    - Approval Controls
    - Versioning Requirements
    - Retention Requirements

    # Search and Discovery Model

    - Search Metadata
    - Navigation Requirements
    - Knowledge Retrieval Considerations

    # Integration Model

    - Power Automate Dependencies
    - Parser Dependencies
    - Knowledge Repository Dependencies
    - Canvas Publishing Dependencies

    # Required Enhancements

    - New Lists
    - New Columns
    - New Content Types
    - New Relationships
    - Required Migration Activities

    # Deployment Considerations

    - Implementation Sequence
    - Risk Areas
    - Impact Considerations

    Focus on implementation-ready outcomes rather
    than theoretical SharePoint design.
    """,

    context=[
        discovery_task,
        build_model_task
    ],

    agent=sharepoint_agent,

    output_file="outputs/sharepoint/sharepoint_architecture.md"
)