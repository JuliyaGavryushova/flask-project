"""
Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/accessories/')
def accessories():
    return render_template('accessories.html')


if __name__ == '__main__':
    app.run(debug=True)