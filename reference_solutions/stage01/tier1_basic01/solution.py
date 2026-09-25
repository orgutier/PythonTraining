distance_km_text = "742.5"
fuel_efficiency_l_per_100km_text = "6.8"
fuel_price_per_liter_text = "1.53"
passengers_text = "3"

distance_km = float(distance_km_text)
fuel_efficiency_l_per_100km = float(fuel_efficiency_l_per_100km_text)
fuel_price_per_liter = float(fuel_price_per_liter_text)
passengers = int(passengers_text)

is_price_a_float = isinstance(fuel_price_per_liter, float)

total_fuel_liters = distance_km / 100 * fuel_efficiency_l_per_100km
total_cost = total_fuel_liters * fuel_price_per_liter
cost_per_passenger = total_cost / passengers

print("Total cost: " + str(total_cost) + ", per passenger: " + str(cost_per_passenger))
