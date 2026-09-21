import datetime
import xml.etree.ElementTree as ET
import pytest
from challenges.challenge18.solution import (
    parse_events_xml,
    is_naive,
    events_after,
    build_events_xml,
)

FEED = '''<events>
  <event title="Standup" time="2024-03-15T09:00:00"/>
  <event title="Launch" time="2024-03-20T14:00:00"/>
</events>'''


def test_parse_events_xml_basic():
    events = parse_events_xml(FEED)
    assert len(events) == 2
    assert events[0]["title"] == "Standup"


def test_parse_events_xml_times_are_aware():
    events = parse_events_xml(FEED)
    assert all(is_naive(e["time"]) is False for e in events)
    assert events[0]["time"].tzinfo == datetime.timezone.utc


def test_parse_events_xml_no_events():
    events = parse_events_xml("<events></events>")
    assert events == []


def test_events_after_filters_and_sorts():
    events = parse_events_xml(FEED)
    cutoff = datetime.datetime(2024, 3, 16, tzinfo=datetime.timezone.utc)
    result = events_after(events, cutoff)
    assert [e["title"] for e in result] == ["Launch"]


def test_events_after_naive_cutoff_raises_typeerror():
    events = parse_events_xml(FEED)
    naive_cutoff = datetime.datetime(2024, 3, 16)
    with pytest.raises(TypeError):
        events_after(events, naive_cutoff)


def test_build_events_xml_roundtrip():
    events = parse_events_xml(FEED)
    xml_out = build_events_xml(events)
    root = ET.fromstring(xml_out)
    rebuilt = root.findall(".//event")
    assert len(rebuilt) == 2
    assert rebuilt[0].get("title") == "Standup"
