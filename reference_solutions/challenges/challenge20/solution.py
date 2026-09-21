import io
import pandas as pd


def _price_tier(price):
    if price < 50:
        return "low"
    if price < 200:
        return "medium"
    return "high"


def two_sum(numbers, target: int):
    """
    Index-label pair (a, b) whose values sum to target, or None.

    Edge cases handled:
      - No pair sums to target -> returns None.
      - A repeated value at two different index labels, together summing
        to target -> both labels are still found correctly, since lookup
        is keyed by value with the label attached, not deduplicated away.
    """
    seen = {}
    for label, value in numbers.items():
        complement = target - value
        if complement in seen:
            return (seen[complement], label)
        seen[value] = label
    return None


def merge_customer_names(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    return orders.merge(customers, on="customer_id")


def add_price_tier(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["tier"] = df["price"].apply(_price_tier)
    return result


def region_product_totals(df: pd.DataFrame) -> pd.Series:
    return df.groupby(["region", "product"])["revenue"].sum()


def diagnostics(df: pd.DataFrame) -> dict:
    buf = io.StringIO()
    df.info(buf=buf)
    return {
        "head": df.head(3),
        "info_text": buf.getvalue(),
        "describe": df.describe(),
    }
