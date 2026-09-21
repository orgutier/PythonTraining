class ConfigError(Exception):
    pass


class ConfigParseError(ConfigError):
    pass


def load_config_value(raw: str) -> int:
    try:
        return int(raw)
    except ValueError as e:
        raise ConfigParseError(f"bad config value: {raw!r}") from e


class NetworkError(Exception):
    pass


class RetryError(Exception):
    pass


def fetch_with_retry_simulation(should_fail: bool) -> str:
    try:
        if should_fail:
            raise NetworkError("connection refused")
        return "ok"
    except NetworkError as e:
        raise RetryError("failed after retries") from e


class ScoreError(Exception):
    pass


def parse_score(raw: str) -> int:
    try:
        score = int(raw)
    except ValueError as e:
        raise ScoreError(f"invalid score: {raw!r}") from e
    if not (0 <= score <= 100):
        raise ScoreError(f"score out of range: {score}") from None
    return score
