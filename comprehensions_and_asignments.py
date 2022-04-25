# Usamos list o dict comprehensions cuando queremos crear estructuras de datos en una sola línea,
# por claridad de código. Cuando queremos realizar operaciones sobre los elementos, que hagan la comprehension
# demasiado compleja, mejor usar un bucle for 

def run_calculation(i : int) -> int:
    pass

numbers = []
for i in range(10):
    numbers.append(run_calculation(i))

numbers = [run_calculation(i) for i in range(10)]

# Generalmente la versión con comprehensions es un poco más eficiente 
# Vamos a ver un ejemplo más complejo de comprehensions y posteriormente,
# asignaciones, que es una nueva feature de Python 3.8


ARN_REGEX = 'hola'

import re
from typing import Iterable, Set

ARN_REGEX = re.compile(r"arn:aws:[a-z0-9\-]*:[a-z0-9\-]*:(?P<account_id>\d+):.*")


def collect_account_ids_from_arns(arns: Iterable[str]) -> Set[str]:
    """Given several ARNs in the form
        arn:partition:service:region:account-id:resource-id
    Collect the unique account IDs found on those strings, and return them.
    """
    collected_account_ids = set()
    for arn in arns:
        matched = re.match(ARN_REGEX, arn)
        if matched is not None:
            account_id = matched.groupdict()["account_id"]
            collected_account_ids.add(account_id)
    return collected_account_ids


def collect_account_ids_from_arns2(arns: Iterable[str]) -> Set[str]:
    matched_arns = filter(None, (re.match(ARN_REGEX, arn) for arn in arns))
    return {m.groupdict()["account_id"] for m in matched_arns}


def collect_account_ids_from_arns3(arns: Iterable[str]) -> Set[str]:
    return {
        matched.groupdict()["account_id"]
        for arn in arns
        if (matched := re.match(ARN_REGEX, arn)) is not None
    }

# filter(function, iterable):
# Devuelve los elementos del iterable que evaluán True en la función 'function'
# Esto es un poco más rebuscado, si usamos filter(None, iterable)
# Nos devuelve los elementos 'truthy', es decir, aquellos que, convertidos a Booleanos,
# devuelven True


if __name__ == '__main__':
    input_example = ["plopezpe", "pedro", "plopezpe@redhat.com", "Toshiba"]
        user_id:name:email:hardware
    res1 = collect_account_ids_from_arns(input_example)
    res2 = collect_account_ids_from_arns_comp(input_example)

    print(res1,res2)