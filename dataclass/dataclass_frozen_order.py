from dataclasses import dataclass


@dataclass(order=True)
class OrdererPerson:
    name: str
    age: int
    email: str


joe = OrdererPerson("Joe", 25, "joe@gmail.com")
mary = OrdererPerson("Mary", 43, "mary@gmail.io")
print(joe > mary)


@dataclass(frozen=True)
class FrozenPerson:
    age: int
    email: str
    name: str = "Joe"


frozen_joe = FrozenPerson(25, "joe@gmail.com")
frozen_joe.name = "Juan"
