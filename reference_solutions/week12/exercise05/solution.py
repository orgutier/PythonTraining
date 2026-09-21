import concurrent.futures
import requests


def fetch_all_concurrently(urls: list) -> list:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(lambda u: requests.get(u).json(), urls))


def run_tasks_with_pool(funcs: list) -> list:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        return list(executor.map(lambda f: f(), funcs))


def compute_squares_concurrently(numbers: list) -> list:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        return list(executor.map(lambda x: x ** 2, numbers))
