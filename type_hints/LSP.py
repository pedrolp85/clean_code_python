class Animal:
    def talk(self) -> str:
        return f'{"I am an animal"}'

    def walk(self) -> None:
        pass


class Dog(Animal):
    def talk(self) -> str:
        return f'{"Guau!"}'


class Bee(Animal):
    def talk(self) -> str:
        return f'{"BZZZ"}'

    def sting(self):
        pass


def talk_to_animal(animal: Animal) -> str:
    reponse = animal.talk()
    return reponse.upper()

def stress_bee(animal: Bee) -> None:
    animal.sting()

a_bee = Bee()
print(talk_to_animal(a_bee))

an_animal = Animal()
stress_bee(an_animal)

