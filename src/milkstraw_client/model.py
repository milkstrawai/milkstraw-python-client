from __future__ import annotations

import milkstraw_client
from milkstraw_client import APIClient


class Model:
    def __init__(self, id: str, name: str, status: str, dataset: str):
        self.id = id
        self.name = name
        self.status = status
        self.dataset = dataset

    def __repr__(self) -> str:
        attributes = ", ".join(f"{key}='{value}'" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attributes})"

    @staticmethod
    def create(name: str, dataset: str) -> Model:
        url = f"{milkstraw_client.edge_service_url}/models/"
        json = {"name": name, "datasetId": dataset}
        response = APIClient.request("post", url, json=json)
        return Model(**response)

    @staticmethod
    def get(id: str) -> Model:
        url = f"{milkstraw_client.edge_service_url}/models/{id}"
        response = APIClient.request("get", url)
        return Model(**response)

    @staticmethod
    def list() -> list[Model]:
        url = f"{milkstraw_client.edge_service_url}/models"
        response = APIClient.request("get", url)
        models = [Model(**model_dict) for model_dict in response]
        return models
