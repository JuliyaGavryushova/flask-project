"""
Доработаем задача про студентов
Создать базу данных для хранения информации о студентах и их оценках в
учебном заведении.
База данных должна содержать две таблицы: "Студенты" и "Оценки".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
и email.
В таблице "Оценки" должны быть следующие поля: id, id студента, название
предмета и оценка.
Необходимо создать связь между таблицами "Студенты" и "Оценки".
Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их оценок.
"""

from flask import Flask, render_template
from hw.hw_3.models_2 import db, Student, Grade
from faker import Faker

fake = Faker()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/grades/')
def all_grades():
    grades = Grade.query.all()
    context = {'grades': grades}
    return render_template('grades.html', **context)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_tables():
    count = 5
    for student in range(1, count + 1):
        new_student = Student(name=fake.first_name(),
                              surname=fake.last_name(),
                              group=fake.random_int(min=1, max=15),
                              email=fake.ascii_free_email())
        db.session.add(new_student)
    db.session.commit()

    for grade in range(1, count + 1):
        new_grade = Grade(student_id=fake.random_int(min=1, max=5),
                          subject=fake.random_element(elements=("mathematics", "informatics", "physics")),
                          grade=fake.random_int(min=1, max=5))
        db.session.add(new_grade)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)