from multiprocessing import Pool
from os import listdir, path


def taskRunner(filename: str, search: str):
    searchLowerCase = search.lower()
    count = 0

    with open(filename) as f:
        for line in f.readlines():
            for word in line.split():
                if searchLowerCase in word:
                    count += 1
    return count


if __name__ == "__main__":
    searchString = input("Enter the search word: ").split()[0]

    files = []
    files_dir = path.abspath('../text_assets')

    for file_name in listdir(files_dir):
        full_file_path = f"{files_dir}/{file_name}"
        if path.isfile(full_file_path):
            files.append([full_file_path, searchString])

    print(f"searching for {searchString} ...")
    with Pool(len(files)) as p:
        result = p.starmap(taskRunner, files)
        print("occurences: ", result)
        print(f"total occureneces of {searchString}: ", sum(result))
