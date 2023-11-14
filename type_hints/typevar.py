from typing import Any


def identity(arg):
    return arg


def any_identity(arg: Any) -> Any:
    return arg


def type_specific(arg: int) -> int:
    return arg


result = any_identity(42)
print(result + "!")

result2 = type_specific(43)
print(result2 + "!")

from typing import TypeVar

T = TypeVar("T")

def generic_identity(arg: T) -> T:
    return arg

result3 = generic_identity(43)
print(result3 + "!")

result4 = generic_identity("hi")
print(result4 + "!")



