# ThreadPoolExecutor

Implement three functions using `concurrent.futures.ThreadPoolExecutor` -- a higher-level alternative to managing `threading.Thread` objects by hand: you submit work and it handles the thread pool for you.

- `fetch_all_concurrently(urls: list[str]) -> list` -- `with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor: return list(executor.map(lambda u: requests.get(u).json(), urls))`.
- `run_tasks_with_pool(funcs: list) -> list` -- `with concurrent.futures.ThreadPoolExecutor() as executor: return list(executor.map(lambda f: f(), funcs))` (run a list of zero-arg callables, collect their results in order).
- `compute_squares_concurrently(numbers: list[int]) -> list[int]` -- `with concurrent.futures.ThreadPoolExecutor() as executor: return list(executor.map(lambda x: x ** 2, numbers))`.

`executor.map` is the thread-pool equivalent of the builtin `map()` -- same call-once-per-item, results-in-order contract, just spread across worker threads instead of running serially.

See the Study Reference presentation, Topic 12 (Advanced tier), for the theory.
