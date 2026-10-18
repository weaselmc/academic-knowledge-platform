from crewai import Task

from agents.governance import governance_agent

from tasks.discovery_platform import discovery_task

gap_analysis_task = Task(
    description="""
    Analyse the current Academic Knowledge Platform using
    the Discovery Model as the baseline.

    Discovery Findings:

    Use the Discovery Model provided by the
    Discovery Task as the authoritative baseline.

    Evaluate whether the platform contains sufficient
    information, governance controls, evidence,
    metadata, relationships and automation support
    to manage:

    - Qualifications
    - Courses
    - Clusters
    - Units
    - TAS Management
    - LAP Management
    - Assessment Management
    - Assessment Mapping Matrices
    - Validation Activities
    - Industry Engagement
    - Student Feedback
    - Employer Feedback
    - Continuous Improvement
    - Change Management
    - Knowledge Management
    - Audit Evidence
    - Canvas Publishing

    Evaluate governance and compliance expectations
    derived from:

    - Standards for RTOs 2025
    - Outcome Standards
    - Compliance Standards
    - TAC Guidance
    - TIWA Requirements
    - Credential Policies
    - Training Package Requirements

    Determine:

    - what currently exists
    - what is missing
    - what must be governed
    - what must be auditable
    - what requires ownership
    - what requires approval workflows
    - what requires evidence tracking
    - what should be represented as structured data
    - what should become reusable knowledge

    Identify:

    - existing entities
    - missing entities
    - existing relationships
    - missing relationships
    - existing governance controls
    - missing governance controls
    - existing evidence
    - missing evidence
    - existing metadata
    - missing metadata
    - duplicated information
    - conflicting information
    - ownership gaps
    - approval gaps
    - automation gaps

    Classify findings as:

    - Mandatory
    - Required
    - Recommended
    - Optional

    Use the current platform implementation
    as the baseline.

    Focus on incremental evolution.

    Produce ONLY valid JSON.

    No markdown.
    No narrative report.
    No recommendations outside the JSON structure.
    """,

    context=[
        discovery_task
    ],

    expected_output="""
{
  "coverage_assessment": {
    "qualification_management": "",
    "course_management": "",
    "unit_management": "",
    "tas_management": "",
    "lap_management": "",
    "assessment_management": "",
    "validation_management": "",
    "industry_engagement_management": "",
    "continuous_improvement_management": "",
    "knowledge_management": "",
    "compliance_management": ""
  },

  "entities": {
    "existing": [],
    "missing": [],
    "required": [
      {
        "name": "",
        "classification": "Mandatory|Required|Recommended|Optional",
        "reason": ""
      }
    ]
  },

  "relationships": {
    "existing": [],
    "missing": [],
    "required": [
      {
        "source_entity": "",
        "target_entity": "",
        "relationship_type": "",
        "classification": "Mandatory|Required|Recommended|Optional"
      }
    ]
  },

  "metadata_requirements": [
    {
      "entity": "",
      "field_name": "",
      "classification": "Mandatory|Required|Recommended|Optional",
      "reason": ""
    }
  ],

  "governance_controls": {
    "existing": [],
    "missing": [],
    "required": [
      {
        "control": "",
        "classification": "Mandatory|Required|Recommended|Optional",
        "reason": ""
      }
    ]
  },

  "approval_requirements": [
    {
      "object_type": "",
      "approval_type": "",
      "owner_role": "",
      "classification": "Mandatory|Required|Recommended|Optional"
    }
  ],

  "ownership_requirements": [
    {
      "entity": "",
      "owner_role": "",
      "classification": "Mandatory|Required|Recommended|Optional"
    }
  ],

  "evidence_requirements": [
    {
      "evidence_type": "",
      "classification": "Mandatory|Required|Recommended|Optional",
      "purpose": ""
    }
  ],

  "automation_requirements": {
    "existing": [],
    "missing": [],
    "required": [
      {
        "capability": "",
        "classification": "Mandatory|Required|Recommended|Optional"
      }
    ]
  },

  "information_analysis": {
    "structured_information": [],
    "document_only_information": [],
    "missing_information": [],
    "duplicated_information": [],
    "conflicting_information": []
  },

  "compliance_requirements": [
    {
      "requirement": "",
      "source": "",
      "classification": "Mandatory|Required|Recommended|Optional",
      "affected_entities": []
    }
  ],

  "audit_requirements": [
    {
      "entity": "",
      "audit_evidence": [],
      "classification": "Mandatory|Required|Recommended|Optional"
    }
  ],

  "platform_gaps": [
    {
      "gap": "",
      "impact": "Compliance|Governance|Operational|Knowledge",
      "classification": "Mandatory|Required|Recommended|Optional"
    }
  ],

  "implementation_priorities": {
    "high": [],
    "medium": [],
    "low": []
  }
}
""",

    agent=governance_agent,

    output_file="outputs/models/compliance_requirements.json"
)