"""
Разработать API для управления списком пользователей с
использованием базы данных SQLite. Для этого создайте
модель User со следующими полями:
id: int (идентификатор пользователя, генерируется
автоматически)
username: str (имя пользователя)
email: str (электронная почта пользователя)
password: str (пароль пользователя)
API должно поддерживать следующие операции:
Получение списка всех пользователей: GET /users/
Получение информации о конкретном пользователе: GET /users/{user_id}/
Создание нового пользователя: POST /users/
Обновление информации о пользователе: PUT /users/{user_id}/
Удаление пользователя: DELETE /users/{user_id}/
Для валидации данных используйте параметры Field модели User.
Для работы с базой данных используйте SQLAlchemy и модуль databases.
"""
from typing import List
import databases
import sqlalchemy
import logging
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = "sqlite:///mydb.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("username", sqlalchemy.String(50)),
                         sqlalchemy.Column("email", sqlalchemy.String(50)),
                         sqlalchemy.Column("password", sqlalchemy.String(15)),)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)

app = FastAPI()


class UserIn(BaseModel):
    username: str = Field(..., max_length=50)
    email: EmailStr = Field(..., max_length=50)
    password: str = Field(..., min_length=6, max_length=15)


class User(UserIn):
    id: int


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(**user.model_dump())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


# from typing import List
#
# from fastapi import FastAPI
# from pydantic import BaseModel, Field, EmailStr
# import databases
# import sqlalchemy

# DATABASE_URL = "sqlite:///mydatabase.db" # создаем базу данных в корневой директории
# database = databases.Database(DATABASE_URL) # переменная из класса Database
# metadata = sqlalchemy.MetaData() # метаданные

# app = FastAPI()

# users = sqlalchemy.Table(
#     "users",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("username", sqlalchemy.String(30)),
#     sqlalchemy.Column("email", sqlalchemy.String(50)),
#     sqlalchemy.Column("password", sqlalchemy.String(20)),)


# class UserIn(BaseModel):
#     username: str = Field(..., max_length=30)
#     email: EmailStr = Field(..., max_length=50)
#     password: str = Field(..., min_length=6, max_length=20)


# class User(UserIn):
#     id: int


# engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# metadata.create_all(engine)


# @app.get("/create_table/{cnt}")
# async def create_table(cnt: int):
# for i in range(cnt):
# query = users.insert().values(username=f'user{i+1}', email=f'mail{i+1}@mail.ru', password=str(111111*(i+1)))
# await database.execute(query)
# return {'msg': 'ready'}

# @app.get("/users/", response_model=List[User])
# async def get_users():
#     query = users.select()
#     return await database.fetch_all(query)


# @app.get("/users/{user_id}", response_model=User)
# async def get_user(users_id: int):
#     query = users.select().where(users.c.id == users_id)
#     return await database.fetch_one(query)


# @app.post("/users/", response_model=UserIn)
# async def create_user(user: UserIn):
#     query = users.insert().values(**user.model_dump())
#     create_id = await database.execute(query)
#     return await get_user(create_id)


# @app.put("/users/{user_id}", response_model=User)
# async def update_user(users_id: int, user: UserIn):
#     query = users.update().where(users.c.id == users_id).values(**user.model_dump())
#     await database.execute(query)
#     return await get_user(users_id)


# @app.delete("/users/{user_id}")
# async def delite_user(users_id: int):
#     query = users.delete().where(users.c.id == users_id)
#     await database.execute(query)
#     return {'msg': 'Delete'}

