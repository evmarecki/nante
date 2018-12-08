
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import psycopg2

def rest():
    cities=["Accra", "Uyo", "Abuja","Lagos","Ikeja"]
    
            ##connect to db
    conn = psycopg2.connect(host="127.0.0.1",database="postgres", user="postgres", password="postgres")
    cur = conn.cursor() #http://www.postgresqltutorial.com/postgresql-python/delete/
     
    cur.execute("truncate Restaurant") #if error, try adding cascade https://stackoverflow.com/questions/15712239/psql-how-to-flush-database-content-without-dropping-table
    conn.commit()

    #accra
    names=["Buka Restaurant Osu","Santoku", "La Chaumiere", "Simret Ethiopian Restaurant"]
    address=["10th St, Accra, Ghana", "16 N Airport Rd, Accra, Ghana", "131 Liberation Road, Accra, Ghana","7A S Ridge Rd, Accra, Ghana"]
    ratings=[4.1, 4.5, 4.3, 4.5]
    isopen=["12-9PM, Monday-Saturday", "12-2:30, 6:30-9:45 Monday-Saturday", "12-2:30, 7:30-11:30 Monday-Saturday","6:30-10, Tuesday-Saturday"]
        
    for i in range(0, len(names)):
        s= "INSERT INTO Restaurant VALUES (%s,%s, %s, %s, %s)"
        cur.execute(s, ('Accra',names[i], address[i], ratings[i], isopen[i]))
     
        ##loose ends
    conn.commit()
    
    #Uyo
    names=['Food Affairs','Kilimanjaro Fast Food','Chop Stop Restaurant','Silver Lounge Restaurant & Bar.']
    address=['Udo Obio Street, Uyo, Akwa Ibom State, Nigeria', '165 Oron Rd, Uyo, Nigeria','Ewet Housing Estate, Uyo, Akwa Ibom State, Nigeria','Udo Udoma Ave, Uyo, Nigeria']
    ratings=[3.9, 3.8,3.9,3.7]
    isopen=["8AM-9PM Monday-Sunday", "7AM-10PM, Monday-Sunday", '10AM-11PM Monday-Sunday','11:30AM-11:30PM Monday-Sunday']
    for i in range(0, len(names)):
        s= "INSERT INTO Restaurant VALUES (%s,%s, %s, %s, %s)"
        cur.execute(s, ('Uyo',names[i], address[i], ratings[i], isopen[i]))
     
        ##loose ends
    conn.commit()
        
    #Abuja
    names=['Nkoyo','BluCabana Restaurant & Cafe','Jevinik Restaurant','Gourmet Pizza Company']
    address=['Ceddi Plaza, Central Business Dis 900211, Abuja, Nigeria','1322 Shehu Yaradua Blvd, Mabushi, Abuja, Nigeria','494 Bangui St, Wuse 2, Abuja, Nigeria','20, Thaba-Tseka Street, Off IBB Way, Wuse 2, Abuja, Nigeria']
    ratings=[4.2,4.3,4.1,4.2]
    isopen=["11AM-11PM Monday-Sunday","8:30AM-12AM Monday-Sunday",'8AM-10PM Monday-Saturday','12-9PM Monday-Sunday']
    for i in range(0, len(names)):
        s= "INSERT INTO Restaurant VALUES (%s,%s, %s, %s, %s)"
        cur.execute(s, ('Abuja',names[i], address[i], ratings[i], isopen[i]))
     
        ##loose ends
    conn.commit()
        
        #Lagos
    names=['RSVP Victoria Island Lagos','Craft Gourmet By Lou Baker','Izanagi Japanese Cuisine','Bungalow\'s']
    address=['9 Eletu Ogabi St, Victoria Island 101001, Lagos, Nigeria','14 Idowu Martins St, Victoria Island, Lagos, Nigeria','19B Idejo St, Victoria Island 101241, Lagos, Nigeria','1296 Akin Adesola St, Victoria Island, Lagos, Nigeria']
    ratings=[4.3,4.4,4.4,4.1]
    isopen=["12PM-10 Tuesday-Sunday","10AM-10PM Tuesday-Sunday",'12-10:30PM Tuesday-Sunday','10:30AM-10PM Monday-Sunday']
    for i in range(0, len(names)):
        s= "INSERT INTO Restaurant VALUES (%s,%s, %s, %s, %s)"
        cur.execute(s, ("Lagos",names[i], address[i], ratings[i], isopen[i]))
     
        ##loose ends
    conn.commit()
        
            #Ikeja
    names=['Ocean Basket','Commint Buka','BhEERHUGZ Café','Rhapsody\'s']
    address=['9 Obafemi Awolowo Way, Oregun, Ikeja, Nigeria','Allen, Ikeja, Nigeria','Ikeja City Mall, Obafemi Awolowo Way, Oregun, Ikeja, Nigeria','12 Old Medical Road, Oregun, Ikeja, Nigeria']
    ratings=[4.3,4.2,3.4,4.1]
    isopen=['8AM-10PM Monday-Sunday','9AM-8 Monday-Sunday','10AM-4AM Monday-Sunday',"11AM-3AM Monday-Sunday"]
    for i in range(0, len(names)):
        s= "INSERT INTO Restaurant VALUES (%s,%s, %s, %s, %s)"
        cur.execute(s, ("Ikeja",names[i], address[i], ratings[i], isopen[i]))
     
        ##loose ends
    conn.commit()
    cur.close()
    conn.close()
    
rest()
        

