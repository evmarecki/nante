# coding: utf-8

# In[33]:


from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import psycopg2

def getHTML():
##make list of all urls
    urls=["https://silverbirdcinemas.com/cinema/accra/","https://silverbirdcinemas.com/cinema/uyo/", "https://silverbirdcinemas.com/cinema/sec-abuja/","https://silverbirdcinemas.com/cinema/galleria/","https://silverbirdcinemas.com/cinema/ikeja/"]
    cities=["Accra", "Uyo", "Abuja","Victoria Island","Ikeja"]
    theaters=["Accra Mall","Ibom Tropicana Entertainment Centre","Silverbird Entertainment Centre","Silverbird Cinemas, Galleria","Ikeja City Mall"]
    count=1
##clear old data
    conn = psycopg2.connect(host="127.0.0.1",database="postgres", user="postgres", password="postgres")
    cur = conn.cursor() #http://www.postgresqltutorial.com/postgresql-python/delete/

    ##clear current table
    cur.execute("truncate Movies") #if error, try adding cascade https://stackoverflow.com/questions/15712239/psql-how-to-flush-database-content-without-dropping-table
    conn.commit()
    cur.close()
    conn.close()
    for j in range(0, len(urls)-1):
        url=urls[j]
        city=cities[j]
        theater=theaters[j]
        ##get html
        with closing(get(url, stream=True)) as webResponse: #https://silverbirdcinemas.com/cinema/accra/
            html=webResponse.content

    ##declare lists 
        MovieTitles=list()
        MovieTimes=list()
        MovieLengths=list()
        MovieRatings=list()
        MovieGenres=list()

    ##parse html
        htmlParsed = BeautifulSoup(html, 'html.parser') #https://realpython.com/python-web-scraping-practical-introduction/

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
        conn = psycopg2.connect(host="127.0.0.1",database="postgres", user="postgres", password="postgres")
        cur = conn.cursor() #http://www.postgresqltutorial.com/postgresql-python/delete/

        ##loop through values, add to table
        for i in range(0, len(MovieTitles)-1):
            s= "INSERT INTO Movies VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cur.execute(s, (city, theater, MovieTitles[i], MovieTimes[i], MovieLengths[i], MovieRatings[i], MovieGenres[i]))

        ##loose ends
        conn.commit()
        cur.close()
        conn.close()
getHTML()
