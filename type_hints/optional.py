from typing import Optional


def _strlen(s: str) -> int:
    if not s:
        return None
    return len(s)


def strlen(s: str) -> Optional[int]:
    if not s:
        return None  # OK
    return len(s)


def my_inc(x: Optional[int]) -> int:
    return x + 1


def _my_inc(x: Optional[int]) -> int:
    _ = x + 1

    if x is None:
        return 0
    else:
        return x + 1


def uppercase_untyped(a_parameter="Default_value"):
    return a_parameter.upper()


def uppercase_typed(a_parameter="Default_value typed"):
    return a_parameter.upper()


def uppercase_untyped_default_blank(a_parameter: str = "default") -> Optional[str]:
    if a_parameter is not None:
        return a_parameter.upper()

    return None


def uppercase_typed_default_none(a_parameter: Optional[str] = None) -> Optional[str]:
    if a_parameter is not None:
        return a_parameter.upper()

    return None


print(uppercase_untyped_default_blank(None))
