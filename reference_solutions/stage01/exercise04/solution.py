def can_enter_venue(age, has_ticket: bool, is_vip: bool) -> bool:
    return (age is not None and age >= 18) and (has_ticket or is_vip)


def access_level(has_ticket: bool, is_vip: bool, is_staff: bool) -> str:
    if is_staff or is_vip:
        return "backstage"
    if has_ticket:
        return "general"
    return "denied"


def is_valid_choice(choice, allowed: list[str]) -> bool:
    return isinstance(choice, str) and choice in allowed and not choice == ""


def toggle_flag(flag: bool) -> bool:
    if flag is True:
        return False
    return True
