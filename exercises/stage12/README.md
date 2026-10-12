# Requests + Threading

Six exercises, two per tier: basic HTTP calls and raw threading in Basic; raise_for_status() error handling and lock-guarded shared state in Mid; sessions with manual retry/backoff, plus ThreadPoolExecutor as the higher-level alternative to managing threads by hand, in Advanced.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage12_<name>` (e.g. `python tools/cli.py test stage12_tier1_basic01`). Work through them in order.

- **`tier1_basic01/`** -- requests.get(), response.json(), requests.post()
- **`tier1_basic02/`** -- threading.Thread, .start(), .join()
- **`tier2_mid01/`** -- response.raise_for_status()
- **`tier2_mid02/`** -- threading.Lock
- **`tier3_advanced01/`** -- requests.Session(), connection reuse, retry/backoff strategies
- **`tier3_advanced02/`** -- concurrent.futures.ThreadPoolExecutor
