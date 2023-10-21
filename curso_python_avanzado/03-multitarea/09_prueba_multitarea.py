"""
Created on Tue Jul 14 16:35:04 2020

@author: Antonio
"""
import _thread
import time


def impresion(nombre):
    for n in range(1, 10):
        print("Imprimiendo " + nombre)
        time.sleep(1)


_thread.start_new_thread(impresion, tuple(["hilo1"]))
_thread.start_new_thread(impresion, tuple(["hilo2"]))
