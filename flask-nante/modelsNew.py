from sqlalchemy import sql, orm
from nanteapp import db

class Location(db.Model):
    __tablename__ = 'location'
    city = db.Column('city', db.String(256), primary_key=True)
    country = db.Column('country', db.String(256))
    population = db.Column('population', db.String(256))
    fun_fact = db.Column('fun_fact', db.String(256))

class Movies(db.Model):
    __tablename__ = 'movies'
    city = db.Column('city', db.String(20),db.ForeignKey('Location.city', primary_key=True))
    theater_name = db.Column('theater_name', db.String(256), primary_key=True)
    title = db.Column('title', db.String(256),primary_key=True)
    time_and_day = db.Column('time_and_day', db.String(256),primary_key=True)
    length = db.Column('length', db.String(256))
    rating = db.Column('rating', db.String(256))
    genre = db.Column('genre', db.String(256))
    

class Weather(db.Model):
    __tablename__ = 'weather'
    city = db.Column('city', db.String(256),
                        db.ForeignKey('Location.city'),
                        primary_key=True)
    summary = db.Column('summary', db.String(256))
    tempC = db.Column('tempc', db.String(256)) 
    tempF = db.Column('tempf', db.String(256))
    humidity = db.Column('humidity', db.String(256))
