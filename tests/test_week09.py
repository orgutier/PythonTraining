import re
from exercises.week09.solution import (
    read_config,
    write_config,
    timestamp_now,
    parse_xml_titles,
)


def test_config_roundtrip(tmp_path):
    p = tmp_path / "config.json"
    write_config(str(p), {"a": 1})
    assert read_config(str(p)) == {"a": 1}


def test_timestamp_now_format():
    ts = timestamp_now()
    assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", ts)


def test_parse_xml_titles():
    xml = (
        "<library>"
        "<book><title>A</title></book>"
        "<book><title>B</title></book>"
        "<book><title>C</title></book>"
        "</library>"
    )
    assert parse_xml_titles(xml) == ["A", "B", "C"]
