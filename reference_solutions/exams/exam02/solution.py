"""
Exam 2 -- Document Archive System (Stages 5-9). Reference solution.
"""
import json
import re
from abc import ABC, abstractmethod
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET


# --------------------------------------------------------------------------- Stage 5

class ArchiveError(Exception):
    pass


class MalformedRecordError(ArchiveError):
    def __init__(self, line):
        super().__init__(f"malformed record line: {line!r}")
        self.line = line


RECORD_PATTERN = re.compile(
    r"^\[(?P<timestamp>[^\]]+)\]\s+AUTHOR=(?P<author>.+?)\s+TITLE=(?P<title>.+?)\s+TAGS=(?P<tags>\S*)$"
)


def parse_record_line(line: str) -> dict:
    match = RECORD_PATTERN.match(line.strip())
    if match is None:
        raise MalformedRecordError(line)
    return match.groupdict()


class ImportSession:
    def __init__(self):
        self.errors = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, MalformedRecordError):
            self.errors += 1
            return True
        return False


def import_documents(lines: list) -> tuple:
    documents = []
    session = ImportSession()
    for line in lines:
        with session:
            documents.append(Document.from_metadata_line(line))
    return documents, session.errors


# --------------------------------------------------------------------------- Stage 6

class TitleDescriptor:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self._name)

    def __set__(self, obj, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("title must be a non-empty string")
        setattr(obj, self._name, value)


# --------------------------------------------------------------------------- Stage 7

class Archivable(ABC):
    @abstractmethod
    def summary(self) -> str:
        ...


class TaggableMixin:
    def __init__(self, tags=None):
        self._tags = set(tags or ())

    def add_tag(self, tag):
        self._tags.add(tag)

    def has_tag(self, tag):
        return tag in self._tags


class TimestampedMixin:
    def __init__(self, created_at=None):
        self.created_at = created_at


class Document(Archivable, TaggableMixin, TimestampedMixin):
    title = TitleDescriptor()

    def __init__(self, title, author, content="", tags=None, created_at=None):
        TaggableMixin.__init__(self, tags)
        TimestampedMixin.__init__(self, created_at)
        self.title = title
        self.author = author
        self._content = content

    @property
    def word_count(self):
        return len(self._content.split())

    @classmethod
    def from_metadata_line(cls, line):
        parsed = parse_record_line(line)
        try:
            created_at = datetime.fromisoformat(parsed["timestamp"])
        except ValueError as exc:
            raise MalformedRecordError(line) from exc
        tags = [t for t in parsed["tags"].split(",") if t]
        return cls(title=parsed["title"], author=parsed["author"], tags=tags, created_at=created_at)

    def summary(self) -> str:
        return f"{self.title} by {self.author} ({self.word_count} words)"

    # ----------------------------------------------------------------- Stage 8

    def __eq__(self, other):
        if not isinstance(other, Document):
            return NotImplemented
        return (self.title, self.author) == (other.title, other.author)

    def __hash__(self):
        return hash((self.title, self.author))

    def __repr__(self):
        return f"Document(title={self.title!r}, author={self.author!r})"

    def __len__(self):
        return self.word_count

    def __iter__(self):
        return iter(self._tags)

    def __contains__(self, tag):
        return self.has_tag(tag)


def archive_summary(items: list) -> list:
    lines = []
    for item in items:
        if isinstance(item, Archivable):
            lines.append(item.summary())
        elif callable(getattr(item, "summary", None)):
            lines.append(item.summary())
        else:
            lines.append(str(item))
    return lines


# --------------------------------------------------------------------------- Stage 9

def scan_archive_directory(root) -> list:
    return sorted(Path(root).rglob("*.txt"))


def documents_to_json(documents: list) -> str:
    def default(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"not JSON serializable: {obj!r}")

    payload = [
        {
            "title": d.title,
            "author": d.author,
            "tags": sorted(d),
            "created_at": d.created_at,
        }
        for d in documents
    ]
    return json.dumps(payload, default=default)


def export_digest_xml(documents: list) -> str:
    root = ET.Element("digest")
    for d in documents:
        doc_el = ET.SubElement(root, "document", title=d.title, author=d.author)
        tags_el = ET.SubElement(doc_el, "tags")
        for tag in sorted(d):
            tag_el = ET.SubElement(tags_el, "tag")
            tag_el.text = tag
    return ET.tostring(root, encoding="unicode")


def parse_digest_xml(xml_string: str) -> list:
    root = ET.fromstring(xml_string)
    result = []
    for doc_el in root.findall("document"):
        tags = [t.text for t in doc_el.findall("./tags/tag")]
        result.append({"title": doc_el.get("title"), "author": doc_el.get("author"), "tags": tags})
    return result


def attach_utc(naive_dt: datetime) -> datetime:
    if naive_dt.tzinfo is not None:
        raise ValueError("expected a naive datetime")
    return naive_dt.replace(tzinfo=timezone.utc)
