"""
Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index/')
def index():
    students = [
        {
            'name': 'Ivan',
            'surname': 'Ivanov',
            'age': 25,
            'average_score': 98
        },
        {
            'name': 'Petr',
            'surname': 'Petrov',
            'age': 30,
            'average_score': 73
        },
        {
            'name': 'Fedor',
            'surname': 'Fedorov',
            'age': 38,
            'average_score': 54
        }
    ]
    context = {'student': students}
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)