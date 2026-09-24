# Requests + Threading

Five exercises covering the requests library and Python threading from Topic 12 at least three times each: basic HTTP calls, sessions and manual retry/backoff, raw threading.Thread, locks guarding shared state against race conditions, and ThreadPoolExecutor as the higher-level alternative to managing threads by hand.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage12_<name>` (e.g. `python tools/cli.py test stage12_exercise01`). Work through them in order.

- **`exercise01/`** -- requests.get() x3, response.json() x3, requests.post(), raise_for_status()
- **`exercise02/`** -- requests.Session() x3, retry/backoff strategy
- **`exercise03/`** -- threading.Thread x3, .start() x3, .join() x3
- **`exercise04/`** -- threading.Lock x3, race conditions
- **`exercise05/`** -- concurrent.futures.ThreadPoolExecutor x3
