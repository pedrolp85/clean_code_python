from dataclasses import dataclass

@dataclass
class Currency:
    value: float = 0.0
    exchange_rate: float = 0.17

@dataclass
class AUD(Currency):
    code: str = "AUD"
    name: str = "Australian Dollar"
    symbol: str = "A$"
    description: str = "AUD (A$) - Australian Dollar"

@dataclass(kw_only=True)
class USD(Currency):
    code: str = "USD"
    is_legal: bool
    name: str = "American Dollar"
    symbol: str = "USD$"
    description: str = "USD (USD$) - American Dollar"

default_currency = AUD()
non_default_currency = AUD(value=1.0, exchange_rate="0.19")
dollar = USD(is_legal=True)

