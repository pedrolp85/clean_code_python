from typing import Tuple

persona1 = ("David", "Garcia", "Alvarez", "Madrid")
persona2 = ("Pedro", "Lopez", "Perez", "Galicia")


def pinta_persona(persona: Tuple[str, ...]):
    print(f"nombre: {persona[0]}")
    print(f"apellidos: {persona[1]}")
    print(f"ciudad: {persona[2]}")


pinta_persona(persona1)
pinta_persona(persona2)

from typing import NamedTuple


class Persona(NamedTuple):
    nombre: str
    apellido: str
    segundo_apellido: str
    ciudad: str


def pinta_persona_2(persona: Persona):
    print(f"nombre: {persona.nombre}")
    print(f"apellidos: {persona.apellido}")
    print(f"ciudad: {persona.ciudad}")


persona1 = Persona(nombre="David", apellido="Garcia", segundo_apellido="Alvarez", ciudad="Madrid")
persona2 = Persona(nombre="Pedro", apellido="Lopez", segundo_apellido="Perez", ciudad="Galicia")

pinta_persona_2(persona1)
pinta_persona_2(persona2)
