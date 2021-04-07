from threading import Thread, Lock
from queue import Queue

total = 0


def sum_list(lock, list_of_nums):
    global total

    sum_local = sum(list_of_nums)
    lock.acquire()
    total += sum_local
    lock.release()


def sum_list_queue(queue, list_of_nums):
    sum_local = sum(list_of_nums)
    queue.put(sum_local)


def calculate_total_sum(queue):
    total = 0
    while True:
        partial_sum = queue.get()
        if (partial_sum == "STOP"):
            break
        total += partial_sum

    print("the total sum is:: ", total)


if __name__ == "__main__":
    nums_list = [
        [1, 5, 2, 6, 4],  # 18
        [1, 1, 2, 3, 4],  # 11
        [1, 5, 0, 6, 4],  # 16
        [1, 15, 2, 6, 4],  # 28
    ]

    lock = Lock()
    queue = Queue()
    threads = []
    for sublist in nums_list:
        thread = Thread(target=sum_list_queue, args=[queue, sublist])
        thread.start()
        threads.append(thread)

    total_sum_calculator = Thread(target=calculate_total_sum, args=[queue])
    total_sum_calculator.start()

    for thread in threads:
        thread.join()

    queue.put("STOP")
