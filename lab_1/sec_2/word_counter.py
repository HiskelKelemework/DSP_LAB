from threading import Thread, Lock
from queue import Queue
total_count = 0


def count_word(file_path, search_word, q):
    global total_count
    counter = 0
    with open(file_path) as f:
        for line in f.readlines():
            for word in line.split():
                if word.lower() == search_word:
                    counter += 1
    print('counted ', counter, 'occurences')
    q.put(counter)


def adder(q):
    total = 0
    while True:
        item = q.get()
        if item == "QUIT":
            break
        total += item
    print("total count is ", total)


file_paths = [
    '../text_assets/a.txt',
    '../text_assets/b.txt',
    '../text_assets/c.txt',
]
q = Queue()
search_word = input('Enter the search word: ').split()[0].lower()
threads = []
for file_path in file_paths:
    thread = Thread(target=count_word, args=[file_path, search_word, q])
    thread.start()
    threads.append(thread)

Thread(target=adder, args=[q]).start()

for thread in threads:
    thread.join()

q.put("QUIT")
