# from typing import Union


# def test_union(x: Union[int, str]) -> None:
def test_union(x: int | str) -> None:
    x + 1
    x + "a"

    if isinstance(x, int):
        x + 1
    else:
        x + "a"


test_union(1)
test_union("x")
test_union(1.1)
