from crewai import Task

from agents.python_dev import python_agent

from tasks.discovery_platform import discovery_task
from tasks.build_model import build_model_task
from tasks.build_sharepoint import sharepoint_task

build_parser_task = Task(
    description="""
    Build the canonical parser and ingestion specification
    for the Academic Knowledge Platform.

    Repository Knowledge:

    {knowledge}

    Use outputs from:

    - Discovery Analysis
    - Platform Model
    - SharePoint Schema

    Treat all existing parser code, extraction services,
    Azure Functions, normalization logic and ingestion
    components as evidence of the current implementation.
    
    Do not include examples, sample rows,
    unit names, qualification names or
    instance data unless required as evidence.

    The objective is to discover schema,
    relationships and metadata definitions.

    Determine:

    - what information must be extracted
    - where information originates
    - authoritative source systems
    - required metadata
    - required relationships
    - required validation logic
    - ingestion requirements
    - governance requirements
    - audit requirements
    - versioning requirements

    Evaluate information sources including:

    - Qualifications
    - Accredited Courses
    - Units
    - Clusters
    - TASs
    - LAPs
    - Assessment Plans
    - Assessment Mapping Matrices
    - Validation Records
    - Industry Consultation Records
    - Student Feedback
    - Employer Feedback
    - Continuous Improvement Records
    - Policies
    - Standards
    - Compliance Documentation
    - Training Package Data

    Identify:

    - extraction requirements
    - normalization requirements
    - enrichment requirements
    - entity mappings
    - data quality requirements
    - relationship generation requirements
    - SharePoint loading requirements
    - Knowledge Repository requirements

    Preserve existing working implementations where possible.

    Output ONLY valid JSON.

    No markdown.
    No narrative report.
    No explanations.
    """,

    expected_output="""
{
  "information_sources": [
    {
      "name": "",
      "source_type": "",
      "authority_level": "",
      "owner": "",
      "entities": []
    }
  ],

  "parser_requirements": [
    {
      "parser_name": "",
      "source_type": "",
      "responsibilities": [],
      "supported_entities": []
    }
  ],

  "entity_mappings": [
    {
      "source": "",
      "target_entity": "",
      "required_fields": [],
      "optional_fields": [],
      "relationships": []
    }
  ],

  "normalization_rules": [
    {
      "entity": "",
      "rule_type": "",
      "description": ""
    }
  ],

  "metadata_requirements": [
    {
      "entity": "",
      "field_name": "",
      "data_type": "",
      "required": true
    }
  ],

  "validation_rules": [
    {
      "entity": "",
      "field": "",
      "rule": "",
      "severity": "Error|Warning|Info"
    }
  ],

  "relationship_generation": [
    {
      "parent_entity": "",
      "child_entity": "",
      "relationship_type": "",
      "resolution_method": ""
    }
  ],

  "sharepoint_loading": {
    "lists": [
      {
        "list_name": "",
        "entity": "",
        "required_fields": []
      }
    ],
    "lookup_relationships": []
  },

  "knowledge_repository": {
    "knowledge_objects": [],
    "classifications": [],
    "metadata_requirements": []
  },

  "implementation_architecture": {
    "python_modules": [],
    "parser_classes": [],
    "services": [],
    "azure_functions": [],
    "api_endpoints": []
  },

  "code_validation": {
    "existing_components": [],
    "reusable_components": [],
    "missing_capabilities": [],
    "required_enhancements": []
  },

  "ingestion_pipeline": [
    {
      "step": "",
      "input": "",
      "output": ""
    }
  ]
}
""",

    context=[
        discovery_task,
        build_model_task,
        sharepoint_task
    ],

    agent=python_agent,

    output_file="outputs/models/parser_specification.json"
)