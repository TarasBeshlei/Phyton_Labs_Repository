from flask import request

from app import app, db
from shopItems import ShopItems


@app.route('/')
def index():
    firstmember = ShopItems.query.first()
    return '<h1> Here you can find device list! </h1>'

@app.route('/device')
def view():
    device = ShopItems.query.first()
    if device is not None:
        return str('First member name \n' + device.to_string())
    else:
        return "Device with this id does not exist"

@app.route('/device/<id>')
def get_device(id):
    device = ShopItems.query.get(id)
    if device is not None:
        return device.to_string()
    else:
        return "Device with this id does not exist"

@app.route('/device', methods=['POST'])
def add_device():
    device_id = request.json['id']
    name = request.json['name']
    item_type = request.json['item_type']
    price = request.json['price']
    brand = request.json['brand']

    new_device = ShopItems()
    new_device.device_id = device_id
    new_device.name = name
    new_device.item_type = item_type
    new_device.price = price
    new_device.brand = brand

    db.session.add(new_device)
    db.session.commit()

    return str(new_device.to_string())

@app.route('/device/<id>', methods=['PUT'])
def device_update(id):
    name = request.json['name']
    item_type = request.json['item_type']
    price = request.json['price']
    brand = request.json['brand']

    new_device = ShopItems.query.get(id)
    new_device.name = name
    new_device.item_type = item_type
    new_device.price = price
    new_device.brand = brand

    db.session.commit()

    return new_device.to_string()

@app.route('/device/<id>', methods=['DELETE'])
def device_delete(id):
    device = ShopItems.query.get(id)
    db.session.delete(device)
    db.session.commit()

    return str("Deleting succssesful")