from webapp.db import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(200), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"Item {self.id}, {self.name}"


class ItemPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))

    def __repr__(self):
        return f"ItemPrice {self.id}, {self.name}"
