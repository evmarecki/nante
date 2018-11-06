# -*- coding: utf-8 -*-

# from flask import Flask, template, jsonify
# from key import key
# app = Flask(Nante
import requests
import psycopg2 as pg2

conn = psycopg2.connect(host="35.229.38.35",database="test", user="postgres", password="postgres")
cursor = connect.cursor()

def kelvinToCelcius(num):
	return num - 273.15

def kelvinToFahrenheit(num):
	return kelvinToCelcius(num) * (float(9)/5) + 32


# api_address = 'api.openweathermap.org/data/2.5/weather?appid=450f081fa3b3d9ed257e4d6dc26f05f0&q='
# api_address = "http://api.openweathermap.org/data/2.5/weather?450f081fa3b3d9ed257e4d6dc26f05f0q=London"
api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

city = "Accra"

url = api_address + city

json_data = requests.get(url).json()

print(json_data)
print("-----")

print(city)

#current time, date

description = json_data["weather"][0]["main"]

print(description)

temperature = json_data["main"]["temp"]
print("temperature in celc")
tempC = kelvinToCelcius(temperature)
print(tempC)
print("temperature in fahr")
tempF = kelvinToFahrenheit(temperature)
print(tempF)

humidity = json_data["main"]["humidity"]
print("humidity")
print(humidity)

insertSql = INSERT INTO WEATHER VALUES (city, description, tempC, tempF, humidity);
updateSql = UPDATE WEATHER SET weather.city = city and weather.description = description and weather.tempC = tempC and weather.tempF = tempF and weather.humidity = humidity where city = city
IF NOT EXISTS(SELECT weather.city from WEATHER where weather.city = city) THEN
cur.execute(insertSql, (city, description, tempC, tempF, humidity))
END IF;

IF NOT EXISTS(SELECT weather.city from WEATHER where weather.city = city) THEN
cur.execute(updateSql, (city, description, tempC, tempF, humidity))
END IF;

conn.commit()
cursor.close()

# if location already exists and we want to update the data, do update 