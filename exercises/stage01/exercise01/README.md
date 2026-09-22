# Profile Basics

Implement three small functions:

- `build_profile(name: str, age: int, height_m: float, is_student: bool) -> dict` -- return a dict with keys `name`, `age`, `height_m`, `is_student` holding those four values unchanged.
- `value_kind(x) -> str` -- return `type(x).__name__` (e.g. `"int"`, `"str"`). This is your first use of `type()`; Exercise 3 goes deeper.
- `display_profile(profile: dict) -> None` -- `print()` a single line in the exact form `"NAME is AGE years old, HEIGHT_Mm tall, student=IS_STUDENT"` (e.g. `"Ada is 30 years old, 1.7m tall, student=False"`). Nothing to return.

All four parameters above use annotated types (`name: str`, `age: int`, ...) -- keep doing that in every function you write this stage; it's not optional decoration, `isinstance()` checks later in the stage assume callers respect it.

See the Study Reference presentation, Topic 1, for the theory.
