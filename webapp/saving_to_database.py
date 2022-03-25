from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False) #backref=db.backref('ItemPrice', lazy=True))
    item = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return 'Item %r' % self.name
    

class ItemPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String, db.ForeignKey('item.url'), nullable=False)
    item = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name
