def both_conferences(east: set, west: set) -> set:
    return east & west


def all_players(east: set, west: set) -> set:
    return east | west


def east_only(east: set, west: set) -> set:
    return east - west


def west_only(east: set, west: set) -> set:
    return west - east


def symmetric_difference_manual(east: set, west: set) -> set:
    return (east - west) | (west - east)
