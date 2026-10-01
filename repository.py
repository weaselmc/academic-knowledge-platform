from pathlib import Path
import json

from crewai import knowledge


class KnowledgeRepository:

    def __init__(self, data_path="data"):
        self.data_path = Path(data_path)

    def load(self):

        knowledge = {
            "python_files": {},
            "json_files": {}
        }

        for file in self.data_path.rglob("*"):

            if file.suffix == ".py":

                knowledge["python_files"][file.name] = (
                    file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )
                )

            elif file.suffix == ".json":

                try:

                    knowledge["json_files"][file.name] = (
                        json.loads(
                            file.read_text(
                                encoding="utf-8",
                                errors="ignore"
                            )
                        )
                    )

                except Exception:

                    knowledge["json_files"][file.name] = (
                        file.read_text(
                            encoding="utf-8",
                            errors="ignore"
                        )
                    )
        
        return knowledge
                    
    def summary(self):

        knowledge = self.load()

        print(
            f"Parsers: {len(knowledge['parsers'])}"
        )

        print(
            f"Flows: {len(knowledge['flows'])}"
        )

        print(
            f"SharePoint: {len(knowledge['sharepoint'])}"
        )

        print(
            f"Other: {len(knowledge['other'])}"
        )