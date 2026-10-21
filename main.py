# main.py

from pathlib import Path
from datetime import datetime
import json

from crew.academic_crew import crew
from repository import KnowledgeRepository


def create_output_folders():
    """Create output folder structure."""

    folders = [
        "outputs",
        "outputs/schema",
        "outputs/sharepoint",
        "outputs/parser",
        "outputs/generated",
        "outputs/logs"
    ]

    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)


def main():

    create_output_folders()

    print("=" * 80)
    print("Academic Platform Schema Generator")
    print("=" * 80)
    print()

    repo = KnowledgeRepository()

    print("Loading knowledge repository...")
    knowledge = repo.load()

    knowledge_text = json.dumps(
        knowledge,
        default=str,
        indent=2
    )

    print(f"Knowledge size: {len(knowledge_text):,} chars")

    # Build inputs FIRST
    inputs = {
        "knowledge": knowledge,
        "knowledge_length": len(knowledge_text),
        "objective": """
Reverse engineer the existing Academic Platform.

Produce machine-readable schema artefacts.

Model entity TYPES only.

Do not model sample records.

Required outputs:

1. discovered_schema.json
2. compliance_schema.json
3. integration_schema.json
4. canonical_schema.json
5. sharepoint_schema.json
6. parser_mapping.json

The canonical schema must define:

- entities
- fields
- data types
- relationships
- authority sources
- ownership
- metadata

The SharePoint schema must define:

- lists
- columns
- lookups
- content types

The parser mapping must define:

- source systems
- required fields
- validation requirements
- relationship mappings

All outputs must be valid JSON.

Outputs must be implementation-ready.

No reports.
No recommendations.
No markdown unless explicitly requested.
"""
    }

    # Debugging
    print("\n=== INPUT DEBUG ===")
    print(f"knowledge present: {'knowledge' in inputs}")
    print(f"knowledge_length present: {'knowledge_length' in inputs}")
    print(f"objective present: {'objective' in inputs}")

    for key, value in inputs.items():

        if isinstance(value, str):
            print(f"{key}: {len(value):,} chars")

        else:
            print(f"{key}: {type(value).__name__}")

    print("===================\n")

    try:

        result = crew.kickoff(inputs=inputs)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        summary_file = (
            Path("outputs")
            / "logs"
            / f"execution_summary_{timestamp}.txt"
        )

        summary_file.write_text(
            str(result),
            encoding="utf-8"
        )

        print()
        print("=" * 80)
        print("Schema Generation Complete")
        print("=" * 80)
        print()
        print(f"Summary: {summary_file}")
        print()
        print(result)

    except Exception as ex:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        error_file = (
            Path("outputs")
            / "logs"
            / f"error_{timestamp}.log"
        )

        error_file.write_text(
            str(ex),
            encoding="utf-8"
        )

        print()
        print("=" * 80)
        print("EXECUTION FAILED")
        print("=" * 80)
        print(ex)
        print(f"\nError log written to: {error_file}")


if __name__ == "__main__":
    main()