import threading
import requests


class APIError(Exception):
    """Raised when the API responds with a non-200 status code."""


def fetch_user_name(user_id: int) -> str:
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if response.status_code != 200:
        raise APIError(f"Request failed with status {response.status_code}")
    return response.json()["name"]


def fetch_many(user_ids: list[int]) -> dict[int, str]:
    results = {}
    lock = threading.Lock()

    def worker(uid):
        name = fetch_user_name(uid)
        with lock:
            results[uid] = name

    threads = [threading.Thread(target=worker, args=(uid,)) for uid in user_ids]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return results
