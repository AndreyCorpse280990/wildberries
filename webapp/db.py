from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from webapp import config


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy()
db.init_app(app)
