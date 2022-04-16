# los context managers se usan para gestionar recursos
# Accesos a sockets, ficheros, bdd, que nos queremos asegurar que van a ser cerrados después de accedidos
# a pesar de que haya una excepción antes o después del código
# generalmente esto se conseguiría con tun try: finally, pero un context manager nos ahorra esta secuencia, 
# con los métodos __enter__ y __exit__

def process_file():
    pass

filename = "temp_file.txt"

fd = open(filename)
try:
    process_file(fd)
finally:
    fd.close()

# with es la keyword que inicia el context manager
# with llama al método __enter__ y devuelve el return de este método será asignado a la variable después de 'as'. Esto es opcional, no hace falta devolver nada
# en el método __enter__ de forma obligatoria

# open es un context manager con una implementación en la librería estándar, para gestionar ficheros, pero podemos implementar cualquier context manager

with open(filename) as fd:
    process_file(fd)

# Después del with, podemos ejecutar código de Python, con el nuevo contexto, y cuando acaba la última línea de este código, se ejecuta el método __exit__
# El método __exit__ se ejecutará siempre, aunque haya una excepción o error en código ejecutado en el nuevo contexto.
# De hecho, si ocurre una excepción, el método __exit__ la recibe por si hay que gestionarla


# Ejemplo:
# Queremos hacer un programa que ejecute un backup de una base de datos,
# Pero la base de datos tiene que estar parada, y luego arrancarla de nuevo


def stop_database():
    run("systemctl stop postgresql.service")

def start_database():
    run("systemctl start postgresql.service")

class DBHandler:
    
    def __enter__(self):
    stop_database()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()

def db_backup():
    run("pg_dump database")



# La librería contextlib de la librería estándar nos ayuda para generar sentencias with
# Resumidament, lo que va antes del yield sería el cuerpo del método __enter__
# yield puede devolver un valor igual que __enter__ puede hacer return x
# el código es sensiblement más corto, pero nos ahorramos definir una clase fake en caso
# de que el contexto no se pueda relacionar con un objeto


import contextlib

@contextlib.contextmanager
def db_handler():
    try:
        stop_database()
        yield
    finally:
        start_database()

if __name__ == "__main__":

    with DBHandler():
        db_backup()

    with db_handler():
        db_backup()



# Otra forma de usar contextlib es con contextlib.ContextDecorator
# contextlib.ContextDecorator es una base Class, que nos da la lógica para aplicar 
# un decorador a una función y hacer que esta se ejecute dentro del context manager
# Para usarlo tenemos que crear una clase que herede de esa Base Class, y crear los magic methods 
# __enter__ y __exit__
# la principal diferencia es que no usamos with, sólo tenemos que ejecutar el método offline_backup
# el problema de hacerlo así es que no podremos acceder al objeto del decorador, podría hacerse así:

'''
def offline_backup():
with dbhandler_decorator() as handler: ...

'''


class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, ext_type, ex_value, ex_traceback):
        start_database()
    
@dbhandler_decorator()
def offline_backup():
    run("pg_dump database")


