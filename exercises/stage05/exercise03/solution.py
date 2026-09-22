"""
Files, Exceptions, Regex -- Exception Chaining
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage05_exercise03.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage05/exercise03/ and import it as a submodule (e.g.
`from exercises.stage05.exercise03 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class ConfigError(Exception):
    pass


class ConfigParseError(ConfigError):
    pass


def load_config_value(raw: str) -> int:
    """int(raw); on ValueError, raise ConfigParseError(...) from e."""
    raise NotImplementedError


class NetworkError(Exception):
    pass


class RetryError(Exception):
    pass


def fetch_with_retry_simulation(should_fail: bool) -> str:
    """"ok" normally; if should_fail, raise NetworkError, catch it, raise RetryError(...) from e."""
    raise NotImplementedError


class ScoreError(Exception):
    pass


def parse_score(raw: str) -> int:
    """int(raw) (chain ValueError via `from e`); validate 0..100 (raise ... from None if not)."""
    raise NotImplementedError
