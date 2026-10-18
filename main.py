# main.py

from pathlib import Path
from datetime import datetime

from crew.academic_crew import crew
from repository import KnowledgeRepository


def create_output_folders():
    """Create standard output structure."""

    folders = [
        "outputs",
        "outputs/platform",
        "outputs/governance",
        "outputs/architecture",
        "outputs/sharepoint",
        "outputs/implementation",
        "outputs/review",
        "outputs/logs"
    ]

    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)


def main():

    create_output_folders()

    print("=" * 80)
    print("Academic Knowledge Platform")
    print("Crew Execution Started")
    print("=" * 80)

    repo = KnowledgeRepository()

    knowledge = repo.load()

    print("Knowledge Repository Loaded")
    print()

    result = crew.kickoff(
        inputs={
            "knowledge": knowledge,
            "project": """
            Build an Academic Knowledge Platform that:

            - Extracts information from TAS documents
            - Extracts information from LAP documents
            - Extracts information from Assessment Plans
            - Extracts information from Mapping Matrices
            - Extracts information from Validation Records
            - Extracts information from Industry Consultation
            - Extracts information from Student Feedback
            - Extracts information from Registration Standards 2025
            - Extracts information from TAC Guidance
            - Extracts information from TIWA Policies
            - Extracts information from Training Package Information

            The platform must:

            - Maintain a central source of truth
            - Support governance requirements
            - Support compliance requirements
            - Support auditability
            - Support version control
            - Support historical reconstruction
            - Support SharePoint Online
            - Support Power Automate
            - Support Knowledge Repository retrieval
            - Support Canvas publication
            - Support future CrewAI agents

            Information should be normalised,
            reusable and stored once wherever possible.
            """
        }
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    summary_file = (
        Path("outputs")
        / f"crew_summary_{timestamp}.md"
    )

    summary_file.write_text(
        str(result),
        encoding="utf-8"
    )

    print()
    print("=" * 80)
    print("Crew Execution Complete")
    print("=" * 80)
    print()
    print(f"Summary: {summary_file}")
    print()

    print(result)


if __name__ == "__main__":
    main()