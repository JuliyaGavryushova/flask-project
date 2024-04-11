"""
Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
Используйте асинхронный подход.
"""
import asyncio
import os

from pathlib import Path


async def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        counts_word = len(contents.split())
        print(f'{f.name} содержит {counts_word} слов')


async def main():
    dir_path = Path('.')
    file_paths = os.walk(dir_path)

    tasks = []
    for root, dirs, files in file_paths:
        for file in files:
            task = asyncio.create_task(process_file(os.path.join(root, file)))
            tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
