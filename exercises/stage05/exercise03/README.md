# Exception Chaining

Implement three functions that catch a low-level exception and re-raise a higher-level, more meaningful one **chained** to it with `raise ... from ...`:

- `ConfigError(Exception)` / `ConfigParseError(ConfigError)` -- `load_config_value(raw: str) -> int`: `try: return int(raw)` `except ValueError as e: raise ConfigParseError(f"bad config value: {raw!r}") from e`.
- `NetworkError(Exception)` / `RetryError(Exception)` -- `fetch_with_retry_simulation(should_fail: bool) -> str`: if `should_fail`, `raise NetworkError("connection refused")`; catch that and `raise RetryError("failed after retries") from e`; if `should_fail` is `False`, just `return "ok"`.
- `ScoreError(Exception)` -- `parse_score(raw: str) -> int`: parse `raw` as `int`; on `ValueError as e`, `raise ScoreError(f"invalid score: {raw!r}") from e`. Then if the parsed score isn't in `0..100`, `raise ScoreError(f"score out of range: {score}") from None` -- `from None` **explicitly suppresses** chaining (there's no underlying exception to chain to here, just a validation failure), which is the other legal form of this syntax.

The chained exception is available afterward as `exc.__cause__` -- that's what the tests check.

See the Study Reference presentation, Topic 5, for the theory.
