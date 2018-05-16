from ua.lviv.iot.shopitem.AutumnRod import AutumnRod
from ua.lviv.iot.shopitem.Boer import Boer
from ua.lviv.iot.shopitem.Coil import Coil
from ua.lviv.iot.shopitem.Hook import Hook
from ua.lviv.iot.shopitem.Items import Item_type
from ua.lviv.iot.shopitem.OneMoreObject import OneMoreObject
from ua.lviv.iot.shopitem.SpringRod import SpringRod
from ua.lviv.iot.shopitem.SummerRod import SummerRod
from ua.lviv.iot.shopitem.WinterRod import WinterRod


class Manager:
    items_list = []

    listForDict = []

    a = {"key" : listForDict}

    def find_by_item_type(self, item_type):
        foended_items = []

        for items in self.items_list:
            if items.item_type == item_type:
                foended_items.append(items)
        return foended_items

    def sort_by_price(self):
        self.items_list.sort(key=lambda items: items.price)
        return self.items_list

    @staticmethod
    def print_list(printed_list):
        for items in printed_list:
            print(items)
        print("\n")


if __name__ == "__main__":
    boer = Boer("Boer ", Item_type.winter.value, 4000, " Flagman ")
    coil = Coil("Coil", Item_type.spring.value, 2050, " Fishing Items ")
    autumnRod = AutumnRod(" Autumn Rod ", Item_type.autumn.value, 3000, " Fisherman ")
    springRod = SpringRod(" Spring Rod", Item_type.spring.value, 213, " Other ")
    summerRod = SummerRod(" Summer Rod ", Item_type.summer.value, 120, " Flagman ")
    winterRod = WinterRod(" Autumn Rod ", Item_type.autumn.value, 3650, " Fisherman ")
    oneMoreObject = OneMoreObject("Object", Item_type.summer, 240, " other brand")


    manager = Manager()
    manager.items_list = [boer, autumnRod, springRod, oneMoreObject]
    manager.print_list(manager.items_list)
    manager.items_list = manager.sort_by_price()
    manager.print_list(manager.items_list)
    manager.items_list = manager.find_by_item_type("winter")
    manager.print_list(manager.items_list)


