class LoggingMixin:
    def log(self, message: str) -> str:
        return f"[{self.__class__.__name__}] {message}"


class SerializableMixin:
    def to_dict(self) -> dict:
        return dict(self.__dict__)


class Widget(LoggingMixin, SerializableMixin):
    def __init__(self, name):
        self.name = name
