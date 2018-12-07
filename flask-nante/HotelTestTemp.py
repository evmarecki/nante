# coding: utf-8

# In[6]:


from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import psycopg2

def getHTML():
    #declare cities, hotel urls
    urls=["https://www.booking.com/city/gh/accra.html", "https://www.booking.com/city/ng/uyo.html","https://www.booking.com/city/ng/abuja.html", "https://www.booking.com/city/ng/lagos.html", "https://www.booking.com/city/ng/ikeja.html"]
    cities=["Accra","Uyo","Abuja", "Lagos", "Ikeja"]
    
    ##clear old data
    conn = psycopg2.connect(host="127.0.0.1",database="postgres", user="postgres", password="postgres")
    cur = conn.cursor() #http://www.postgresqltutorial.com/postgresql-python/delete/

    ##clear current table
    cur.execute("truncate Hotel") #if error, try adding cascade https://stackoverflow.com/questions/15712239/psql-how-to-flush-database-content-without-dropping-table
    conn.commit()
    cur.close()
    conn.close()
    
    ##start loop through cities
    for i in range(0,len(urls)):
        url=urls[i]
        city=cities[i]
        with closing(get(url, stream=True)) as webResponse: #https://silverbirdcinemas.com/cinema/accra/
            html=webResponse.content
        htmlParsed = BeautifulSoup(html, 'html.parser')
    
    
        ##declare lists
        description=list()
        price=list()
        rating=list()
        name=list()
    
        ##description
        count1=0;
        for m in htmlParsed.findAll("p", { "class" : "bui-card__text hotel-card__text--wrapped" }):
            count1+=1
            dummy=' '.join([line.strip() for line in m.get_text().strip().splitlines()])
            if count1<7:
                description.append(dummy)
        #print(m.get_text())
        
    ##price 
        count1=0;
        for m in htmlParsed.findAll("div", { "class" : "hotel-card__price bui-spacer--small" }):
            count1+=1
            dummy=m.get_text().strip()
            if count1<7:
                price.append(float(dummy[19:]))
        if city=="Uyo":
            price=[-1, -1, -1, -1, -1, -1]
        
        
        ##rating
        count1=0;
        for m in htmlParsed.findAll("div", { "class" : "bui-card__text" }):
            count1+=1
            dummy=m.get_text().strip()
            
            if count1<7:
                rating.append(float(dummy[:3]))
        if city=="Uyo":
            rating=[-1, -1, -1, -1, -1, -1]
        
        ##name
        count1=0;
        for m in htmlParsed.findAll("h3", { "class" : "bui-card__title" }):
        #print(m.get_text())
            count1+=1
            if count1<7:
                name.append(m.get_text().strip())

 ##connect to db
        conn = psycopg2.connect(host="127.0.0.1",database="postgres", user="postgres", password="postgres")
        cur = conn.cursor() #http://www.postgresqltutorial.com/postgresql-python/delete/

        ##loop through values, add to table
        for i in range(0, len(name)):
            s= "INSERT INTO Hotel VALUES (%s, %s, %s, %s)"
            cur.execute(s, (city, name[i], rating[i], price[i]))
     
        ##loose ends
        conn.commit()
        cur.close()
        conn.close()

    
getHTML()

# def getHTML(url):


##get html
with closing(get("https://silverbirdcinemas.com/cinema/accra/", stream=True)) as webResponse: #https://silverbirdcinemas.com/cinema/accra/
    html=webResponse.content


##declare lists 

MovieTitles=list()
MovieTimes=list()
MovieLengths=list()
MovieRatings=list()
MovieGenres=list()


##parse html
htmlParsed = BeautifulSoup(html, 'html.parser') #https://realpython.com/python-web-scraping-practical-introduction/
count=0


#city
city = 'Accra'


#theater name
theater_name = 'Silver Bird Cinemas'


##title
for m in htmlParsed.findAll("h4", { "class" : "entry-title" }): 
    MovieTitles.append(m.get_text())
    print("titles")
    print(m.get_text())


print()
##movie length
for m in htmlParsed.findAll("div", { "class" : "entry-date" }):
    print("lengths")
    print(m.get_text())
    MovieLengths.append(m.get_text())
    
print()
##movie times
for m in htmlParsed.findAll("p", { "class" : "cinema_page_showtime" }):
    MovieTimes.append(m.get_text())
    print("times")
    print(m.get_text())
    print()
##genre
for m in htmlParsed.findAll("div", { "class" : "note" }):
    MovieGenres.append(m.get_text())
    print("genre")
    print(m.get_text())


print()

##rating
for m in htmlParsed.findAll("span", { "class" : "rate" }):
    MovieRatings.append(m.get_text())
    print("rating")
    print(m.get_text())
print()
##connect to db
conn = psycopg2.connect(host="127.0.0.1",database="postgres", user="postgres", password="postgres")
cur = conn.cursor() #http://www.postgresqltutorial.com/postgresql-python/delete/

##clear current table

cur.execute("truncate Movies") #if error, try adding cascade https://stackoverflow.com/questions/15712239/psql-how-to-flush-database-content-without-dropping-table




















