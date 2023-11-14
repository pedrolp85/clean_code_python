import random
from typing import Sequence
from typing import TypeVar

Choosable = TypeVar("Choosable", str, float)


def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)


only_str = choose(["Guido", "Jukka", "Ivan"])
only_int = choose([1, 2, 3])
bool_and_float = choose([True, 42, 3.14])
string_and_int = choose(["Python", 3, 7])
