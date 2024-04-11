"""
Написать программу, которая скачивает изображения с заданных URL-адресов и
сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
файле, название которого соответствует названию изображения в URL-адресе.
Например URL-адрес: https://example/images/image1.jpg -> файл на диске:
image1.jpg
Программа должна использовать многопоточный, многопроцессорный и
асинхронный подходы.
Программа должна иметь возможность задавать список URL-адресов через
аргументы командной строки.
Программа должна выводить в консоль информацию о времени скачивания
каждого изображения и общем времени выполнения программы.
"""
import requests
import time
import threading
from multiprocessing import Process, Pool
import asyncio
import aiohttp


urls = ['https://wallbox.ru/wallpapers/main/201546/13dcd7162ea7a31.jpg',
        'https://i.artfile.ru/2137x1412_600336_[www.ArtFile.ru].jpg',
        'https://i.pinimg.com/originals/5b/e2/56/5be25606a1b0a0e951600ec09c4147f1.jpg']


# Асинхронный подход (1,11 сек.)


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = url[-10:]
            with open(filename, "bw") as f:
                f.write(await response.read())
                print(f'Файл скачан за {time.time() - start_time:.2f} сек.')


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        # task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

start_time = time.time()

if __name__ == '__main__':
    asyncio.run(main())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())


# Многопроцессорный подход (1,55 сек.)


# def download(url):
#     response = requests.get(url)
#     filename = url[-10:]
#     with open(filename, "bw") as f:
#         f.write(response.content)
#         print(f'Файл скачан за {time.time() - start_time:.2f} сек.')
#
#
# processes = []
#
# start_time = time.time()
#
# if __name__ == '__main__':
#     for url in urls:
#         process = Process(target=download, args=(url,))
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()


# Многопоточный подход (2,57 сек.)


# def download(url):
#     response = requests.get(url)
#     filename = url[-10:]
#     with open(filename, "bw") as f:
#         f.write(response.content)
#         print(f'Файл скачан за {time.time() - start_time:.2f} сек.')
#
#
# threads = []
#
# start_time = time.time()
#
# for url in urls:
#     thread = threading.Thread(target=download, args=[url])
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()


# Синхронный подход

# start_time = time.time()
#
# for url in urls:
#     response = requests.get(url)
#     filename = url[-10:]
#     with open(filename, "bw") as f:
#         f.write(response.content)
#         print(f'Файл скачан за {time.time() - start_time:.2f} сек.')
