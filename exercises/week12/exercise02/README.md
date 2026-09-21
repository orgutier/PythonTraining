# Sessions and Retry/Backoff

Implement:

- `make_default_session()` -- `requests.Session()`.
- `create_session_with_headers(headers: dict)` -- build a `requests.Session()`, call `.headers.update(headers)` on it, and return it.
- `fetch_multiple_with_session(urls: list[str]) -> list` -- `with requests.Session() as session:` then `[session.get(u).json() for u in urls]`. A `Session` reuses its underlying TCP connection across requests instead of opening a fresh one every time -- **connection reuse** -- which matters a lot when you're about to make several requests to the same host.
- `fetch_with_retry(url: str, max_attempts: int) -> dict` -- loop up to `max_attempts` times: `try`: `r = requests.get(url)`, `r.raise_for_status()`, `return r.json()`; `except requests.exceptions.RequestException:` if this was the last attempt, re-`raise`; otherwise `time.sleep(0.01 * (2 ** attempt))` (**exponential backoff**: wait longer after each failure) and try again.

See the Study Reference presentation, Topic 12, for the theory.
