from dataclasses import dataclass
from dataclasses import field


@dataclass
class FieldExamples:
    sort_index: float = field(init=False, repr=False)
    height: float = field(default_factory=make_french_deck)
    password: str = field(repr=False, default="p4ssw0rd")

    def __post_init__(self):
        self.sort_index = self.height


joe = Person("Joe", 25, 1.85, "joe@dataquest.io")
mary = Person("Mary", 43, 1.67, "mary@dataquest.io")

print(joe > mary)
