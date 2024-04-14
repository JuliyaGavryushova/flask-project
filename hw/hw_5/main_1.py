"""
Создать API для добавления нового пользователя в базу данных. Приложение
должно иметь возможность принимать POST запросы с данными нового
пользователя и сохранять их в базу данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для добавления нового пользователя (метод POST).
Создайте маршрут для обновления информации о пользователе (метод PUT).
Создайте маршрут для удаления информации о пользователе (метод DELETE).
Реализуйте валидацию данных запроса и ответа.
"""
import logging
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    password: str


user_1 = User(id=1, name='Alex', email='alex@mail.ru', password='Qazasd')
user_2 = User(id=2, name='Tom', email='tom@mail.ru', password='wsxsdf123')
user_3 = User(id=3, name='Bob', email='bob@mail.ru', password='Rfvfgh456')

users = [user_1, user_2, user_3]


@app.get("/users/")
async def read_users():
    logger.info('Обработан запрос для users')
    return {'users': users}


@app.post("/users/")
async def add_user(user: User):
    users.append(user)
    logger.info('Отработал POST запрос для добавления user')
    return user


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for i in range(len(users)):
        if users[i].id == user_id:
            users[i] = user
            logger.info(f'Отработал PUT запрос для user id = {user}.')
    return user


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for i in range(len(users)):
        if users[i].id == user_id:
            return {"user_id": users.pop(i)}
    return HTTPException(status_code=404, detail='User not found')