import datetime
import xml.etree.ElementTree as ET


def catalog_timestamp() -> str:
    return datetime.datetime.now().isoformat()


def parse_catalog_titles(path: str) -> list[str]:
    root = ET.parse(path).getroot()
    return [el.text for el in root.findall(".//title")]


def parse_catalog_titles_from_string(xml_string: str) -> list[str]:
    root = ET.fromstring(xml_string)
    return [el.text for el in root.findall(".//title")]


def count_catalog_books(path: str) -> int:
    root = ET.parse(path).getroot()
    return len(root.findall(".//book"))
