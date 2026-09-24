# Digital Clock Decoder

A monitoring system logs elapsed time as a raw seconds count, and a daylight-saving flag as literal text -- both as strings, don't modify:

```python
total_seconds_text = "9384"
is_daylight_saving_text = "False"
```

Using only Basic-tier tools, write plain top-level code that computes:

- `total_seconds` -- `total_seconds_text` cast to `int`.
- `hours`, `minutes`, `seconds` -- decompose `total_seconds` into hours/minutes/seconds using `//` and `%` (chain them: get `hours` and a remainder, then get `minutes` from that remainder and a second remainder, then `seconds` from that).
- `is_daylight_saving` -- a genuine `bool`, `True` only if `is_daylight_saving_text` is literally the text `"True"`. **Do not write `bool(is_daylight_saving_text)`** -- in Python, `bool("False")` is `True`, because *any* non-empty string is truthy, including the string `"False"` itself. Compare the text against the string `"True"` instead (`==`) to get a correct result.

Finish with one `print()` call (concatenation + `str()`, no f-strings yet) summarizing the decoded time, e.g. something like `"9384s = " + str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s"`.
