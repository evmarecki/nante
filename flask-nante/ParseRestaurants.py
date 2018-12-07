from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import json

def simple_get():
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    ###TO DO: add urls for "Uyo","Abuja", "Lagos", "Ikeja"
    urls = ['https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Accra+Ghana&key=AIzaSyC75TiPjZdPTa4e_5aT6wu0NeXczGME33A',
    'https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Uyo+Nigeria&key=AIzaSyC75TiPjZdPTa4e_5aT6wu0NeXczGME33A',
    'https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Abuja+Nigeria&key=AIzaSyC75TiPjZdPTa4e_5aT6wu0NeXczGME33A',
    'https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Lagos+Nigeria&key=AIzaSyC75TiPjZdPTa4e_5aT6wu0NeXczGME33A',
    'https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Ikeja+Nigeria&key=AIzaSyC75TiPjZdPTa4e_5aT6wu0NeXczGME33A']
    
    cities=["Accra", "Uyo", "Abuja","Lagos","Ikeja"]
    
    #loop through all cities/urls
    for j in range(0, len(urls)):
        
        #get json from site
        with closing(get(urls[j], stream=True)) as resp:
            data = resp.content
        
        #read json 
        with open(data, encoding = 'utf-8') as data_file:
            jsonData = json.loads(data_file.read()) #if error, try changing to load, not loads
        #get array of all restaurants and their data
        allResults=jsonData["results"]
    
        #initialize arrays to return
        ids=list()
        names=list()
        address=list()
        ratings=list()
        isopen=list()
    
        #loop through all restaurants data, get values you want
        for p in allResults:
            ids.append(p["place_id"])
            names.append(p["name"])
            address.append(p["formatted_address"])
            ratings.append(p["rating"])
            isopen.append(p["opening_hours"]["open_now"])
            
        ##connect to db
        conn = psycopg2.connect(host="127.0.0.1",database="postgres", user="postgres", password="postgres")
        cur = conn.cursor() #http://www.postgresqltutorial.com/postgresql-python/delete/
        cur.execute("truncate Restaurant")
        ##loop through values, add to table
        for i in range(0, len(name)):
            s= "INSERT INTO Restaurant VALUES (%s, %s, %s, %s)"
            cur.execute(s, (names[i], address[i], ratings[i], isopen[i]))
     
        ##loose ends
        conn.commit()
        cur.close()
        conn.close()
    
simple_get()