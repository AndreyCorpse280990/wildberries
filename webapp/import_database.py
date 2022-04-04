import selenium_similar
from webapp.saving_to_database import *
import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

def save_to_base():
    info = selenium_similar.get_html(url=config.URL_SELENIUM)
    for name, price, url in zip(info[0], info[1], info[2]):
        item = Item(name=name, url=url)
        item_price = ItemPrice(price=price, name=name)
        db.session.add(item)
        db.session.add(item_price)
        db.session.commit()





if __name__ == "__main__":
    save_to_base()
