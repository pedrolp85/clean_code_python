"""
Created on Tue Jul 28 17:37:27 2020

@author: Antonio
"""


# class Prueba:
#    data=5
#    def metodo(self):
#        print("metodo")
# print(Prueba.__dict__)
# ob=Prueba()
# def mifuncion():
#    print("metodo nuevo")
# def otrafuncion(x):
#    print("otro más")
# ob.metodo2=mifuncion
# ob.metodo()
# ob.metodo2()
# setattr(Prueba,"metodo3",otrafuncion)
# setattr(Prueba,"data2",80)
# print(Prueba.__dict__)
# ob.metodo3()
# ob2=Prueba()
# ob2.metodo3()
# print(ob2.data2)
class Test:
    pass


setattr(Test, "dato", 100)


def func(s):
    print("metodo nuevo")


setattr(Test, "metodo", func)
obj = Test()
print(obj.dato)  # 100
obj.metodo()  # imprime metodo nuevo
print(Test.__dict__)
