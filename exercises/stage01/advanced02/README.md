# Big Numbers and String Identity

Given, don't modify:

```python
base_text = "97"
exponent_text = "42"
```

Using Advanced-tier tools, write plain top-level code that computes:

- `base`, `exponent` (`int`).
- `huge_power` -- `base ** exponent`. Python integers have arbitrary precision, so this doesn't overflow no matter how large it gets.
- `huge_power_digit_count` -- `len(str(huge_power))`, proving `huge_power` is genuinely bigger than any fixed-width integer could hold.
- `small_int_a`, `small_int_b` -- both set to the literal `100`.
- `small_ints_share_identity` -- `small_int_a is small_int_b`. CPython caches small integers (`-5` to `256`), so this is `True`.
- `large_int_from_literal`, `large_int_from_conversion` -- the first is the literal `1_000_000`; the second is `int("1000000")` (built at runtime, **not** a second literal -- two identical literals in the same file can get folded into a single cached object by the compiler, which would defeat the point of this exercise).
- `large_ints_share_identity` -- `large_int_from_literal is large_int_from_conversion`. Large integers are **not** guaranteed to be cached, so (with the runtime-constructed value above) this is `False`.
- `string_literal_a`, `string_literal_b` -- both set to the literal `"python_stage01"`.
- `string_literals_share_identity` -- `string_literal_a is string_literal_b`. Simple string literals are interned at compile time, so this is `True`.
- `string_built_at_runtime` -- `"".join(["python_", "stage01"])` (same text, built dynamically).
- `runtime_string_shares_identity` -- `string_literal_a is string_built_at_runtime`. Dynamically built strings are **not** automatically interned, so this is `False` even though the two strings are `==`-equal.

Finish with one `print()` call reporting `huge_power_digit_count`.
