# __new__ y __init__ son llamados cada vez que se instancia una clase, pero new se hace
# de forma implícita
# __new__() es un método estático de la clase object
# firma: object.__new__(class, *args, **kwargs)
# donde el primer argumento es la clase que quieres instanciar
# el resto de argumentos deben coincidir con los de __init__() aunque new no los use
# __new__() debería devolver una instancia de la clase, aunque no es obligatorio
# Cuando defines una nueva clase, esa clase hereda implícitamente de la clase object
# Se podría hacer override del __new__() y aunque no podemos reescribir la creacion del objeto,
# podemos hacer una especie de decorador llamando al new de object con super().__new__()
# lo cual nos permitiría añadir líneas previas y posteriormente a la creación de la instancia
# In Python, a class is callable. When you call
# the class to create a new object:
# Python will call the __new__() and __init__() methods


class Person:
    def __init__(self, name):
        self.name = name


person = Person("John")
print(person.__dict__)

person = object.__new__(Person)
print(person.__dict__)
person.__init__("John")
print(person.__dict__)


class Animal:
    def __new__(cls, type):
        print(f"Creating a new {cls.__name__} object...")
        return super().__new__(cls)

    def __init__(self, type):
        print(f"Initializing the animal object...")
        self.type = type


animal = Animal("Perro")
print(animal.__dict__)


x = "Hello World"
print(x.__str__())
print(x.__repr__())


class PrintThis:
    def __init__(self):
        self.greet = "Hola"
        self.audience = "Coruña"

    def __str__(self):
        return f"{self.greet} {self.audience}"


obj = PrintThis()
print(obj)


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age

        elif isinstance(other, int):
            return self.age == other

        return False


john = Person("John", "Doe", 25)
jane = Person("Jane", "Doe", 25)
mary = Person("Mary", "Doe", 27)

print(john == jane)
print(john == mary)
print(john == 25)
