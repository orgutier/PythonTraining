import xml.etree.ElementTree as ET
import datetime


def parse_events_xml(xml_string: str) -> list:
    """
    Parse an <events><event title="..." time="..."/>...</events> document.

    Edge cases handled:
      - No <event> children -> returns [].
      - Every returned "time" is timezone-aware (UTC), regardless of the
        input string's own format, since we explicitly attach it.
    """
    root = ET.fromstring(xml_string)
    events = []
    for el in root.findall(".//event"):
        naive_time = datetime.datetime.fromisoformat(el.get("time"))
        aware_time = naive_time.replace(tzinfo=datetime.timezone.utc)
        events.append({"title": el.get("title"), "time": aware_time})
    return events


def is_naive(dt) -> bool:
    return dt.tzinfo is None


def events_after(events: list, cutoff) -> list:
    matching = [e for e in events if e["time"] > cutoff]
    return sorted(matching, key=lambda e: e["time"])


def build_events_xml(events: list) -> str:
    root = ET.Element("events")
    for event in events:
        ET.SubElement(root, "event", title=event["title"], time=event["time"].isoformat())
    return ET.tostring(root, encoding="unicode")
