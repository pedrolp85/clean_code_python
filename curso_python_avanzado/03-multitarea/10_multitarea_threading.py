"""
Created on Wed Jul 15 18:58:15 2020

@author: Antonio
"""
import threading
import time


class Multi(threading.Thread):
    def __init__(self, num):
        # threading.Thread.__init__(self)
        super().__init__()
        self.numero = num

    def run(self):
        conta = 1
        while conta <= 10:
            print("%d x %d = %d \n" % (self.numero, conta, self.numero * conta))
            conta = conta + 1
            time.sleep(1)


t1 = Multi(5)
t2 = Multi(8)
t1.start()
t2.start()
