# -*- coding: utf-8 -*-

# from flask import Flask, template, jsonify
import requests
# from key import key
# app = Flask(Nante

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
print(kelvinToCelcius(temperature))
print("temperature in fahr")
print(kelvinToFahrenheit(temperature))

humidity = json_data["main"]["humidity"]
print("humidity")
print(humidity)



