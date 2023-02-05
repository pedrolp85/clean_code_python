# Escribe un decorador que cambie el resultado de la función decorada a mayúsculas
from typing import Callable


def to_uppercase(func: Callable) -> Callable:
    print(f'{"Entramos en el decorador"}')

    def wrapper() -> str:
        original_value = func()
        return original_value.upper()

    print(f'{"salimos del decorador"}')

    return wrapper


@to_uppercase
def first_test_func() -> str:
    return f'{"Esto es la primera string de retorno"}'


@to_uppercase
def second_test_func() -> str:
    return f'{"Esto es la segunda string de retorno"}'


print(first_test_func())
print(second_test_func())
