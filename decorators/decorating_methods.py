import functools
from typing import Callable
from typing import Tuple


def conditional_uppercase(func: Callable) -> Callable:
    @functools.wraps(func)
    def conditional_uppercase_wrapper(*args, **kwargs) -> Tuple[str, int]:
        original_value = func(*args, **kwargs)
        lenght = len(original_value)

        if lenght % 2 == 0:
            return original_value, lenght
        else:
            return original_value.upper(), lenght

    return conditional_uppercase_wrapper


class Cadena:
    def __init__(self, initial_value="aa"):
        self.cadena = initial_value

    def get_string(self):
        return f"{self.cadena}"

    def add_more_cadena(self, adding_chars):
        self.cadena += adding_chars


cadena = Cadena()
cadena.add_more_cadena("bb")
print(cadena.get_string())
