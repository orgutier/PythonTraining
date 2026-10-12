# Challenge 19 — Sales Data Analyzer

**Do this after:** Stage 10 (Pandas)
**Correctness is pytest-tested:** `python tools/cli.py test challenge19` (or `pytest tests/test_challenge19.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

A realistic data-engineer interview task: given an orders CSV, report
revenue by region, the top customers, a region/product breakdown, and a
memory-optimized version of the data -- with **zero explicit row-by-row
Python loops**, only `groupby`, boolean indexing, and other vectorized
pandas operations.

Implement:

```python
def load_orders(path: str) -> pd.DataFrame:
    """pd.read_csv(path)."""

def revenue_by_region(df: pd.DataFrame) -> pd.Series:
    """Total revenue per region, highest first."""

def top_customers(df: pd.DataFrame, n: int) -> pd.Series:
    """The n customers with the highest total revenue, highest first."""

def high_value_orders(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """Every row whose revenue exceeds threshold."""

def region_product_pivot(df: pd.DataFrame) -> pd.DataFrame:
    """Regions as rows, products as columns, total revenue as the cell values."""

def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """A COPY of df with "region", "product", and "customer" cast to the "category" dtype."""
```

Assume the CSV/DataFrame has columns `region`, `product`, `customer`, and
`revenue`.

## Constraints on HOW you write it

1. **No explicit `for`/`while` loop over rows anywhere** -- every function
   here has a one-or-two-line vectorized pandas equivalent
   (`groupby`/`sort_values`/boolean indexing/`pivot_table`/`astype`).
2. **`revenue_by_region` and `top_customers` must both use `.groupby(...)
   [...].sum()` followed by `.sort_values(ascending=False)`** -- not
   `.value_counts()` (wrong statistic -- that counts rows, not sums
   revenue) and not a manual dict-building loop.
3. **`high_value_orders` must use boolean indexing**
   (`df[df["revenue"] > threshold]`), not `.query()` or `.apply()` with a
   lambda.
4. **`region_product_pivot` must use `df.pivot_table(index=..., "
   "columns=..., values=..., aggfunc="sum")`.**
5. **`optimize_dtypes` must return a new DataFrame (`df.copy()` or
   `df.astype({...})`, which itself returns a copy)** -- the caller's
   original `df` must be unchanged, and specifically must still have its
   original (non-`category`) dtypes afterward.
6. **A docstring on `revenue_by_region`** listing edge cases: a region
   with only one order, and two regions tied for the same total revenue
   (both are still returned; their relative order between ties isn't
   asserted by the tests).
