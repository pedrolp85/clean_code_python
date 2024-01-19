from typing import NamedTuple


class Coordinate(NamedTuple):
    long: float
    lat: float


def from_coordinate(coord: Coordinate) -> None:
    pass


def from_tuple(coord: tuple[float, float]) -> None:
    pass


c = Coordinate(0.1, 0.2)
tc = (0.001, 0.002)

from_coordinate(c)
from_tuple(tc)

from_coordinate(tc)
from_tuple(c)
