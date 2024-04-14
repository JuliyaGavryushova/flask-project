"""
Создать API для получения списка фильмов по жанру. Приложение должно
иметь возможность получать список фильмов по заданному жанру.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Movie с полями id, title, description и genre.
Создайте список movies для хранения фильмов.
Создайте маршрут для получения списка фильмов по жанру (метод GET).
Реализуйте валидацию данных запроса и ответа.
"""
import logging
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    genre: str


movie_1 = Movie(id=1, title='Title 1', description='Description 1', genre='comedy')
movie_2 = Movie(id=2, title='Title 2', description='Description 2', genre='horrors')
movie_3 = Movie(id=3, title='Title 3', description='Description 3', genre='comedy')

movies = [movie_1, movie_2, movie_3]


@app.get('/movies/')
async def read_movie():
    logger.info('Обработан запрос для movies')
    return {'movies': movies}


@app.get('/movies/{genre}')
async def read_movie_genre(genre: str):
    logger.info('Обработан запрос для movies')
    genre_list = []
    for i in range(len(movies)):
        if movies[i].genre == genre:
            genre_list.append(movies[i])
    return genre_list


@app.post("/movies/")
async def add_movie(movie: Movie):
    movies.append(movie)
    logger.info('Отработал POST запрос для добавления movie')
    return movie


@app.put("/movies/{movie_id}")
async def update_movie(movie_id: int, movie: Movie):
    for i in range(len(movies)):
        if movies[i].id == movie_id:
            movies[i] = movie
            logger.info(f'Отработал PUT запрос для movie id = {movie}.')
    return movie


@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int):
    for i in range(len(movies)):
        if movies[i].id == movie_id:
            return {"movie_id": movies.pop(i)}
    return HTTPException(status_code=404, detail='Movie not found')

