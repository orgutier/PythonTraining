import pytest
from challenges.challenge01.solution import (
    parse_config_line,
    load_config,
    describe_types,
    merge_configs,
)


def test_parse_config_line_int():
    assert parse_config_line("PORT=8080") == ("PORT", 8080)


def test_parse_config_line_float():
    assert parse_config_line("RATE = 3.14 ") == ("RATE", 3.14)


def test_parse_config_line_bool_mixed_case():
    assert parse_config_line("DEBUG=True") == ("DEBUG", True)
    assert parse_config_line("VERBOSE=FALSE") == ("VERBOSE", False)


def test_parse_config_line_none_for_empty_value():
    assert parse_config_line("TIMEOUT=") == ("TIMEOUT", None)


def test_parse_config_line_str_fallback():
    assert parse_config_line("NAME=myapp") == ("NAME", "myapp")


def test_parse_config_line_splits_on_first_equals_only():
    assert parse_config_line("URL=http://example.com?x=1") == ("URL", "http://example.com?x=1")


def test_parse_config_line_negative_int_and_float():
    assert parse_config_line("OFFSET=-5") == ("OFFSET", -5)
    assert parse_config_line("DELTA=-2.5") == ("DELTA", -2.5)


def test_parse_config_line_no_equals_raises():
    with pytest.raises(ValueError):
        parse_config_line("not a config line")


def test_load_config_skips_blank_lines():
    result = load_config(["PORT=8080", "  ", "NAME=app", ""])
    assert result == {"PORT": 8080, "NAME": "app"}


def test_load_config_duplicate_keys_last_wins():
    result = load_config(["PORT=8080", "PORT=9090"])
    assert result == {"PORT": 9090}


def test_load_config_does_not_mutate_input_list():
    lines = ["PORT=8080"]
    original = list(lines)
    load_config(lines)
    assert lines == original


def test_describe_types_distinguishes_bool_from_int():
    config = {"a": True, "b": 1, "c": 1.5, "d": "x", "e": None}
    assert describe_types(config) == {
        "a": "bool", "b": "int", "c": "float", "d": "str", "e": "NoneType",
    }


def test_merge_configs_override_wins_and_returns_new_dict():
    base = {"a": 1, "b": 2}
    override = {"b": 20, "c": 3}
    result = merge_configs(base, override)
    assert result == {"a": 1, "b": 20, "c": 3}
    assert result is not base
    assert result is not override
    assert base == {"a": 1, "b": 2}
    assert override == {"b": 20, "c": 3}
