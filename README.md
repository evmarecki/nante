## Nante
Brief intro goes here

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
