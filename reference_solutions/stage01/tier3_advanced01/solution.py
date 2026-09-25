import math
from decimal import Decimal

price_each_text = "19.99"
quantity_text = "7"

price_each_float = float(price_each_text)
quantity = int(quantity_text)

float_total = price_each_float * quantity
exact_total = Decimal(price_each_text) * Decimal(quantity_text)

totals_are_exactly_equal = float(exact_total) == float_total
totals_are_close = math.isclose(float(exact_total), float_total)

point_one_plus_point_two = 0.1 + 0.2
is_exactly_point_three = point_one_plus_point_two == 0.3
is_close_to_point_three = math.isclose(point_one_plus_point_two, 0.3)

print(f"Exact total: {exact_total}, exactly matched float total: {totals_are_exactly_equal}")
