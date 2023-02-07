from typing import Callable
import functools


def my_decorator(func: Callable) -> None:
    @functools.wraps(func)
    def wrapper() -> None:
           
        HOUR = 22 
        if 7 <= HOUR < 22:
            func()
        else:
            print("shhh")   
    
    return wrapper 

@my_decorator
def shout() -> None:
    print(f'{"HOLAAAAA!!!"}')


print(shout)