def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def bmi_calculator(weight_kg: float, height_m: float) -> float:
    return round(weight_kg / height_m ** 2, 2)
