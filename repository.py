# repository.py

from pathlib import Path
import json


class KnowledgeRepository:

    def __init__(self, data_path="data"):
        self.data_path = Path(data_path)

    def load(self):

        knowledge = {
            "python_files": {},
            "json_files": {},
            "markdown_files": {},
            "yaml_files": {},
            "other_files": {}
        }

        for file in self.data_path.rglob("*"):

            if not file.is_file():
                continue

            try:

                if file.suffix.lower() == ".py":

                    knowledge["python_files"][str(file)] = (
                        file.read_text(
                            encoding="utf-8",
                            errors="ignore"
                        )
                    )

                elif file.suffix.lower() == ".json":

                    try:

                        knowledge["json_files"][str(file)] = (
                            json.loads(
                                file.read_text(
                                    encoding="utf-8",
                                    errors="ignore"
                                )
                            )
                        )

                    except Exception:

                        knowledge["json_files"][str(file)] = (
                            file.read_text(
                                encoding="utf-8",
                                errors="ignore"
                            )
                        )

                elif file.suffix.lower() in [".md", ".markdown"]:

                    knowledge["markdown_files"][str(file)] = (
                        file.read_text(
                            encoding="utf-8",
                            errors="ignore"
                        )
                    )

                elif file.suffix.lower() in [".yaml", ".yml"]:

                    knowledge["yaml_files"][str(file)] = (
                        file.read_text(
                            encoding="utf-8",
                            errors="ignore"
                        )
                    )

                else:

                    knowledge["other_files"][str(file)] = {
                        "name": file.name,
                        "extension": file.suffix
                    }

            except Exception as ex:

                print(f"Failed to load {file}: {ex}")

        return knowledge

    def summary(self):

        knowledge = self.load()

        