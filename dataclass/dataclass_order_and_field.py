from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int
    height: float
    email: str

    def __post_init__(self):
        self.sort_index = self.age


joe = Person("Joe", 45, 1.85, "joe@gmail.com")
mary = Person("Mary", 43, 1.67, "mary@gmail.com")

print(joe > mary)
