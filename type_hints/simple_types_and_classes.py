y: float = 1.0
z: bool = True
v: str = "test"
b: bytes = b"test"

a_number: int = 5


class A:
    def __init__(self, x: int) -> None:
        self.x = x
        self.tags = []


a = A(1)
a.x = 2
a.y = 3


def get_attribute_x(a: A) -> int:
    return a.x

result: int = get_attribute_x(a)
print(result)
