"""
Challenge 03 - Log Stream Parser and Scanner
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge03.py / `python tools/cli.py test challenge03`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (for...else for the scan, enumerate()/zip() where specified, and explicit truthiness/short-circuit for the health check).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/stageNN/solution.py.
"""


def parse_log_stream(lines: list[str]) -> list[tuple[str, str, str]]:
    """Parse "HH:MM LEVEL message" lines into (time, level, message) tuples; skip blanks."""
    raise NotImplementedError


def first_critical_index(entries: list[tuple], levels: tuple = ("ERROR", "CRITICAL")) -> int:
    """Index of the first entry whose level is in levels, or -1 -- a for...else."""
    raise NotImplementedError


def label_entries(entries: list[tuple]) -> list[str]:
    """["0: LEVEL - message", ...] via enumerate()."""
    raise NotImplementedError


def pair_with_severity(entries: list[tuple], severities: list[int]) -> list[tuple]:
    """[(entry, severity), ...] via zip()."""
    raise NotImplementedError


def is_healthy(entries: list[tuple], levels: tuple = ("CRITICAL",)) -> bool:
    """entries is non-empty AND none of them has a level in levels -- one and/not expression."""
    raise NotImplementedError
