class GasEngine:
    def start(self) -> str:
        return "Gas engine roaring to life..."


class ElectricEngine:
    def start(self) -> str:
        return "Electric engine humming..."


class Boat:
    def __init__(self, engine):
        self.engine = engine

    def start(self) -> str:
        return self.engine.start()


def swap_engine(boat, new_engine) -> None:
    boat.engine = new_engine
