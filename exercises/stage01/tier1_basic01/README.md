# Road Trip Fuel Ledger

Four friends are splitting the fuel cost of a road trip. The raw trip data below arrives as **strings** (as if read from a form) -- do not modify these four given lines:

```python
distance_km_text = "742.5"
fuel_efficiency_l_per_100km_text = "6.8"
fuel_price_per_liter_text = "1.53"
passengers_text = "3"
```

Using only what the Basic tier has covered so far (arithmetic operators, explicit `int()`/`float()` casting, comparison operators, `isinstance()`, `type()`, `print()`) -- **no `if`/`for`/`while`, no f-strings, no `+=`** (all of those are Mid/Advanced-tier tools, saved for later exercises) -- write plain top-level code that computes:

- `distance_km`, `fuel_efficiency_l_per_100km`, `fuel_price_per_liter` (each cast to `float`) and `passengers` (cast to `int`).
- `is_price_a_float` -- `True` iff `fuel_price_per_liter` is a genuine `float` (use `isinstance()`; this should obviously be `True` here, but writing the check is the point -- you'll rely on this exact pattern again once the numbers aren't guaranteed like they are here).
- `total_fuel_liters` -- liters needed for the whole trip: `distance_km / 100 * fuel_efficiency_l_per_100km`.
- `total_cost` -- `total_fuel_liters * fuel_price_per_liter`.
- `cost_per_passenger` -- `total_cost / passengers`.

Finish with one `print()` call summarizing the trip, built with string concatenation and `str()` (still no f-strings) -- something like `"Total cost: " + str(total_cost)`.
