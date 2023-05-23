import os

from milkstraw_client.api_client import APIClient
from milkstraw_client.generator import Generator

edge_service_url = os.environ.get("MILKSTRAW_EDGE_SERVICE_URL")
if edge_service_url is None:
    edge_service_url = "https://backend.milkstraw.ai/api/v1"

user_email = os.environ.get("MILKSTRAW_USER_EMAIL")
user_password = os.environ.get("MILKSTRAW_USER_PASS")
