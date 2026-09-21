import time
import threading
import concurrent.futures
import requests


class RetryingJobSubmitter:
    def __init__(self, session, max_attempts: int = 3) -> None:
        self.session = session
        self.max_attempts = max_attempts

    def submit_job(self, url: str, payload: dict) -> dict:
        """
        POST payload to url, retrying transient failures.

        Edge cases handled:
          - Succeeds on the first attempt -> no sleep at all.
          - Fails every attempt -> the ORIGINAL exception from the last
            attempt propagates unchanged, not a wrapped/generic one.
        """
        for attempt in range(self.max_attempts):
            try:
                r = self.session.post(url, json=payload)
                r.raise_for_status()
                return r.json()
            except requests.exceptions.RequestException:
                if attempt == self.max_attempts - 1:
                    raise
                time.sleep(0.01 * (2 ** attempt))


class SafeCounter:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._count = 0

    def increment(self) -> None:
        with self._lock:
            self._count += 1

    @property
    def value(self) -> int:
        return self._count


def submit_all_with_pool(submitter: RetryingJobSubmitter, jobs: list, max_workers: int = 4) -> list:
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(lambda job: submitter.submit_job(*job), jobs))


def submit_all_and_count_successes(submitter: RetryingJobSubmitter, jobs: list, counter: SafeCounter, max_workers: int = 4) -> list:
    def run(job):
        result = submitter.submit_job(*job)
        counter.increment()
        return result

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(run, jobs))
