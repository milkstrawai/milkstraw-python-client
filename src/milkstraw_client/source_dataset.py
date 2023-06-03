from __future__ import annotations

import milkstraw_client
from milkstraw_client import APIClient


class SourceDataset:
    def __init__(self, id: str, name: str, status: str):
        self.id = id
        self.name = name
        self.status = status

    def __repr__(self) -> str:
        attributes = ", ".join(f"{key}='{value}'" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attributes})"

    @staticmethod
    def upload(name: str, file_path: str) -> SourceDataset:
        url = f"{milkstraw_client.edge_service_url}/datasets/"
        params = {"name": name}
        file_paths = {"file": file_path}
        response = APIClient.request("post", url, params=params, file_paths=file_paths)
        return SourceDataset(**response)

    @staticmethod
    def get(id: str) -> SourceDataset:
        url = f"{milkstraw_client.edge_service_url}/datasets/{id}"
        response = APIClient.request("get", url)
        return SourceDataset(**response)

    @staticmethod
    def list() -> list[SourceDataset]:
        url = f"{milkstraw_client.edge_service_url}/datasets"
        response = APIClient.request("get", url)
        datasets = [SourceDataset(**dataset_dict) for dataset_dict in response]
        return datasets

    @staticmethod
    def download(id: str, file_path: str) -> str:
        url = f"{milkstraw_client.edge_service_url}/datasets/download/{id}"
        response = APIClient.request("get", url, return_raw=True)
        with open(file_path, "w") as f:
            f.write(response)
        return file_path
