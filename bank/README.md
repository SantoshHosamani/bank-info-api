

A RESTful API written in Django to get any branch details using ifsc code and find all the branches of a bank in a Indian city.


### Setting up
This project was built with python +3.5

$ pip3 install -r requirements.txt
$ cd bank
$ python3 manage.py runserver


Then head to 

To login
http://127.0.0.1:8000/api/token/ 
 
http://127.0.0.1:8000/ifsc/{ifsccode}
http://127.0.0.1:8000/branches/{city}/{bank-name}

in your browser to get started.

