"""
Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить".
При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def get_submit():
    return render_template('age.html')


@app.post('/')
def post_submit():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age > 18:
            return f'Здравствуйте, {name}. Отлично! Вам есть 18!'
        else:
            return f'Здравствуйте, {name}. К сожалению, Вам нет 18!'
    return render_template('age.html')


if __name__ == '__main__':
    app.run(debug=True)