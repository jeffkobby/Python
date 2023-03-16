from pprint import pp

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlite3 import OperationalError
import sqlite3

app = Flask(__name__)
# database = sqlite3.connect('books-collection.db')
# cursor = database.cursor()
#
#
# cursor.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) "
#                "NOT NULL, rating FLOAT NOT NULL)")
#
#
# cursor.execute("INSERT OR IGNORE INTO books VALUES(2, 'Tales of Two Cities', 'Charles Dickens', 7/10)")
# database.commit()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
database = SQLAlchemy(app)

class Book(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(250), unique=True, nullable=False)
    author = database.Column(database.String(250), nullable=False)
    rating = database.Column(database.Float, nullable=False)

database.create_all()

# create new entry
# new_book = Book(title="Test", author="Charles Dickens", rating="7.5")
# database.session.add(new_book)
# database.session.commit()

# read all records
# all_books = database.session.query(Book).all()
# for book in all_books:
#     pp(book.title)

# read a particular record by query
# book = Book.query.filter_by(author="J.K Rowling").first()
# print(book.title)

# update a record by query
# book_to_update = Book.query.filter_by(title="Test").first()
# book_to_update.title = "The Chimes"
# book_to_update.rating = 8.9
# database.session.commit()

# update a record by primary key
# book_id = 3
# book_to_update = Book.query.get(book_id)
# book_to_update.rating = 6.5
# database.session.commit()


@app.route('/')
def home():
    # read all records from database
    all_books = database.session.query(Book).all()

    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        form = request.form

        new_book = Book(title=form['book_name'], author=form['book_author'], rating=form['book_rating'])
        database.session.add(new_book)
        database.session.commit()


        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit/id=<int:book_id>", methods=['GET', 'POST'])
def edit_rating(book_id):
    requested_book = Book.query.get(book_id)

    if request.method == "POST":
        form = request.form
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = form['new_rating']
        database.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", book=requested_book)

@app.route("/delete/id=<int:book_id>", methods=['GET', 'POST'])
def delete(book_id):
    book_to_delete = Book.query.get(book_id)
    database.session.delete(book_to_delete)
    database.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

