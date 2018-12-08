
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import modelsNew
import ParseMovies
import ParseHotels
import ParseWeather

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

@app.route('/')
def main():
    ParseWeather.getWeather()
    ParseMovies.getHTML()
    ParseHotels.getHTML()
    return render_template('homepage.html')

@app.route('/city/<city>')
def City(city):
    CityMovies = db.session.query(modelsNew.Movies)        .filter(modelsNew.Movies.city == city).all()
    CityWeather = db.session.query(modelsNew.Weather)        .filter(modelsNew.Weather.city == city).all()
    CityHotels = db.session.query(modelsNew.Hotel)        .filter(modelsNew.Hotel.city == city).all()
    CityRestaurants = db.session.query(modelsNew.Restaurant)        .filter(modelsNew.Restaurant.city == city).all()
    return render_template('city.html', movies=CityMovies, weather=CityWeather, hotels = CityHotels, restaurants = CityRestaurants)
   
@app.route('/city/<city>/movie/<rating>')
def Movie(city, rating):
    CityMovies = db.session.query(modelsNew.Movies)        .filter(modelsNew.Movies.city == city).filter(modelsNew.Movies.rating >=rating).all()
    return render_template('movie.html', movies=CityMovies)

@app.route('/city/<city>/hotel/<price>')
def Hotel(city, price):
    CityHotels = db.session.query(modelsNew.Hotel)        .filter(modelsNew.Hotel.city == city).filter(modelsNew.Hotel.price <=price).all()
    return render_template('hotel.html', hotels=CityHotels)

@app.route('/city/<city>/restaurant/<rating>')
def Restaurant(city, rating):
    CityRestaurants = db.session.query(modelsNew.Restaurant)        .filter(modelsNew.Restaurant.city == city).filter(modelsNew.Restaurant.rating >= rating).all()
    return render_template('restaurant.html', restaurants=CityRestaurants)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

