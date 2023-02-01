# Clase básica de decoradores en Real Python:
# https://realpython.com/primer-on-python-decorators/
# CONCEPTO 1
# Las funciones en Python son first-class objects, lo cual quiere decir que
# puden ser pasadas como argumentos de otras funciones como cualquier otro objeto: string, int, float etc
# Por ejemplo la funcion greet_bob espera como argumento una funcion


def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


"""
>>> greet_bob(say_hello)
'Hello Bob'

>>> greet_bob(be_awesome)
'Yo Bob, together we are the awesomest!'
"""

# CONCEPTO 2
# Inner functions: es posible definir funciones dentro de otras funciones


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


print(parent())


# CONCEPTO 3
# Las Funciones pueden devolver como valores de retorno otras funciones
def parent_with_return(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)

"""
>>> first
<function parent.<locals>.first_child at 0x7f599f1e2e18>

>>> second
<function parent.<locals>.second_child at 0x7f599dad5268>
"""

# Decorador simple
def my_decorator(func):  # (Según I) my_decorator() acepta funciones como argumento
    def wrapper():  # (según II) wrapper() es una función con scope local a my_decorator
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper  # (según III) la función my_decorator devuelve la función interna
    # wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)  # (según III) say_whee ahora contiene una referencia
#  la función interna wrapper, y es callable con say_whee()


"""
>>> say_whee()
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
"""

say_whee = my_decorator(say_whee)

"""
>>> say_whee
<function my_decorator.<locals>.wrapper at 0x7f3c5dfd42f0>
"""

# Sintaxis en Python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")
