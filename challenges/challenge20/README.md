# Challenge 20 — Two Sum, Pandas-Style, with Joins and Diagnostics

**Do this after:** Stage 10 (Pandas)
**Correctness is pytest-tested:** `python tools/cli.py test challenge20` (or `pytest tests/test_challenge20.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

A companion to Challenge 19: LeetCode #1 ("Two Sum") solved the way a data
engineer would -- as a vectorized `pandas.Series` operation, not a Python
loop -- plus a small set of everyday pandas utilities (joining two tables,
a derived column, a multi-indexed summary, and a combined diagnostics
report) that round out the rest of this stage's toolkit.

Implement:

```python
def two_sum(numbers: "pd.Series", target: int):
    """(index_a, index_b) of the first pair whose values sum to target, or None. Returns INDEX LABELS, not positions."""

def merge_customer_names(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    """orders joined with customers on "customer_id", bringing in the customer's name."""

def add_price_tier(df: pd.DataFrame) -> pd.DataFrame:
    """A copy of df with a new "tier" column: "low" (price < 50), "medium" (50-199), "high" (200+)."""

def region_product_totals(df: pd.DataFrame) -> pd.Series:
    """Total revenue per (region, product) pair -- a MultiIndex result."""

def diagnostics(df: pd.DataFrame) -> dict:
    """{"head": df.head(3), "info_text": <df.info() captured as a string>, "describe": df.describe()}."""
```

```python
numbers = pd.Series([2, 7, 11, 15], index=["a", "b", "c", "d"])
two_sum(numbers, 9)   # -> ("a", "b"), since numbers["a"] + numbers["b"] == 9
```

## Constraints on HOW you write it

1. **`two_sum` must have no explicit nested loop over the values**
   (no `for i in ...: for j in ...:` comparing every pair). Build a
   complement lookup (`target - numbers`, or a `dict` of value -> index)
   and use a vectorized/O(1)-lookup pass instead.
2. **`merge_customer_names` must use `orders.merge(customers, on=
   "customer_id")`**, not a manual dict-based lookup joined in a loop.
3. **`add_price_tier` must build the "tier" column with `df["price"]
   .apply(...)`** (a helper function or `lambda`), not a chain of boolean
   masks assigned separately.
4. **`region_product_totals` must be `df.groupby(["region", "product"])
   ["revenue"].sum()`** -- a two-key `groupby`, producing a `MultiIndex`
   result (a test checks `isinstance(result.index, pd.MultiIndex)`).
5. **`diagnostics`'s `"info_text"` must be `df.info()` redirected through
   an `io.StringIO` buffer** (`df.info()` itself prints and returns
   `None` -- there's no other way to capture its text).
6. **A docstring on `two_sum`** listing edge cases: no pair sums to
   `target` (returns `None`), and a `Series` with a repeated value where
   two *different* index labels both hold it and together sum to
   `target`.
