# *args y ** kwargs se usan en funciones con numero de argumentos variable
# *args
# Se usa cuando nos pasan un número de argumentos en los que el nombre del argumento es indiferente
# *arg convierte los input en una tupla, que podemos iterar dentro de la función


def multiply(a, b):
    return a * b


def multiply3(a, b, c):
    return a * b * c


def multiply_list(*args):
    result = 1
    for n in args:
        result *= n
    return result


print(multiply_list(1, 2, 3, 5))
print(multiply_list(3, 4, 3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1))


# **kwargs
# Usamos kwargs cuando el nombre del argumento sí es importante,
# **kwargs convierte los input en un diccionario, de forma que los inputs se pueden
# acceder en la forma clave-valor


def presentacion(name, age, **kwargs):
    print(f"Hello {name}!")
    print(f"You are {age} years old")
    if kwargs.get("driving_license", False):
        print("This is your car!")
    if job := kwargs.get("job", None):
        print(f"Oh! you are '{job}'")


presentacion("David", 28, driving_license=True)
presentacion("David", 28, job="police")

# Funciones genéricas:
# Esta firma: def generic_function(*args, **kwargs):
# Se podría usar para cualquier input, y se usa por ejemplo para decoradores
# No podría hacerse sólo con *kwargs ya que requeriría el nombre


def generic_function(*args, **kwargs):
    print(args)
    print(kwargs)
    print("__________________")


generic_function()
generic_function(1, 2, "3")
generic_function(hola="que ase")
generic_function(1, 2, 3, hola="que ase")

# Argumentos opcionales
# Son los que sin no recibimos un argumento en la llamda a la función,
# les pasamos un valor por defecto
# cuando llamamos a la función, si sólo tiene un argumento opcional no es necesario
# especificar en la llamada
# el nombre, del argumento, pero si tiene más de uno, los toma por orden


def default_value(name, age, job="developer", married=False) -> None:
    print(f"hola {name}")


default_value("Pedro", 30)
default_value("Pedro", 30, "fireman")
default_value("Pedro", 30, married=False)

# Argumentos opcionales en funciones con type hints
# Optional se pone cuando un argumento puede ser None, si sólo es opcional y va a tener un
# valor por defecto, se tipa como ese valor por defecto

from typing import Optional


def default_value_type_hints(
    name: str, age: int, job: str = "developer", married: Optional[bool] = None
) -> None:
    print(f"hola {name}")
