# Challenge 03 — Sales Data Analyzer

**Do this after:** Week 10 (Pandas)
**Not pytest-tested.** Grade it yourself against the constraints below.

## Problem

A very common data/backend-engineer interview task: "here's a CSV of
transactions, write code that answers these business questions." You're
given a DataFrame of orders with columns:

| column | type | meaning |
|---|---|---|
| `order_id` | str | unique order identifier |
| `customer` | str | customer name |
| `month` | str | `"YYYY-MM"`, e.g. `"2024-03"` |
| `amount` | float | order revenue in dollars |

Implement three functions that answer three real questions a manager would
actually ask:

```python
def monthly_revenue(orders: pd.DataFrame) -> pd.Series:
    """Total revenue per month, sorted chronologically."""

def top_customers(orders: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """The n customers with the highest total revenue, highest first."""

def revenue_drop_alerts(orders: pd.DataFrame, threshold: float = 0.20) -> list[str]:
    """Months where revenue fell more than `threshold` (20% by default)
    versus the previous month. Return the list of such months, in order."""
```

## Constraints on HOW you write it

1. **No explicit `for` loop over DataFrame rows, anywhere** (no
   `.iterrows()`, `.itertuples()`, or manual row indexing). Every
   computation must go through `groupby`, vectorized arithmetic, or
   `.apply()` on a *Series* (never on the whole DataFrame row-by-row).
   This is the actual pandas skill being tested: idiomatic, vectorized
   pandas is what separates a real pandas user from someone looping over
   `range(len(df))`.
2. **Each function needs a docstring with a comprehensive list of the
   assumptions it makes about the input**, and what it does for: a month
   with no orders at all (should it appear with 0 revenue, or be absent?
   pick one and document it), a customer with exactly one order, and a
   tie for the Nth spot in `top_customers` (document your tie-breaking
   rule).
3. **`revenue_drop_alerts` must compare each month only to the
   immediately preceding month** in the sorted monthly series -- state in
   the docstring what happens for the first month in the data (there is no
   previous month to compare against).
4. Return types must match exactly what's declared above (`pd.Series`,
   `pd.DataFrame`, `list[str]`) so the functions are usable by other code
   without extra conversion.

## Try it yourself

There's no fixture CSV provided on purpose -- build a small DataFrame by
hand (or with `pd.DataFrame({...})`) covering at least: three customers
across three months, one month with a >20% revenue drop, and one month
with no orders at all, to prove your functions handle every case above.
