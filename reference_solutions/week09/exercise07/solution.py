import xml.etree.ElementTree as ET


def parse_xml_titles(path: str) -> list[str]:
    root = ET.parse(path).getroot()
    return [el.text for el in root.findall(".//title")]


def parse_xml_string_titles(xml_string: str) -> list[str]:
    root = ET.fromstring(xml_string)
    return [el.text for el in root.findall(".//title")]


def count_elements(path: str, tag: str) -> int:
    root = ET.parse(path).getroot()
    return len(root.findall(f".//{tag}"))


def get_attribute_values(path: str, tag: str, attr: str) -> list[str]:
    root = ET.parse(path).getroot()
    return [el.get(attr) for el in root.findall(f".//{tag}")]


def build_simple_xml(items: list[str]) -> str:
    root = ET.Element("items")
    for item in items:
        child = ET.SubElement(root, "item")
        child.text = item
    return ET.tostring(root, encoding="unicode")
