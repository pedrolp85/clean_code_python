# los arrays se implementa en Python mediante srt, list y tuple

# Implementa una versión propia del método shuffle del module random, usando el 
# randrange(n) , que devuelve un int aleatorio entre 0 y n-1 
# input: una lista
# output: cualquier reordenáción de la lista es igualmente probable

import random
from typing import List

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)

def shuffle_implementation(input_list: List) -> List:
    return_list = []
    new_elements = []
    
    for i in input_list:
        new_position = random.randrange(l:=len(input_list))
        