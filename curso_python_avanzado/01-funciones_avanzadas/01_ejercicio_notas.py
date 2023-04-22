# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

notas=[]
opcion=0

def menu():
    print("1. Añadir nota")
    print("2. Calcular media")
    print("3. Total aprobados")
    print("4. Lista de notas")
    print("5. Salir")
    global opcion
    opcion=int(input("opcion:"))
    return
def leerNota():
    nota=int(input("Introduce una nota\n"))
    notas.append(nota)
    return
def notaMedia():
    media=0.0    
    for n in notas:
        media+=n
    media/=len(notas)
    print("Nota media: ",media)
    return
def aprobados():
    aprobados=0
    for n in notas:
        if n>=5:
            aprobados+=1
    print("Total de aprobados ", aprobados)
    return
def verNotas():
    notas.sort()
    print (notas)
    return 
while(opcion<5):
    menu()
    print(opcion)
    if opcion==1:     
        leerNota()
    elif opcion==2:
        notaMedia()
    elif opcion==3:
        aprobados()
    elif opcion==4:
        verNotas()

        

