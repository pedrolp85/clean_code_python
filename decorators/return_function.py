from typing import Callable


def choose_your_return_function(number: int) -> Callable:
    def function_one() -> None:
        print(f'{"hi I am function one"}')

    def function_two() -> None:
        print(f'{"hi I am function two"}')

    match number:
        case 1:
            return function_one
        case 2:
            return function_two
        case _:
            print(f'{"No return for wildcard"}')


first = choose_your_return_function(1)
print(first)
first()

print("\n")

second = choose_your_return_function(2)
print(second)
second()
