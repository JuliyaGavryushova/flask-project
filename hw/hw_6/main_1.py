"""
Создать API для управления списком задач. Каждая задача должна содержать поля "название",
"описание" и "статус" (выполнена/не выполнена). API должен позволять выполнять CRUD операции с задачами.
Напишите API для управления списком задач. Для этого создайте модель Task со следующими полями:
id: int (первичный ключ)
title: str (название задачи)
description: str (описание задачи)
done: bool (статус выполнения задачи)
API должно поддерживать следующие операции:
Получение списка всех задач: GET /tasks/
Получение информации о конкретной задаче: GET /tasks/{task_id}/
Создание новой задачи: POST /tasks/
Обновление информации о задаче: PUT /tasks/{task_id}/
Удаление задачи: DELETE /tasks/{task_id}/
Для валидации данных используйте параметры Field модели Task. Для работы с базой данных используйте SQLAlchemy и модуль databases.
"""
from typing import List
import databases
import sqlalchemy
import logging
from fastapi import FastAPI
from pydantic import BaseModel, Field


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = "sqlite:///mydb1.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table("tasks",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("title", sqlalchemy.String(50)),
                         sqlalchemy.Column("description", sqlalchemy.String(120)),
                         sqlalchemy.Column("done", sqlalchemy.Boolean()),)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)

app = FastAPI()


class TaskIn(BaseModel):
    title: str = Field(..., max_length=50)
    description: str = Field(default=None, max_length=120)
    done: bool


class Task(TaskIn):
    id: int


@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    query = tasks.select()
    logger.info('Обработан запрос')
    return await database.fetch_all(query)


@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    logger.info(f'Отработан запрос по task id')
    return await database.fetch_one(query)


@app.post("/tasks/", response_model=Task)
async def create_task(task: TaskIn):
    query = tasks.insert().values(**task.model_dump())
    last_record_id = await database.execute(query)
    logger.info('Отработан POST запрос для добавления task')
    return {**task.model_dump(), "id": last_record_id}


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, new_task: Task):
    query = tasks.update().where(tasks.c.id == task_id).values(**new_task.model_dump())
    logger.info('Отработан PUT запрос')
    await database.execute(query)
    return {**new_task.model_dump(), "id": task_id}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {'message': 'Task deleted'}