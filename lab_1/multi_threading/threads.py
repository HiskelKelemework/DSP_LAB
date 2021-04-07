from threading import Thread, current_thread, Semaphore, Lock, BoundedSemaphore
from queue import Queue
from random import randint
from time import sleep

active_threads = []


def print_num(s: BoundedSemaphore, l: BoundedSemaphore):
    s.acquire()

    thread_name = current_thread().name

    l.acquire()
    active_threads.append(thread_name)
    l.release()

    print('running threads:', active_threads)
    sleep(1)

    l.acquire()
    active_threads.remove(thread_name)
    l.release()

    s.release()


if __name__ == "__main__":
    s = BoundedSemaphore(10)
    l = BoundedSemaphore(1)

    threads = []
    for i in range(20):
        thread = Thread(target=print_num, args=(s, l), name=f"thread_{i}")
        # thread.daemon = True
        thread.start()
        threads.append(thread)

    # for thread in threads:
    #     thread.join()
