# CRUD Book App
This repo is about flask microframework with postgresql database.

## Features
* Register with email confirmation.
* Login.
* Create, Read, Update, Delete Favorite Book.



## How to run:
1. git clone https://github.com/akhisyabab/flask-book.git
2. cd flask-book
3. virtualenv -p python3 env
4. source env/bin/activate
5. pip install -r requirements.txt
5. edit your config in config.py, SQLALCHEMY_DATABASE_URI = 'postgres://name:password@localhost/database_name'
6. python3 db_create.py
7. python3 run.py
