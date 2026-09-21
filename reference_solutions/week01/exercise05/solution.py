def ask_name() -> str:
    return input("What is your name? ")


def ask_age() -> int:
    return int(input("How old are you? "))


def ask_yes_no(prompt: str) -> bool:
    answer = input(prompt).strip().lower()
    return answer in ("y", "yes")


def greet(name: str) -> None:
    print(f"Hello, {name}!")


def greeting_flow() -> str:
    name = ask_name()
    greet(name)
    return name
