"""
OS, JSON, Datetime, XML -- XML with ElementTree
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week09_exercise07.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week09/exercise07/ and import it as a submodule (e.g.
`from exercises.week09.exercise07 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import xml.etree.ElementTree as ET


def parse_xml_titles(path: str) -> list[str]:
    """ET.parse(path).getroot(), then every <title> element's text."""
    raise NotImplementedError


def parse_xml_string_titles(xml_string: str) -> list[str]:
    """Same as parse_xml_titles, but via ET.fromstring(xml_string)."""
    raise NotImplementedError


def count_elements(path: str, tag: str) -> int:
    """How many <tag> elements exist anywhere in the tree."""
    raise NotImplementedError


def get_attribute_values(path: str, tag: str, attr: str) -> list[str]:
    """The attr attribute of every <tag> element."""
    raise NotImplementedError


def build_simple_xml(items: list[str]) -> str:
    """<items><item>...</item>...</items>, via ET.Element/SubElement/tostring."""
    raise NotImplementedError
