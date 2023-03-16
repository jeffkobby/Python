import flask
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy

# important for hashing/encrypting passwords during registering
from werkzeug.security import generate_password_hash, check_password_hash

# important for logging into the app
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

############################### Configure the flask application ############################
app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = "static/files"
filename = "cheat_sheet.pdf"
db = SQLAlchemy(app)

# configure the flask_login application
login_manager = LoginManager()
login_manager.init_app(app)


#############################################################################################


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Load the user object from the ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # if email already exists in the database
    if User.query.filter_by(email=request.form.get('email')).first():
        flash("You've already signed up with that email, log in instead!")
        return redirect(url_for('login'))

    # create a new user
    else:
        if request.method == "POST":
            new_user = User(
                email=request.form['email'],
                password=generate_password_hash(password=request.form['password'],
                                                salt_length=8),
                name=request.form['name']
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('secrets', name=new_user.name))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # find a user in the database by using the email as a search query
        user = User.query.filter_by(email=email).first()

        # if email does not exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))

        # compare the password hash to password entered
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))

        # email and password is correct
        else:
            login_user(user)
            flash("You have successfully logged in")
            return redirect(url_for('secrets', name=user.name))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets/<name>')
@login_required
def secrets(name):
    return render_template("secrets.html", name=name, logged_in=True)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
@login_required
def download():
    # use the send_from_directory() method to send a file from a given directory / upload a file
    return send_from_directory(directory=app.config['UPLOAD_FOLDER'], path="cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
