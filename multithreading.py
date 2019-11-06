from time import *
import time
# from timeit import *
from threading import *

start=time.time()

class Hola(Thread):
    def run(self):
        for i in range(4):
            print("Thread 1")
            print("----------")
            sleep(1)

class Hey(Thread):
    def run(self):
        for i in range(4):
            print("Thread 2")
            print("----------")
            sleep(1)

class Chao(Thread):
    def run(self):
        for i in range(4):
            print("Thread 3")
            print("----------")
            sleep(1)

class Arigato(Thread):
    def run(self):
        for i in range(4):
            print("Thread 4")
            print("----------")
            sleep(1)

t1=Hola()
t2=Hey()
t3=Chao()
t4=Arigato()


t1.start()
sleep(0.01)
t2.start()
sleep(0.01)
t3.start()
sleep(0.01)
t4.start()
sleep(0.01)


t1.join()
t2.join()
t3.join()
t4.join()

# print(timeit()*60)
print("bye bye!!")
print(f"tiempo: {time.time()-start}")
