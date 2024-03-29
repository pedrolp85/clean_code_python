from typing import Callable
from typing import Optional


def argument_function_one() -> None:
    print(f'{"I am a function passed as an argument"}')


def argument_function_two(name: str) -> None:
    print(f"I am a function passed as an argument wich receives the argument {name}")


def receive_func_as_arg(func: Callable, proxy_arg: Optional[str] = None) -> None:
    print(f"I receive {func} as an argument")

    func(proxy_arg) if proxy_arg else func()


print("ejecutamos las funciones simples")

argument_function_one()
argument_function_two("demo")

print("\n")
print("ejecutamos la funcion compleja con la primera de argumento")

receive_func_as_arg(argument_function_one)

print("\n")
print("ejecutamos la funcion compleja con la segunda de argumento")

receive_func_as_arg(argument_function_two, proxy_arg="pedro")
