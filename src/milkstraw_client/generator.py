from __future__ import annotations

import milkstraw_client
from milkstraw_client import APIClient


class Generator:
    def __init__(self, id: str, name: str, status: str):
        self.id = id
        self.name = name
        self.status = status

    def __repr__(self):
        return f"Generator(id='{self.id}', name='{self.name}', status='{self.status}')"

    @classmethod
    def get(cls, id: str) -> Generator:
        url = f"{milkstraw_client.edge_service_url}/generators/{id}"
        response = APIClient.request("get", url)
        return Generator(id=response["id"], name=response["name"], status=response["status"])

    @classmethod
    def list(cls) -> list[Generator]:
        url = f"{milkstraw_client.edge_service_url}/generators"
        response = APIClient.request("get", url)
        generators = [Generator(id=gen["id"], name=gen["name"], status=gen["status"]) for gen in response]
        return generators

    @classmethod
    def download(cls, id: str, file_path: str) -> str:
        url = f"{milkstraw_client.edge_service_url}/generators/download/{id}"
        response = APIClient.request("get", url, return_raw=True)
        with open(file_path, "w") as f:
            f.write(response)
        return file_path

    @classmethod
    def add(cls, name: str, records_num: str, file_path: str) -> Generator:
        url = f"{milkstraw_client.edge_service_url}/generators"
        params = {"name": name, "recordsNum": records_num}
        file_paths = {"file": file_path}
        response = APIClient.request("post", url, params=params, file_paths=file_paths)
        return Generator(id=response["id"], name=response["name"], status=response["status"])
