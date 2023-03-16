from flask import Flask, render_template, url_for, redirect, flash

from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

from forms import RegisterUser, LoginUser


app = Flask(__name__)
app.config['SECRET_KEY'] = "a random string"
Bootstrap(app)

# TODO: Create a database for registered users with password encryption
# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alpha.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), nullable=False, unique=False)
    last_name = db.Column(db.String(250), nullable=False, unique=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)

# db.create_all()


# TODO: Add authentication with Flask to your project
# TODO: Ensure that only authenticated users can have access to the content of the website

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/elements')
def elements():
    return render_template('elements.html')


@app.route('/generic')
def generic():
    return render_template('generic.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/register')
def register():
    register = RegisterUser()
    return render_template('register.html', form=register)


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
