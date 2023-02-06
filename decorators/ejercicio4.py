from typing import Callable


def repeat_func(func: Callable):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs), "decorator_return"

    return wrapper


@repeat_func
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


res1, res2 = return_greeting("Pedro")

print(res1, res2)
