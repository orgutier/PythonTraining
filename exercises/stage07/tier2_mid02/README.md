# Composition and Swappable Engines

Two interchangeable engines and a boat that **has an** engine, rather than **is an** engine -- the point of composition. Implement:

- `GasEngine.start(self) -> str` -- `"Gas engine roaring to life..."`.
- `ElectricEngine.start(self) -> str` -- `"Electric engine humming..."`.
- `Boat.__init__(self, engine)` -- store `self.engine = engine` (**composition**: `Boat` doesn't extend `GasEngine`/`ElectricEngine`, it just *holds one*). `start(self) -> str` -- `self.engine.start()` (delegates to whichever engine it was given).
- `swap_engine(boat, new_engine) -> None` -- `boat.engine = new_engine`.

This is what composition buys you that inheritance can't: `swap_engine` changes a `Boat`'s behavior **at runtime**, with no class hierarchy to touch at all. Rewriting this with inheritance would mean either a `GasBoat`/`ElectricBoat` class pair (can't switch after construction) or multiple inheritance from both engine classes at once (`Boat` would *be* both kinds of engine, which doesn't make sense).

See the Study Reference presentation, Topic 7 (Mid tier), for the theory.
