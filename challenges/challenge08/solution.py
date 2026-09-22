"""
Challenge 08 - Longest Consecutive Run of Records
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge08.py / `python tools/cli.py test challenge08`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (an O(n) set-based scan (no full sort of the input), namedtuple records, and sorted()/set-union to build derived reports).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/stageNN/solution.py.
"""


import collections

Run = collections.namedtuple("Run", ["start", "length"])


def all_runs(numbers: list) -> list:
    """Every maximal consecutive run in numbers, as Run records sorted by start."""
    raise NotImplementedError


def longest_consecutive_run(numbers: list) -> Run:
    """The single longest Run (reuse all_runs); raise ValueError if numbers is empty."""
    raise NotImplementedError


def runs_overlap(run_a: Run, run_b: Run) -> bool:
    """True if the two runs' integer ranges overlap."""
    raise NotImplementedError


def unique_numbers_covered(runs: list) -> set:
    """Every integer covered by any run, as one set."""
    raise NotImplementedError
