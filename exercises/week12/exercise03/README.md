# Threading Basics

Implement:

- `run_in_background(func, *args) -> threading.Thread` -- `t = threading.Thread(target=func, args=args)`; `t.start()`; return `t`.
- `wait_for_all(threads: list) -> None` -- `for t in threads: t.join()`.
- `run_and_wait(funcs: list) -> None` -- create one `threading.Thread(target=f)` per function in `funcs`, `.start()` every one, **then** `.join()` every one (start them all first, so they actually run concurrently -- starting and immediately joining each one in the same loop would run them one at a time, defeating the point).

See the Study Reference presentation, Topic 12, for the theory.
