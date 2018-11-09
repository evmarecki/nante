# -*- coding: utf-8 -*-

import requests
import psycopg2 as pg2

def kelvinToCelcius(num):
	return int(num - 273.15)

def kelvinToFahrenheit(num):
	return int(kelvinToCelcius(num) * (float(9)/5) + 32)

connect = pg2.connect(host="127.0.0.1",database="postgres", user="postgres", password="postgres")
cursor = connect.cursor()

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

cursor.execute("TRUNCATE WEATHER")
cursor.execute("SELECT city FROM LOCATION")
cities = cursor.fetchall()
for city in cities:
	url = api_address + city[0]
	json_data = requests.get(url).json()
	#TO DO: output current time, date
	description = json_data["weather"][0]["main"]
	temperature = json_data["main"]["temp"]
	tempC = kelvinToCelcius(temperature)
	tempF = kelvinToFahrenheit(temperature)
	humidity = json_data["main"]["humidity"]
	cursor.execute("INSERT INTO WEATHER VALUES (%s, %s, %s, %s, %s)", (city, description, tempC, tempF, humidity))

connect.commit()
cursor.close()
connect.close()
