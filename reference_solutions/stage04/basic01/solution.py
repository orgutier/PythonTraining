def build_results(names: list[str], times: list[float]) -> list[tuple]:
    results = []
    for name, time in zip(names, times):
        results.append((name, time))
    return results


def rank_by_time(results: list[tuple]) -> list[tuple]:
    return sorted(results, key=lambda r: r[1])


def fastest_n(ranked_results: list[tuple], n: int) -> list[tuple]:
    return ranked_results[:n]


def podium_labels(fastest: list[tuple]) -> list[str]:
    return [f"{i+1}. {name} ({time}s)" for i, (name, time) in enumerate(fastest)]


def racer_count(names: list[str]) -> int:
    return len(names)
