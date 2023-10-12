# Example of Flask application, simple market
Project structure

````
market/
├── models
├── routers
├── services
├── static
├── templates
│   └── includes
└── webforms
````
Clone project
````
git clone git@github.com:bohdan-sk7/flask-market.git
cd flask-market
````

Install project requirements
````
pip install -r requirements.txt
````
Install MySQL database

[Download MySQL](https://dev.mysql.com/downloads/)

Create .env file in the root of the project, with following variables
````
SECRET_KEY=(some random secret value, can be generated hash value) 
DATABASE_URI=mysql+pymysql://{username}:password@localhost/{db name}?charset=utf8mb4
````
To start application run following command:
````
python run.py
````
Alternative way to start application on Linux OS using CLI
````
export FLASK_APP=run.py
flask run
````
On Windows CMD:
````
set FLASK_APP=run.py
flask run
````