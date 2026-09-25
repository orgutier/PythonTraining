def compute_total(*item_prices, tax_rate=0.08, **surcharges) -> float:
    subtotal = sum(item_prices)
    tax = subtotal * tax_rate
    return round(subtotal + tax + sum(surcharges.values()), 2)


def apply_discount(price, pct=0.10) -> float:
    return round(price * (1 - pct), 2)
