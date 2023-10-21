"""
Created on Fri Jun 26 17:08:41 2020

@author: antonio
"""


notas = {}
opcion = 0


def menu():
    print("1. Añadir nota")
    print("2. Calcular media")
    print("3. Total aprobados")
    print("4. Recuperar nota")
    print("5. Ver suspensos")
    print("6. Salir")
    global opcion
    opcion = int(input("opcion:"))
    return


def leerNota():
    nota = int(input("Introduce una nota\n"))
    nombre = input("Introduce un nombre")
    notas[nombre] = nota
    return


def notaMedia():
    media = 0.0
    for n in notas.values():
        media += n
    media /= len(notas)
    print("Nota media: ", media)
    return


def aprobados():
    aprobados = 0
    for n in notas.values():
        if n >= 5:
            aprobados += 1
    print("Total de aprobados ", aprobados)
    return


def recuperarNota():
    nombre = input("Introduce un nombre")
    nota = notas[nombre]
    print(nota)
    return


def suspensos():
    suspensos = list(filter(lambda k: notas[k] < 5, notas.keys()))
    print(suspensos)
    return


while opcion < 5:
    menu()
    if opcion == 1:
        leerNota()
    elif opcion == 2:
        notaMedia()
    elif opcion == 3:
        aprobados()
    elif opcion == 4:
        recuperarNota()
    elif opcion == 5:
        suspensos()
