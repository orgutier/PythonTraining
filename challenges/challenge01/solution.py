"""
Challenge 01 - Typed Config Loader
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge01.py / `python tools/cli.py test challenge01`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (no try/except for numeric detection, isinstance()/type() used explicitly, and no mutation of the inputs).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/stageNN/solution.py.
"""


def parse_config_line(line: str) -> tuple[str, object]:
    """Parse "KEY=value" into (key, typed_value). See README for the type-inference rules."""
    raise NotImplementedError


def load_config(lines: list[str]) -> dict[str, object]:
    """Parse every non-blank line in lines via parse_config_line into a dict."""
    raise NotImplementedError


def describe_types(config: dict) -> dict[str, str]:
    """{key: type(value).__name__ for key, value in config.items()} -- use type(), not isinstance()."""
    raise NotImplementedError


def merge_configs(base: dict, override: dict) -> dict:
    """A NEW dict: base's entries, with override's entries taking priority. Never mutate base or override."""
    raise NotImplementedError
