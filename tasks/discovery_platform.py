from crewai import Task

from agents.discovery import discovery_agent


discovery_task = Task(
    description="""
    Extract schema definitions from repository knowledge.

    Repository Knowledge:

    {knowledge}

    OBJECTIVE

    Generate discovered_schema.json.

    Recover the platform information model.

    CRITICAL

    Model ENTITY TYPES only.

    Never model:

    - records
    - sample rows
    - example values
    - qualification instances
    - unit instances
    - assessment instances
    - TAS instances
    - LAP instances

    PRIORITY OF EVIDENCE

    Priority 1:
    - JSON schemas
    - Parse JSON definitions
    - Schema files
    - Dataclasses
    - Pydantic models

    Priority 2:
    - SharePoint column definitions
    - SharePoint content types
    - SharePoint lookup fields

    Priority 3:
    - Power Automate definitions
    - Integration definitions

    Priority 4:
    - Sample records

    Sample records may ONLY be used
    to validate field types.

    They must never define entities.

    Extract:

    - entities
    - fields
    - primary keys
    - business keys
    - relationships
    - source systems

    For each entity identify:

    - entity name
    - source system
    - source artefact

    For each field identify:

    - field name
    - field type
    - required status

    For each relationship identify:

    - source entity
    - target entity
    - relationship type
    - cardinality

    Produce schema definitions only.

    Do not:

    - analyse governance
    - analyse compliance
    - analyse workflows
    - write reports
    - write summaries
    - create recommendations

    Output valid JSON only.
    """,

    expected_output="""
{
  "source_systems": [
    {
      "name": "",
      "type": ""
    }
  ],

  "entities": [
    {
      "name": "",
      "source_system": "",
      "source_artefacts": [],

      "primary_key": "",

      "business_keys": [],

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
  ]
}
""",

    agent=discovery_agent,

    output_file="outputs/schema/discovered_schema.json"
)