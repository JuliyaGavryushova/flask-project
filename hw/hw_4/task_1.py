"""
Напишите программу на Python, которая будет находить сумму элементов массива из 1 000 000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
В каждом решении нужно вывести время выполнения вычислений.
"""
import random
import threading
import time

# Многопоточный подход

arr = [random.randint(1, 100) for _ in range(1000000)]

num_threads = 10
chunk_size = len(arr) // num_threads
total_sum = 0


def sum_array(chunk):
    global total_sum
    chunk_arr_sum = sum(chunk)
    total_sum += chunk_arr_sum


threads = []

start_time = time.time()

for i in range(num_threads):
    start = i * chunk_size
    end = start + chunk_size
    chunk_arr = arr[start:end]

    thread = threading.Thread(target=sum_array, args=[chunk_arr])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'Сумма элементов массива {total_sum}. Время выполнения вычислений {time.time() - start_time:.2f} сек.')
