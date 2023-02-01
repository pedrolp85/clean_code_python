# 1 1 2 3 5 8 13 21
from datetime import datetime


def calculate_fibonacci(pos):
    if pos <= 2:
        return 1
    anterior = 1
    anterior_anterior = 1
    for _ in range(2, pos):
        aux = anterior
        anterior = anterior + anterior_anterior
        anterior_anterior = aux
    return anterior


def recursive_fibonacci(pos):
    if pos <= 2:
        return 1
    return recursive_fibonacci(pos - 1) + recursive_fibonacci(pos - 2)


def dynamic_progr_fibonacci(n):
    f = [1, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


for i in range(1, 1000):
    print(f"procedemos a calcular el fib de {i}")
    ahora = datetime.now()
    print(f"Calculo iterativo '{calculate_fibonacci(i)}' ha tardado: '{datetime.now() - ahora}'")
    ahora = datetime.now()
    print(f"Calculo recursivo '{recursive_fibonacci(i)}' ha tardado: '{datetime.now() - ahora}'")
    ahora = datetime.now()
    print(f"Con dynamic prgrmmng '{dynamic_progr_fibonacci(i)}' tarda: '{datetime.now() - ahora}'")
