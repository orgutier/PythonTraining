# Library Catalog: Dates and XML

A tiny library catalog stored as XML, plus a timestamp helper. Given XML shaped like:

```xml
<library>
  <book id="1"><title>Dune</title></book>
  <book id="2"><title>Foundation</title></book>
</library>
```

Implement:

- `catalog_timestamp() -> str` -- `datetime.datetime.now().isoformat()`.
- `parse_catalog_titles(path: str) -> list[str]` -- `ET.parse(path).getroot()`, then `[el.text for el in root.findall(".//title")]` (`.//title` finds every `<title>` element anywhere in the tree, at any depth).
- `parse_catalog_titles_from_string(xml_string: str) -> list[str]` -- the same idea, but parse an in-memory string with `ET.fromstring(...)` instead of a file with `ET.parse(...)`.
- `count_catalog_books(path: str) -> int` -- `len(root.findall(".//book"))`.

See the Study Reference presentation, Topic 9 (Basic tier), for the theory.
