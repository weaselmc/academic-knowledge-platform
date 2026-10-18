from crewai import Task

from agents.python_dev import python_agent

from tasks.build_model import build_model_task
from tasks.parser_mapping import parser_mapping_task


parser_code_task = Task(
    description="""
    Generate parser implementations.

    Inputs:

    - canonical_schema.json
    - parser_mapping.json

    OBJECTIVE

    Generate Python parser specifications
    that can be implemented directly.

    For every entity define:

    - parser class name
    - source type
    - extraction methods
    - normalization methods
    - validation methods

    Existing parser code should be reused
    wherever possible.

    Produce implementation-ready JSON.

    Do not produce reports.

    Output JSON only.
    """,

    context=[
        build_model_task,
        parser_mapping_task
    ],

    expected_output="""
{
  "parsers": [
    {
      "entity": "",
      "parser_class": "",
      "source_type": "",
      "input_documents": [],
      "methods": [
        "extract",
        "normalize",
        "validate",
        "map_relationships"
      ],
      "target_entity": ""
    }
  ]
}
""",

    agent=python_agent,

    output_file="outputs/generated/parser_generation_spec.json"
)