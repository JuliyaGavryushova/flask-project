"""
Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить".
При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def get_submit():
    return render_template('calculator.html')


@app.post('/')
def post_submit():
    if request.method == 'POST':
        num_1 = int(request.form.get('num_1'))
        num_2 = int(request.form.get('num_2'))
        sign = request.form.get('sign')
        if sign == '+':
            result = num_1 + num_2
        elif sign == '-':
            result = num_1 - num_2
        elif sign == '*':
            result = num_1 * num_2
        elif sign == '/':
            result = num_1 / num_2
        else:
            result = 'Неверные данные'
        return str(result)
    return render_template('calculator.html')


if __name__ == '__main__':
    app.run(debug=True)