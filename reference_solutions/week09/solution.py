import json
from datetime import datetime, timezone
import xml.etree.ElementTree as ET


def read_config(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def write_config(path: str, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f)


def timestamp_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_xml_titles(xml_string: str) -> list[str]:
    root = ET.fromstring(xml_string)
    return [el.text for el in root.findall(".//title")]
