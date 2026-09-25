class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


class TemperatureBuggy:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5


class Counter:
    def __init__(self, start=0):
        self.value = start

    @classmethod
    def from_string(cls, text):
        return cls(int(text))


class CounterBuggy:
    def __init__(self, start=0):
        self.value = start

    @classmethod
    def from_string(cls, text):
        return cls(text)


_check_log = []


def check(description: str, condition: bool) -> bool:
    _check_log.append((description, condition))
    return condition


def run_all_checks() -> dict:
    _check_log.clear()

    check("Temperature(100).fahrenheit == 212.0", Temperature(100).fahrenheit == 212.0)
    check("TemperatureBuggy(100).fahrenheit == 212.0", TemperatureBuggy(100).fahrenheit == 212.0)

    check("Counter.from_string('5').value == 5", Counter.from_string("5").value == 5)
    check("CounterBuggy.from_string('5').value == 5", CounterBuggy.from_string("5").value == 5)

    total = len(_check_log)
    passed = sum(1 for _, ok in _check_log if ok)
    failed = [desc for desc, ok in _check_log if not ok]
    return {"total": total, "passed": passed, "failed": failed}
