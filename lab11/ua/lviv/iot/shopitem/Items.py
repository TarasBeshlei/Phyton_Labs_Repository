from enum import Enum


class Item_type(Enum):
    winter = "winter"
    spring = "spring"
    summer = "summer"
    autumn = "autumn"

class Items:

 def __init__(self, name, item_type, price):
     self.item_type = item_type
     self.price = price
     self.name = name


 def __str__(self):
     return "Name " + str(self.name) + "Price " + str(self.price) + "Item type " + str(self.item_type)

