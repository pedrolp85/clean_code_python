from collections.abc import Iterable
from collections.abc import Mapping
from collections.abc import MutableMapping
from collections.abc import Sequence


def fmapping(my_mapping: Mapping[int, str]) -> list[int]:
    my_mapping[5] = "maybe"
    return list(my_mapping.keys())


fmapping({3: "yes", 4: "no"})


def fmut_mapping(my_mapping: MutableMapping[int, str]) -> set[str]:
    my_mapping[5] = "maybe"
    return set(my_mapping.values())


fmut_mapping({3: "yes", 4: "no"})


_a_set = {1, 2, 3}
_a_dict = {1: "a", 2: "b", 3: "c"}
_a_list = [1, 2, 3]


def bar_sequence(numbers: Sequence[int]) -> bool:
    sorted = True

    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            sorted = False

    return sorted


def bar_iterable(numbers: Iterable[int]) -> bool:
    sorted = True

    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            sorted = False

    return sorted


print(bar_iterable(_a_set))
print(bar_iterable(_a_dict))
print(bar_iterable(_a_list))
print(bar_sequence(_a_set))
print(bar_sequence(_a_dict))
print(bar_sequence(_a_list))


def foo_iterable(numbers: Iterable[int]) -> list[int]:
    digits = list()

    for number in numbers:
        if 0 <= number <= 9:
            digits.append(number)

    return digits


def foo_sequence(numbers: Sequence[int]) -> list[int]:
    digits = list()

    for number in numbers:
        if 0 <= number <= 9:
            digits.append(number)

    return digits


print(foo_iterable(_a_set))
print(foo_iterable(_a_dict))
print(foo_iterable(_a_list))
print(foo_sequence(_a_set))
print(foo_sequence(_a_dict))
print(foo_sequence(_a_list))
