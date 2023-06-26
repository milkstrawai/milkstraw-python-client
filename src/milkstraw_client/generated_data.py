from __future__ import annotations

from typing import Optional

import milkstraw_client
from milkstraw_client import APIClient


class GeneratedData:
    def __init__(self, id: str, model: str, status: str):
        self.id = id
        self.model = model
        self.status = status

    def __repr__(self) -> str:
        attributes = ", ".join(f"{key}='{value}'" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attributes})"

    @staticmethod
    def generate(model: str, records_num: int, condition: Optional[dict] = None) -> GeneratedData:
        url = f"{milkstraw_client.edge_service_url}/generated-data/"
        json = {"modelId": model, "recordsNum": records_num}
        if condition is not None:
            json["condition"] = condition
        response = APIClient.request("post", url, json=json)
        return GeneratedData(**response)

    @staticmethod
    def get(id: str) -> GeneratedData:
        url = f"{milkstraw_client.edge_service_url}/generated-data/{id}"
        response = APIClient.request("get", url)
        return GeneratedData(**response)

    @staticmethod
    def list() -> list[GeneratedData]:
        url = f"{milkstraw_client.edge_service_url}/generated-data"
        response = APIClient.request("get", url)
        data = [GeneratedData(**data_dict) for data_dict in response]
        return data

    @staticmethod
    def download(id: str, file_path: str) -> str:
        url = f"{milkstraw_client.edge_service_url}/generated-data/download/{id}"
        return APIClient.download_file(file_path, url)

    @staticmethod
    def download_report(id: str, file_path: str) -> str:
        url = f"{milkstraw_client.edge_service_url}/generated-data/download/report/{id}"
        return APIClient.download_file(file_path, url)
