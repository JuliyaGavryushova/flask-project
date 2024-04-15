"""
Создать веб-приложение на FastAPI, которое будет предоставлять API для
работы с базой данных пользователей. Пользователь должен иметь
следующие поля:
ID (автоматически генерируется при создании пользователя)
Имя (строка, не менее 2 символов)
Фамилия (строка, не менее 2 символов)
Дата рождения (строка в формате "YYYY-MM-DD")
Email (строка, валидный email)
Адрес (строка, не менее 5 символов)
API должен поддерживать следующие операции:
Добавление пользователя в базу данных
Получение списка всех пользователей в базе данных
Получение пользователя по ID
Обновление пользователя по ID
Удаление пользователя по ID
Приложение должно использовать базу данных SQLite3 для хранения
пользователей.
"""
from typing import List
import databases
import sqlalchemy
import logging
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from datetime import date


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = "sqlite:///mydb2.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(50)),
                         sqlalchemy.Column("surname", sqlalchemy.String(50)),
                         sqlalchemy.Column("birthdate", sqlalchemy.Date()),
                         sqlalchemy.Column("email", sqlalchemy.String(50)),
                         sqlalchemy.Column("password", sqlalchemy.String(50)),)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)

app = FastAPI()


class UserIn(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    surname: str = Field(..., min_length=2, max_length=50)
    birthdate: date = Field(default=None)
    email: EmailStr = Field(..., max_length=50)
    address: str = Field(default=None, min_length=5, max_length=50)


class User(UserIn):
    id: int