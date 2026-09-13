import re


def word_frequency(text: str) -> dict[str, int]:
    words = re.findall(r"[a-zA-Z']+", text.lower())
    return {word: words.count(word) for word in set(words)}
