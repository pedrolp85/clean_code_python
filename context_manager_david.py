# Context manager
# Usage
# with xxxxx() as XXXX:
#    pass
# with xxxxx():
#    pass
#
from contextlib import contextmanager


class Example:
    def __init__(self):
        self.saludo = "Hola"

    def __enter__(self):
        print("start")
        return self.saludo

    def __exit__(self, type, value, traceback):
        print(f"{type} - {value} - {traceback}")
        print("end")


with Example() as ejemplo:
    print("some")
    print(ejemplo)
with Example():
    print("upss!")
    # raise Exception()


@contextmanager
def open_file(name):
    f = open(name, "w")
    try:
        yield f
    finally:
        f.close()
