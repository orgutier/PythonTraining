# Requests Basics

Implement:

- `fetch_json(url: str) -> dict` -- `requests.get(url).json()`.
- `fetch_status_code(url: str) -> int` -- `requests.get(url).status_code`.
- `post_data(url: str, payload: dict) -> dict` -- `requests.post(url, json=payload).json()`.
- `fetch_with_raise(url: str) -> dict` -- `r = requests.get(url)`; `r.raise_for_status()` (raises `requests.HTTPError` for a 4xx/5xx status instead of silently returning the error body); then `return r.json()`.

The tests never touch the network -- they patch `requests.get`/`requests.post` with a fake response object. **Never** point one of these functions at a live URL from a test or a git hook; see the README's "Git hook integration" section.

See the Study Reference presentation, Topic 12, for the theory.
