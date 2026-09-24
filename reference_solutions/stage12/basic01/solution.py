import requests


def fetch_json(url: str) -> dict:
    return requests.get(url).json()


def fetch_status_code(url: str) -> int:
    return requests.get(url).status_code


def post_data(url: str, payload: dict) -> dict:
    return requests.post(url, json=payload).json()
