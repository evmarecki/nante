from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import modelsNew

app = Flask(__name__)
app.secret_key = 's3cr3t'
# app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

@app.route('/')
def main():
    return render_template('homepage.html')

@app.route('/Accra')
def Accra():
    AccraWeather = db.session.query(modelsNew.Weather)\
        .filter(modelsNew.Location.city == 'Accra').one()
    AccraMovies = db.session.query(modelsNew.Movies)\
        .filter(modelsNew.Location.city == 'Accra').one()
    return render_template('AccraTemplate.html', AccraMovies=AccraMovies, AccraWeather= AccraWeather)

@app.route('/Uyo')
def Uyo():
    AccraWeather = db.session.query(modelsNew.Weather)\
        .filter(modelsNew.Location.city == 'Uyo').one()
    AccraMovies = db.session.query(modelsNew.Movies)\
        .filter(modelsNew.Location.city == 'Uyo').one()
    return render_template('UyoTemplate.html', UyoMovies=UyoMovies, UyoWeather= UyoWeather)

@app.route('/Abuja')
def Abuja():
    AbujaWeather = db.session.query(modelsNew.Weather)\
        .filter(modelsNew.Location.city == 'Abuja').one()
    AbujaMovies = db.session.query(modelsNew.Movies)\
        .filter(modelsNew.Location.city == 'Abuja').one()
    return render_template('AbujaTemplate.html', AbujaMovies=AbujaMovies, AbujaWeather= AbujaWeather)

@app.route('/Lagos')
def Lagos():
    LagosWeather = db.session.query(modelsNew.Weather)\
        .filter(modelsNew.Location.city == 'Lagos').one()
    LagosMovies = db.session.query(modelsNew.Movies)\
        .filter(modelsNew.Location.city == 'Lagos').one()
    return render_template('LagosTemplate.html', LagosMovies=LagosMovies, LagosWeather= LagosWeather)

@app.route('/Ikeja')
def Ikeja():
    IkejaWeather = db.session.query(modelsNew.Weather)\
        .filter(modelsNew.Location.city == 'Ikeja').one()
    IkejaMovies = db.session.query(modelsNew.Movies)\
        .filter(modelsNew.Location.city == 'Ikeja').one()
    return render_template('IkejaTemplate.html', IkejaMovies=IkejaMovies, IkejaWeather= IkejaWeather)


    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)