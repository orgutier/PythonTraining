from exercises.week01.solution import celsius_to_fahrenheit, bmi_calculator


def test_celsius_to_fahrenheit_freezing():
    assert celsius_to_fahrenheit(0) == 32.0


def test_celsius_to_fahrenheit_boiling():
    assert celsius_to_fahrenheit(100) == 212.0


def test_bmi_calculator():
    assert abs(bmi_calculator(70, 1.75) - 22.86) < 0.01
