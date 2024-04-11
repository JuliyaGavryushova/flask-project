"""
Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
Используйте процессы.
"""
import os
from multiprocessing import Process

from pathlib import Path


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        counts_word = len(contents.split())
        print(f'{f.name} содержит {counts_word} слов')


def main():
    dir_path = Path('.')
    file_paths = os.walk(dir_path)

    processes = []
    for root, dirs, files in file_paths:
        for file in files:
            process = Process(target=process_file(os.path.join(root, file)))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()


if __name__ == '__main__':
    main()
