# Requests Basics

Implement:

- `fetch_json(url: str) -> dict` -- `requests.get(url).json()`.
- `fetch_status_code(url: str) -> int` -- `requests.get(url).status_code`.
- `post_data(url: str, payload: dict) -> dict` -- `requests.post(url, json=payload).json()`.

The tests never touch the network -- they patch `requests.get`/`requests.post` with a fake response object. **Never** point one of these functions at a live URL from a test or a git hook; see the README's "Git hook integration" section.

See the Study Reference presentation, Topic 12 (Basic tier), for the theory.
