{% extends 'homepage.html' %} {% block heading %}Accra, Ghana{% endblock %} {% block content %} 

{% for movies in AccraMovies %} 
{{movies.title}}: {{movie.time_and_day}}
{% endfor %}

{% for data in AccraWeather %} 
Temperature (Celsius): {{data.tempC}}
Temperature (Fahrenheit): {{data.tempF}}
Description: {{data.summary}}
Humidity: {{data.humidity}}

{% endfor %}

{% endblock %} 