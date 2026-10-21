from crewai import Task

from agents.governance import governance_agent

from tasks.discovery_platform import discovery_task


compliance_task = Task(
    description="""
Generate compliance schema requirements.

DEBUG INFORMATION

Knowledge Length:
{knowledge_length}

Repository Knowledge:

{knowledge}

INPUT

- discovered_schema.json

OBJECTIVE

Identify additional schema requirements that must
exist to satisfy compliance, governance,
auditability and evidence requirements.

The output will be merged into:

- canonical_schema.json

CRITICAL

Before generating compliance requirements:

1. Verify repository knowledge was received.
2. Verify repository knowledge is not empty.
3. Verify discovery_task output was received.
4. Count discovered entities.
5. Count discovered relationships.
6. Count discovered fields.
7. Record any validation failures.

Model ENTITY TYPES only.

Never model:

- records
- sample rows
- example values
- qualification instances
- unit instances
- assessment instances

Ignore operational data.

Focus only on:

- entities
- fields
- relationships
- metadata
- auditability
- ownership
- evidence

Use repository artefacts as evidence.

Determine:

- mandatory entities
- mandatory fields
- mandatory relationships
- audit metadata
- ownership metadata
- approval metadata
- retention metadata
- evidence metadata

Do not analyse gaps.

Do not assess maturity.

Do not write recommendations.

Do not write reports.

Generate schema requirements only.

Output valid JSON only.
""",

    context=[
        discovery_task
    ],

    expected_output="""
{
  "debug": {
    "knowledge_received": true,
    "knowledge_length": 0,
    "discovered_entity_count": 0,
    "discovered_relationship_count": 0,
    "discovered_field_count": 0,
    "validation_errors": []
  },

  "required_entities": [
    {
      "name": "",
      "classification": "mandatory|required|recommended|optional"
    }
  ],

  "required_fields": [
    {
      "entity": "",
      "field_name": "",
      "field_type": "",
      "required": true
    }
  ],

  "required_relationships": [
    {
      "source_entity": "",
      "target_entity": "",
      "relationship_type": ""
    }
  ],

  "audit_metadata": [
    {
      "field_name": "",
      "field_type": ""
    }
  ],

  "ownership_metadata": [
    {
      "field_name": "",
      "field_type": ""
    }
  ],

  "approval_metadata": [
    {
      "field_name": "",
      "field_type": ""
    }
  ],

  "retention_metadata": [
    {
      "field_name": "",
      "field_type": ""
    }
  ],

  "evidence_metadata": [
    {
      "entity": "",
      "field_name": "",
      "field_type": ""
    }
  ]
}
""",

    agent=governance_agent,

    output_file="outputs/schema/compliance_schema.json"
)