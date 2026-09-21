"""
Challenge 18 - XML Feed to Timezone-Aware Digest
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge18.py / `python tools/cli.py test challenge18`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (ElementTree.fromstring()/findall() for parsing, building a fresh XML tree back out, and explicit naive-to-aware datetime handling).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


import xml.etree.ElementTree as ET
import datetime


def parse_events_xml(xml_string: str) -> list:
    """Parse <event title=... time=...> elements; attach UTC to each naive time. See README."""
    raise NotImplementedError


def is_naive(dt) -> bool:
    """True if dt has no attached timezone."""
    raise NotImplementedError


def events_after(events: list, cutoff) -> list:
    """Events after cutoff (an aware datetime), sorted by time."""
    raise NotImplementedError


def build_events_xml(events: list) -> str:
    """A fresh <events><event title=... time=.../>...</events> string, via ET.Element/SubElement/tostring."""
    raise NotImplementedError
