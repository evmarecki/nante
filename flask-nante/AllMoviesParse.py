# coding: utf-8
 # In[30]:
from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import psycopg2 as pg2
    
##get html
with closing(get("https://silverbirdcinemas.com/cinema/accra/", stream=True)) as webResponse: #https://silverbirdcinemas.com/cinema/accra/
    html=webResponse.content
 ##declare lists 
MovieTitles=list()
MovieTimes=list()
MovieDays=list()
MovieLengths=list()
MovieRatings=list()
MovieGenres=list()

 ##parse html
htmlParsed = BeautifulSoup(html, 'html.parser') #https://realpython.com/python-web-scraping-practical-introduction/
count=0

##title
for m in htmlParsed.findAll("h4", { "class" : "entry-title" }): 
    MovieTitles.append(m.get_text())
    
##movie length
for m in htmlParsed.findAll("div", { "class" : "entry-date" }):
    MovieLengths.append(m.get_text())
    
##movie times
for m in htmlParsed.findAll("p", { "class" : "cinema_page_showtime" }):
    MovieTimes.append(m.get_text())
    
##genre
for m in htmlParsed.findAll("div", { "class" : "note" }):
    MovieGenres.append(m.get_text())
##rating
for m in htmlParsed.findAll("span", { "class" : "rate" }):
    MovieRatings.append(m.get_text())

 ##connect to db
connect = pg2.connect(host="127.0.0.1",database="postgres", user="postgres", password="postgres")
cursor = connect.cursor() #http://www.postgresqltutorial.com/postgresql-python/delete/
 ##clear current table
cursor.execute("truncate Movies;") #if error, try adding cascade https://stackoverflow.com/questions/15712239/psql-how-to-flush-database-content-without-dropping-table
 ##loop through values, add to table
for i in range(0, len(MovieTitles)-1):
    s= "INSERT INTO Movies VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(s, (city, theater_name, MovieTitles[i], MovieTimes[i], MovieLengths[i], MovieRatings[i], MovieGenres[i]))
 ##loose ends
cursor.close()
connect.close()
