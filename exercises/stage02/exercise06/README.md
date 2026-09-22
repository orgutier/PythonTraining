# Ternary Expressions

Implement three functions, each a single-line ternary (`X if COND else Y`) -- no `if` statements:

- `grade_label(score: int) -> str` -- `"pass"` if `score >= 60`, else `"fail"`.
- `abs_value(n: int) -> int` -- `n` if `n >= 0`, else `-n`.
- `clamp_to_range(n: int, lo: int, hi: int) -> int` -- `n` clamped into `[lo, hi]`. Chain two ternaries: `lo if n < lo else hi if n > hi else n`.

See the Study Reference presentation, Topic 2, for the theory.
