
# coding: utf-8

# In[33]:


from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import psycopg2

def getHTML(url):
    
##get html
    with closing(get("https://silverbirdcinemas.com/cinema/accra/", stream=True)) as webResponse: #https://silverbirdcinemas.com/cinema/accra/
        html=webResponse.content

##declare lists 
    MovieTitles=list()
    MovieTimes=list()
    MovieDays=list()
    MovieLength=list()
    MovieLang=list()
    MovieRating=list()
    MovieGenre=list()
    PhotoLink=list()

##parse html
    htmlParsed = BeautifulSoup(html, 'html.parser') #https://realpython.com/python-web-scraping-practical-introduction/
    count=0
##title
    for m in htmlParsed.findAll("h4", { "class" : "entry-title" }): 
        MovieTitles.append(m.get_text())
        
##movie length
    for m in htmlParsed.findAll("div", { "class" : "entry-date" }):
        MovieLength.append(m.get_text())
        
##movie times
    for m in htmlParsed.findAll("p", { "class" : "cinema_page_showtime" }):
        MovieTimes.append(m.get_text())
        
##genre
    for m in htmlParsed.findAll("div", { "class" : "note" }):
        MovieTitles.append(m.get_text())
##rating
    for m in htmlParsed.findAll("span", { "class" : "rate" }):
        MovieTitles.append(m.get_text())

##connect to db
#host : http://0.0.0.0:5000/
#	35.229.38.35
    conn = psycopg2.connect(host="127.0.0.1",database="postgres", user="postgres", password="postgres")
    cur = conn.cursor() #http://www.postgresqltutorial.com/postgresql-python/delete/

##clear current table
    cur.execute("truncate Movies") #if error, try adding cascade https://stackoverflow.com/questions/15712239/psql-how-to-flush-database-content-without-dropping-table

##loop through values, add to table
    for i in range(0, len(MovieTitles)-1):
        s= "INSERT INTO Movies (city, Theater_name ,title, time_and_day, length, rating, genre) VALUES ($s,%s,%s, %s, %s, %s, %s);"
        cur.execute(s,'Accra', "Silver Bird Cinemas", MovieTitles[i], MovieTimes[i], MovieLength[i], MovieRating[i], MovieGenre[i])

##loose ends
    cur.close()
    conn.close()

