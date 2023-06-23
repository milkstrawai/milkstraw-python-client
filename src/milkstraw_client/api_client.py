from __future__ import annotations

from typing import Union

import requests
from requests.exceptions import HTTPError

import milkstraw_client


class APIClient:
    token = None

    @classmethod
    def download_file(cls, file_path: str, url: str) -> str:
        response = APIClient.request("get", url, return_raw=True)
        with open(file_path, "wb") as f:
            f.write(response)
        return file_path

    @classmethod
    def request(
        cls,
        method: str,
        url: str,
        params: dict = {},
        json: dict = {},
        file_paths: dict[str, str] = {},
        return_raw=False,
    ) -> Union[dict, str]:
        cls.set_token()
        files = {file_param: open(file_path, "rb") for file_param, file_path in file_paths.items()}
        headers = {"Authorization": f"Bearer {cls.token}"}
        response = requests.request(method, url, headers=headers, params=params, json=json, files=files)
        if response.status_code not in {200, 201}:
            response_formatted = f"status_code: `{response.status_code}`, message: `{response.text}`"
            raise HTTPError(f"Request to Milkstraw API failed. {response_formatted}")
        if return_raw:
            return response.content
        json_response: dict = response.json()
        return json_response

    @classmethod
    def set_token(cls):
        if cls.token is not None:
            return
        login_data = {"email": milkstraw_client.user_email, "password": milkstraw_client.user_password}
        login_url = f"{milkstraw_client.edge_service_url}/users/login"
        response = requests.post(login_url, json=login_data)
        if response.status_code != 200:
            response_formatted = f"status_code: `{response.status_code}`, message: `{response.text}`"
            raise HTTPError(f"Failed to login to Milkstraw API. {response_formatted}")
        json_response: dict = response.json()
        cls.token = json_response.get("token")
