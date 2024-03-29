# Problema: En una instancia del padre animal, usamos siempre la clave animal
# en una instancia de la clase hija, podemos usar
# la clave del padre o la específica, dependiendo del path
# queremos que los clientes llamen a la interfaz de la misma
# forma ya sea una instancia padre o hija, por eso usamos *args en el padre
import re
from dataclasses import dataclass
from dataclasses import field


@dataclass
class Animal:
    api_name: str = "animal"

    def get_key(self, *args):
        return self.api_name


@dataclass
class Perro(Animal):
    api_name_raza: str = "doberman"
    # We use this key when hitting /azure or ocp_on_azure endpoints
    # we use parent api_name when hittin ocp_on_cloud endpoints

    def get_key(self, path):
        if _ := re.search("raza", path):
            return self.api_name_raza
        else:
            return super().get_key()


GENERAL_PATH = "/reports/general/"
SPECIFIC_PATH = "/reports/raza/"

animal_generico = Animal()
print(animal_generico.get_key(GENERAL_PATH))
print(animal_generico.get_key(SPECIFIC_PATH))


animal_perro = Perro()
print(animal_perro.get_key(GENERAL_PATH))
print(animal_perro.get_key(SPECIFIC_PATH))


@dataclass
class Pez:
    api_name: str = "pez"


@dataclass
class Besugo(Pez, context="general"):
    api_name: str = field(init=False)

    def __post_init__(self, context):
        if context == "general":
            self.api_name = "pez"
        else:
            self.api_name = "besugo"
