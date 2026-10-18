from crewai import Task

from agents.sharepoint import sharepoint_agent

from tasks.build_model import build_model_task


sharepoint_task = Task(
    description="""
    Generate SharePoint Online deployment schema.

    Repository Knowledge:

    {knowledge}

    Inputs:

    - canonical_schema.json

    OBJECTIVE

    Convert the canonical platform schema into
    SharePoint implementation structures.

    The canonical schema is the source of truth.

    Do not perform:

    - governance analysis
    - compliance analysis
    - architecture analysis
    - discovery analysis

    Do not create new entities.

    Do not redesign the platform.

    Use the entities and relationships from the
    canonical schema exactly as defined.

    Generate SharePoint structures required for:

    - Academic Master Data
    - Qualification Management
    - Course Management
    - Unit Management
    - TAS Management
    - LAP Management
    - Assessment Management
    - Validation Management
    - Industry Engagement
    - Continuous Improvement
    - Governance Records

    For every entity generate:

    - list name
    - internal name
    - columns
    - content type
    - indexes

    For every relationship generate:

    - lookup fields
    - relationship behaviour
    - referential integrity requirements

    For document entities generate:

    - document libraries
    - associated content types
    - metadata columns

    Pay particular attention to:

    - Portfolio ownership
    - Team ownership
    - Qualification delivery ownership

    The platform should support:

    Qualification
        -> QualificationDelivery
            -> TAS
                -> LAP
                    -> Assessment

    Generate deployment-ready SharePoint schema.

    Output ONLY valid JSON.

    No markdown.
    No reports.
    No explanations.
    No recommendations.
    """,

    expected_output="""
{
  "solution_name": "",

  "lists": [
    {
      "name": "",
      "entity": "",
      "description": "",

      "columns": [
        {
          "internal_name": "",
          "display_name": "",
          "type": "",
          "required": true,
          "indexed": false,
          "unique": false
        }
      ]
    }
  ],

  "document_libraries": [
    {
      "name": "",
      "entity": "",
      "content_type": ""
    }
  ],

  "content_types": [
    {
      "name": "",
      "parent": "",
      "columns": []
    }
  ],

  "site_columns": [
    {
      "internal_name": "",
      "display_name": "",
      "type": ""
    }
  ],

  "lookup_relationships": [
    {
      "source_list": "",
      "source_column": "",
      "target_list": "",
      "target_column": "",
      "relationship_type": "1:1|1:M|M:M"
    }
  ],

  "managed_metadata": [
    {
      "term_set": "",
      "terms": []
    }
  ],

  "permission_model": [
    {
      "entity": "",
      "owner_group": "",
      "contributor_group": "",
      "reader_group": ""
    }
  ],

  "deployment_order": [
    "site_columns",
    "content_types",
    "lists",
    "lookup_relationships"
  ]
}
""",

    context=[
        build_model_task
    ],

    agent=sharepoint_agent,

    output_file="outputs/sharepoint/sharepoint_schema.json"
)