from crewai import Task

from agents.architect import architect

from tasks.discovery_platform import discovery_task
from tasks.gap_analysis import gap_analysis_task
from tasks.analyse_flows import flow_analysis_task

build_model_task = Task(
    description="""
    Build the canonical Academic Knowledge Platform model.

    Use outputs from:

    - Discovery Analysis
    - Gap Analysis
    - Flow Analysis
    - Governance Analysis
    - Standards Analysis

    Repository Knowledge:

    {knowledge}

    Treat all repository artefacts, SharePoint structures,
    Power Automate definitions, parser code, governance assets,
    standards documentation and knowledge repositories as
    evidence of the current implementation.

    The objective is to create the authoritative platform
    data model that will drive:

    - SharePoint list design
    - Power Automate design
    - Canvas publishing
    - Python parser validation
    - Compliance reporting
    - Governance workflows
    - Document generation
    - Knowledge retrieval

    Determine:

    - existing entities
    - authoritative entities
    - source-of-truth locations
    - ownership boundaries
    - lifecycle states
    - governance controls
    - audit requirements
    - retention requirements
    - metadata requirements
    - integration requirements
    - change propagation paths

    Include entities where relevant:

    - Qualification
    - AccreditedCourse
    - Cluster
    - Unit
    - TAS
    - LAP
    - Assessment
    - AssessmentMapping
    - AssessmentPlan
    - Validation
    - IndustryMeeting
    - IndustryFeedback
    - StudentFeedback
    - EmployerFeedback
    - Recommendation
    - ImprovementAction
    - ChangeRequest
    - Approval
    - GovernanceRecord
    - LearningResource
    - CanvasCourse
    - AutomationFlow
    - SharePointList

    Ensure:

    - information is captured once
    - duplication is minimized
    - relationships are explicit
    - ownership is defined
    - governance is auditable
    - historical reconstruction is possible
    - automation dependencies are traceable

    Produce ONLY valid JSON.

    No markdown.
    No narrative report.
    No explanations.
    """,

    expected_output="""
{
  "platform_domains": [
    {
      "name": "",
      "description": ""
    }
  ],

  "source_systems": [
    {
      "name": "",
      "authority_level": "",
      "owned_entities": []
    }
  ],

  "entities": [
    {
      "name": "",
      "description": "",
      "owner": "",
      "authority_level": "",
      "source_of_truth": "",
      "retention_requirement": "",
      "lifecycle_states": [],
      "fields": [
        {
          "name": "",
          "type": "",
          "required": true,
          "unique": false,
          "description": ""
        }
      ]
    }
  ],

  "relationships": [
    {
      "parent_entity": "",
      "child_entity": "",
      "relationship_type": "",
      "cardinality": ""
    }
  ],

  "governance": {
    "ownership_roles": [],
    "approval_roles": [],
    "audit_roles": [],
    "compliance_requirements": []
  },

  "metadata_requirements": [
    {
      "entity": "",
      "field": "",
      "purpose": ""
    }
  ],

  "integrations": [
    {
      "system": "",
      "integration_type": "",
      "entities": [],
      "purpose": ""
    }
  ],

  "knowledge_model": {
    "knowledge_objects": [],
    "taxonomies": [],
    "retrieval_requirements": []
  },

  "change_propagation": [
    {
      "source_entity": "",
      "target_entity": "",
      "impact_description": ""
    }
  ],

  "audit_requirements": [
    {
      "entity": "",
      "requirement": ""
    }
  ]
}
""",

    context=[
        discovery_task,
        gap_analysis_task,
        flow_analysis_task
    ],

    agent=architect,

    output_file="outputs/models/platform_model.json"
)