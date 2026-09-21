import pandas as pd
from challenges.challenge20.solution import (
    two_sum,
    merge_customer_names,
    add_price_tier,
    region_product_totals,
    diagnostics,
)


def test_two_sum_basic():
    numbers = pd.Series([2, 7, 11, 15], index=["a", "b", "c", "d"])
    assert two_sum(numbers, 9) == ("a", "b")


def test_two_sum_no_pair():
    numbers = pd.Series([1, 2, 3], index=["a", "b", "c"])
    assert two_sum(numbers, 100) is None


def test_two_sum_repeated_value():
    numbers = pd.Series([5, 5], index=["a", "b"])
    assert two_sum(numbers, 10) == ("a", "b")


def test_merge_customer_names():
    orders = pd.DataFrame({"customer_id": [1, 2], "revenue": [100, 200]})
    customers = pd.DataFrame({"customer_id": [1, 2], "name": ["Ada", "Grace"]})
    result = merge_customer_names(orders, customers)
    assert list(result["name"]) == ["Ada", "Grace"]


def test_add_price_tier():
    df = pd.DataFrame({"price": [10, 100, 500]})
    result = add_price_tier(df)
    assert list(result["tier"]) == ["low", "medium", "high"]
    assert "tier" not in df.columns  # original untouched


def test_region_product_totals_is_multi_indexed():
    df = pd.DataFrame({
        "region": ["east", "east", "west"],
        "product": ["A", "B", "A"],
        "revenue": [100, 50, 200],
    })
    result = region_product_totals(df)
    assert isinstance(result.index, pd.MultiIndex)
    assert result[("east", "A")] == 100


def test_diagnostics():
    df = pd.DataFrame({"x": [1, 2, 3]})
    result = diagnostics(df)
    assert len(result["head"]) == 3
    assert "RangeIndex" in result["info_text"]
    assert result["describe"].loc["mean", "x"] == 2.0
