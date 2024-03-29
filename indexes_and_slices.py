my_numbers = (4, 5, 3, 9)
print(type(my_numbers))

print(my_numbers[-1])
print(my_numbers[-3])

del my_numbers

# En Python tenemos índices negativos para indicar que comiencen
#  a contar por el final, siendo -1 el último elemento del iterador

more_numbers = (1, 1, 2, 3, 5, 8, 13, 21)
slic = more_numbers[1:5]
print(slic)

# Nota: los slices, el primer indice es inclusivo,
#  el segundo exclusivo : [1:5] seria del indice 1 al 4

from_start = more_numbers[:3]
print(from_start)
to_the_end = more_numbers[3:]
print(to_the_end)

# Si quitamos una de las 2 referencias coge desde el
# principio o hasta el final, respectivamente

with_step_two = more_numbers[1:7:2]
print(with_step_two)

# Pasar intervalos es por debajo pasar un objeto Slice de Python

print("con objeto slice")

interval = slice(1, 7, 2)
print(more_numbers[interval])

interval = slice(None, 3)
print(more_numbers[interval] == more_numbers[:3])
