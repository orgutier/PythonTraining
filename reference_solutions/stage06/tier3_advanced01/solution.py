class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self._name)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self._name[1:]} must be >= 0")
        setattr(obj, self._name, value)


class Product:
    price = PositiveNumber()

    def __init__(self, name, price):
        self.name = name
        self.price = price
