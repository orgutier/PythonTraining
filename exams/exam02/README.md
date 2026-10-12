# Exam 2 -- Document Archive System

Covers: Stages 5-9

An evaluation exam, not a graded exercise: it exists to prove you can
combine Stage 5-9 material (Files/Exceptions/Regex, OOP I, OOP II, the
Data Model, and OS/JSON/Datetime/XML) in one connected system, not five
separate snippets. Unlike the stage exercises, this is not required to
move on -- treat it as a checkpoint.

Build a small document-archive system: parse metadata records with
regex, model each document as a class built from an ABC and mixins with
a full set of dunders, scan a real directory tree for files, and export
the whole archive as both JSON and XML.

## What to implement

All of it lives in `solution.py`.

### Stage 5 -- Files, Exceptions, Regex

- **`ArchiveError`** / **`MalformedRecordError(ArchiveError)`** -- a
  two-level custom exception hierarchy. `MalformedRecordError` carries
  the offending `line`.
- **`parse_record_line(line)`** -- a compiled regex with **named groups**
  matching lines shaped
  `"[2024-01-15T10:30:00] AUTHOR=Jane Doe TITLE=Quarterly Report TAGS=finance,q1"`
  (`timestamp`, `author`, `title`, `tags`). Return `match.groupdict()`;
  raise `MalformedRecordError(line)` if the line doesn't match.
- **`ImportSession`** -- a class-based context manager
  (`__enter__`/`__exit__`) that suppresses any `MalformedRecordError`
  raised inside its `with` block instead of letting it propagate, and
  counts each one in `self.errors`. Reusable across a loop -- `errors`
  accumulates across every `with session:` block, and is **not** reset
  on `__enter__`, only in `__init__`.
- **`import_documents(lines)`** -- for each line, use `ImportSession` and
  `Document.from_metadata_line` (below) to build a `Document`; a
  malformed line is skipped (counted, not raised). Return
  `(documents, error_count)`.

### Stage 6 -- OOP I

- **`TitleDescriptor`** -- a validating descriptor (uses
  `__set_name__`/`__get__`/`__set__`): rejects a `title` that isn't a
  non-empty `str`, raising `ValueError`.
- **`Document`** (see also Stages 7-8 below) -- uses `TitleDescriptor` for
  `title`, keeps its body in a private `_content` attribute, exposes a
  computed **`@property word_count`** (`len(self._content.split())`), and
  a **`@classmethod from_metadata_line(cls, line)`** alternate
  constructor: parses the line with `parse_record_line`, converts
  `timestamp` via `datetime.fromisoformat`, and **chains**
  (`raise ... from ...`) any `ValueError` from that conversion into a
  `MalformedRecordError`.

### Stage 7 -- OOP II

- **`Archivable(abc.ABC)`** -- an abstract base with one abstract method,
  `summary() -> str`.
- **`TaggableMixin`** / **`TimestampedMixin`** -- mixins providing tag
  storage (`add_tag`, `has_tag`) and a `created_at` attribute,
  respectively.
- **`Document(Archivable, TaggableMixin, TimestampedMixin)`** --
  multiple inheritance, cooperating through each mixin's own `__init__`
  (not a single blind `super().__init__()` chain -- call each mixin's
  initializer explicitly). Implements `summary()`.
- **`archive_summary(items)`** -- for each item: if it's an
  `Archivable`, call `.summary()`; otherwise, duck-type -- if it has a
  callable `summary` attribute, call that; otherwise fall back to
  `str(item)`. Returns the list of resulting strings.

### Stage 8 -- The Python Data Model

`Document` also implements:

- `__eq__` -- equal iff `title` and `author` match.
- `__hash__` -- consistent with `__eq__`.
- `__repr__` -- unambiguous, includes title and author.
- `__len__` -- returns `word_count`.
- `__iter__` -- iterates the document's tags.
- `__contains__` -- tag membership (`"finance" in doc`).

### Stage 9 -- OS, JSON, Datetime, XML

- **`scan_archive_directory(root)`** -- `pathlib.Path(root).rglob("*.txt")`,
  returned as a sorted `list` of `Path` objects.
- **`documents_to_json(documents)`** -- `json.dumps` of
  `[{"title", "author", "tags", "created_at"}, ...]`, using a
  `default=` callback to serialize each `datetime` (`.isoformat()`).
- **`export_digest_xml(documents)`** -- build an
  `<digest><document title="..." author="..."><tags><tag>...</tag></tags></document>...</digest>`
  tree with `xml.etree.ElementTree`, returned as a string
  (`ET.tostring(root, encoding="unicode")`).
- **`parse_digest_xml(xml_string)`** -- parse that XML back
  (`ET.fromstring`, `.findall()`) into
  `[{"title", "author", "tags": [...]}, ...]`.
- **`attach_utc(naive_dt)`** -- explicitly attach `timezone.utc` to a
  naive `datetime` (raise `ValueError` if it's already aware).

## Grading

`python tools/cli.py test exam02` runs `tests/test_exam02.py` -- the same
correctness check as any exercise or challenge. A green run only proves
the happy path and documented edge cases; whether you actually used the
required technique (a descriptor, cooperative mixins, `raise ... from
...`, etc.) for each piece is a code-review job pytest can't fully
verify.
