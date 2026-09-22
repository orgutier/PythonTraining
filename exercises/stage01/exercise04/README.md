# Boolean Logic

Implement four small boolean/string functions:

- `can_enter_venue(age, has_ticket: bool, is_vip: bool) -> bool` -- `True` only if `age` is known (`age is not None`) **and** `age >= 18`, **and** (`has_ticket` **or** `is_vip`).
- `access_level(has_ticket: bool, is_vip: bool, is_staff: bool) -> str` -- return `"backstage"` if `is_staff` **or** `is_vip`; else `"general"` if `has_ticket`; else `"denied"`.
- `is_valid_choice(choice, allowed: list[str]) -> bool` -- `True` only if `choice` is a `str` (`isinstance`) **and** `choice` is **in** `allowed` **and not** an empty string.
- `toggle_flag(flag: bool) -> bool` -- **must** use the literal keywords `True`/`False` (via an `if flag is True: ... else: ...`), not the `not` operator, even though `not flag` would be shorter. The point here is practicing the `True`/`False` literals directly, and `is True` as the idiomatic way to compare against the singleton.

See the Study Reference presentation, Topic 1, for the theory.
