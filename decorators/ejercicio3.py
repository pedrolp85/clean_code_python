"""
Escribe una función que acepte un argumento y devuelva un string
Decora la función de forma que se ejecute 2 veces
Crea otra función igual a la primera pero con 2 argumentos
Modifica el decorador para que valga para ambas
"""


def repeat_func_one_argument(func):
    def wrapper(inner_arg: str):
        func(inner_arg)
        func(inner_arg)

    return wrapper


def repeat_func_any_argument(func):
    def wrapper_repeat_func(*arg, **kwargs):
        func(*arg, **kwargs)
        func(*arg, **kwargs)

    return wrapper_repeat_func


@repeat_func_one_argument
def test_func_one_argument(argument: str) -> None:
    print(f"Esto está decorado con {argument}")


@repeat_func_any_argument
def test_func_one_argument_general(argument: str) -> None:
    print(f"Esto está decorado con {argument}")


@repeat_func_any_argument
def test_func_two_arguments(one_arg: str, other_arg: str) -> None:
    print(f"Decoramos con {one_arg}, {other_arg}")


test_func_one_argument(f'{"un solo arg"}')
test_func_one_argument_general(f'{"un solo arg"}')
test_func_two_arguments(f'{"un arg"}', f'{"otro arg"}')
