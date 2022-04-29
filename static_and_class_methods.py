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
print(Person.get_languaje())
Person.breathe()
p.breathe()
s = SpanishPerson()
print(s.get_languaje())
print(s.average_life_ex())