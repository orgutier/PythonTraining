# Raising on HTTP Errors

Implement:

- `fetch_with_raise(url: str) -> dict` -- `r = requests.get(url)`; `r.raise_for_status()` (raises `requests.HTTPError` for a 4xx/5xx status instead of silently returning the error body); then return `r.json()`.
- `url_is_healthy(url: str) -> bool` -- `try: requests.get(url).raise_for_status(); return True` `except requests.exceptions.RequestException: return False` (turn the same `raise_for_status()` check into a plain yes/no answer, instead of letting the error propagate).

See the Study Reference presentation, Topic 12 (Mid tier), for the theory.
