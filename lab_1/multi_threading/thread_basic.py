from threading import Thread, current_thread
from time import sleep


def myfunc(text, num):
    sleep(0.1)
    print(current_thread().name, i)
    # print("my func is running..", text)


for i in range(100):
    Thread(target=myfunc, args=("text to print", i, "third", "foiurth"),
           name=f"thread {i}").start()

print('in the main thread')
