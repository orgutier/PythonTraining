"""
OS, JSON, Datetime, XML -- Library Catalog: Dates and XML
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage09_tier1_basic02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage09/tier1_basic02/ and import it as a submodule (e.g.
`from exercises.stage09.tier1_basic02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import datetime
import xml.etree.ElementTree as ET


def catalog_timestamp() -> str:
    """datetime.datetime.now().isoformat()."""
    raise NotImplementedError


def parse_catalog_titles(path: str) -> list[str]:
    """ET.parse(path).getroot(), then every <title> element's text."""
    raise NotImplementedError


def parse_catalog_titles_from_string(xml_string: str) -> list[str]:
    """Same as parse_catalog_titles, but via ET.fromstring(xml_string)."""
    raise NotImplementedError


def count_catalog_books(path: str) -> int:
    """How many <book> elements exist anywhere in the tree."""
    raise NotImplementedError
