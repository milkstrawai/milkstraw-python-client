import requests


def test_url(url: str):
    response = requests.get(url)
    print(f"The url '{url}' responsed with {response.status_code} status code.")
