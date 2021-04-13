from threading import Thread, Lock, Semaphore, BoundedSemaphore, current_thread
from time import sleep
from queue import Queue

balance = 200


def withdraw(amount: int, lock: Lock):
    lock.acquire()
    global balance
    newbalance = balance - amount
    balance = newbalance
    print('withdrawn ', amount, ' Birr')
    lock.release()


def print_hello(name, other, index):
    sleep(1)
    print('running in ', current_thread().name)
    # print('hello ', name, other, index)


thred_names = []


def request_handler(l: Lock, s: Semaphore):
    s.acquire()
    name = current_thread().name

    l.acquire()
    thred_names.append(name)
    l.release()

    print(thred_names)
    # processing some stuff
    sleep(0.5)

    l.acquire()
    thred_names.remove(name)
    l.release()

    s.release()


def run_first(s: Semaphore):
    print('running run_first')
    s.release()


def run_second(s: Semaphore):
    s.acquire()
    print('running run_second')


def producer(queue: Queue):
    for i in range(100):
        queue.put(i)


def consumer(queue: Queue):
    while True:
        next_item = queue.get()

        if (next_item == "QUIT"):
            print('quitting')
            break

        print('processing ', next_item, 'result ', next_item * next_item)
        print('processed by ', current_thread().name)


lock = Lock()
s = Semaphore(0)

# for amount in range(100):
#     thread = Thread(target=request_handler, args=[lock, s])
#     thread.start()

# Thread(target=run_second, args=[s]).start()
# sleep(1)
# Thread(target=run_first, args=[s]).start()

q = Queue()
for i in range(100):
    Thread(target=consumer, args=[q]).start()

producers = []
for i in range(2):
    thread = Thread(target=producer, args=[q])
    thread.start()
    producers.append(thread)

for producer in producers:
    producer.join()

for i in range(100):
    q.put('QUIT')
