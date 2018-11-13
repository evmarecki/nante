from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import modelsNew
import forms

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

@app.route('/')
def main():
    return render_template('homepage.html')

@app.route('/city/<city>')
def City(city):
    CityWeather = db.session.query(modelsNew.Weather)\
        .filter(modelsNew.Weather.city == city).one()
    CityMovies = db.session.query(modelsNew.Movies)\
        .filter(modelsNew.Location.city == city).one() #TODO: fix, want multiple movies, then fix template
    return render_template('city.html', Movies=CityMovies, Weather= CityWeather)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)