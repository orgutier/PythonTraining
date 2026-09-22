class Engine:
    def start(self) -> str:
        return "Engine starting..."


class Boat:
    def __init__(self, engine):
        self.engine = engine

    def start(self) -> str:
        return self.engine.start()


class Duck:
    def quack(self) -> str:
        return "Quack!"


class Person:
    def quack(self) -> str:
        return "I'm quacking like a duck!"


def make_it_quack(obj) -> str:
    return obj.quack()


def is_duck_instance(obj) -> bool:
    return isinstance(obj, Duck)
