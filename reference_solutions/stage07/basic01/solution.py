class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"


class Cat(Animal):
    def __init__(self, name: str, indoor: bool = True):
        super().__init__(name)
        self.indoor = indoor

    def speak(self) -> str:
        return f"{self.name} says Meow!"


def describe_animal(animal) -> str:
    return animal.speak()


class Duck:
    def quack(self) -> str:
        return "Quack!"


class Person:
    def quack(self) -> str:
        return "I'm quacking like a duck!"


def make_it_quack(obj) -> str:
    return obj.quack()
