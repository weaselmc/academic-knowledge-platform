from crewai import Task

from agents.sharepoint import sharepoint_agent

from tasks.build_model import build_model_task


sharepoint_task = Task(
    description="""
Generate a SharePoint deployment schema.

The canonical schema provided by the previous task is the authoritative source.

INPUT

- canonical_schema.json (from task context)

OBJECTIVE

Transform the canonical schema into
SharePoint Online deployment structures.

Use the canonical schema exactly as defined.

CRITICAL

Do not:

- redesign entities
- redesign relationships
- create new entities
- infer additional entities
- perform architecture analysis
- perform governance analysis
- perform compliance analysis
- write recommendations
- write reports

Generate deployable SharePoint structures only.

Before generating output verify:

- entities are present
- fields are present
- relationships are present

For every entity generate:

- list definition
- internal list name
- display name
- columns
- content type
- indexes

For every field generate:

- SharePoint field type
- internal name
- display name
- required flag
- indexed flag
- unique flag

For every relationship generate:

- lookup columns
- lookup targets
- relationship behaviour

For document entities generate:

- document libraries
- metadata columns
- content types

The generated schema must support:

- SharePoint Online
- Microsoft Graph provisioning
- PnP PowerShell provisioning
- Power Automate
- Canvas integration

OUTPUT RULES

Use only entities, fields and relationships
defined in the canonical schema.

Do not invent new structures.

Produce deployment-ready definitions only.

Output ONLY valid JSON.

No markdown.
No reports.
No commentary.
No explanations.
""",

    expected_output="""
{
  "site_name": "",

  "lists": [
    {
      "entity": "",
      "internal_name": "",
      "display_name": "",

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
      "entity": "",
      "internal_name": "",
      "display_name": "",
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

  "lookup_relationships": [
    {
      "source_list": "",
      "source_column": "",
      "target_list": "",
      "target_column": "",
      "cardinality": ""
    }
  ],

  "indexes": [
    {
      "list": "",
      "columns": []
    }
  ]
}
""",

    context=[
        build_model_task
    ],

    agent=sharepoint_agent,

    output_file="outputs/sharepoint/sharepoint_schema.json"
)