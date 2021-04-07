from multiprocessing import Process, current_process, Queue
from os import listdir, path
from time import sleep


def taskRunner(filename: str, search: str, queue: Queue):
    searchLowerCase = search.lower()
    count = 0

    with open(filename) as f:
        for line in f.readlines():
            for word in line.split():
                if searchLowerCase in word:
                    count += 1
    print(count)
    queue.put(count)


def sum_occurences(queue: Queue):
    total = 0
    while True:
        count = queue.get()
        if (count == 'DONE'):
            break

        total += count

    print(f'total occurences are {total}')


if __name__ == "__main__":
    searchString = input("Enter the search word: ").split()[0]
    print(f"searching for {searchString} ...")

    files = [file for file in listdir('../text_assets/') if path.isfile(file)]
    queue = Queue()

    processes = []
    # creating a worker process for each file
    for index, filename in enumerate(files):
        args = (filename, searchString, queue)
        # process runs the taskRunner function
        process = Process(target=taskRunner, args=args, name=f"process{index}")
        process.start()
        processes.append(process)

    # a separate process for summing the counts from each process.
    sum_process = Process(target=sum_occurences, args=[
                          queue], name="sum process")
    sum_process.start()

    # wait for each process to finish execution.
    for process in processes:
        process.join()

    queue.put('DONE')
