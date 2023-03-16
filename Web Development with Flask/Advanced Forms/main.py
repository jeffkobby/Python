from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

# form validators
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = "random string"


class MyFirstFlaskForm(FlaskForm):
    email = StringField(label="email", validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField(label="password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Submit")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = MyFirstFlaskForm()
    test_email = "admin@email.com"
    test_password = "123456789"

    if login_form.validate_on_submit():
        if login_form.email.data == test_email and login_form.password.data == test_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login.html', form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
