# file name: __init__.py
# shioppingMall_zioyou/start_shoppingmall/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# register SQLAlchemy
app.secret_key = 'lkb032088*'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kb:lkb032088*@localhost:3306/testDB'
app.config['SQlALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




