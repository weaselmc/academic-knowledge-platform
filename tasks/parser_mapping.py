from crewai import Task

from agents.python_dev import python_agent

from tasks.build_model import build_model_task
from tasks.build_sharepoint import sharepoint_task


parser_mapping_task = Task(
    description="""
    Generate parser mappings from the canonical schema.

    Inputs:

    - canonical_schema.json
    - sharepoint_schema.json

    OBJECTIVE

    Define the extraction requirements needed
    to populate all platform entities.

    Model entity TYPES.

    Do not model records.

    For every entity identify:

    - source systems
    - source documents
    - required fields
    - optional fields
    - validation rules
    - relationship mappings

    Define the information required by
    downstream parser generators.

    Produce valid JSON only.
    """,

    context=[
        build_model_task,
        sharepoint_task
    ],

    expected_output="""
{
  "entities": [
    {
      "entity": "",
      "source_systems": [],
      "source_documents": [],
      "required_fields": [],
      "optional_fields": [],
      "validation_rules": [],
      "relationship_mappings": []
    }
  ]
}
""",

    agent=python_agent,

    output_file="outputs/parser/parser_mapping.json"
)