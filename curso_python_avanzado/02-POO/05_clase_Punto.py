# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:02:29 2020

@author: Antonio
"""

class Punto:
    x=0
    y=0
    dimension=2
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def imprimir(self):
        print(self.x,self.y)
p1=Punto()
p1.imprimir()
p2=Punto(5,8)
p2.imprimir()
print(Punto.dimension)