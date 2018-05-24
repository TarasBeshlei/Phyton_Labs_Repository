from enum import Enum


class Item_type(Enum):
    winter = "winter"
    spring = "spring"
    summer = "summer"
    autumn = "autumn"

class Items:

 def __init__(self, name, item_type, price, brand):
     self.item_type = item_type
     self.price = price
     self.name = name
     self.brand = brand


 def __str__(self):
     return "Name " + str(self.name) + "Price " + str(self.price) + "Item type " + str(self.item_type)

