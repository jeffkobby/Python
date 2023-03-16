from pprint import pp

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db = SQLAlchemy(app)


# movie table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(250), unique=True, nullable=False)


#
# create tables
# db.create_all()

# movie table entry
# new_movie = Movie(title="Drive",
#                   year=2011,
#                   description="A mysterious Hollywood stuntman and mechanic moonlights as a getaway driver and finds "
#                               "himself in "
#                               "trouble when he helps out his neighbor in this action drama",
#                   rating=7.5,
#                   ranking=10,
#                   review="Loved it!",
#                   img_url="https://www.shortlist.com/media/images/2019/05/the-30-coolest-alternative-movie-posters"
#                           "-ever-2-1556670563-K61a-column-width-inline.jpg")
# db.session.add(new_movie)
# db.session.commit()

# edit form
class EditForm(FlaskForm):
    rating = StringField(label="Your rating out of 10 eg. 7.5")
    review = StringField(label="Your review")
    submit = SubmitField(label="Done")


# add movie form
class AddMovie(FlaskForm):
    name = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()

    for rank in range(len(all_movies)):
        all_movies[rank].ranking = len(all_movies)-1
    db.session.commit()
    return render_template("index.html", movies=all_movies)


# add a movie to the database
@app.route("/add", methods=['GET', 'POST'])
def add():
    add_form = AddMovie()

    if add_form.validate_on_submit():
        # get user input from the add form
        movie_title = add_form.name.data
        params = {
            "api_key": "4683ed9298204e75e1ca3cbdbdc3a32a",
            "query": movie_title
        }

        # get movies based on user's search query
        response = requests.get(url="https://api.themoviedb.org/3/search/movie", params=params)
        movie_data = response.json()['results']

        # render 'select.html' that displays a list of movies based on user's search query
        return render_template('select.html', options=movie_data)

    return render_template("add.html", form=add_form)


# get movie details based on user's selction in 'select.html'
@app.route("/find")
def find_movie():
    movie_api_id = request.args.get('id')
    MOVIE_IMG_PATH = "https://image.tmdb.org/t/p/w500"
    params = {
        'api_key': '4683ed9298204e75e1ca3cbdbdc3a32a',
        'language': 'en-US'
    }
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_api_id}", params=params)
    data = response.json()

    # add movie to the database
    new_movie = Movie(
        title=data['original_title'],
        img_url=f"{MOVIE_IMG_PATH}{data['backdrop_path']}",
        year=data["release_date"].split("-")[0],
        description=data['overview']
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', movie_id=new_movie.id))


@app.route("/edit/id=<int:movie_id>", methods=['POST', 'GET'])
def edit(movie_id):
    edit_form = EditForm()
    if edit_form.validate_on_submit():

        # update rating if user wants to update rating only
        if edit_form.rating.data != "" and edit_form.review.data == "":
            movie_to_update = Movie.query.get(movie_id)
            movie_to_update.rating = edit_form.rating.data
            db.session.commit()

        # update review only
        elif edit_form.review.data != "" and edit_form.rating.data == "":
            movie_to_update = Movie.query.get(movie_id)
            movie_to_update.review = edit_form.review.data
            db.session.commit()

        # update both fields
        else:
            movie_to_update = Movie.query.get(movie_id)
            movie_to_update.review = edit_form.review.data
            movie_to_update.rating = edit_form.rating.data
            db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=edit_form)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
