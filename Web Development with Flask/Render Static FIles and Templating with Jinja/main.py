from flask import Flask, render_template
from datetime import datetime as dt
import requests
from pprint import pp

GENDERIZE_API_ENDPOINT = "https://api.genderize.io?"
AGIFY_API_ENDPOINT = "https://api.agify.io?"


app = Flask(__name__)


@app.route('/')
def index():
    current_year = dt.now().year
    return render_template("index.html", current_year=current_year)

@app.route('/guess/<name>')
def guess_name(name):
    parameters = {
        "name": name
    }
    genderize_response = requests.get(url=GENDERIZE_API_ENDPOINT, params=parameters)
    genderize_data = genderize_response.json()

    agify_response = requests.get(url=AGIFY_API_ENDPOINT, params=parameters)
    agify_data = agify_response.json()

    user_name = parameters['name']
    user_age = agify_data['age']
    user_gender = genderize_data['gender']

    return render_template("guess.html", name=user_name, age=user_age,  gender=user_gender)
if __name__ == "__main__":
    app.run(debug=True)

