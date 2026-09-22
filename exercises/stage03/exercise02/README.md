# Args and Kwargs

Implement:

- `sum_all(*args: int) -> int` -- sum any number of positional arguments: `sum_all(1, 2, 3) == 6`.
- `build_config(**kwargs) -> dict` -- return the keyword arguments as a plain dict: `build_config(host="x", port=1) == {"host": "x", "port": 1}`.
- `describe_call(*args, **kwargs) -> str` -- return `f"args={args}, kwargs={kwargs}"` (both packed into their respective tuple/dict).

See the Study Reference presentation, Topic 3, for the theory.
