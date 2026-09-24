# Session Log Files

Implement four small file-handling functions, each using `with open(...) as f:` (never a bare `open()`/`close()` pair):

- `write_lines(path: str, lines: list[str]) -> None` -- open `path` for writing (`"w"`), write each line followed by `"\n"`.
- `read_lines(path: str) -> list[str]` -- open `path` for reading, return `f.read().splitlines()`.
- `append_line(path: str, line: str) -> None` -- open `path` for appending (`"a"`), write `line + "\n"`.
- `count_lines(path: str) -> int` -- open `path` for reading, return how many lines it has.

See the Study Reference presentation, Topic 5 (Basic tier), for the theory.
