from threading import Thread, Lock
from queue import Queue

total_counter = 0


def match_string(lock, file_path, search_string):
    global total_counter
    counter = 0

    with open(file_path) as f:
        for line in f.readlines():
            words = line.split()
            for word in words:
                if search_string in word:
                    counter += 1

    print(f"in {file_path}, {search_string} was found {counter} times")
    lock.acquire()
    total_counter += counter
    lock.release()


if __name__ == "__main__":
    files = [
        '../text_assets/a.txt',
        '../text_assets/b.txt',
        '../text_assets/c.txt',
    ]

    search_string = input("Enter the search string: ").split()[0]
    lock = Lock()

    threads = []
    for file_path in files:
        thread = Thread(target=match_string, args=[
                        lock, file_path, search_string])
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("total matches:: ", total_counter)
