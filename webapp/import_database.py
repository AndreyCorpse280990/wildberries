import selenium_similar
import config

from webapp.parsing.models import Item, ItemPrice
from webapp.db import db


def save_to_base():
    info = selenium_similar.get_html(url=config.URL_SELENIUM)
    for name, price, url in zip(info[0], info[1], info[2]):
        item = Item(name=name, url=url)
        item_price = ItemPrice(price=price, name=name)
        url_exists = Item.query.filter(Item.url == url).first()
        if not url_exists: # не работает с этим циклом хз почему.
            db.session.add(item)
            db.session.add(item_price)
            db.session.commit()


if __name__ == "__main__":
    save_to_base()
