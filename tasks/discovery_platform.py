from crewai import Task

from agents.discovery import discovery_agent


discovery_task = Task(
    description="""
    Analyse the repository and extract the existing
    platform schema.

    Repository Knowledge:

    {knowledge}

    OBJECTIVE

    Discover the current information model used by
    the Academic Knowledge Platform.

    CRITICAL

    Model ENTITY TYPES only.

    Do not model:

    - records
    - sample rows
    - qualification instances
    - unit instances
    - assessment instances
    - TAS instances
    - LAP instances

    Ignore example data.

    Focus on metadata and structure.

    Analyse:

    - SharePoint Lists
    - SharePoint Libraries
    - SharePoint Content Types
    - SharePoint Columns
    - Power Automate Definitions
    - Azure Functions
    - Python Parsers
    - Knowledge Repository Assets
    - TAS Artefacts
    - LAP Artefacts
    - Assessment Artefacts
    - Validation Artefacts
    - Governance Artefacts
    - Industry Engagement Artefacts

    Discover:

    - entity types
    - fields
    - field types
    - relationships
    - source systems
    - authority sources
    - metadata structures

    For each entity identify:

    - entity name
    - description
    - source system
    - source artefact
    - owner
    - authority level

    For each field identify:

    - field name
    - field type
    - required status

    For each relationship identify:

    - source entity
    - target entity
    - relationship type

    Produce machine-readable schema artefacts.

    Output ONLY valid JSON.

    No markdown.
    No reports.
    No recommendations.
    No commentary.
    """,

    expected_output="""
{
  "source_systems": [
    {
      "name": "",
      "type": "",
      "authority_level": ""
    }
  ],

  "entities": [
    {
      "name": "",
      "description": "",

      "source_system": "",

      "source_artefacts": [],

      "owner": "",

      "authority_level": "",

      "fields": [
        {
          "name": "",
          "type": "",
          "required": true
        }
      ]
    }
  ],

  "relationships": [
    {
      "source_entity": "",

      "target_entity": "",

      "relationship_type": "",

      "cardinality": ""
    }
  ],

  "metadata": [
    {
      "entity": "",

      "field": "",

      "purpose": ""
    }
  ],

  "document_types": [
    {
      "name": "",

      "related_entity": ""
    }
  ]
}
""",

    agent=discovery_agent,

    output_file="outputs/schema/discovered_schema.json"
)