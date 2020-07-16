#Author: Gabriel Rayburn, Johnnie Clark
#Created 7/9/2020
#Open Source Project: Dragon Hunt

class Item:
    name = ""
    desc = ""
    sell_price = 0
    
    def __init__(self,name,desc,sell_price):
        self.name = name
        self.desc = desc
        self.sell_price = sell_price
    def display(self):
        print("Name: ", self.name)
        print("Description: ", self.desc)
        print("Sell Price: ", self.sell_price)

class Weapon(Item):
    damage = 0
    
class Armor(Item):
    phys_def = 0
    mag_def = 0