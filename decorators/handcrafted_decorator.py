from typing import Callable

def my_decorator(func: Callable) -> None:
    
    def wrapper() -> None:
           
        HOUR = 22 
        if 7 <= HOUR < 22:
            func()
        else:
            print("shhh")   
    
    return wrapper 


def shout() -> None:
    print(f'{"HOLAAAAA!!!"}')


shout()
print(shout)

shout = my_decorator(shout)
print(shout)
shout()