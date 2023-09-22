import functools
from typing import Callable
from typing import Tuple


def decorator_factory(input_arg: int) -> Callable:
    def conditional_uppercase(func: Callable) -> Callable:
        @functools.wraps(func)
        def conditional_uppercase_wrapper(*args, **kwargs) -> Tuple[str, int]:
            original_value = func(*args, **kwargs)
            lenght = len(original_value)

            if input_arg % 2 == 0:
                return original_value, lenght
            else:
                return original_value.upper(), lenght

        return conditional_uppercase_wrapper

    return conditional_uppercase


@decorator_factory(2)
def test_return_even_str() -> str:
    return f'{"this is even"}'


@decorator_factory(1)
def test_return_odd_str() -> str:
    return f'{"this is odd"}'


@decorator_factory(1)
def test_arg_to_str(param: str) -> str:
    return f"the arg {param}"


first_return = test_return_even_str()
print(first_return)

second_return = test_return_odd_str()
print(second_return)

third_return = test_arg_to_str("odd")
print(third_return)
