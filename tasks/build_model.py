from crewai import Task

from agents.architect import architect

from tasks.discovery_platform import discovery_task
from tasks.compliance import compliance_task
from tasks.analyse_flows import flow_analysis_task


build_model_task = Task(
    description="""
    Build the Canonical Academic Knowledge Platform Schema.

    Repository Knowledge:

    {knowledge}

    Inputs:

    - discovered_schema.json
    - compliance_schema.json
    - integration_schema.json

    OBJECTIVE

    Generate the authoritative schema for the
    Academic Knowledge Platform.

    This schema will become the source of truth
    for all downstream generators.

    CRITICAL

    Model ENTITY TYPES.

    Do not model:

    - records
    - sample data
    - qualification instances
    - unit instances
    - assessment instances

    Ignore example values.

    The output must describe platform structure,
    not platform content.

    MERGE

    Discovery provides:

    - entities
    - fields
    - relationships
    - metadata

    Compliance provides:

    - mandatory entities
    - mandatory fields
    - audit requirements
    - governance requirements

    Integration provides:

    - system relationships
    - entity flows
    - source systems
    - destination systems

    GENERATE

    For each entity define:

    - schema name
    - description
    - source of truth
    - owner
    - primary key
    - fields
    - relationships
    - audit metadata

    For each field define:

    - field name
    - type
    - required
    - unique
    - default value
    - description

    For each relationship define:

    - source entity
    - target entity
    - cardinality
    - relationship type

    OUTPUT REQUIREMENTS

    The schema must be suitable for:

    - SharePoint list generation
    - Content type generation
    - Power Automate generation
    - Parser validation
    - Canvas publishing
    - Governance controls
    - Knowledge Repository storage

    Produce ONLY valid JSON.

    Do not output markdown.

    Do not output reports.

    Do not output recommendations.

    Do not output explanations.
    """,

    expected_output="""
{
  "schema_version": "",

  "entities": [
    {
      "name": "",
      "description": "",

      "owner": "",

      "source_of_truth": "",

      "primary_key": "",

      "audit_enabled": true,

      "fields": [
        {
          "name": "",
          "type": "string|number|boolean|date|datetime|lookup|choice|person",

          "required": true,

          "unique": false,

          "default_value": null,

          "description": ""
        }
      ]
    }
  ],

  "relationships": [
    {
      "source_entity": "",

      "target_entity": "",

      "relationship_type":
        "lookup|composition|aggregation|reference",

      "cardinality":
        "1:1|1:M|M:M"
    }
  ],

  "source_systems": [
    {
      "name": "",

      "authority_level": "",

      "entities": []
    }
  ],

  "audit_fields": [
    {
      "name": "",
      "type": ""
    }
  ],

  "ownership_fields": [
    {
      "name": "",
      "type": ""
    }
  ],

  "retention_fields": [
    {
      "name": "",
      "type": ""
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