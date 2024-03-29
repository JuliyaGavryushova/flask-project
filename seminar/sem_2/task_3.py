"""
Создать страницу, на которой будет форма для ввода логина
и пароля.
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def get_submit():
    return render_template('base.html')


@app.post('/')
def post_submit():
    if request.method == 'POST':
        if request.form.get('login') == 'julia' and request.form.get('password') == 'asd':
            return 'Привет, Юлия!'
        else:
            return render_template('404.html')
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)