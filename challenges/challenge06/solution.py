"""
Challenge 06 - Streaming Metrics Aggregator
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge06.py / `python tools/cli.py test challenge06`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (a generator (yield) for batching, positional-only and keyword-only parameters together, module state via global, and functools.partial for a reusable transform).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/stageNN/solution.py.
"""


import functools


def stream_batches(data: list, size: int, /):
    """Generator: yield chunks of data up to size items long. Both params positional-only."""
    raise NotImplementedError


_total_processed = 0


def process_batch(batch: list, /, *, transform=lambda x: x) -> list:
    """Apply transform to each item; add len(batch) to the global _total_processed."""
    raise NotImplementedError


def get_total_processed() -> int:
    """Return _total_processed."""
    raise NotImplementedError


def reset_total_processed() -> None:
    """Reset _total_processed to 0."""
    raise NotImplementedError


def _scale(factor, value):
    return value * factor


def make_scaled_transform(factor: int):
    """functools.partial(_scale, factor) -- not a lambda/closure."""
    raise NotImplementedError
