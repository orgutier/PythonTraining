"""
Tests for Exam 2 -- Document Archive System (Stages 5-9).
"""
import json
from datetime import datetime, timezone
import pytest
from exams.exam02.solution import (
    ArchiveError,
    MalformedRecordError,
    parse_record_line,
    ImportSession,
    import_documents,
    TitleDescriptor,
    Archivable,
    TaggableMixin,
    TimestampedMixin,
    Document,
    archive_summary,
    scan_archive_directory,
    documents_to_json,
    export_digest_xml,
    parse_digest_xml,
    attach_utc,
)

GOOD_LINE = "[2024-01-15T10:30:00] AUTHOR=Jane Doe TITLE=Quarterly Report TAGS=finance,q1"
BAD_LINE = "this is not a record line at all"


# --------------------------------------------------------------------------- Stage 5

def test_malformed_record_error_is_archive_error():
    assert issubclass(MalformedRecordError, ArchiveError)


def test_parse_record_line_extracts_named_groups():
    parsed = parse_record_line(GOOD_LINE)
    assert parsed["author"] == "Jane Doe"
    assert parsed["title"] == "Quarterly Report"
    assert parsed["tags"] == "finance,q1"
    assert parsed["timestamp"] == "2024-01-15T10:30:00"


def test_parse_record_line_raises_on_bad_line():
    with pytest.raises(MalformedRecordError):
        parse_record_line(BAD_LINE)


def test_import_session_suppresses_and_counts():
    session = ImportSession()
    with session:
        raise MalformedRecordError("x")
    assert session.errors == 1
    with session:
        pass
    assert session.errors == 1
    with session:
        raise MalformedRecordError("y")
    assert session.errors == 2


def test_import_session_does_not_suppress_other_errors():
    session = ImportSession()
    with pytest.raises(ValueError):
        with session:
            raise ValueError("unrelated")


def test_import_documents_skips_malformed_and_counts():
    documents, errors = import_documents([GOOD_LINE, BAD_LINE, GOOD_LINE])
    assert len(documents) == 2
    assert errors == 1
    assert all(isinstance(d, Document) for d in documents)


# --------------------------------------------------------------------------- Stage 6

def test_title_descriptor_rejects_empty_string():
    doc = Document(title="Valid", author="A")
    with pytest.raises(ValueError):
        doc.title = ""


def test_title_descriptor_rejects_non_string():
    doc = Document(title="Valid", author="A")
    with pytest.raises(ValueError):
        doc.title = 123


def test_document_word_count_property():
    doc = Document(title="T", author="A", content="one two three")
    assert doc.word_count == 3


def test_document_from_metadata_line_builds_document():
    doc = Document.from_metadata_line(GOOD_LINE)
    assert doc.title == "Quarterly Report"
    assert doc.author == "Jane Doe"
    assert doc.created_at == datetime(2024, 1, 15, 10, 30, 0)
    assert "finance" in doc


def test_document_from_metadata_line_chains_malformed_timestamp():
    bad_timestamp_line = "[not-a-date] AUTHOR=A TITLE=T TAGS="
    with pytest.raises(MalformedRecordError) as exc_info:
        Document.from_metadata_line(bad_timestamp_line)
    assert exc_info.value.__cause__ is not None


# --------------------------------------------------------------------------- Stage 7

def test_document_is_archivable_and_mixins():
    doc = Document(title="T", author="A", tags=["x"])
    assert isinstance(doc, Archivable)
    assert isinstance(doc, TaggableMixin)
    assert isinstance(doc, TimestampedMixin)


def test_document_summary():
    doc = Document(title="T", author="A", content="a b")
    assert "T" in doc.summary()
    assert "A" in doc.summary()


def test_archivable_cannot_be_instantiated_directly():
    with pytest.raises(TypeError):
        Archivable()


def test_archive_summary_dispatches_by_isinstance_and_duck_typing():
    class NotArchivable:
        def summary(self):
            return "duck-typed summary"

    class NoSummaryAtAll:
        def __str__(self):
            return "plain str"

    doc = Document(title="T", author="A", content="a b")
    results = archive_summary([doc, NotArchivable(), NoSummaryAtAll()])
    assert results[0] == doc.summary()
    assert results[1] == "duck-typed summary"
    assert results[2] == "plain str"


# --------------------------------------------------------------------------- Stage 8

def test_document_equality_by_title_and_author():
    a = Document(title="T", author="A")
    b = Document(title="T", author="A", content="different content")
    c = Document(title="Other", author="A")
    assert a == b
    assert a != c


def test_document_hash_consistent_with_eq():
    a = Document(title="T", author="A")
    b = Document(title="T", author="A")
    assert hash(a) == hash(b)


def test_document_repr_includes_title_and_author():
    doc = Document(title="T", author="A")
    r = repr(doc)
    assert "T" in r and "A" in r


def test_document_len_is_word_count():
    doc = Document(title="T", author="A", content="one two three four")
    assert len(doc) == 4


def test_document_iter_yields_tags():
    doc = Document(title="T", author="A", tags=["x", "y"])
    assert set(iter(doc)) == {"x", "y"}


def test_document_contains_tag():
    doc = Document(title="T", author="A", tags=["finance"])
    assert "finance" in doc
    assert "nope" not in doc


# --------------------------------------------------------------------------- Stage 9

def test_scan_archive_directory_finds_txt_files(tmp_path):
    (tmp_path / "a.txt").write_text("hello")
    (tmp_path / "b.md").write_text("skip me")
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "c.txt").write_text("nested")
    found = scan_archive_directory(tmp_path)
    names = sorted(p.name for p in found)
    assert names == ["a.txt", "c.txt"]


def test_documents_to_json_serializes_datetime():
    doc = Document(title="T", author="A", tags=["x"], created_at=datetime(2024, 1, 1, 0, 0, 0))
    result = json.loads(documents_to_json([doc]))
    assert result[0]["title"] == "T"
    assert result[0]["created_at"] == "2024-01-01T00:00:00"
    assert result[0]["tags"] == ["x"]


def test_export_and_parse_digest_xml_roundtrip():
    doc = Document(title="T", author="A", tags=["x", "y"])
    xml_string = export_digest_xml([doc])
    assert "<digest>" in xml_string
    parsed = parse_digest_xml(xml_string)
    assert parsed == [{"title": "T", "author": "A", "tags": ["x", "y"]}]


def test_attach_utc_adds_timezone():
    naive = datetime(2024, 1, 1, 12, 0, 0)
    aware = attach_utc(naive)
    assert aware.tzinfo == timezone.utc
    assert aware.replace(tzinfo=None) == naive


def test_attach_utc_rejects_already_aware():
    aware = datetime(2024, 1, 1, tzinfo=timezone.utc)
    with pytest.raises(ValueError):
        attach_utc(aware)
