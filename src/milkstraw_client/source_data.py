from __future__ import annotations

import milkstraw_client
from milkstraw_client import APIClient


class SourceData:
    def __init__(self, id: str, name: str, status: str):
        self.id = id
        self.name = name
        self.status = status

    def __repr__(self) -> str:
        attributes = ", ".join(f"{key}='{value}'" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attributes})"

    @staticmethod
    def upload(name: str, file_path: str) -> SourceData:
        url = f"{milkstraw_client.edge_service_url}/source-data/"
        params = {"name": name}
        file_paths = {"file": file_path}
        response = APIClient.request("post", url, params=params, file_paths=file_paths)
        return SourceData(**response)

    @staticmethod
    def get(id: str) -> SourceData:
        url = f"{milkstraw_client.edge_service_url}/source-data/{id}"
        response = APIClient.request("get", url)
        return SourceData(**response)

    @staticmethod
    def list() -> list[SourceData]:
        url = f"{milkstraw_client.edge_service_url}/source-data"
        response = APIClient.request("get", url)
        data = [SourceData(**data_dict) for data_dict in response]
        return data

    @staticmethod
    def download(id: str, file_path: str) -> str:
        url = f"{milkstraw_client.edge_service_url}/source-data/download/{id}"
        return APIClient.download_file(file_path, url)
