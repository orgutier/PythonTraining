def build_profile(name: str, age: int, height_m: float, is_student: bool) -> dict:
    return {"name": name, "age": age, "height_m": height_m, "is_student": is_student}


def value_kind(x) -> str:
    return type(x).__name__


def display_profile(profile: dict) -> None:
    print(
        f"{profile['name']} is {profile['age']} years old, "
        f"{profile['height_m']}m tall, student={profile['is_student']}"
    )
