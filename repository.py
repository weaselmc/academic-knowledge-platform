from pathlib import Path
import json


class KnowledgeRepository:

    def __init__(self, data_path="data"):
        self.data_path = Path(data_path)

    def _extract_parse_json_schemas(self, content):

        schemas = {}

        try:

            actions = (
                content
                .get("properties", {})
                .get("definition", {})
                .get("actions", {})
            )

            for action_name, action in actions.items():

                if (
                    isinstance(action, dict)
                    and action.get("type") == "ParseJson"
                ):

                    schema = (
                        action
                        .get("inputs", {})
                        .get("schema")
                    )

                    if schema:
                        schemas[action_name] = schema

        except Exception:
            pass

        return schemas

    def _is_sharepoint_schema(self, content):

        if not isinstance(content, dict):
            return False

        sharepoint_keys = [
            "list_name",
            "listName",
            "sharepoint_column",
            "lookupList",
            "lookupField",
            "columns",
            "fields"
        ]

        return any(
            key in content
            for key in sharepoint_keys
        )

    def _is_python_model(self, text):

        return any(
            token in text
            for token in [
                "BaseModel",
                "@dataclass",
                "TypedDict"
            ]
        )

    def load(self):

        knowledge = {
            "schemas": {},
            "sharepoint": {},
            "models": {}
        }

        for file in self.data_path.rglob("*"):

            if not file.is_file():
                continue

            try:

                suffix = file.suffix.lower()

                # ==========================================
                # JSON FILES
                # ==========================================

                if suffix == ".json":

                    try:

                        content = json.loads(
                            file.read_text(
                                encoding="utf-8",
                                errors="ignore"
                            )
                        )

                    except Exception:
                        continue

                    # Power Automate Parse JSON schemas

                    parse_schemas = (
                        self._extract_parse_json_schemas(
                            content
                        )
                    )

                    if parse_schemas:

                        knowledge["schemas"][
                            str(file)
                        ] = parse_schemas

                        continue

                    # SharePoint list definitions

                    if self._is_sharepoint_schema(content):

                        knowledge["sharepoint"][
                            str(file)
                        ] = content

                        continue

                    # Generic JSON schema

                    if (
                        isinstance(content, dict)
                        and "properties" in content
                    ):

                        knowledge["schemas"][
                            str(file)
                        ] = content

                # ==========================================
                # PYTHON MODELS
                # ==========================================

                elif suffix == ".py":

                    text = file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )

                    if self._is_python_model(text):

                        knowledge["models"][
                            str(file)
                        ] = text

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