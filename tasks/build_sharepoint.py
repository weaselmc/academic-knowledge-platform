from crewai import Task

from agents.sharepoint import sharepoint_agent

from tasks.discovery_platform import discovery_task
from tasks.build_model import build_model_task

sharepoint_task = Task(
    description="""
    Build the canonical SharePoint schema for the
    Academic Knowledge Platform.

    Repository Knowledge:

    {knowledge}

    Use outputs from:

    - Discovery Analysis
    - Platform Model

    Treat existing SharePoint assets as evidence of
    the current implementation.
    
    Do not include examples, sample rows,
    unit names, qualification names or
    instance data unless required as evidence.

    The objective is to discover schema,
    relationships and metadata definitions.

    Analyse and identify:

    - existing lists
    - existing libraries
    - existing content types
    - existing site columns
    - existing metadata
    - existing relationships
    - existing permissions
    - existing governance controls

    Determine:

    - authoritative SharePoint locations
    - ownership boundaries
    - duplicate structures
    - reusable components
    - required enhancements
    - required governance controls
    - required retention controls
    - required security controls

    Build the SharePoint information architecture
    required to support:

    - Qualifications
    - Accredited Courses
    - Clusters
    - Units
    - TASs
    - LAPs
    - Assessments
    - Assessment Mapping Matrices
    - Assessment Plans
    - Validation Activities
    - Industry Engagement
    - Student Feedback
    - Employer Feedback
    - Continuous Improvement
    - Recommendations
    - Approvals
    - Governance Records
    - Change Requests
    - Learning Resources
    - Knowledge Assets
    - Canvas Publishing
    - Power Automate Integration
    - Audit Evidence

    Preserve existing structures where possible.

    Extend rather than replace existing solutions
    unless duplication or governance concerns
    require redesign.

    Produce only valid JSON.

    No markdown.
    No narrative report.
    No explanations.
    """,

    expected_output="""
{
  "site_architecture": {
    "site_name": "",
    "domains": [
      {
        "name": "",
        "description": ""
      }
    ]
  },

  "lists": [
    {
      "name": "",
      "purpose": "",
      "owner": "",
      "authority_level": "",
      "entity": "",

      "columns": [
        {
          "name": "",
          "type": "",
          "required": true,
          "indexed": false,
          "unique": false,
          "description": ""
        }
      ]
    }
  ],

  "document_libraries": [
    {
      "name": "",
      "purpose": "",
      "content_types": []
    }
  ],

  "content_types": [
    {
      "name": "",
      "parent_content_type": "",
      "site_columns": []
    }
  ],

  "site_columns": [
    {
      "name": "",
      "type": "",
      "required": true
    }
  ],

  "managed_metadata": [
    {
      "term_set": "",
      "terms": []
    }
  ],

  "lookup_relationships": [
    {
      "source_list": "",
      "source_column": "",
      "target_list": "",
      "target_column": "",
      "relationship_type": ""
    }
  ],

  "hierarchical_relationships": [
    {
      "parent_list": "",
      "child_list": "",
      "relationship": ""
    }
  ],

  "permissions": [
    {
      "scope": "",
      "owners": [],
      "members": [],
      "visitors": []
    }
  ],

  "governance_controls": {
    "versioning_enabled": [],
    "approval_required": [],
    "retention_labels": [],
    "audit_requirements": []
  },

  "search_configuration": {
    "searchable_columns": [],
    "refiners": [],
    "navigation_terms": []
  },

  "integrations": {
    "power_automate": [
      {
        "flow_name": "",
        "dependent_lists": []
      }
    ],

    "canvas": [
      {
        "content_source": "",
        "target_course": ""
      }
    ],

    "knowledge_repository": [
      {
        "source": "",
        "classification": ""
      }
    ]
  },

  "deployment_plan": {
    "existing_assets_to_reuse": [],
    "new_lists_required": [],
    "new_content_types_required": [],
    "migration_requirements": []
  }
}
""",

    context=[
        discovery_task,
        build_model_task
    ],

    agent=sharepoint_agent,

    output_file="outputs/models/sharepoint_schema.json"
)