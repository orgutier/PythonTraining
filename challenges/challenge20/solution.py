"""
Challenge 20 - Two Sum, Pandas-Style, with Joins and Diagnostics
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge20.py / `python tools/cli.py test challenge20`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (a vectorized two_sum (no nested loop), df.merge(), df.apply(), a multi-indexed groupby, and df.head()/df.info()/df.describe() combined into one diagnostics report).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


import io
import pandas as pd


def two_sum(numbers, target: int):
    """Index-label pair summing to target, via a vectorized lookup (no nested loop)."""
    raise NotImplementedError


def merge_customer_names(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    """orders.merge(customers, on="customer_id")."""
    raise NotImplementedError


def add_price_tier(df: pd.DataFrame) -> pd.DataFrame:
    """Copy of df with a "tier" column, via df["price"].apply(...)."""
    raise NotImplementedError


def region_product_totals(df: pd.DataFrame) -> pd.Series:
    """Total revenue per (region, product), via a two-key groupby (MultiIndex result)."""
    raise NotImplementedError


def diagnostics(df: pd.DataFrame) -> dict:
    """{"head": ..., "info_text": ..., "describe": ...}."""
    raise NotImplementedError
