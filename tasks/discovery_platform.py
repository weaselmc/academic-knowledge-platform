from crewai import Task

from agents.discovery import discovery_agent


discovery_task = Task(
    description="""
Extract schema definitions from repository knowledge.

DEBUG INFORMATION

Knowledge Length:
{knowledge_length}

Repository Knowledge:

{knowledge}

OBJECTIVE

Generate discovered_schema.json.

Recover the platform information model.

DEBUG REQUIREMENTS

Before producing the schema:

1. Verify knowledge was received.
2. Verify knowledge is not empty.
3. Identify source artefacts found.
4. Count discovered entities.
5. Count discovered fields.
6. Count discovered relationships.
7. Record any validation or extraction errors.

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
  "debug": {
    "knowledge_received": true,
    "knowledge_length": 0,
    "entity_count": 0,
    "field_count": 0,
    "relationship_count": 0,
    "source_artefacts_detected": [],
    "validation_errors": []
  },

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