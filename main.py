# main.py

from crew.academic_crew import crew
from repository import KnowledgeRepository

repo = KnowledgeRepository()

knowledge = repo.load()

# print("Knowledge loaded")
# print("=" * 50)

# for category, files in knowledge.items():
#     print(f"\n{category}")

#     if isinstance(files, dict):
#         print(f"Count: {len(files)}")

#         for name in files.keys():
#             print(f"  - {name}")

# print("Knowledge loaded:")
# print(knowledge.keys())

result = crew.kickoff(
    inputs={
        "knowledge": knowledge,
        "project": """
        Build an academic platform that extracts
        information from:

        - TAS
        - LAP
        - Assessment Plans
        - Validation Records
        - Registration Standards 2025
        - TAC Guidance
        - TIWA Policies
        - Training Package Information

        and stores all information in a
        normalized central academic model.
        """
    }
)

from pathlib import Path

Path("outputs").mkdir(
exist_ok=True
)

with open(
    "outputs/result.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(str(result))

print(result)