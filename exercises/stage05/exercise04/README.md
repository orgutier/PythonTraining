# Regex Basics

Implement:

- `contains_digit(text: str) -> bool` -- `re.search(r"\d", text) is not None`.
- `find_all_numbers(text: str) -> list[str]` -- `re.findall(r"\d+", text)`.
- `starts_with_word(text: str, word: str) -> bool` -- `re.match(re.escape(word), text) is not None` (`re.match` only anchors at the *start* of the string, unlike `re.search`).
- `normalize_whitespace(text: str) -> str` -- `re.sub(r"\s+", " ", text).strip()` (collapse runs of whitespace to a single space).
- `EMAIL_PATTERN` (module level) -- `re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")`, and `extract_emails(text: str) -> list[str]` -- `EMAIL_PATTERN.findall(text)`. Compiling once at module level (instead of calling `re.search`/`re.findall` with a raw string every time) is the idiomatic move when a pattern is reused.

See the Study Reference presentation, Topic 5, for the theory.
