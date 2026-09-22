"""
Tests for Exam 1 -- Order Processing Pipeline (Stages 1-4).
"""
import pytest
from exams.exam01.solution import (
    parse_inventory_line,
    find_item_by_sku,
    restock_report,
    label_stock_levels,
    zip_orders_with_customers,
    is_valid_order,
    make_discount_policy,
    memoize,
    cached_shipping_rate,
    apply_shipping,
    process_order,
    Order,
    group_orders_by_customer,
    top_selling_skus,
    common_tags,
    sorted_inventory_by_price,
)


@pytest.fixture
def inventory():
    return [
        {"sku": "A1", "name": "Widget", "price": 9.99, "qty": 0, "tags": {"tools", "sale"}},
        {"sku": "B2", "name": "Gadget", "price": 19.99, "qty": 5, "tags": {"tools", "new"}},
        {"sku": "C3", "name": "Gizmo", "price": 4.5, "qty": 50, "tags": {"toys"}},
    ]


# --------------------------------------------------------------------------- Stage 1

def test_parse_inventory_line_basic():
    result = parse_inventory_line("A1,Widget,9.99,3,tools|sale")
    assert result == {"sku": "A1", "name": "Widget", "price": 9.99, "qty": 3, "tags": {"tools", "sale"}}


def test_parse_inventory_line_strips_whitespace():
    result = parse_inventory_line(" A1 , Widget , 9.99 , 3 , tools ")
    assert result["sku"] == "A1"
    assert result["name"] == "Widget"
    assert result["tags"] == {"tools"}


def test_parse_inventory_line_wrong_field_count_raises():
    with pytest.raises(ValueError):
        parse_inventory_line("A1,Widget,9.99")


def test_parse_inventory_line_types():
    result = parse_inventory_line("A1,Widget,9.99,3,tools")
    assert isinstance(result["price"], float)
    assert isinstance(result["qty"], int)
    assert isinstance(result["tags"], set)


# --------------------------------------------------------------------------- Stage 2

def test_find_item_by_sku_found(inventory):
    item = find_item_by_sku(inventory, "B2")
    assert item["name"] == "Gadget"


def test_find_item_by_sku_not_found_returns_none(inventory):
    assert find_item_by_sku(inventory, "ZZ") is None


def test_restock_report_includes_low_stock_and_completion_marker(inventory):
    report = restock_report(inventory, threshold=10)
    assert ("Widget", 0) in report
    assert ("Gadget", 5) in report
    assert ("Gizmo", 50) not in report
    assert report[-1] == ("__complete__", True)


def test_restock_report_empty_inventory():
    assert restock_report([], threshold=10) == [("__complete__", True)]


def test_label_stock_levels(inventory):
    labels = label_stock_levels(inventory)
    assert labels[0] == (0, "Widget", "OUT")
    assert labels[1] == (1, "Gadget", "LOW")
    assert labels[2] == (2, "Gizmo", "OK")


def test_zip_orders_with_customers():
    result = zip_orders_with_customers([10, 20], ["alice", "bob"])
    assert result == [("alice", 10), ("bob", 20)]


def test_is_valid_order_true():
    assert is_valid_order(2, "A1", {"A1", "B2"}) is True


def test_is_valid_order_false_zero_qty():
    assert is_valid_order(0, "A1", {"A1"}) is False


def test_is_valid_order_false_unknown_sku():
    assert is_valid_order(2, "ZZ", {"A1"}) is False


def test_is_valid_order_false_discontinued():
    assert is_valid_order(2, "DISCONTINUED-A1", {"DISCONTINUED-A1"}) is False


# --------------------------------------------------------------------------- Stage 3

def test_make_discount_policy_applies_rate():
    ten_percent_off = make_discount_policy(0.10)
    assert ten_percent_off(100) == 90.0


def test_make_discount_policy_independent_closures():
    off10 = make_discount_policy(0.10)
    off50 = make_discount_policy(0.50)
    assert off10(100) == 90.0
    assert off50(100) == 50.0


def test_memoize_preserves_metadata():
    @memoize
    def add(a, b):
        """docstring"""
        return a + b

    assert add.__name__ == "add"
    assert add.__doc__ == "docstring"


def test_memoize_caches_result():
    calls = []

    @memoize
    def slow(x):
        calls.append(x)
        return x * 2

    assert slow(3) == 6
    assert slow(3) == 6
    assert calls == [3]


def test_cached_shipping_rate_is_lru_cached():
    assert cached_shipping_rate(10) == cached_shipping_rate(10)
    assert hasattr(cached_shipping_rate, "cache_info")


def test_apply_shipping_base_case():
    assert apply_shipping(weight_kg=2) == 6.0


def test_apply_shipping_with_surcharges():
    assert apply_shipping(weight_kg=2, fuel=1.5, remote=2.5) == 10.0


def test_process_order_computes_total():
    assert process_order("A1", 3, unit_price=10.0) == 30.0


def test_process_order_requires_keyword_unit_price():
    with pytest.raises(TypeError):
        process_order("A1", 3, 10.0)


def test_process_order_rejects_keyword_sku():
    with pytest.raises(TypeError):
        process_order(sku="A1", qty=3, unit_price=10.0)


# --------------------------------------------------------------------------- Stage 4

def test_order_is_frozen_dataclass():
    order = Order(customer="alice", sku="A1", qty=2, total=20.0)
    assert order.customer == "alice"
    with pytest.raises(Exception):
        order.qty = 5


def test_group_orders_by_customer():
    orders = [
        Order("alice", "A1", 1, 10.0),
        Order("bob", "B2", 2, 40.0),
        Order("alice", "C3", 3, 15.0),
    ]
    grouped = group_orders_by_customer(orders)
    assert len(grouped["alice"]) == 2
    assert len(grouped["bob"]) == 1
    assert grouped["nobody"] == []


def test_top_selling_skus():
    orders = [
        Order("alice", "A1", 5, 50.0),
        Order("bob", "A1", 3, 30.0),
        Order("carol", "B2", 1, 10.0),
    ]
    top = top_selling_skus(orders, 1)
    assert top == [("A1", 8)]


def test_common_tags():
    a = {"tags": {"tools", "sale", "new"}}
    b = {"tags": {"sale", "toys"}}
    assert common_tags(a, b) == {"sale"}


def test_sorted_inventory_by_price_does_not_mutate(inventory):
    original_order = [item["sku"] for item in inventory]
    result = sorted_inventory_by_price(inventory)
    assert [item["sku"] for item in result] == ["C3", "A1", "B2"]
    assert [item["sku"] for item in inventory] == original_order
