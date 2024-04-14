"""
Создать API для управления списком задач. Приложение должно иметь
возможность создавать, обновлять, удалять и получать список задач.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте маршрут для получения списка задач (метод GET).
Создайте маршрут для создания новой задачи (метод POST).
Создайте маршрут для обновления задачи (метод PUT).
Создайте маршрут для удаления задачи (метод DELETE).
Реализуйте валидацию данных запроса и ответа.
"""
import logging
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: Optional[str] = None


# @app.get('/')
# async def read_root():
#     logger.info('Отработал GET запрос')
#     return {'Hello': 'World'}


@app.get('/tasks/{task_id}')
async def read_task(task_id: int, title: str):
    return {'task_id': task_id, 'title': title}


@app.post('/tasks/')
async def create_task(task: Task):
    logger.info('Отработал POST запрос')
    return task


@app.put('/tasks/{task_id}')
async def update_task(task_id: int, task: Task):
    logger.info(f'Отработал PUT запрос для task id = {task_id}')
    return {'task_id': task_id, 'task': task}


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    logger.info(f'Отработал DELETE запрос для task id = {task_id}')
    return {'task_id': task_id}


# from fastapi import FastAPI, HTTPException
# from typing import Optional
# from pydantic import BaseModel
# import logging
# 
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# app = FastAPI()
#
#
# class Task(BaseModel):
#     id: int
#     title: str
#     description: Optional[str] = None
#     status: Optional[str] = None
#
#
# task_1 = Task(id=1, title='string 1', description='Description for task 1', status='New')
# task_2 = Task(id=2, title='string 2', description='Description for task 2', status='InProgress')
#
# tasks = [task_1, task_2]
#
#
# @app.get("/tasks/")
# async def read_tasks():
#     global tasks
#     logger.info(f'Обработан запрос для tasks')
#     return {"tasks": tasks}
#
#
# @app.post("/tasks/")
# async def create_task(task: Task):
#     tasks.append(task)
#     logger.info('Отработал POST запрос для создания задачи.')
#     return task
#
#
# @app.put("/tasks/{task_id}")
# async def update_task(task_id: int, task: Task):
#     for i in range(len(tasks)):
#         if tasks[i].id == task_id:
#             tasks[i] = task
#             logger.info(f'Отработал PUT запрос для task id = {task}.')
#     return task
#
#
# @app.delete("/tasks/{task_id}")
# async def delete_task(task_id: int):
#     for i in range(len(tasks)):
#         if tasks[i].id == task_id:
#         return {"item_id": tasks.pop(i)}
#     return HTTPException(status_code=404, detail='Task not found')
