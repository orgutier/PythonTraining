import threading


class SafeCounter:
    def __init__(self):
        self._lock = threading.Lock()
        self._value = 0

    def increment(self) -> None:
        with self._lock:
            self._value += 1

    @property
    def value(self) -> int:
        return self._value


class SafeList:
    def __init__(self):
        self._lock = threading.Lock()
        self._items = []

    def append_safe(self, item) -> None:
        with self._lock:
            self._items.append(item)

    @property
    def items(self) -> list:
        return self._items


def transfer_funds(accounts: dict, lock: threading.Lock, from_key, to_key, amount) -> None:
    with lock:
        accounts[from_key] -= amount
        accounts[to_key] += amount


def parallel_increment(counter, times: int, num_threads: int) -> None:
    per_thread = times // num_threads

    def worker():
        for _ in range(per_thread):
            counter.increment()

    threads = [threading.Thread(target=worker) for _ in range(num_threads)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
