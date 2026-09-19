import pandas as pd


def monthly_revenue(orders: pd.DataFrame) -> pd.Series:
    """
    Total revenue per month, sorted chronologically.

    A month with zero orders never appears as a row in `orders` at all, so
    it is simply absent from the returned Series -- it is not filled in
    with a 0. Callers that need a continuous month range should reindex
    the result themselves against their own calendar.
    """
    return orders.groupby("month")["amount"].sum().sort_index()


def top_customers(orders: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    The n customers with the highest total revenue, highest first, as a
    two-column DataFrame (customer, amount).

    A customer with exactly one order is summed the same as any other --
    their single order's amount is their total. Ties for the Nth spot are
    broken by pandas' stable sort, which preserves the customers' original
    groupby order (alphabetical by customer name) among tied amounts, so
    the result is deterministic across runs on the same input.
    """
    totals = orders.groupby("customer")["amount"].sum().sort_values(ascending=False)
    return totals.head(n).rename_axis("customer").reset_index(name="amount")


def revenue_drop_alerts(orders: pd.DataFrame, threshold: float = 0.20) -> list[str]:
    """
    Months where revenue fell by more than `threshold` (as a fraction,
    e.g. 0.20 = 20%) compared to the immediately preceding month in the
    sorted monthly series. Returns the affected months in chronological
    order.

    The first month in the data has no preceding month to compare against
    and can never be flagged, by definition.
    """
    monthly = monthly_revenue(orders)
    pct_change = monthly.pct_change()
    dropped = pct_change[pct_change < -threshold]
    return list(dropped.index)
