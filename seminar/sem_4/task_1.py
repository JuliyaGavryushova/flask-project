"""
Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
Используйте потоки.
"""
import os
import threading

from pathlib import Path


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        counts_word = len(contents.split())
        print(f'{f.name} содержит {counts_word} слов')


def main():
    dir_path = Path('.')
    file_paths = os.walk(dir_path)

    threads = []
    for root, dirs, files in file_paths:
        for file in files:
            thread = threading.Thread(target=process_file(os.path.join(root, file)))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


if __name__ == '__main__':
    main()