from crewai import Task
from agents.flow_analyst import flow_agent


flow_analysis_task = Task(
    description="""
    Extract integration schema definitions from
    Power Automate and integration artefacts.
    Knowledge Size:
    {knowledge_length} characters

    Repository Knowledge:

    {knowledge}

    OBJECTIVE

    Generate integration_schema.json.

    Recover how entities move between systems.

    CRITICAL

    Model ENTITY TYPES only.

    Never model:

    - records
    - examples
    - sample rows
    - qualification instances
    - unit instances
    - assessment instances

    Ignore business content.

    Focus only on:

    - systems
    - entities
    - integrations
    - dependencies
    - ownership
    - data movement

    PRIORITY OF EVIDENCE

    Priority 1:
    - Power Automate definitions
    - Parse JSON schemas
    - API definitions
    - Integration configurations

    Priority 2:
    - SharePoint lookup structures
    - Repository schemas

    Priority 3:
    - Sample records

    Sample records may only be used
    to validate data structures.

    They must never define entities.

    Extract:

    - systems
    - source systems
    - destination systems
    - entity ownership
    - source-of-truth systems
    - integration relationships
    - entity flows
    - dependencies

    For each entity identify:

    - source system
    - owning system
    - consuming systems

    For each integration identify:

    - source system
    - destination system
    - affected entity
    - operation

    Produce integration schema definitions only.

    Do not:

    - analyse governance
    - assess risks
    - write reports
    - write recommendations
    - redesign integrations

    Output ONLY valid JSON.
    Do not include:

    - markdown
    - explanations
    - code fences
    - commentary
    - headings
    - notes
    - recommendations

    The response must begin with:

    {

    and end with:

    }
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

  "entity_ownership": [
    {
      "entity": "",
      "source_of_truth": "",
      "owning_system": "",
      "consuming_systems": []
    }
  ],

  "entity_flows": [
    {
      "entity": "",
      "source_system": "",
      "target_system": "",
      "operation": "create|update|delete|read"
    }
  ],

  "integration_relationships": [
    {
      "source_system": "",
      "target_system": "",
      "entity": "",
      "operation": ""
    }
  ],

  "dependencies": [
    {
      "entity": "",
      "depends_on": []
    }
  ]
}
""",

    agent=flow_agent,

    output_file="outputs/schema/integration_schema.json",
    callback=lambda output: print(
        f"\nFlow Analysis Output Size: {len(str(output)):,} chars"
    )
)