# ATRIBUTOS
# En Python no hay atributos privados per se, pero hay ciertas convenciones
# los atributos privados (Por ejemplo timeout, más abajo) son precedidos por una _
from inspect import Attribute


class Connector:
    def __init__(self, source):
        self.source = source
        self._timeout = 60


conn = Connector("postgresql://localhost")
print(conn.source)

print(conn._timeout)
print(conn.__dict__)

"""
{'source': 'postgresql://localhost', '_timeout': 60}

"""

# Hay una misconecption bastante extendida con el doble underscore en Python, __
# El siguiente ejemplo va a fallar:

"""
>>> class Connector:
... def __init__(self, source):
... self.source = source
... self.__timeout = 60
...
... def connect(self):
... print("connecting with {0}s".format(self.__timeout))
... # ...
...
>>> conn = Connector("postgresql://localhost")
>>> conn.connect()
connecting with 60s
>>> conn.__timeout
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'Connector' object has no attribute '__timeout'

"""

# Esta vez definimos el atributo timeout con self.__timeout,
# y cuando intentamos acceder a él desde fuera, tenemos un error, pero este error no es 'no se puede acceder',
# si no 'El atributo no existe'
# esto es debido a que cuando usamos __ Python cambia el nombre del atributo a _classname__attrname, en este caso seria _Connector__timeout
# y se debería acceder de la siguiente forma: conn._Connector__timeout = 30

# En realidad, el __ en Python se creó para algo totalmente distinto, para override de métodos de clase que va a ser
# entendida múltiples veces, para que no hay colisiones con los nombres de los métodos

# La double underscore __ NO DEBERÍA USARSE EN PYTHON


# PROPIEDADES

# LLamamos propiedades a los 'managed attributes'
# Son atributos de los que podemos modificar su implmentación interna sin cambiar la API pública de la clase
# Si los atributos son accesibles desde fuera de la clase, el que use la clase puede modificarlos, pero si
# llega un momento que la implentación interna cambia, el que usa la clase debería cambiar todo el código

# Otros lenguajes como Java o C++ aconsejan nunca exponer los atributos para evitar este tipo de problema, sino implementar
# métodos setter y getter


# Setters y getters:


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value


point = Point(12, 5)
equis = point.get_x()

ygriega = point.get_y()

point.set_x(42)
point.get_x()

# Los atributos pueden seguir accediendose desde fuera
# ya que nada en Python lo impide

print(point._x)
print(point._y)


# Setters y Getters en estilo python: convertir los atributos en properties
# las properties son métodos que se comportan como propiedades


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius


circle = Circle(42.0)

print(circle.radius)
circle.radius = 100.0

print(circle.radius)

del circle.radius

"""
>>> circle.radius
Get radius
Traceback (most recent call last):
    ...
AttributeError: 'Circle' object has no attribute '_radius'

"""

# ATRIBUTOS READ-ONLY

# El principal uso de @property es que el usario de la clase no pueda modificar un atributo
# Por ejemplo digamos que queremos crear una clase Rectangulo con la propiedad lado que no queremos
# que puedan cambiar de valor


class Rectangulo:
    def __init__(self, largo: float, ancho: float):
        self._largo = largo
        self._ancho = ancho

    @property
    def largo(self):
        return self._largo

    @property
    def ancho(self):
        return self._ancho


rect = Rectangulo(12.0, 6.0)
rect.largo
rect.ancho

"""
>>> # Write coordinates
>>> point.x = 42
Traceback (most recent call last):
    ...
AttributeError: can't set attribute

"""

# Podemos hacer que unos atributos modifiquen a otros y que todos los atributos
# pasen por un setter antes de incializar la clase

"""

import enum

class Player():
    def init(self, name : str, number: int, average_points: float) -> None:
        self.number = number
        #self._number = number Esto es lo que hacíamos antes, ahora llamamos al setter

    @property
    def number(self) -> int:
        return self._number

    @property.setter
    def number(number: int) -> int:
        print("Seteamos el numero")
        try:
            return int(number)
        except:
            raise ValueError("El número no es un número")

    @property
    def average_points(self) -> float:
        return self._average_points

    @property.setter
    def average_points(avg: float) -> int:
        print("Seteamos la media")
        try:
            return float(number)
        except:
            raise ValueError("La media no es un float")
"""

# CHACHEAR ATRIBUTOS
# Cuando tenemos atributos que son usados muy recurrentemente, y los datos no cambian,
# o atributos cuyo cálculo es muy pesado, podemos cachearlos de forma que se calculen sólo
# 1 vez

# Esto se puede implmentar de forma que el atributo sea modificable desde fuera o no
# En este ejemplo sí podrías modificar el atributo radius

from functools import cached_property
from time import sleep


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def diameter(self):
        sleep(0.5)  # Simulate a costly computation
        return self.radius * 2


"""

>>> from circle import Circle

>>> circle = Circle(42.0)
>>> circle.diameter  # With delay
84.0
>>> circle.diameter  # Without delay
84.0

>>> circle.radius = 100
>>> circle.diameter  # Wrong diameter
84.0

>>> # Allow direct assignment
>>> circle.diameter = 200
>>> circle.diameter  # Cached value
200

"""

# Para evitar que se pueda modificar desde fuera el atributo, habría que hacerlo así:

# circle.py

from functools import lru_cache  # python 3.8

# from functools import cache Python 3.9
from time import sleep


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    @lru_cache
    def diameter(self):
        sleep(0.5)  # Simulate a costly computation
        return self.radius * 2


"""

>>> from circle import Circle

>>> circle = Circle(42.0)

>>> circle.diameter  # With delay
84.0
>>> circle.diameter  # Without delay
84.0

>>> circle.radius = 100
>>> circle.diameter
84.0

>>> circle.diameter = 200
Traceback (most recent call last):
    ...
AttributeError: can't set attribute

"""

# DATACLASS

# Sirven para crear código de clases de forma más compacta
# En principio están pensadas para

# Esta es la definición clásica de un método __init__


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


# Esto es lo mismo con una dataclass

from dataclasses import dataclass


@dataclass
class DataClassCard:
    rank: str
    suit: str


# Además una dataclass implement por detrás, además del __init__,
# otros métodos que nos ayudan, como __repr__ para tener una representación de la clase en str
# __eq__ que nos sirve para comparar objetos. Para que una clase normal fuese igual que una dataclass de inicio,
# debería ser algo así:


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.__class__.__name__}" f"(rank={self.rank!r}, suit={self.suit!r})"

    # Nota: !r en fstring llama al método __repr__ de la variable representada

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)


print("Prueba clase init")

card = RegularCard("Q", "Hearts")
print(card)

card2 = RegularCard("Q", "Hearts")

if card == card2:
    print("Son iguales")
