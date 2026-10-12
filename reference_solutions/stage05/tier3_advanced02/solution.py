import contextlib
import time


@contextlib.contextmanager
def temporary_value(obj, attr, value):
    original = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, original)


@contextlib.contextmanager
def suppress_and_log(log: list, *exc_types):
    try:
        yield
    except exc_types as e:
        log.append(str(e))


@contextlib.contextmanager
def timing_block(results: list):
    start = time.time()
    try:
        yield
    finally:
        results.append(time.time() - start)
