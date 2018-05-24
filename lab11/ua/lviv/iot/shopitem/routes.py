from flask import request

from ua.lviv.iot.shopitem.Boer import Boer
from ua.lviv.iot.shopitem.Coil import Coil
from ua.lviv.iot.shopitem.Items import Item_type
from ua.lviv.iot.shopitem.myapp import app

new_Boer = Boer("Boer", Item_type.winter.value, 4000, " Flagman ")
new_Coil = Coil("Coil", Item_type.winter.value, 3500, " Fisherman ")

new_dict = {
    '1': new_Boer,
    '2': new_Coil
}


@app.route('/fishingshop/items/<id>', methods=['GET'])
def getItem(id):
    if id in new_dict:
        return new_dict[id].__dict__.__str__()


@app.route('/fishingshop/items', methods=['POST', 'PUT'])
def postItem():
    req_data = request.get_json()
    name = req_data['name']
    item_type = req_data['Item_type']
    price = req_data['price']
    brand = req_data['brand']
    id = req_data['id']
    new_item = Boer(name, item_type, price, brand)
    new_dict[id] = new_item
    return 'post works or put works'

@app.route('/fishingshop/items', methods=['DELETE'])
def deleteItem():
    req_data = request.get_json()
    id = req_data['id']
    new_dict.pop(id)
    return 'delete works'
