"""
Challenge 03 - Sales Data Analyzer
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge03.py / `python tools/cli.py test challenge03`); see README.md in this folder
for the full problem statement, the expected DataFrame columns, and the
constraints your solution must follow (no row-by-row loops, documented
assumptions, and exact return types).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""
import pandas as pd


def monthly_revenue(orders: pd.DataFrame) -> pd.Series:
    """
    Total revenue per month, sorted chronologically. Fill in this docstring
    as part of the challenge: state what happens for a month with zero
    orders (absent from the input entirely).
    """
    raise NotImplementedError


def top_customers(orders: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    The n customers with the highest total revenue, highest first. Fill in
    this docstring: state your tie-breaking rule for the Nth spot.
    """
    raise NotImplementedError


def revenue_drop_alerts(orders: pd.DataFrame, threshold: float = 0.20) -> list[str]:
    """
    Months where revenue fell more than `threshold` versus the immediately
    preceding month. Fill in this docstring: state what happens for the
    first month in the data (no previous month to compare against).
    """
    raise NotImplementedError
