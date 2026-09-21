import functools
import pytest
from challenges.challenge06.solution import (
    stream_batches,
    process_batch,
    get_total_processed,
    reset_total_processed,
    make_scaled_transform,
)


def test_stream_batches_chunks_with_short_last_chunk():
    assert list(stream_batches([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]


def test_stream_batches_is_a_real_generator():
    gen = stream_batches([1, 2, 3], 1)
    assert hasattr(gen, "__next__")
    assert next(gen) == [1]


def test_stream_batches_empty_data():
    assert list(stream_batches([], 3)) == []


def test_stream_batches_positional_only():
    with pytest.raises(TypeError):
        list(stream_batches(data=[1, 2], size=1))


def test_process_batch_default_transform_and_global_total():
    reset_total_processed()
    assert process_batch([1, 2, 3]) == [1, 2, 3]
    assert get_total_processed() == 3


def test_process_batch_with_transform_accumulates_total():
    reset_total_processed()
    process_batch([1, 2, 3])
    process_batch([4, 5], transform=make_scaled_transform(10))
    assert get_total_processed() == 5


def test_process_batch_batch_is_positional_only():
    with pytest.raises(TypeError):
        process_batch(batch=[1, 2])


def test_process_batch_transform_is_keyword_only():
    with pytest.raises(TypeError):
        process_batch([1, 2], lambda x: x)


def test_make_scaled_transform_uses_functools_partial():
    triple = make_scaled_transform(3)
    assert triple(4) == 12
    assert isinstance(triple, functools.partial)
