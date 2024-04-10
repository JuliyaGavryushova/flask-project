"""
Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
содержать следующие поля:
- Имя пользователя (обязательное поле)
- Электронная почта (обязательное поле, с валидацией на корректность ввода email)
- Пароль (обязательное поле, с валидацией на минимальную длину пароля)
- Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
заполнено или данные не прошли валидацию, то должно выводиться соответствующее
сообщение об ошибке.
Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
об ошибке.
"""

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from hw.hw_3.models_3 import db, User

from hw.hw_3.forms_1 import RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data

        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return 'Error: User already exists. Please choose a different username or email'

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return 'Registration successful'

    return render_template('register.html', form=form)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


if __name__ == '__main__':
    app.run(debug=True)
