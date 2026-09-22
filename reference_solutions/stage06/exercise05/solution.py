class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self._name)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self._name[1:]} must be >= 0")
        setattr(obj, self._name, value)


class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self._name)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self._name[1:]} must be a {self.expected_type.__name__}")
        setattr(obj, self._name, value)


class Product:
    price = PositiveNumber()

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Person:
    name = Typed(str)
    age = Typed(int)

    def __init__(self, name, age):
        self.name = name
        self.age = age
