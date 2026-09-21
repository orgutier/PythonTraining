# CLI Interaction

Implement five functions that model a tiny command-line interaction (these are exactly the building blocks `tools/cli.py` itself is built from -- see the Appendix topic in the presentation for more):

- `ask_name() -> str` -- `return input("What is your name? ")`.
- `ask_age() -> int` -- `return int(input("How old are you? "))`.
- `ask_yes_no(prompt: str) -> bool` -- read `input(prompt)`, `.strip().lower()` it, and return `True` only if the result is `"y"` **or** `"yes"` (use `in ("y", "yes")`).
- `greet(name: str) -> None` -- `print(f"Hello, {name}!")`.
- `greeting_flow() -> str` -- call `ask_name()`, pass the result to `greet()`, then return the name.

The tests simulate a user typing by patching `builtins.input` with `monkeypatch` and capture `print()` output with `capsys` -- you don't need to do anything special in your code for that; just call the real `input()`/`print()` builtins normally.

See the Study Reference presentation, Topic 1, for the theory.
