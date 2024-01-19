from collections.abc import Callable

# from typing import Callable (python <3.9)


def twice(i: int, next: Callable[[int], int]) -> int:
    return next(next(i))


def add(i: int) -> int:
    return i + 1


print(twice(3, add))
