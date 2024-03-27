"""
Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!".
"""

from flask import Flask

app = Flask(__name__)

html = """
<h1>Моя первая HTML страница</h1>
<p>Привет, мир!</p>
"""


@app.route('/text/')
def text():
    return html


if __name__ == '__main__':
    app.run(debug=True)