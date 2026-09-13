"""
Week 10 - Pandas
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in tests/test_week10.py
imports directly from here.
"""


import pandas as pd


def load_sales_data(path: str) -> pd.DataFrame:
    raise NotImplementedError


def total_sales_by_region(df: pd.DataFrame) -> pd.Series:
    raise NotImplementedError


def top_n_products(df: pd.DataFrame, n: int) -> pd.DataFrame:
    raise NotImplementedError
