class Example:
    pass


print(dir(Example))


# __new__ y __init__ son llamados cada vez que se instancia una clase, pero new se hace
# de forma implícita


class Employee:
    def __new__(cls):
        print("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst

    def __init__(self):
        print("__init__ magic method is called")
        self.name = "Satya"


Employee()


class OverwriteWithSuper:
    def __new__(cls):
        print("En __new__")
        return super().__new__(cls)

    def __init__(self):
        print("en __init__")


OverwriteWithSuper()
