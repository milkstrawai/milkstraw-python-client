import os

from milkstraw_client.api_client import APIClient
from milkstraw_client.generator import Generator
from milkstraw_client.test_api import test_url

edge_service_url = os.environ.get("MILKSTRAW_EDGE_SERVICE_URL")

user_email = os.environ.get("MILKSTRAW_USER_EMAIL")
user_password = os.environ.get("MILKSTRAW_USER_PASS")
