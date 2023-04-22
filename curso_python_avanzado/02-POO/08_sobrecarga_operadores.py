# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 08:03:29 2020

@author: Antonio
"""

class Punto:
    x=0
    y=0
    dimension=2
    
    def __init__(self,x=None,y=None):
        self.x=x
        self.y=y
    def imprimir(self):
        print(self.x,self.y)
    def __str__(self):
        return str(self.x)+":"+str(self.y)
    def __repr__(self):
        return '{self.__class__.__name__}'.format(self=self)
    def __add__(self, p):
        return Punto(self.x+p.x, self.y+p.y)
    
p1=Punto(2,8)
p2=Punto(6,3)
print(str(p1+p2)) #8:11
