# XML with ElementTree

Implement four functions using `xml.etree.ElementTree`:

- `parse_xml_titles(path: str) -> list[str]` -- `ET.parse(path).getroot()`, then `[el.text for el in root.findall(".//title")]` (`.//title` finds every `<title>` element anywhere in the tree, at any depth).
- `parse_xml_string_titles(xml_string: str) -> list[str]` -- same idea, but parse an in-memory string with `ET.fromstring(...)` instead of a file with `ET.parse(...)`.
- `count_elements(path: str, tag: str) -> int` -- `len(root.findall(f".//{tag}"))`.
- `get_attribute_values(path: str, tag: str, attr: str) -> list[str]` -- `[el.get(attr) for el in root.findall(f".//{tag}")]`.
- `build_simple_xml(items: list[str]) -> str` -- build a tree from scratch: `root = ET.Element("items")`; for each item, `child = ET.SubElement(root, "item")` then `child.text = item`; return `ET.tostring(root, encoding="unicode")`.

See the Study Reference presentation, Topic 9, for the theory.
