"""
Дорабатываем задачу 1.
Добавьте две дополнительные страницы в ваше веб-приложение:
 - страницу "about"
 - страницу "contact".
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'My name is Julia'


@app.route('/contact/')
def contact():
    return 'Number phone 8 800 000 0 000'


if __name__ == '__main__':
    app.run(debug=True)