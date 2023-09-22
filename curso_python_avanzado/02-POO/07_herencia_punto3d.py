# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:07:04 2020

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
class Punto3d(Punto):
    z=0
    def __init__(self,x=0,y=0,z=0):
       Punto.__init__(self,x,y) #para llamar a constructor de superclase
       self.z=z
    def imprimir(self):
       super(Punto3d,self).imprimir()
       print(self.z)
    def __add__(self, p):
        return Punto3d(self.x+p.x, self.y+p.y,self.z+p.z)
    def __str__(self):
        return str(self.x)+":"+str(self.y)+":"+str(self.z)

pd1=Punto3d(3,1,7)
pd1.imprimir()
pd2=Punto3d(2)
pd3=pd1+pd2
print(pd3)