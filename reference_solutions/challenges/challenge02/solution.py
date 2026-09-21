def classify_pairs(items: list) -> dict:
    """
    Classify every (i, j), i < j pair in items.

    Edge cases handled:
      - Empty list or single-item list -> zero pairs, all counts 0.
      - Every item the exact same object -> every pair is "same_object".
      - A list containing None -> None compares by identity/equality like
        any other value (two Nones are always the same object, since None
        is a singleton).
    """
    counts = {"same_object": 0, "equal_but_different": 0, "different": 0}
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = items[i], items[j]
            if a is b:
                counts["same_object"] += 1
            elif a == b:
                counts["equal_but_different"] += 1
            else:
                counts["different"] += 1
    return counts


def dedupe_by_identity(items: list) -> list:
    result = []
    for item in items:
        already_kept = False
        for kept in result:
            if kept is item:
                already_kept = True
                break
        if not already_kept:
            result.append(item)
    return result


def dedupe_by_equality(items: list) -> list:
    result = []
    for item in items:
        already_kept = False
        for kept in result:
            if kept == item:
                already_kept = True
                break
        if not already_kept:
            result.append(item)
    return result


def prompt_login(username: str = None) -> str:
    if username is None:
        username = input("Username: ")
    input(f"Password for {username}: ")
    print(f"Welcome, {username}!")
    return username
