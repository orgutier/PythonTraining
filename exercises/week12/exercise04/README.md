# Locks and Race Conditions

Implement three things protected by a `threading.Lock`:

- `SafeCounter.__init__(self)` -- `self._lock = threading.Lock()`, `self._value = 0`. `increment(self) -> None` -- `with self._lock: self._value += 1`. Without the lock, two threads could both read the current value, both compute `value + 1`, and both write it back -- one increment silently lost. This is a **race condition**; the lock makes `+= 1` effectively atomic across threads.
- `SafeList.__init__(self)` -- `self._lock = threading.Lock()`, `self._items = []`. `append_safe(self, item) -> None` -- `with self._lock: self._items.append(item)`.
- `transfer_funds(accounts: dict, lock: threading.Lock, from_key, to_key, amount) -> None` -- `with lock: accounts[from_key] -= amount; accounts[to_key] += amount` -- the classic bank-transfer example: without the lock, a concurrent transfer could interleave between the two lines and leave the books unbalanced.
- `parallel_increment(counter, times: int, num_threads: int) -> None` -- split `times` calls to `counter.increment()` evenly across `num_threads` threads, start them all, then join them all. Used by the tests to prove `SafeCounter` ends up with the *exact* right total even under real concurrency.

See the Study Reference presentation, Topic 12, for the theory.
