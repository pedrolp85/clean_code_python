# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 19:46:38 2020

@author: Antonio
"""

class Contacto:
    def __init__(self,nombre,email,edad):
        self.nombre=nombre
        self.email=email
        self.edad=edad
        
agenda={}
opcion=0
def menu():
    print("1. Nuevo contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Mostrar nombres")
    print("5. Salir")
    global opcion
    opcion=int(input("opcion:"))
    return
def nuevoContacto():
    email=input("Introduce email\n")
    if existeContacto(email):
        print("Ese contacto ya existe")
        return
    nombre=input("Introduce un nombre\n")
    edad=input("Introduce edad\n")
    contacto=Contacto(nombre,email,edad)
    agenda[email]=contacto
    return
def eliminarContacto():
    email=input("Introduce email\n")
    if existeContacto(email):
        del agenda[email]
    return
def existeContacto(email):
    #filtramos la agenda on los contactos que tienen ese email
    #si la longitud de la lista resultante es mayor que 0, es que ya existe
    if len(list(filter(lambda c:c.email==email,agenda.values())))>0:
        return True
    else:
        return False
def buscarContacto():
    email=input("Introduce email\n")
    contactos=list(filter(lambda c:c.email==email,agenda.values()))
    if len(contactos)>0:
        print(contactos[0].nombre+" "+contactos[0].email)
    else:
        print("El contacto no existe")
def mostrarContactos():
    for c in agenda.values():
        print(c.nombre)
    return
while(opcion<5):
    menu()
    if opcion==1:     
        nuevoContacto()
    elif opcion==2:
        eliminarContacto()
    elif opcion==3:
        buscarContacto()
    elif opcion==4:
        mostrarContactos()
   