"""
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить".
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".
"""

from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

app.secret_key = 'gfgjjnhvgfcfggjklkmnnbbhbjk657658'


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}', 'success')
        return redirect(url_for('form'))
    return render_template('name.html')


if __name__ == '__main__':
    app.run(debug=True)