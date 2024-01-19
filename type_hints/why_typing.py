import uuid
from collections.abc import Sequence
from dataclasses import dataclass
from dataclasses import field


def _generic_action(items):
    result = []

    for item in items:
        result.append(item.value.uuid)

    return result


@dataclass
class CustomValue:
    uuid: str = field(default_factory=lambda: str(uuid.uuid1()))


@dataclass
class Item:
    value: CustomValue


def generic_action(items: Sequence[Item]) -> list[str]:
    result = []

    for item in items:
        result.append(item.value.uuid)

    return result


a_sequence = (Item(CustomValue()), Item(CustomValue()), Item(CustomValue()))
a_bad_sequence = None
print(generic_action(a_sequence))

print(_generic_action(a_bad_sequence))
print(generic_action(a_bad_sequence))
