# funciones con numero de argumentos variable


def multiply(a, b):
    return a*b

def multiply3(a, b,c):
    return a*b*c

def multiply_list(*args):
    result = 1
    for n in args:
        result *=n
    return result

print(multiply_list(1,2,3,5))
print(multiply_list(3,4,3,1,1,1,1,1,2,1,1,1,1,1,1,1))


def presentacion(name, age, **kwargs):
    print(f"Hello {name}!")
    print(f"You are {age} years old")
    if kwargs.get("driving_license", False):
        print("This is your car!")
    if job := kwargs.get("job", None):
        print(f"Oh! you are '{job}'")


presentacion("David", 28, driving_license=True)
presentacion("David", 28, job="police")

def generic_function(*args, **kwargs):
    print(args)
    print(kwargs)
    print("__________________")

generic_function()
generic_function(1,2, "3")
generic_function(hola="que ase")
generic_function(1,2,3, hola="que ase")

def default_value(name, age, job='developer', married=False) -> None:
    print(f"hola {name}")

default_value('Pedro', 30)
default_value('Pedro', 30, 'fireman')
default_value('Pedro', 30, married=False)

from typing import Optional

def default_value_type_hints(name: str, age: int, job: str = 'developer', married: Optional[bool] = None) -> None:
    print(f"hola {name}")