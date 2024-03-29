"""
Создать страницу, на которой будет форма для ввода имени
и электронной почты.
При отправке которой будет создан cookie файл с данными
пользователя.
Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти".
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""

from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)


@app.get('/')
def get_submit():
    return render_template('form.html')


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        e_mail = request.form.get('e_mail')
        response = make_response(redirect('/welcome'))
        response.set_cookie('user_data', f'{name} : {e_mail}')
        return response
    return render_template('form.html')


@app.route('/welcome')
def welcome():
    user_data = request.cookies.get('user_data', None)
    if user_data:
        name, _ = user_data.split(':')
        return render_template('welcome.html', name=name)
    return redirect('/')


@app.route('/del_cookie')
def del_cookie():
    response = make_response(redirect('/'))
    response.set_cookie('user_data', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)