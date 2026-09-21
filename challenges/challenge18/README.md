# Challenge 18 — XML Feed to Timezone-Aware Digest

**Do this after:** Week 09 (OS, JSON, Datetime, XML)
**Correctness is pytest-tested:** `python tools/cli.py test challenge18` (or `pytest tests/test_challenge18.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

Real event feeds (calendars, webhooks, RSS-style formats) are almost
always XML with a naive timestamp string, and almost every bug in code
that touches them comes from treating a naive time as if it already had a
timezone. This challenge parses one, makes the naive-vs-aware distinction
explicit, filters by it, and writes a fresh feed back out.

Implement:

```python
def parse_events_xml(xml_string: str) -> list:
    """Parse xml_string; for every <event title="..." time="..."> element, build {"title": ..., "time": <aware datetime, UTC>}. The XML's "time" attribute is a naive ISO string -- treat it as UTC and attach that timezone explicitly."""

def is_naive(dt) -> bool:
    """True if dt has no attached timezone."""

def events_after(events: list, cutoff) -> list:
    """Events whose "time" is later than cutoff, sorted by time. cutoff must be an aware datetime -- comparing against a naive one is the caller's mistake, not something this function should hide."""

def build_events_xml(events: list) -> str:
    """A fresh <events> document, one <event title="..." time="..."> per event, "time" written back out as an ISO string."""
```

```python
xml_string = '''<events>
  <event title="Standup" time="2024-03-15T09:00:00"/>
  <event title="Launch" time="2024-03-20T14:00:00"/>
</events>'''

events = parse_events_xml(xml_string)
is_naive(events[0]["time"])   # -> False -- parse_events_xml already made it aware
events_after(events, datetime.datetime(2024, 3, 16, tzinfo=datetime.timezone.utc))
# -> [{"title": "Launch", "time": ...}]
build_events_xml(events)       # -> a fresh <events>...</events> XML string
```

## Constraints on HOW you write it

1. **`parse_events_xml` must use `ET.fromstring(xml_string)` and
   `root.findall(".//event")`** -- not string parsing / regex on the raw
   XML text.
2. **Every parsed time must be made timezone-aware with
   `.replace(tzinfo=datetime.timezone.utc)`** (not `.astimezone(...)`,
   which would *convert* a time that's already aware in some other zone
   -- these input strings are naive, so there's nothing to convert *from*,
   only a timezone to explicitly attach).
3. **`events_after` must NOT silently coerce a naive `cutoff`** -- if the
   caller passes a naive `cutoff`, comparing it against the (now aware)
   event times must raise `TypeError`, same as it would anywhere else in
   Python. Don't wrap the comparison in a `try`/`except` that papers over
   it.
4. **`build_events_xml` must build the tree with `ET.Element`/
   `ET.SubElement`** and return `ET.tostring(root, encoding="unicode")` --
   not manual string concatenation/an f-string template.
5. **A docstring on `parse_events_xml`** listing edge cases: an `<events>`
   element with no `<event>` children (returns `[]`), and confirming
   every returned `"time"` is timezone-aware (never naive) regardless of
   how the input was formatted.
