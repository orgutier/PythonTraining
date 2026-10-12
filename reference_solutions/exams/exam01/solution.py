"""
Exam 1 -- Order Processing Pipeline (Stages 1-4). Reference solution.
"""
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache, wraps


# --------------------------------------------------------------------------- Stage 1

def parse_inventory_line(line: str) -> dict:
    fields = line.strip().split(",")
    if len(fields) != 5:
        raise ValueError(f"expected 5 comma-separated fields, got {len(fields)}: {line!r}")
    sku, name, price, qty, tags = fields
    sku = sku.strip()
    name = name.strip()
    parsed_price = float(price.strip())
    parsed_qty = int(qty.strip())
    tag_set = {t.strip() for t in tags.split("|") if t.strip()}
    if sku is None or name is None:
        raise ValueError("sku/name must not be missing")
    return {"sku": sku, "name": name, "price": parsed_price, "qty": parsed_qty, "tags": tag_set}


# --------------------------------------------------------------------------- Stage 2

def find_item_by_sku(inventory: list, sku: str):
    for item in inventory:
        if item["sku"] == sku:
            break
    else:
        return None
    return item


def restock_report(inventory: list, threshold: int) -> list:
    working = list(inventory)
    report = []
    while working:
        item = working.pop(0)
        if item["qty"] < threshold:
            report.append((item["name"], item["qty"]))
    else:
        report.append(("__complete__", True))
    return report


def label_stock_levels(inventory: list) -> list:
    result = []
    for index, item in enumerate(inventory):
        label = "OUT" if item["qty"] == 0 else "LOW" if item["qty"] < 10 else "OK"
        result.append((index, item["name"], label))
    return result


def zip_orders_with_customers(order_totals: list, customers: list) -> list:
    return list(zip(customers, order_totals))


def is_valid_order(qty: int, sku: str, inventory_skus: set) -> bool:
    return qty > 0 and sku in inventory_skus and not sku.startswith("DISCONTINUED-")


# --------------------------------------------------------------------------- Stage 3

def make_discount_policy(rate: float):
    def apply(price: float) -> float:
        return round(price * (1 - rate), 2)
    return apply


def memoize(fn):
    cache = {}

    @wraps(fn)
    def wrapper(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    return wrapper


@lru_cache(maxsize=None)
def cached_shipping_rate(distance_km: float) -> float:
    return round(4.0 + distance_km * 0.1, 2)


def apply_shipping(*, weight_kg, base_rate=5.0, **surcharges):
    return round(base_rate + weight_kg * 0.5 + sum(surcharges.values()), 2)


def process_order(sku, qty, /, *, unit_price):
    return qty * unit_price


# --------------------------------------------------------------------------- Stage 4

@dataclass(frozen=True)
class Order:
    customer: str
    sku: str
    qty: int
    total: float


def group_orders_by_customer(orders: list) -> defaultdict:
    grouped = defaultdict(list)
    for order in orders:
        grouped[order.customer].append(order)
    return grouped


def top_selling_skus(orders: list, n: int) -> list:
    counts = Counter()
    for order in orders:
        counts[order.sku] += order.qty
    return counts.most_common(n)


def common_tags(item_a: dict, item_b: dict) -> set:
    return item_a["tags"] & item_b["tags"]


def sorted_inventory_by_price(inventory: list) -> list:
    return sorted(inventory, key=lambda item: item["price"])
