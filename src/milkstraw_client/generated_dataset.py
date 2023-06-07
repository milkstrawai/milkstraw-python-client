from __future__ import annotations

import milkstraw_client
from milkstraw_client import APIClient


class GeneratedDataset:
    def __init__(self, id: str, model: str, status: str):
        self.id = id
        self.model = model
        self.status = status

    def __repr__(self) -> str:
        attributes = ", ".join(f"{key}='{value}'" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attributes})"

    @staticmethod
    def generate(model: str, records_num: int) -> GeneratedDataset:
        url = f"{milkstraw_client.edge_service_url}/data/"
        json = {"modelId": model, "recordsNum": records_num}
        response = APIClient.request("post", url, json=json)
        return GeneratedDataset(**response)

    @staticmethod
    def get(id: str) -> GeneratedDataset:
        url = f"{milkstraw_client.edge_service_url}/data/{id}"
        response = APIClient.request("get", url)
        return GeneratedDataset(**response)

    @staticmethod
    def list() -> list[GeneratedDataset]:
        url = f"{milkstraw_client.edge_service_url}/data"
        response = APIClient.request("get", url)
        datasets = [GeneratedDataset(**dataset_dict) for dataset_dict in response]
        return datasets

    @staticmethod
    def download(id: str, file_path: str) -> str:
        url = f"{milkstraw_client.edge_service_url}/data/download/{id}"
        response = APIClient.request("get", url, return_raw=True)
        with open(file_path, "w") as f:
            f.write(response)
        return file_path
