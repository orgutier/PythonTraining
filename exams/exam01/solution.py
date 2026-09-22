"""
Exam 1 -- Order Processing Pipeline (Stages 1-4).
Implement every function/class below. See README.md for the full spec.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- tests/test_exam01.py imports
directly from here.
"""
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache, wraps


# --------------------------------------------------------------------------- Stage 1

def parse_inventory_line(line: str) -> dict:
    """Parse "SKU,name,price,qty,tag1|tag2" into a typed dict. See README."""
    raise NotImplementedError


# --------------------------------------------------------------------------- Stage 2

def find_item_by_sku(inventory: list, sku: str):
    """for...else search. See README."""
    raise NotImplementedError


def restock_report(inventory: list, threshold: int) -> list:
    """while...else loop. See README."""
    raise NotImplementedError


def label_stock_levels(inventory: list) -> list:
    """enumerate() + chained ternary. See README."""
    raise NotImplementedError


def zip_orders_with_customers(order_totals: list, customers: list) -> list:
    """zip(). See README."""
    raise NotImplementedError


def is_valid_order(qty: int, sku: str, inventory_skus: set) -> bool:
    """One and/not expression. See README."""
    raise NotImplementedError


# --------------------------------------------------------------------------- Stage 3

def make_discount_policy(rate: float):
    """Closure returning price -> discounted price. See README."""
    raise NotImplementedError


def memoize(fn):
    """Decorator, functools.wraps-preserving, hand-rolled cache. See README."""
    raise NotImplementedError


@lru_cache(maxsize=None)
def cached_shipping_rate(distance_km: float) -> float:
    """functools.lru_cache-backed shipping rate. See README."""
    raise NotImplementedError


def apply_shipping(*, weight_kg, base_rate=5.0, **surcharges):
    """Keyword-only params + **kwargs surcharges. See README."""
    raise NotImplementedError


def process_order(sku, qty, /, *, unit_price):
    """Positional-only sku/qty, keyword-only unit_price. See README."""
    raise NotImplementedError


# --------------------------------------------------------------------------- Stage 4

@dataclass(frozen=True)
class Order:
    """Frozen dataclass: customer, sku, qty, total."""
    customer: str
    sku: str
    qty: int
    total: float


def group_orders_by_customer(orders: list) -> defaultdict:
    """collections.defaultdict grouping. See README."""
    raise NotImplementedError


def top_selling_skus(orders: list, n: int) -> list:
    """collections.Counter.most_common(n), weighted by qty. See README."""
    raise NotImplementedError


def common_tags(item_a: dict, item_b: dict) -> set:
    """Set intersection of two items' tags. See README."""
    raise NotImplementedError


def sorted_inventory_by_price(inventory: list) -> list:
    """sorted(..., key=...) ascending by price, non-mutating. See README."""
    raise NotImplementedError
