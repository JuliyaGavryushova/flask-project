"""
Напишите программу на Python, которая будет находить сумму элементов массива из 1 000 000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
В каждом решении нужно вывести время выполнения вычислений.
"""
import multiprocessing
import random
import time
from multiprocessing import Process

# Многопроцессорный подход

arr = [random.randint(1, 100) for _ in range(1000000)]

num_processes = 4
chunk_size = len(arr) // num_processes
total_sum = 0


def sum_array(chunk, res):
    chunk_arr_sum = sum(chunk)
    res.put(chunk_arr_sum)


result_queue = multiprocessing.Queue()

processes = []

start_time = time.time()

if __name__ == '__main__':
    for i in range(num_processes):
        start = i * chunk_size
        end = start + chunk_size
        chunk_arr = arr[start:end]

        process = Process(target=sum_array, args=(chunk_arr, result_queue,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_sum = sum(result_queue.get() for _ in range(num_processes))

    print(f'Сумма элементов массива {total_sum}. Время выполнения вычислений {time.time() - start_time:.2f} сек.')
