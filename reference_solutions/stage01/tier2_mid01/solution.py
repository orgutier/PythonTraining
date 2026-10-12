price_a_text = "19.99"
price_b_text = "18.995"
quantity_text = "4"

price_a = float(price_a_text)
price_b = float(price_b_text)
quantity = int(quantity_text)

savings_message = f"Switching suppliers saves {(savings := abs(price_a - price_b) * quantity):.2f}"

both_under_20 = 0 <= price_a < 20 and 0 <= price_b < 20

total_cost = 0.0
total_cost += price_a * quantity
total_cost += price_b * quantity

weighted_score = 2 + 3 * price_a ** 2

print(savings_message)
