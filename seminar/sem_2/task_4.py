"""
Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def get_submit():
    return render_template('count_word.html')


@app.post('/')
def post_submit():
    if request.method == 'POST':
        text = request.form.get('text')
        result = len(text.split(' '))
        return f'Количество слов в тексте = {result}'
    return render_template('count_word.html')


if __name__ == '__main__':
    app.run(debug=True)