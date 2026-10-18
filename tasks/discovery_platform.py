from crewai import Task

from agents.discovery import discovery_agent

discovery_task = Task(
    description="""
    Analyse the supplied repository and all available
    knowledge artefacts.

    Repository Knowledge:

    {knowledge}

    Treat the repository as evidence of the current
    Academic Knowledge Platform implementation.

    Analyse:

    - Parser outputs
    - SharePoint structures
    - Lists
    - Libraries
    - Metadata
    - Content Types
    - Power Automate flows
    - Azure Function integrations
    - Python services
    - Knowledge repository assets
    - TAS artefacts
    - LAP artefacts
    - Assessment artefacts
    - Validation artefacts
    - Governance artefacts
    - Continuous Improvement artefacts
    - Industry Engagement artefacts
    - Canvas artefacts

    Discover:

    - entities
    - relationships
    - business rules
    - workflows
    - integrations
    - governance controls
    - authority sources
    - knowledge assets
    - taxonomies
    - metadata structures
    - business capabilities

    Determine:

    - what exists
    - where it exists
    - who owns it
    - what consumes it
    - what depends upon it
    - what systems it integrates with

    Identify:

    - authoritative systems
    - source-of-truth locations
    - duplicated information
    - conflicting information
    - upstream dependencies
    - downstream dependencies
    - change propagation chains

    For every significant object identify:

    - name
    - type
    - source system
    - source artefact
    - ownership
    - authority level
    - consuming systems

    Classify findings as:

    - Confirmed
    - Strong Evidence
    - Inferred
    - Unknown

    Focus exclusively on reverse engineering and
    documenting the current implementation.

    Do not redesign the solution.

    Produce ONLY valid JSON.

    No markdown.
    No narrative report.
    No recommendations.
    """,

    expected_output="""
{
  "platform_capabilities": [
    {
      "name": "",
      "description": "",
      "confidence": "Confirmed|Strong Evidence|Inferred|Unknown"
    }
  ],

  "systems": [
    {
      "name": "",
      "type": "",
      "purpose": "",
      "owner": "",
      "authority_level": "",
      "confidence": "Confirmed|Strong Evidence|Inferred|Unknown"
    }
  ],

  "entities": [
    {
      "name": "",
      "type": "",
      "purpose": "",
      "owner": "",
      "authority_level": "",
      "source_system": "",
      "source_artefact": "",
      "consuming_systems": [],
      "confidence": "Confirmed|Strong Evidence|Inferred|Unknown"
    }
  ],

  "relationships": [
    {
      "source_entity": "",
      "target_entity": "",
      "relationship_type": "",
      "confidence": "Confirmed|Strong Evidence|Inferred|Unknown"
    }
  ],

  "business_rules": [
    {
      "rule": "",
      "source": "",
      "confidence": "Confirmed|Strong Evidence|Inferred|Unknown"
    }
  ],

  "workflows": [
    {
      "name": "",
      "workflow_type": "Business|Automation|Knowledge",
      "steps": [],
      "systems": [],
      "confidence": "Confirmed|Strong Evidence|Inferred|Unknown"
    }
  ],

  "integrations": [
    {
      "source_system": "",
      "target_system": "",
      "integration_type": "",
      "artefacts": [],
      "confidence": "Confirmed|Strong Evidence|Inferred|Unknown"
    }
  ],

  "authority_model": {
    "source_of_truth_systems": [
      {
        "entity": "",
        "system": ""
      }
    ],

    "derived_systems": [],

    "consumer_systems": []
  },

  "governance_controls": [
    {
      "control": "",
      "owner": "",
      "evidence_source": "",
      "confidence": "Confirmed|Strong Evidence|Inferred|Unknown"
    }
  ],

  "knowledge_assets": [
    {
      "name": "",
      "asset_type": "",
      "classification": "",
      "metadata": []
    }
  ],

  "taxonomies": [
    {
      "name": "",
      "terms": []
    }
  ],

  "metadata_structures": [
    {
      "entity": "",
      "fields": []
    }
  ],

  "dependencies": {
    "upstream": [
      {
        "entity": "",
        "depends_on": ""
      }
    ],

    "downstream": [
      {
        "entity": "",
        "consumed_by": ""
      }
    ],

    "change_propagation": [
      {
        "source_entity": "",
        "affected_entities": [],
        "impact": ""
      }
    ]
  },

  "evidence": [
    {
      "artefact": "",
      "finding": "",
      "classification": "Confirmed|Strong Evidence|Inferred|Unknown"
    }
  ],

  "unknowns": [
    {
      "area": "",
      "reason": ""
    }
  ]
}
""",

    agent=discovery_agent,

    output_file="outputs/models/discovery_inventory.json"
)
