from typing import List
from typing import Optional
from typing import Tuple

larry = [1, 6, 5, 2, 4, 3]


def split_array(
    array: List[int], index: int
) -> Tuple[Optional[List[int]], Optional[List[int]], Optional[List[int]]]:
    # return array[:index], array[index:index+3], array[index+3:]
    inicio = array[:index] if array[:index] else None
    subset = array[index : index + 3] if len(array[index : index + 3]) == 3 else None
    final = array[index + 3 :] if array[index + 3 :] else None

    return inicio, subset, final


def asemble_arrays(*args) -> List[int]:
    return_list = []

    for element in args:
        if element:
            return_list += element

    return return_list


def rotate_array(array: List[int]) -> List[int]:
    return array[1 : len(array)] + array[0:1]


def is_first_the_lowest(array: List[int]) -> bool:
    return min(array) == array[0]


print(f"larry al inicio {larry}")

index = 0


while index < len(larry) - 1:

    print(f"para index {index}")

    if (larry[index + 1] - larry[index]) > 1:

        first_part, subset, last_part = split_array(larry, index + 1)
        print(f"subconjutnos inicio {first_part}, subset: {subset}, final: {last_part}")

        if subset:

            while not (i := is_first_the_lowest(subset)):
                subset = rotate_array(subset)
                # print(f" subset rotado{rotate_array(subset)}")

            # print(f"No es necesario rotar mas {subset}")
            larry = asemble_arrays(first_part, subset, last_part)
            print(f"larry {larry}")

        index += 1

    else:
        print(f"los indices {index}, {index+1} estan ordenados")
        index += 1
