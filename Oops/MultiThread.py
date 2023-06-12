from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

# t1.run()
t1.start()
sleep(0.2) # to avoid collision
t2.start()

# print("Bye")  # main thread is responsible to print bye to print bye at last by adding join
t1.join()
t2.join()
print("Bye")
# to execute the code simultaneously hello should be subclass of Thread and need to import threading Module to create
# 2 different threads instead of calling run method
# we need to call start method(internally it calls run method)
