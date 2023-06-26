from __future__ import annotations

from typing import Optional

import milkstraw_client
from milkstraw_client import APIClient


class Model:
    def __init__(self, id: str, name: str, status: str, source_data: str):
        self.id = id
        self.name = name
        self.status = status
        self.source_data = source_data

    def __repr__(self) -> str:
        attributes = ", ".join(f"{key}='{value}'" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attributes})"

    @staticmethod
    def create(name: str, source_data: str, anonymize_personal_info: Optional[bool] = None) -> Model:
        url = f"{milkstraw_client.edge_service_url}/models/"
        json = {"name": name, "sourceDataId": source_data}
        if anonymize_personal_info is not None:
            json["anonymizePersonalInfo"] = anonymize_personal_info
        response = APIClient.request("post", url, json=json)
        return Model.__parse_dict(response)

    @staticmethod
    def get(id: str) -> Model:
        url = f"{milkstraw_client.edge_service_url}/models/{id}"
        response = APIClient.request("get", url)
        return Model.__parse_dict(response)

    @staticmethod
    def list() -> list[Model]:
        url = f"{milkstraw_client.edge_service_url}/models"
        response = APIClient.request("get", url)
        models = [Model.__parse_dict(model_dict) for model_dict in response]
        return models

    @staticmethod
    def __parse_dict(model_dict: dict[str, str]) -> Model:
        return Model(
            id=model_dict["id"],
            name=model_dict["name"],
            status=model_dict["status"],
            source_data=model_dict["sourceData"],
        )
