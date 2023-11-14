class Bird:
    pass


class Duck(Bird):
    def __init(self):
        pass

    def quack(self):
        print("Quack!")


def alert(birdie):
    birdie.quack()


def alert_duck(birdie: Duck) -> None:
    birdie.quack()


# type_hints/duck_vs_norminal.py:22: error: "Bird" has no attribute "quack"  [attr-defined]
def alert_bird(birdie: Bird) -> None:
    birdie.quack()


daffy = Duck()
alert(daffy)

alert_duck(daffy)
alert_bird(daffy)
