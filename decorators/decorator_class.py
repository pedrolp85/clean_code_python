import functools


class MyDecorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_times = 0

    def __call__(self, *args, **kwargs):
        
        original_value = self.func(*args, **kwargs)
        self.num_times +=1
        print(f"Call {self.num_times} of {self.func.__name__!r}")

        if self.num_times % 2 == 0:
            return original_value
        else:
            return original_value.upper()


@MyDecorator
def test_return_even_str() -> str:
    return f'{"this is even"}'


@MyDecorator
def test_return_odd_str() -> str:
    return f'{"this is odd"}'


@MyDecorator
def test_arg_to_str(param: str) -> str:
    return f"the arg {param}"


first_return = test_return_even_str()
print(first_return)

first_return = test_return_even_str()
print(first_return)

second_return = test_return_odd_str()
print(second_return)

third_return = test_arg_to_str("odd")
print(third_return)