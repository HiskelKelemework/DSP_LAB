from threading import Thread, Lock

total_count = 0


def count_word(filepath, search_word, l):
    global total_count
    counter = 0
    with open(filepath) as f:
        for line in f.readlines():
            for word in line.split():
                if word.lower() == search_word:
                    counter += 1

    l.acquire()
    total_count += counter
    l.release()


print(__name__)

if __name__ == "__main__":
    search_word = input('Enter a search word: ').split()[0].lower()
    file_paths = [
        '../text_assets/a.txt',
        '../text_assets/b.txt',
        '../text_assets/c.txt',
    ]
    lock = Lock()
    threads = []
    for file_path in file_paths:
        thread = Thread(target=count_word, args=[file_path, search_word, lock])
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print('total occurences: ', total_count)
