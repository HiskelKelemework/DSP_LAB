from threading import Thread, current_thread
from queue import Queue


def worker(q: Queue):
    while True:
        val = q.get()
        print(current_thread().name, "processed: ", val)


def master(q: Queue):
    for i in range(100):
        q.put(i)


if __name__ == "__main__":
    queue = Queue()

    for i in range(10):
        Thread(target=worker, args=[queue], name=f"Thread {i}").start()

    Thread(target=master, args=[queue], name=f"Master Thread").start()
