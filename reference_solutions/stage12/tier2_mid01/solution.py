import requests


def fetch_with_raise(url: str) -> dict:
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def url_is_healthy(url: str) -> bool:
    try:
        requests.get(url).raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False
