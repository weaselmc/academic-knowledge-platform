from crewai import Task

from agents.governance import governance_agent

from tasks.discovery_platform import discovery_task


gap_analysis_task = Task(
    description="""
    Analyse the current Academic Knowledge Platform using
    the discovery inventory as the baseline.

    Discovery Findings:

    {context}

    Evaluate whether the platform contains sufficient
    information, evidence, governance controls,
    relationships and automation support to manage:

    - Qualifications
    - Courses
    - Clusters
    - Units
    - TAS management
    - LAP management
    - Assessment management
    - Assessment Mapping Matrices
    - Validation activities
    - Industry engagement
    - Student feedback
    - Employer feedback
    - Continuous improvement
    - Change management
    - Knowledge management
    - Audit evidence
    - Canvas publishing

    Evaluate compliance and governance requirements drawn
    from:

    - Standards for RTOs 2025
    - Outcome Standards
    - Compliance Standards
    - TAC guidance
    - TIWA requirements
    - Credential policies
    - Training Package requirements

    Identify:

    1. Existing entities
    2. Missing entities

    3. Existing relationships
    4. Missing relationships

    5. Existing governance controls
    6. Missing governance controls

    7. Existing evidence sources
    8. Missing evidence sources

    9. Existing metadata
    10. Missing metadata

    11. Existing approval pathways
    12. Missing approval pathways

    13. Existing information ownership
    14. Missing ownership definitions

    15. Existing automation support
    16. Missing automation support

    17. Duplicated information
    18. Conflicting information

    19. Information stored only in documents

    20. Information that should be represented
        as structured data

    Determine:

    - What already exists
    - What must exist
    - What is missing
    - What should be governed
    - What should become structured data
    - What should become reusable knowledge

    Recommend enhancements that extend the
    current platform.

    Do not redesign the platform from scratch.

    Use the discovered implementation as the
    authoritative baseline.

    Focus on practical platform evolution,
    governance maturity and compliance readiness.
    """,

    context=[
        discovery_task
    ],

    expected_output="""
    A governance and capability assessment containing:

    # Current Platform Capability

    - Existing Capabilities
    - Existing Governance
    - Existing Evidence Sources

    # Coverage Analysis

    ## Qualification Coverage

    ## TAS Coverage

    ## LAP Coverage

    ## Assessment Coverage

    ## Validation Coverage

    ## Industry Engagement Coverage

    ## Continuous Improvement Coverage

    ## Knowledge Management Coverage

    ## Compliance Coverage

    # Entity Analysis

    - Existing Entities
    - Missing Entities
    - Recommended Entities

    # Relationship Analysis

    - Existing Relationships
    - Missing Relationships
    - Governance Relationships

    # Information Analysis

    - Structured Information
    - Information Only In Documents
    - Missing Information
    - Duplicated Information

    # Governance Analysis

    - Existing Controls
    - Missing Controls
    - Ownership Gaps
    - Approval Gaps

    # Evidence Analysis

    - Existing Evidence
    - Missing Evidence
    - Audit Risks

    # Compliance Analysis

    Classify findings as:

    - Mandatory
    - Required
    - Recommended
    - Optional

    # Recommended Platform Extensions

    Prioritised by:

    - Compliance Impact
    - Governance Impact
    - Operational Impact
    - Implementation Complexity

    # Priority Recommendations

    High Priority

    Medium Priority

    Low Priority

    Focus on practical, incremental enhancements
    to the current implementation.
    """,

    agent=governance_agent,

    output_file="outputs/governance/gap_analysis.md"
)