# Bus Route Ticket Counter

A bus's boarding log is a list of event strings -- given, don't modify:

```python
events = ["IN:2", "IN:1", "OUT:1", "SKIP", "BAD", "IN:5", "OUT:2", "IN:0", "OUT:10"]
capacity = 6
```

Each event is `"IN:n"` (n people board), `"OUT:n"` (n people leave), `"SKIP"` (an empty stop, nothing happens), or -- anything else -- malformed data to be silently ignored.

Process `events` **in order with a `while` loop** (an index cursor, not a `for`), tracking `passengers` starting at `0`:

- `"IN:n"` -- if adding `n` would push `passengers` over `capacity`, the trip ends immediately: set `trip_ended_early = True` and `break` (don't add those n people at all). Otherwise add them.
- `"OUT:n"` -- subtract `n` from `passengers`; if that would go negative, clamp it to `0` (people can't un-leave).
- `"SKIP"` -- advance the cursor and `continue` immediately, no other change.
- anything else -- explicitly do nothing (`pass`); this is malformed data, not a stop that affects the count.

`trip_ended_early` must start `False` (only the overflow case sets it `True`).

Then, **separately**, using nested `for` loops (not the `while` loop above), compute the bus's total seat count: given `sections = 3`, `rows_per_section = 2`, `seats_per_row = 2` (all given, don't modify), loop over sections and, for each, over its rows, adding `seats_per_row` to a running `total_seats` each time. Then set `capacity_is_valid = capacity <= total_seats`.
