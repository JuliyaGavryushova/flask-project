"""
Создать базу данных для хранения информации о студентах университета.
База данных должна содержать две таблицы: "Студенты" и "Факультеты".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
возраст, пол, группа и id факультета.
В таблице "Факультеты" должны быть следующие поля: id и название
факультета.
Необходимо создать связь между таблицами "Студенты" и "Факультеты".
Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их факультета.
"""

from flask import Flask
from .models_1 import db, Student, Faculty
from faker import Faker

fake = Faker()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello'


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("fill-db")
def fill_tables():
    count = 5
    for student in range(1, count + 1):
        new_stud = Student(name=fake.first_name(),
                           surname=fake.last_name(),
                           age=fake.random_int(min=17, max=30),
                           sex=fake.random_element(elements=("male", "female")),
                           group=fake.random_int(min=100, max=999),
                           id_faculty=1)
        db.session.add(new_stud)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
