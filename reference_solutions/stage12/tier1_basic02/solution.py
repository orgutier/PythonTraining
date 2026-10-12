import threading


def run_in_background(func, *args) -> threading.Thread:
    t = threading.Thread(target=func, args=args)
    t.start()
    return t


def wait_for_all(threads: list) -> None:
    for t in threads:
        t.join()


def run_and_wait(funcs: list) -> None:
    threads = [threading.Thread(target=f) for f in funcs]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
