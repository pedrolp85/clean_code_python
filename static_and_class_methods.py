# Existen varios tipos de métodos de clase

# Métodos de instancia
# 
# Son los métodos básicos o 'normales'
# Son los métodos que definen comportimientos de objetos de la clase
# sólo se pueden referenciar a través de instancias de la clase, y su primer argumento es self
# Self apunta a una instancia de la clase a la que pertenecen

# A través de self, una instancia puede acceder a atributos y propiedades del objeto
# también pueden acceder a la misma clase con el atributo self.__class__


# Métodos de clase
#
# Se definen con el decorador @classmethod
# Son métodos que no defien el compartimiento de una instancia, si no de la clase
# en lugar de self, reciben como primer parámetro cls, que es el acrónimo de Python para Class
# al no tener acceso a self, no pueden moficar el el estado del objeto o de la clase

# Metodos estáticos
#
# No recibe ni cls ni self
# Se declara con el decorador @staticmethod


class Person:
    life_expectancy=70

    def __init__(self):
        self.age = 32
        self.languaje = "english"
    
    def increase_age(self):
        self.age+=1

    def get_languaje(self):
        print(self)
        return self.languaje
    
    @classmethod
    def average_life_ex(cls):
        print(cls)
        return cls.life_expectancy
    
    @staticmethod
    def breathe():
        print("Sssss!")

class SpanishPerson(Person):
    life_expectancy=84

    def __init__(self):
        super().__init__()
        self.languaje = "spanish"

    
p = Person()
print(p.get_languaje())
print(p.average_life_ex())
#print(Person.get_languaje())
Person.breathe()
p.breathe()
s = SpanishPerson()
print(s.get_languaje())
print(s.average_life_ex())


# otro ejemplo

from dataclasses import dataclass
import random

@dataclass
class Animal:
    especie: str = "mammal"

    @staticmethod
    def get_random_animal():
       
        all_subcls = [ subclass() for subclass in Animal.__subclasses__() ]
        print(all_subcls)
        return random.choice(all_subcls)


@dataclass
class Dog(Animal):
    especie : str = "Canino"
    legs: int = 4
    description: str = "Es un Perro"

@dataclass
class Cat(Animal):
    especie : str ="Felino"
    legs: int = 4
    description: str = "Es un Gato"


animal = Animal.get_random_animal()

print(animal)