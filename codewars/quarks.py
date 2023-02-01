from enum import Enum


class Error(Exception):
    """Base class for other exceptions"""

    pass


class InvalidColor(Error):
    """Raised when the input color is not valid"""

    pass


class InvalidFlavor(Error):
    """Raised when the input flavor is not valid"""

    pass


class Flavor(Enum):
    up = "up"
    down = "down"
    strange = "strange"
    charm = "charm"
    top = "top"
    bottom = "bottom"


class Color(Enum):
    red = "red"
    blue = "blue"
    green = "green"


class Quark:
    def __init__(self, color: str, flavor: str):
        if hasattr(Color, color):
            self.color = color
        else:
            raise InvalidColor

        if hasattr(Flavor, flavor):
            self.flavor = flavor
        else:
            raise InvalidFlavor

        self.baryon_number = 1 / 3

    def interact(self, another_quark) -> None:
        self.color, another_quark.color = another_quark.color, self.color


q1 = Quark("red", "up")
print(q1.color)
print(q1.flavor)
q2 = Quark("blue", "strange")
print(q2.color)

print(q2.baryon_number)
q1.interact(q2)
print(q1.color)
print(q2.color)
