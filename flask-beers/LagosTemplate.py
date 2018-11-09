{% extends 'homepage.html' %} {% block heading %}Lagos, Nigeria{% endblock %} {% block content %} 

{% for movies in LagosMovies %} 
{{movies.title}}: {{movie.time_and_day}}
{% endfor %}

{% for data in LagosWeather %} 
Temperature (Celsius): {{data.tempC}}
Temperature (Fahrenheit): {{data.tempF}}
Description: {{data.summary}}
Humidity: {{data.humidity}}

{% endfor %}

{% endblock %} 