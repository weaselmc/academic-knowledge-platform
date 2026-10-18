from crewai import Task
from agents.flow_analyst import flow_agent

flow_analysis_task = Task(
    description="""
    Analyse the supplied Power Automate solution artefacts:

    - definition.json
    - connectionsMap.json
    - apisMap.json

    Repository Knowledge:

    {knowledge}

    Reverse engineer the existing automation implementation.

    Treat the supplied artefacts as the authoritative
    source of evidence.

    Model entity TYPES, not records.

    Do not include examples, sample rows,
    unit names, qualification names or
    instance data unless required as evidence.

    The objective is to discover schema,
    relationships and metadata definitions.

    Identify and extract:

    - flows
    - triggers
    - actions
    - connectors
    - SharePoint dependencies
    - Azure Function dependencies
    - external integrations
    - business rules
    - entity relationships
    - source systems
    - target systems
    - ownership boundaries
    - lifecycle events
    - governance controls

    Determine:

    - how information enters the platform
    - how information moves through the platform
    - how information is transformed
    - how information is synchronized
    - how information is published
    - which systems consume information
    - which systems produce information
    - where duplication exists
    - where governance controls exist
    - where governance controls are missing

    Identify change propagation paths.

    Example:

    Qualification
      -> Cluster
        -> Unit
          -> TAS
            -> LAP
              -> Canvas

    Extract automation metadata and relationships.

    Do not redesign the solution.

    Do not produce a narrative report.

    Output valid JSON only.

    No markdown.
    No explanations.
    No commentary.
    """,

    expected_output="""
{
  "flows": [
    {
      "name": "",
      "status": "",
      "trigger": {
        "type": "",
        "source": ""
      },
      "actions": [
        {
          "name": "",
          "type": "",
          "connector": ""
        }
      ]
    }
  ],

  "systems": [
    {
      "name": "",
      "role": "source|target|both"
    }
  ],

  "entities": [
    {
      "name": "",
      "owner": "",
      "source_of_truth": ""
    }
  ],

  "relationships": [
    {
      "source_entity": "",
      "target_entity": "",
      "relationship_type": ""
    }
  ],

  "transformations": [
    {
      "flow": "",
      "source": "",
      "target": "",
      "transformation": ""
    }
  ],

  "business_rules": [
    {
      "rule": "",
      "classification": "Confirmed|Strong Evidence|Inferred|Unknown",
      "evidence": ""
    }
  ],

  "dependencies": {
    "sharepoint": [],
    "azure_functions": [],
    "canvas": [],
    "external_integrations": []
  },

  "data_flows": [
    {
      "source_system": "",
      "target_system": "",
      "flow_name": "",
      "payload": ""
    }
  ],

  "change_propagation": [
    {
      "source_entity": "",
      "affected_entity": "",
      "impact": ""
    }
  ],

  "governance": {
    "ownership_boundaries": [],
    "existing_controls": [],
    "missing_controls": []
  },

  "risks": [
    {
      "risk": "",
      "severity": "Low|Medium|High",
      "description": ""
    }
  ],

  "technical_debt": [
    {
      "issue": "",
      "impact": ""
    }
  ],

  "unknowns": []
}
""",

    agent=flow_agent,

    output_file="outputs/models/automation_model.json"
)