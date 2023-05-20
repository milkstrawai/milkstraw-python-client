from __future__ import annotations

import milkstraw_client
from milkstraw_client import APIClient


class Generator:
    def __init__(
        self,
        id: str,
        name: str,
        status: str,
        user_id: str,
        original_data: str,
        generated_data: str,
        records_num: int,
    ):
        self.id = id
        self.name = name
        self.status = status
        self.user_id = user_id
        self.original_data = original_data
        self.generated_data = generated_data
        self.records_num = records_num

    def __repr__(self):
        return f"Generator(id='{self.id}', name='{self.name}', status='{self.status}')"

    @classmethod
    def get(cls, id: str) -> Generator:
        url = f"{milkstraw_client.edge_service_url}/generators/{id}"
        response = APIClient.request("get", url)
        return Generator(
            id=response["_id"],
            name=response["name"],
            status=response["status"],
            user_id=response["UserId"],
            original_data=response["originalData"],
            generated_data=response["generatedData"],
            records_num=response["recordsNum"],
        )

    @classmethod
    def list(cls) -> list[Generator]:
        url = f"{milkstraw_client.edge_service_url}/generators"
        response = APIClient.request("get", url)
        generators = [
            Generator(
                id=generator["_id"],
                name=generator["name"],
                status=generator["status"],
                user_id=generator["UserId"],
                original_data=generator["originalData"],
                generated_data=generator["generatedData"],
                records_num=generator["recordsNum"],
            )
            for generator in response
        ]
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
        return Generator(
            id=response["_id"],
            name=response["name"],
            status=response["status"],
            user_id=response["UserId"],
            original_data=response["originalData"],
            generated_data=response["generatedData"],
            records_num=response["recordsNum"],
        )
