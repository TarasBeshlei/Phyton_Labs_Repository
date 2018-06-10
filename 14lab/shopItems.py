
from app import db


class ShopItems(db.Model):
    __tablename__ = "iot"
    device_id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.String(20))
    item_type = db.Column('item_type', db.String(20))
    price = db.Column('price', db.Integer)
    brand = db.Column('brand', db.String(20))

    def to_string(self):
        return str("id: " + str(self.device_id) + "\nname: " + str(self.name) +
                   "\nprice: " + str(self.price) + "\nbrand: " + str(self.brand) +
                   "\ntype: " + str(self.item_type))