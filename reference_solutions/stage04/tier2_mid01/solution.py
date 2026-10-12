import collections
import dataclasses


@dataclasses.dataclass
class Player:
    name: str
    position: str


PlayerRecord = collections.namedtuple("PlayerRecord", ["name", "position"])


def convert_to_record(player: Player) -> PlayerRecord:
    return PlayerRecord(player.name, player.position)


def players_are_equal(a: Player, b: Player) -> bool:
    return a == b


def records_are_equal(a: PlayerRecord, b: PlayerRecord) -> bool:
    return a == b
