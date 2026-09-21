import datetime


def naive_now():
    return datetime.datetime.now()


def aware_now_utc():
    return datetime.datetime.now(datetime.timezone.utc)


def is_timezone_aware(dt) -> bool:
    return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None


def to_utc_isoformat(dt) -> str:
    return dt.astimezone(datetime.timezone.utc).isoformat()


def make_aware(dt, tz):
    return dt.replace(tzinfo=tz)
