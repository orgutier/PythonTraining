# Requests + Threading

Six exercises, two per tier: basic HTTP calls and raw threading in Basic; raise_for_status() error handling and lock-guarded shared state in Mid; sessions with manual retry/backoff, plus ThreadPoolExecutor as the higher-level alternative to managing threads by hand, in Advanced.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage12_<name>` (e.g. `python tools/cli.py test stage12_basic01`). Work through them in order.

- **`basic01/`** -- requests.get(), response.json(), requests.post()
- **`basic02/`** -- threading.Thread, .start(), .join()
- **`mid01/`** -- response.raise_for_status()
- **`mid02/`** -- threading.Lock
- **`advanced01/`** -- requests.Session(), connection reuse, retry/backoff strategies
- **`advanced02/`** -- concurrent.futures.ThreadPoolExecutor
