import pandas as pd

from challenges.challenge03.solution import (
    monthly_revenue,
    revenue_drop_alerts,
    top_customers,
)


def _orders() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"order_id": "1", "customer": "Alice", "month": "2024-01", "amount": 100.0},
            {"order_id": "2", "customer": "Bob", "month": "2024-01", "amount": 50.0},
            {"order_id": "3", "customer": "Alice", "month": "2024-02", "amount": 200.0},
            {"order_id": "4", "customer": "Carol", "month": "2024-02", "amount": 30.0},
            {"order_id": "5", "customer": "Alice", "month": "2024-03", "amount": 20.0},
            {"order_id": "6", "customer": "Bob", "month": "2024-03", "amount": 10.0},
        ]
    )


def test_monthly_revenue_sums_and_sorts_chronologically():
    result = monthly_revenue(_orders())
    assert result.to_dict() == {"2024-01": 150.0, "2024-02": 230.0, "2024-03": 30.0}


def test_top_customers_ranks_by_total_revenue():
    result = top_customers(_orders(), n=2)
    assert list(result["customer"]) == ["Alice", "Bob"]
    assert list(result["amount"]) == [320.0, 60.0]


def test_top_customers_respects_n():
    result = top_customers(_orders(), n=1)
    assert len(result) == 1
    assert result.iloc[0]["customer"] == "Alice"


def test_revenue_drop_alerts_detects_a_big_drop():
    assert revenue_drop_alerts(_orders()) == ["2024-03"]


def test_revenue_drop_alerts_ignores_small_drops():
    orders = pd.DataFrame(
        [
            {"order_id": "1", "customer": "Alice", "month": "2024-01", "amount": 100.0},
            {"order_id": "2", "customer": "Alice", "month": "2024-02", "amount": 90.0},
        ]
    )
    assert revenue_drop_alerts(orders) == []


def test_revenue_drop_alerts_first_month_never_flagged():
    orders = pd.DataFrame(
        [{"order_id": "1", "customer": "Alice", "month": "2024-01", "amount": 5.0}]
    )
    assert revenue_drop_alerts(orders) == []
