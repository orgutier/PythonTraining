class Shape:
    def area(self):
        raise NotImplementedError


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class SquareBuggy(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * 2


class Duck:
    def quack(self):
        return "Quack!"


def make_it_quack_correct(obj):
    return obj.quack()


def make_it_quack_buggy(obj):
    return obj.quack


_check_log = []


def check(description: str, condition: bool) -> bool:
    _check_log.append((description, condition))
    return condition


def run_all_checks() -> dict:
    _check_log.clear()

    check("Square(4).area() == 16", Square(4).area() == 16)
    check("SquareBuggy(4).area() == 16", SquareBuggy(4).area() == 16)

    check("make_it_quack_correct(Duck()) == 'Quack!'", make_it_quack_correct(Duck()) == "Quack!")
    check("make_it_quack_buggy(Duck()) == 'Quack!'", make_it_quack_buggy(Duck()) == "Quack!")

    total = len(_check_log)
    passed = sum(1 for _, ok in _check_log if ok)
    failed = [desc for desc, ok in _check_log if not ok]
    return {"total": total, "passed": passed, "failed": failed}
