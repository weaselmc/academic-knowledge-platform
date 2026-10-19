from crewai import Task

from agents.architect import architect

from tasks.discovery_platform import discovery_task
from tasks.compliance import compliance_task
from tasks.analyse_flows import flow_analysis_task


build_model_task = Task(
    description="""
    Generate the canonical Academic Knowledge Platform schema.

    Repository Knowledge:

    {knowledge}

    Inputs:

    - discovered_schema.json
    - compliance_schema.json
    - integration_schema.json

    OBJECTIVE

    Merge all discovered schema information into
    a single canonical schema.

    This schema becomes the authoritative source
    for:

    - SharePoint schema generation
    - Parser generation
    - Validation generation
    - Power Automate generation
    - Canvas integration
    - Knowledge Repository storage

    CRITICAL

    Model ENTITY TYPES only.

    Never model:

    - records
    - sample rows
    - example values
    - qualification instances
    - unit instances
    - assessment instances

    Ignore operational data.

    Focus exclusively on structure.

    MERGE

    Discovery contributes:

    - entities
    - fields
    - data types
    - relationships

    Compliance contributes:

    - mandatory entities
    - mandatory fields
    - audit metadata
    - ownership metadata
    - approval metadata
    - retention metadata

    Integration contributes:

    - source systems
    - consuming systems
    - entity flows
    - integration relationships

    NORMALISE

    Ensure:

    - entities are unique
    - field names are consistent
    - duplicate fields are removed
    - duplicate entities are merged
    - relationships are normalized
    - metadata is reusable

    GENERATE

    For every entity define:

    - entity name
    - primary key
    - business keys
    - fields

    For every field define:

    - name
    - type
    - required
    - unique

    For every relationship define:

    - source entity
    - target entity
    - relationship type
    - cardinality

    Output schema definitions only.

    Do not generate:

    - reports
    - architecture documents
    - recommendations
    - commentary
    - implementation plans

    Output ONLY valid JSON.
    """,

    expected_output="""
{
  "schema_version": "",

  "entities": [
    {
      "name": "",

      "primary_key": "",

      "business_keys": [],

      "fields": [
        {
          "name": "",
          "type": "",
          "required": true,
          "unique": false
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

  "source_systems": [
    {
      "name": "",
      "entities": []
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
  ]
}
""",

    context=[
        discovery_task,
        compliance_task,
        flow_analysis_task
    ],

    agent=architect,

    output_file="outputs/schema/canonical_schema.json"
)