import time


class Timer:
    def __enter__(self):
        self._start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self._start
        return False


class SuppressErrors:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and issubclass(exc_type, self.exc_type)


class FileLineCounter:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self._f = open(self.path)
        return self._f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._f.close()
        return False
