y: float = 1.0
z: bool = True
v: str = "test"
b: bytes = b"test"

a_number: int = 5

def stringify(num: int, secondary_num: int="") -> str:
    return f"{num}{secondary_num}/fin"

print(stringify(a_number))


def plus(num1: float, num2: int) -> float:
    return num1 + num2



# A commom error that could be detected by mypy
class A:
    def __init__(self, x: int) -> None:
        self.x = x  # Aha, attribute 'x' of type 'int'

a = A(1)
a.x = 2  # OK!
a.y = 3  # Error: "A" has no attribute "y"


def get_a_class(a: A) -> int:
    return a.x

result : int=get_a_class(a)
print(result)
