# Escribe un decorador que cambie el resultado de la función decorada a mayúsculas
import functools
from typing import Callable


def conditional_uppercase(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> str:
        original_value = func(*args, **kwargs)
        lenght = len(original_value)

        if lenght % 2 == 0:
            return func(*args, **kwargs), lenght
        else:
            return original_value.upper(), lenght

    return wrapper


@conditional_uppercase
def test_func_even() -> str:
    return f'{"Esto es una string par"}'


@conditional_uppercase
def test_func_odd() -> str:
    return f'{"Esto es otra string impar"}'


@conditional_uppercase
def test_func_one_arg(param: str) -> str:
    return f"Esto es una string con un parametro  {param}"


@conditional_uppercase
def test_func_two_arg(param: str, another_param: str) -> str:
    return f"Esto es una string con dos param {param}, {another_param}"


print(test_func_even)
return_value, num_char = test_func_even()
print(return_value, num_char)

print("\n")

print(test_func_odd)
return_value, num_char = test_func_odd()
print(return_value, num_char)

print("\n")

print(test_func_one_arg)
return_value, num_char = test_func_one_arg("par")
print(return_value, num_char)

print("\n")

print(test_func_two_arg)
return_value, num_char = test_func_two_arg("par", "imp")
print(return_value, num_char)
