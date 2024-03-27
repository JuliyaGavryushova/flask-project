"""
Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через
контекст.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index/')
def index():
    news = [
        {
            'heading': 'Заголовок №1',
            'description': 'Описание №1',
            'date': '27.03.2024'
        },
        {
            'heading': 'Заголовок №2',
            'description': 'Описание №2',
            'date': '27.03.2024'
        },
        {
            'heading': 'Заголовок №3',
            'description': 'Описание №3',
            'date': '27.03.2024'
        }
    ]
    context = {'item': news}
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)