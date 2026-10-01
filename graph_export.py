from pathlib import Path
import json
import requests

from azure.identity import InteractiveBrowserCredential


SITE_URL = "tafewa.sharepoint.com:/sites/NMT_IntegratedTechnologies_Teams"

OUTPUT_DIR = Path("data/sharepoint")


class GraphExporter:
    def __init__(self):
        self.credential = InteractiveBrowserCredential()

        self.token = self.credential.get_token(
            "https://graph.microsoft.com/.default"
        ).token

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get(self, url):
        response = requests.get(
            url,
            headers=self.headers
        )

        response.raise_for_status()

        return response.json()

    def get_site(self):

        url = (
            f"https://graph.microsoft.com/v1.0/sites/"
            f"{SITE_URL}"
        )

        return self.get(url)

    def get_lists(self, site_id):

        url = (
            f"https://graph.microsoft.com/v1.0/sites/"
            f"{site_id}/lists"
        )

        return self.get(url)["value"]

    def get_columns(self, site_id, list_id):

        url = (
            f"https://graph.microsoft.com/v1.0/sites/"
            f"{site_id}/lists/{list_id}/columns"
        )

        return self.get(url)["value"]

    def get_items(self, site_id, list_id, top=10):

        url = (
            f"https://graph.microsoft.com/v1.0/sites/"
            f"{site_id}/lists/{list_id}/items"
            f"?expand=fields"
            f"&$top={top}"
        )

        return self.get(url)["value"]

    def export(self):

        OUTPUT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        site = self.get_site()

        print(f"Site: {site['displayName']}")

        site_id = site["id"]

        lists = self.get_lists(site_id)

        master_schema = []

        for lst in lists:

            list_name = lst["displayName"]

            if lst.get("system"):
                continue

            print(f"Exporting {list_name}")

            columns = self.get_columns(
                site_id,
                lst["id"]
            )

            try:
                items = self.get_items(
                    site_id,
                    lst["id"]
                )
            except Exception:
                items = []

            schema = {
                "list_id": lst["id"],
                "list_name": list_name,
                "description": lst.get(
                    "description"
                ),
                "columns": [],
                "sample_items": items
            }

            for col in columns:

                schema["columns"].append(
                    {
                        "id": col.get("id"),
                        "name": col.get("name"),
                        "display_name": col.get(
                            "displayName"
                        ),
                        "required": col.get(
                            "required"
                        ),
                        "read_only": col.get(
                            "readOnly"
                        ),
                        "hidden": col.get(
                            "hidden"
                        ),
                        "column_type": list(
                            set(
                                col.keys()
                            )
                            - {
                                "id",
                                "name",
                                "displayName",
                                "required",
                                "readOnly",
                                "hidden"
                            }
                        )
                    }
                )

            master_schema.append(schema)

            output_file = (
                OUTPUT_DIR /
                f"{list_name}.json"
            )

            with open(
                output_file,
                "w",
                encoding="utf-8"
            ) as f:
                json.dump(
                    schema,
                    f,
                    indent=2,
                    ensure_ascii=False
                )

        with open(
            OUTPUT_DIR /
            "sharepoint_schema.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                master_schema,
                f,
                indent=2,
                ensure_ascii=False
            )

        print(
            f"Exported {len(master_schema)} lists"
        )


if __name__ == "__main__":
    GraphExporter().export()