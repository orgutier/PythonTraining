import pytest
from challenges.challenge05.solution import (
    make_pipeline,
    count_calls,
    memoize,
    cached_expensive,
)


def test_pipeline_register_and_run():
    register, run = make_pipeline()

    @register("double")
    def double(x):
        return x * 2

    assert run("double", 5) == 10
    assert double.__name__ == "double"


def test_pipeline_run_missing_handler_raises_keyerror():
    register, run = make_pipeline()
    with pytest.raises(KeyError):
        run("missing")


def test_pipeline_instances_are_independent():
    register_a, run_a = make_pipeline()
    register_b, run_b = make_pipeline()

    @register_a("greet")
    def greet(name):
        return f"hi {name}"

    assert run_a("greet", "Ada") == "hi Ada"
    with pytest.raises(KeyError):
        run_b("greet", "Ada")


def test_count_calls_tracks_count_and_kwargs():
    @count_calls
    def add(a, b=0):
        return a + b

    assert add(1, b=2) == 3
    assert add(1) == 1
    assert add.call_count == 2


def test_memoize_caches_by_args_and_kwargs():
    calls = []

    @memoize
    def slow_add(a, b=0):
        calls.append((a, b))
        return a + b

    assert slow_add(1, 2) == 3
    assert slow_add(1, 2) == 3
    assert slow_add(1, b=2) == 3
    assert len(calls) == 2  # (1,2) positional cached separately from b=2 keyword


def test_cached_expensive_correctness_and_caching():
    assert cached_expensive(16) == 4.0
    assert hasattr(cached_expensive, "cache_info")


def test_cached_expensive_precision_is_keyword_only():
    with pytest.raises(TypeError):
        cached_expensive(16, 3)
