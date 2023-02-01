from pprint import pprint

constante_1 = {"saludo": "hola", "despedida": "adios"}


def mutable_params(diction=constante_1):
    pprint(diction)
    return diction


a = mutable_params()
a["tonto"] = "tu"

mutable_params()


def por_valor_y_referencia(a: int, b: str, c: list, d: dict) -> None:
    print(f"{id(a)} {id(b)} {id(c)} {id(d)}")
    a = 0
    b = ""
    c = []
    d = {}
    print(f"{id(a)} {id(b)} {id(c)} {id(d)}")


entero = 1
cadena = "string"
lista = [1, 2, 3, 4]
diccionario = {"h": "b"}


print(f"{id(entero)} {id(cadena)} {id(lista)} {id(diccionario)}")

por_valor_y_referencia(entero, cadena, lista, diccionario)

print(f"{entero} {cadena} {lista} {diccionario}")
