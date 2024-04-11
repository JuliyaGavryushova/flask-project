"""
Напишите программу на Python, которая будет находить сумму элементов массива из 1 000 000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
В каждом решении нужно вывести время выполнения вычислений.
"""
import asyncio
import random
import time

arr = [random.randint(1, 100) for _ in range(1000000)]

# Асинхронный подход


async def sum_array(chunk):
    return sum(chunk)


async def main():
    num_processes = 10
    chunk_size = len(arr) // num_processes
    tasks = []
    for i in range(num_processes):
        start = i * chunk_size
        end = start + chunk_size
        chunk_arr = arr[start:end]
        task = asyncio.create_task(sum_array(chunk_arr))
        tasks.append(task)
    chunk_sum = await asyncio.gather(*tasks)
    total_sum = sum(chunk_sum)
    print(f'Сумма элементов массива {total_sum}. Время выполнения вычислений {time.time() - start_time:.2f} сек.')

start_time = time.time()

if __name__ == '__main__':
    asyncio.run(main())

