from crewai import Task
from agents.flow_analyst import flow_agent

flow_analysis_task = Task(
    description="""
    Analyse the supplied Power Automate artefacts:

    - definition.json
    - connectionsMap.json
    - apisMap.json

    Repository Knowledge:

    {knowledge}

    OBJECTIVE

    Build an integration schema model which describes
    how information moves between systems.

    CRITICAL

    Model ENTITY TYPES, not records.

    Ignore:

    - sample rows
    - qualification instances
    - unit instances
    - example data

    Focus on:

    - systems
    - entities
    - relationships
    - integrations
    - data movement
    - transformation points

    Treat supplied artefacts as the authoritative
    source of integration evidence.

    Extract:

    - source systems
    - destination systems
    - connectors
    - triggers
    - actions
    - entities referenced
    - entities created
    - entities updated
    - entities deleted
    - transformation points
    - synchronization points
    - publishing points

    For every integration identify:

    - source system
    - target system
    - entity
    - operation
    - dependency

    For every entity identify:

    - system of record
    - producing systems
    - consuming systems

    Do not:

    - produce reports
    - assess risks
    - recommend changes
    - redesign solutions

    Produce machine-readable schema artefacts only.

    Output valid JSON only.
    """,

    expected_output="""
{
  "systems": [
    {
      "name": "",
      "type": "",
      "role": "source|target|both"
    }
  ],

  "entities": [
    {
      "name": "",
      "source_of_truth": "",
      "producing_systems": [],
      "consuming_systems": []
    }
  ],

  "integrations": [
    {
      "name": "",
      "source_system": "",
      "target_system": "",
      "connector": "",
      "trigger": "",
      "operation": "create|update|delete|read"
    }
  ],

  "entity_flows": [
    {
      "entity": "",
      "source_system": "",
      "target_system": "",
      "operation": ""
    }
  ],

  "transformations": [
    {
      "entity": "",
      "source_structure": "",
      "target_structure": ""
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

  "dependencies": [
    {
      "system": "",
      "depends_on": "",
      "reason": ""
    }
  ]
}
""",

    agent=flow_agent,

    output_file="outputs/schema/integration_schema.json"
)