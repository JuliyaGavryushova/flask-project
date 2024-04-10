"""
Создать базу данных для хранения информации о книгах в библиотеке.
База данных должна содержать две таблицы: "Книги" и "Авторы".
В таблице "Книги" должны быть следующие поля: id, название, год издания,
количество экземпляров и id автора.
В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
Необходимо создать связь между таблицами "Книги" и "Авторы".
Написать функцию-обработчик, которая будет выводить список всех книг с
указанием их авторов.
"""

from flask import Flask, render_template
from hw.hw_3.models_1 import db, Book, Author
from faker import Faker

fake = Faker()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi'


@app.route('/books/')
def all_books():
    books = Book.query.all()
    context = {'books': books}
    return render_template('books.html', **context)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_tables():
    count = 5
    for author in range(1, count + 1):
        new_author = Author(name=fake.first_name(), surname=fake.last_name())
        db.session.add(new_author)
    db.session.commit()

    for book in range(1, count * 2):
        new_book = Book(title=fake.sentence(nb_words=10),
                        publication=fake.random_int(min=1800, max=1999),
                        quantity=fake.random_int(min=100, max=1000),
                        author_id=fake.random_int(min=1, max=5))
        db.session.add(new_book)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)