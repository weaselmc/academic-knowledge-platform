from crewai import Task

from agents.governance import governance_agent

from tasks.discovery_platform import discovery_task


compliance_task = Task(
    description="""
    Generate compliance and governance schema requirements.

    Repository Knowledge:

    {knowledge}

    Input:

    - discovered_schema.json

    OBJECTIVE

    Transform governance and compliance requirements
    into machine-readable schema requirements.

    The output will be merged into the
    canonical platform schema.

    CRITICAL

    Model ENTITY TYPES only.

    Do not model:

    - records
    - examples
    - sample rows
    - qualification instances
    - unit instances
    - assessment instances

    Ignore data values.

    Focus on:

    - entities
    - fields
    - relationships
    - ownership
    - approvals
    - auditability
    - retention
    - evidence

    Evaluate requirements derived from:

    - Standards for RTOs 2025
    - Outcome Standards
    - Compliance Standards
    - TAC Guidance
    - TIWA Requirements
    - Credential Policies
    - Training Package Requirements

    Determine:

    - mandatory entities
    - mandatory fields
    - mandatory relationships
    - ownership requirements
    - audit requirements
    - approval requirements
    - retention requirements
    - evidence requirements

    Identify schema elements required to support:

    - Qualifications
    - Courses
    - Units
    - TAS
    - LAP
    - Assessments
    - Validation
    - Industry Engagement
    - Student Feedback
    - Employer Feedback
    - Continuous Improvement
    - Governance
    - Change Requests
    - Approvals

    Generate schema requirements only.

    Do not generate reports.

    Do not generate recommendations.

    Produce ONLY valid JSON.

    No markdown.
    No commentary.
    No explanations.
    """,

    context=[
        discovery_task
    ],

    expected_output="""
{
  "required_entities": [
    {
      "name": "",
      "purpose": "",
      "classification": "mandatory|required|recommended|optional"
    }
  ],

  "required_relationships": [
    {
      "source_entity": "",
      "target_entity": "",
      "relationship_type": "",
      "classification": "mandatory|required|recommended|optional"
    }
  ],

  "required_fields": [
    {
      "entity": "",
      "field_name": "",
      "field_type": "",
      "required": true,
      "classification": "mandatory|required|recommended|optional"
    }
  ],

  "audit_fields": [
    {
      "field_name": "",
      "field_type": "",
      "purpose": ""
    }
  ],

  "ownership_fields": [
    {
      "field_name": "",
      "field_type": "",
      "purpose": ""
    }
  ],

  "approval_fields": [
    {
      "field_name": "",
      "field_type": "",
      "purpose": ""
    }
  ],

  "retention_fields": [
    {
      "field_name": "",
      "field_type": "",
      "purpose": ""
    }
  ],

  "evidence_requirements": [
    {
      "entity": "",
      "evidence_type": "",
      "required_metadata": []
    }
  ],

  "governance_requirements": [
    {
      "entity": "",
      "required_controls": []
    }
  ]
}
""",

    agent=governance_agent,

    output_file="outputs/schema/compliance_schema.json"
)