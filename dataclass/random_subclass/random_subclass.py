import random
from dataclasses import dataclass


@dataclass
class Currency:
    value: float = 0.0

    @staticmethod
    def get_random_currency():
        all_subcls = [subclass() for subclass in Currency.__subclasses__()]
        return random.choice(all_subcls)


@dataclass
class AUD(Currency):
    code: str = "AUD"
    name: str = "Australian Dollar"
    symbol: str = "A$"
    description: str = "AUD (A$) - Australian Dollar"


@dataclass
class CAD(Currency):
    code: str = "CAD"
    name: str = "Canadian Dollar"
    symbol: str = "CA$"
    description: str = "CAD (CA$) - Canadian Dollar"


@dataclass
class RND(Currency):
    code: str = "RND"
    name: str = "Whatever"
    symbol: str = "RDN"
    description: str = "This is random"


moneda = Currency.get_currency("DOG")

print(moneda)
