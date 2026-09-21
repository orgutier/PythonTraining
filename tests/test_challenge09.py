import threading
import time

from challenges.challenge09.solution import BoundedBlockingQueue


def test_enqueue_then_dequeue_basic():
    q = BoundedBlockingQueue(capacity=2)
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.size() == 0


def test_enqueue_blocks_when_full_then_unblocks():
    q = BoundedBlockingQueue(capacity=1)
    q.enqueue("a")

    unblocked = threading.Event()

    def producer():
        q.enqueue("b")  # should block until "a" is dequeued
        unblocked.set()

    t = threading.Thread(target=producer, daemon=True)
    t.start()
    time.sleep(0.2)
    assert not unblocked.is_set(), "enqueue() did not block on a full queue"

    assert q.dequeue() == "a"
    t.join(timeout=2)
    assert unblocked.is_set(), "enqueue() never unblocked after room freed up"
    assert q.dequeue() == "b"


def test_dequeue_blocks_when_empty_then_unblocks():
    q = BoundedBlockingQueue(capacity=1)
    result = {}

    def consumer():
        result["value"] = q.dequeue()  # should block until something is enqueued

    t = threading.Thread(target=consumer, daemon=True)
    t.start()
    time.sleep(0.2)
    assert "value" not in result, "dequeue() did not block on an empty queue"

    q.enqueue(42)
    t.join(timeout=2)
    assert result.get("value") == 42


def test_multiple_producers_and_consumers_never_lose_or_duplicate_items():
    q = BoundedBlockingQueue(capacity=3)
    total_items = 40
    produced = list(range(total_items))
    consumed = []
    consumed_lock = threading.Lock()

    def produce(items):
        for item in items:
            q.enqueue(item)

    def consume(count):
        for _ in range(count):
            value = q.dequeue()
            with consumed_lock:
                consumed.append(value)

    chunks = [produced[0:10], produced[10:20], produced[20:30], produced[30:40]]
    producers = [threading.Thread(target=produce, args=(chunk,)) for chunk in chunks]
    consumers = [threading.Thread(target=consume, args=(10,)) for _ in range(4)]

    for c in consumers:
        c.start()
    for p in producers:
        p.start()

    for p in producers:
        p.join(timeout=5)
    for c in consumers:
        c.join(timeout=5)

    assert sorted(consumed) == produced
    assert q.size() == 0
