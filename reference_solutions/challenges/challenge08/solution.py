import collections

Run = collections.namedtuple("Run", ["start", "length"])


def all_runs(numbers: list) -> list:
    """
    Every maximal consecutive run in numbers, as Run records sorted by start.

    Edge cases handled:
      - Empty numbers -> returns [].
      - Duplicate numbers -> deduplicated first (via set()), so they don't
        inflate a run's length.
      - Negative numbers -> runs work identically on either side of zero,
        since only relative order (n, n+1, n+2, ...) matters.
    """
    if not numbers:
        return []

    uniq = sorted(set(numbers))
    runs = []
    start = uniq[0]
    prev = uniq[0]
    for n in uniq[1:]:
        if n != prev + 1:
            runs.append(Run(start=start, length=prev - start + 1))
            start = n
        prev = n
    runs.append(Run(start=start, length=prev - start + 1))
    return runs


def longest_consecutive_run(numbers: list) -> Run:
    runs = all_runs(numbers)
    if not runs:
        raise ValueError("numbers must not be empty")
    return max(runs, key=lambda r: r.length)


def runs_overlap(run_a: Run, run_b: Run) -> bool:
    a_end = run_a.start + run_a.length
    b_end = run_b.start + run_b.length
    return run_a.start < b_end and run_b.start < a_end


def unique_numbers_covered(runs: list) -> set:
    covered = set()
    for run in runs:
        covered |= set(range(run.start, run.start + run.length))
    return covered
