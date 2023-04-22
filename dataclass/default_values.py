from dataclasses import dataclass

@dataclass
class Currency:
    value: float = 0.0
    exchange_rate: float = 0.17
    is_legal: bool = True


@dataclass
class AUD(Currency):

    code: str = "AUD"
    name: str = "Australian Dollar"
    symbol: str = "A$"
    description: str = "AUD (A$) - Australian Dollar"
    

default_currency = AUD()
print(default_currency)

non_default_currency = AUD(value=1.0, exchange_rate="0.19")
print(non_default_currency)