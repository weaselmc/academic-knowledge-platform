# repository.py

from pathlib import Path
import json


class KnowledgeRepository:

    def __init__(self, data_path="data"):
        self.data_path = Path(data_path)

    def load(self):

        knowledge = {
            "schema_files": {},
            "sharepoint_files": {},
            "flow_files": {},
            "python_models": {},
            "documents": {},
            "other_files": {}
        }

        for file in self.data_path.rglob("*"):

            if not file.is_file():
                continue

            try:

                suffix = file.suffix.lower()

                # --------------------------------------------------
                # JSON
                # --------------------------------------------------

                if suffix == ".json":

                    raw = file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )

                    try:
                        content = json.loads(raw)
                    except Exception:
                        content = raw

                    lower_name = file.name.lower()

                    if any(
                        x in lower_name
                        for x in [
                            "schema",
                            "model",
                            "entity",
                            "definition"
                        ]
                    ):

                        knowledge["schema_files"][
                            str(file)
                        ] = content

                    elif any(
                        x in lower_name
                        for x in [
                            "sharepoint",
                            "list",
                            "column",
                            "contenttype"
                        ]
                    ):

                        knowledge["sharepoint_files"][
                            str(file)
                        ] = content

                    elif any(
                        x in lower_name
                        for x in [
                            "flow",
                            "powerautomate",
                            "logicapp",
                            "workflow"
                        ]
                    ):

                        knowledge["flow_files"][
                            str(file)
                        ] = content

                    else:

                        knowledge["other_files"][
                            str(file)
                        ] = content

                # --------------------------------------------------
                # PYTHON
                # --------------------------------------------------

                elif suffix == ".py":

                    text = file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )

                    # only keep likely schema models
                    if any(
                        pattern in text
                        for pattern in [
                            "BaseModel",
                            "@dataclass",
                            "TypedDict",
                            "Field(",
                            "class "
                        ]
                    ):

                        knowledge["python_models"][
                            str(file)
                        ] = text

                # --------------------------------------------------
                # DOCUMENTATION
                # --------------------------------------------------

                elif suffix in [".md", ".markdown"]:

                    knowledge["documents"][
                        str(file)
                    ] = file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )

                # --------------------------------------------------
                # YAML
                # --------------------------------------------------

                elif suffix in [".yaml", ".yml"]:

                    text = file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )

                    lower_name = file.name.lower()

                    if any(
                        x in lower_name
                        for x in [
                            "flow",
                            "workflow",
                            "logicapp"
                        ]
                    ):

                        knowledge["flow_files"][
                            str(file)
                        ] = text

                    else:

                        knowledge["documents"][
                            str(file)
                        ] = text

                # --------------------------------------------------
                # EVERYTHING ELSE
                # --------------------------------------------------

                else:

                    knowledge["other_files"][
                        str(file)
                    ] = {
                        "name": file.name,
                        "extension": suffix
                    }

            except Exception as ex:

                print(
                    f"Failed to load {file}: {ex}"
                )

        return knowledge

    def summary(self):

        knowledge = self.load()

        print("\nRepository Summary")
        print("-" * 50)

        for category, items in knowledge.items():
            print(
                f"{category}: {len(items)} artefacts"
            )

        return knowledge