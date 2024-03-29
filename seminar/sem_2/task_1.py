"""
Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/submit')
def get_submit():
    return render_template('form.html')


@app.post('/submit')
def post_submit():
    name = request.form.get('name')
    return f'Привет, {name}!'


if __name__ == '__main__':
    app.run(debug=True)