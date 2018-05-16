from ua.lviv.iot.shopitem.Items import Items


class AutumnRod(Items):


    def __init__(self, name, item_type, price, brand):
        self.name = name
        self.item_type = item_type
        self.price = price
        self.brand = brand


    def __str__(self):
        return Items.__str__(self)