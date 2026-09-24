"""
Files, Exceptions, Regex -- Config and Log Parsers
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage05_mid02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage05/mid02/ and import it as a submodule (e.g.
`from exercises.stage05.mid02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import re

LINE_PATTERN = re.compile(r"(?P<key>\w+)=(?P<value>.+)")
DATE_PATTERN = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")
LOG_PATTERN = re.compile(r"(?P<level>\w+): (?P<message>.+)")


def parse_config_line(line: str) -> dict:
    """LINE_PATTERN.match(line).groupdict(); ValueError if no match."""
    raise NotImplementedError


def find_date(text: str) -> dict:
    """DATE_PATTERN.search(text).groupdict(); ValueError if none found."""
    raise NotImplementedError


def parse_log_entry(line: str) -> dict:
    """LOG_PATTERN.match(line).groupdict(); ValueError if no match."""
    raise NotImplementedError
