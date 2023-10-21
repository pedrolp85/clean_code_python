from dataclasses import dataclass

@dataclass
class NBAPlayer:
    name: str
    last_name: str
    number: int

king =NBAPlayer("Lebron", "James", 23)
durantula = NBAPlayer("Kevin", "Durant", 35)

print(king)
print(durantula)
print(king == durantula)

class RegularNBAPlayer:
    def __init__(self, name, last_name, number):
        self.name = name
        self.last_name = last_name
        self.number = number

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(name={self.name}, last name={self.last_name})"
        )

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.name, self.last_name, self.number) == (
            other.name,
            other.last_name,
            other.number,
        )

king = RegularNBAPlayer("Lebron", "James", 23)
durantula = RegularNBAPlayer("Kevin", "Durant", 35)

print(king)
print(durantula)
print(king == durantula)
