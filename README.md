## Nante
Brief intro goes here

## Getting Started
How to compile, set up, deploy, and use your system goes here
Setting up PostgreSQL: https://cloud.google.com/community/tutorials/setting-up-postgres 

Code for creating the tables

CREATE TABLE Location
(city VARCHAR(256) NOT NULL UNIQUE,
 country VARCHAR(256) NOT NULL,
PRIMARY KEY(city,country));

CREATE TABLE Movies
(city VARCHAR(256) NOT NULL REFERENCES Location(city),
Theater_name VARCHAR(256) NOT NULL,
 title VARCHAR(256) NOT NULL,
Time_and_day  VARCHAR(256) NOT NULL,
length INT,
rating DECIMAL(10,2),
genre VARCHAR(256),
PRIMARY KEY(title, time_and_day, city, Theater_name));

CREATE TABLE Weather
(city VARCHAR(256) NOT NULL REFERENCES Location(city),
summary VARCHAR(256),
tempc VARCHAR(256),
tempf VARCHAR(256),
humidity VARCHAR(256),
PRIMARY KEY(city));

CREATE TABLE Restaurant 
(city VARCHAR(256) NOT NULL REFERENCES Location(city),
name VARCHAR(256) NOT NULL,
address VARCHAR(256) NOT NULL,
rating DECIMAL(10,2),
hours VARCHAR(256) NOT NULL,
PRIMARY KEY(name, address));

CREATE TABLE Hotel 
(city VARCHAR(256) NOT NULL REFERENCES Location(city),
name VARCHAR(256) NOT NULL,
rating DECIMAL(10,2),
price DECIMAL(10,2) , 
PRIMARY KEY(city, name));

CREATE TABLE ServedIn
(address VARCHAR(256) NOT NULL,
city VARCHAR(256) NOT NULL,
Name VARCHAR(256) NOT NULL,
PRIMARY KEY (name, address, city));

## Built With
* [Flask](http://flask.pocoo.org/) - The web framework used
* [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL Toolkit and ORM

## Contributers
Refer to [members.txt](https://github.com/evmarecki/nante/blob/master/members.txt).

## Code Structure
* [nanteapp.py](https://github.com/evmarecki/nante/blob/master/flask-nante/nanteapp.py) - Main app to run to launch website.
* [static](https://github.com/evmarecki/nante/tree/master/flask-nante/static) - Contains static files - images.
* [templates](https://github.com/evmarecki/nante/tree/master/flask-nante/templates) - Contains all html files.

