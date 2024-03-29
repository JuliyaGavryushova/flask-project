"""
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить".
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def get_submit():
    return render_template('square.html')


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        return f'Квадрат числа {number} равен {number * number}'
    return render_template('square.html')


if __name__ == '__main__':
    app.run(debug=True)