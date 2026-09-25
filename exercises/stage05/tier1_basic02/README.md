# Support Ticket Intake

A support inbox's raw ticket text needs scanning and cleaning. Implement:

- `extract_ticket_ids(text: str) -> list[str]` -- `re.findall(r"TICKET-\d+", text)`.
- `contains_urgent_flag(text: str) -> bool` -- `re.search(r"\bURGENT\b", text) is not None`.
- `clean_ticket_text(text: str) -> str` -- `re.sub(r"\s+", " ", text).strip()` (collapse whitespace runs to a single space).
- `looks_like_ticket_id(text: str) -> bool` -- `re.match(r"TICKET-\d+$", text) is not None` (`re.match` only anchors at the **start**, and `$` anchors the **end**, so this is `True` only if `text` is *entirely* a ticket id, unlike `extract_ticket_ids` above which finds ids anywhere).
- `parse_priority(raw: str) -> int` -- `try: return int(raw)` `except ValueError: raise Exception(f"invalid priority: {raw!r}")` (catch the specific error, then `raise` a plain `Exception` with a clearer message).
- `parse_priority_with_default(raw: str, default: int = 0) -> int` -- `try: return int(raw)` `except ValueError: return default` `finally:` increment the module-level `_parse_attempts` counter -- `finally` runs whether or not the `except` fired, which is exactly why it's the right place to count *every* attempt.
- `get_parse_attempts() -> int` -- read `_parse_attempts`.

See the Study Reference presentation, Topic 5 (Basic tier), for the theory.
