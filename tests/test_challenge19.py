import pandas as pd
from challenges.challenge19.solution import (
    load_orders,
    revenue_by_region,
    top_customers,
    high_value_orders,
    region_product_pivot,
    optimize_dtypes,
)


def _sample_df():
    return pd.DataFrame({
        "region": ["east", "east", "west", "west", "west"],
        "product": ["A", "B", "A", "A", "B"],
        "customer": ["c1", "c2", "c1", "c3", "c2"],
        "revenue": [100, 50, 200, 300, 75],
    })


def test_load_orders(tmp_path):
    path = tmp_path / "orders.csv"
    path.write_text("region,product,customer,revenue\neast,A,c1,100\n")
    df = load_orders(str(path))
    assert list(df.columns) == ["region", "product", "customer", "revenue"]


def test_revenue_by_region():
    result = revenue_by_region(_sample_df())
    assert result.index[0] == "west"
    assert result["west"] == 575
    assert result["east"] == 150


def test_top_customers():
    result = top_customers(_sample_df(), 2)
    assert list(result.index) == ["c1", "c3"]
    assert result["c1"] == 300


def test_high_value_orders():
    result = high_value_orders(_sample_df(), 150)
    assert list(result["revenue"]) == [200, 300]


def test_region_product_pivot():
    result = region_product_pivot(_sample_df())
    assert result.loc["east", "A"] == 100
    assert result.loc["west", "A"] == 500


def test_optimize_dtypes_returns_copy_with_category_dtype():
    df = _sample_df()
    result = optimize_dtypes(df)
    assert str(result["region"].dtype) == "category"
    assert str(df["region"].dtype) != "category"
