
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship





app = Flask(__name__)
app.config.from_pyfile('config.py')
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"User {self.id}, {self.username}"


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(200), unique=True)

    def __repr__(self):
        return f"Item {self.id}, {self.name}"


class ItemPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    item = relationship('Item')
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))

    def __repr__(self):
        return f"ItemPrice {self.id}, {self.item}"



