## Nante
Nante means journey in Akan (a major language spoken in Ghana). The word captures the the essence of this web-based application. 

The intention of this current iteration of Nante is to create a web application that will be a guide to West Africa, specifically Ghana and Nigeria for now. The application will take city and country (in West Africa) as inputs. It will output weather, languages, population data, various movies, and food options available in the area. The motivation behind this project is to have an application which tourists can use to plan their daily activities while in a major African city.



## Getting Started

Setting up PostgreSQL: https://cloud.google.com/community/tutorials/setting-up-postgres 

[createTables.txt](https://github.com/evmarecki/nante/blob/master/createTables.txt) - Code for creating tables in PostgreSQL

## Built With
* [Flask](http://flask.pocoo.org/) - The web framework used
* [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL Toolkit and ORM

## Contributers
Refer to [members.txt](https://github.com/evmarecki/nante/blob/master/members.txt).

## Code Structure
* [nanteapp.py](https://github.com/evmarecki/nante/blob/master/flask-nante/nanteapp.py) - Main app to run to launch website.
* [static](https://github.com/evmarecki/nante/tree/master/flask-nante/static) - Contains static files - images.
* [templates](https://github.com/evmarecki/nante/tree/master/flask-nante/templates) - Contains all html files.

## Running the app
To run the website, in your Flask app directory on the VM, simply issue the following command:
python nanteapp.py

[More information on running Flask](https://sites.duke.edu/compsci316_01_f2018/help/flask/) 


## Limitations on current implementation 
The filters to narrow down data items by price and rating are only done for Accra, Ghana, rather than for all the cities. 
