from threading import Thread, current_thread, Lock, Semaphore, BoundedSemaphore
from time import sleep
from queue import Queue

balance = 200


def withdraw(lock, amount):
    global balance
    if (amount > 0):
        lock.acquire()
        newbalance = balance - amount
        balance = newbalance
        lock.release()


def greet(name):
    sleep(1)
    print('hello ', name)


def run_first(s):
    sleep(1)
    print('this run first')
    s.release()


def run_second(s):
    s.acquire()
    sleep(1)
    print('this run second')
    s.release()


thread_names = []


def request_handler(s, l):
    s.acquire()

    name = current_thread().name
    l.acquire()
    thread_names.append(name)
    l.release()

    print(thread_names)
    sleep(1)

    l.acquire()
    thread_names.remove(name)
    l.release()

    s.release()


def consumer(q):
    name = current_thread().name
    while True:
        item = q.get()
        if (item == "QUIT"):
            break
        print(name, " processed", item, " result: ", item**2)


def producer(q):
    for i in range(100):
        q.put(i)

    for i in range(30):
        q.put("QUIT")


queue = Queue()
for i in range(30):
    Thread(target=consumer, args=[queue]).start()

Thread(target=producer, args=[queue]).start()
