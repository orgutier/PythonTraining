import dataclasses


@dataclasses.dataclass
class Point:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


@dataclasses.dataclass(frozen=True)
class FrozenPoint:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


@dataclasses.dataclass
class TaggedItem:
    name: str
    tags: list = dataclasses.field(default_factory=list)

    def add_tag(self, tag: str) -> None:
        self.tags.append(tag)
