import time
import requests


def make_default_session():
    return requests.Session()


def create_session_with_headers(headers: dict):
    session = requests.Session()
    session.headers.update(headers)
    return session


def fetch_multiple_with_session(urls: list) -> list:
    with requests.Session() as session:
        return [session.get(u).json() for u in urls]


def fetch_with_retry(url: str, max_attempts: int) -> dict:
    for attempt in range(max_attempts):
        try:
            r = requests.get(url)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException:
            if attempt == max_attempts - 1:
                raise
            time.sleep(0.01 * (2 ** attempt))
