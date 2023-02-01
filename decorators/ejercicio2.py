# escribe un decorador que cambiar los caracteres impares de un string a mayuscula y otro que los cambie a Ascii
from typing import Callable


def odd_char_to_capital(func: Callable) -> Callable:
    def wrapper() -> str:
        initial_string = func()
        odd_list_translated = [
            char.upper() if index % 2 == 0 else char for index, char in enumerate(initial_string)
        ]
        return "".join(odd_list_translated)

    return wrapper


def odd_chars_to_b(func: Callable) -> Callable:
    def wrapper() -> str:
        initial_string = func()
        odd_list_translated = [
            f"b" if index % 2 == 0 else char for index, char in enumerate(initial_string)
        ]
        return "".join(odd_list_translated)

    return wrapper


@odd_chars_to_b
@odd_char_to_capital
def first_test_func() -> str:
    return f"Estoesunstring"


print(first_test_func())
