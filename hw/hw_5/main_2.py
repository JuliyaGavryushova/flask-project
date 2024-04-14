"""
Создать веб-страницу для отображения списка пользователей. Приложение
должно использовать шаблонизатор Jinja для динамического формирования HTML
страницы.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
содержать заголовок страницы, таблицу со списком пользователей и кнопку для
добавления нового пользователя.
Создайте маршрут для отображения списка пользователей (метод GET).
Реализуйте вывод списка пользователей через шаблонизатор Jinja.
"""
import logging
from fastapi import FastAPI, Request
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    password: str


user_1 = User(id=1, name='Alex', email='alex@mail.ru', password='Qazasd')
user_2 = User(id=2, name='Tom', email='tom@mail.ru', password='wsxsdf123')
user_3 = User(id=3, name='Bob', email='bob@mail.ru', password='Rfvfgh456')

users = [user_1, user_2, user_3]


@app.get("/", response_class=HTMLResponse)
async def list_users(request: Request):
    return templates.TemplateResponse("base.html", {"request": request, "users": users})
