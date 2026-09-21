import re

EMAIL_PATTERN = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")


def contains_digit(text: str) -> bool:
    return re.search(r"\d", text) is not None


def find_all_numbers(text: str) -> list[str]:
    return re.findall(r"\d+", text)


def starts_with_word(text: str, word: str) -> bool:
    return re.match(re.escape(word), text) is not None


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_emails(text: str) -> list[str]:
    return EMAIL_PATTERN.findall(text)
