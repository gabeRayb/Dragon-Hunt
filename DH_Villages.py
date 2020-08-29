# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:11:04 2020

Authors: Johnnie Clark, Gabriel Rayburn
"""
import DH_Items as all_items
import DH_Title_Screen as ts
############################## VILLAGES & SHOPS ##############################

class village():
    def __init__(self, items):
        self.items = {}
    
    def intro(self):
        print('You enter the ' + self.name + ' Shop...')
        print(self.shopkeeper + ': Welcome to ' + self.name + '! My name is ' + self.shopkeeper + '.')
        print(self.shopkeeper + ': Let me know if you would like to buy or sell anything. I can also give you info or history of the town.')
        
    def display_items(self, player):
        ts.clr()
        print('''Here are the items I have to offer, just tell me the name of the item you wish to purchase and we can do business. If you're done shopping just type 'done'. (Case sensitive)''')
        print(f"Your gold: {player.gold}\n")
        for i in self.items:
            self.items[i].display()
            print('\n')
    def sell_item(self, player):
        self.display_items(player)
        choice = input(">")
        while choice != "Done":
            if self.items.get(choice) == None:
                print('''That isn't a valid input, please choose an item I am selling or type 'done' to leave the shop.''')
                choice = input(">")
                continue
            if self.items[choice].sell_price > player.gold:
                print("You don't have enough coin to cover the cost of that item.")
            else:
                player.items.append(self.items[choice])
                if isinstance(self.items[choice], all_items.offensive):
                    player.attack += self.items[choice].dmg
                elif isinstance(self.items[choice], all_items.defensive):
                    player.defense += self.items[choice].armor
                player.gold -= self.items[choice].sell_price
                del self.items[choice]
                ts.clr()
                self.display_items(player)
                print(f"You received a {choice}.\n")
            choice = input("Would you like to buy another item?\n>")
        return
class west_lacdel(village):
    def __init__(self, items, name = None, shopkeeper = None):
        super().__init__(items)
        self.items = all_items.first_shop
        self.name = 'West Lacdel'
        self.shopkeeper = 'Bart Maxim'
    
    def backstory(self):
        print(self.shopkeeper + ': If you noticed on your way in, the area surrounding our town is covered in a thick fog. West Lacdel is home to many conspiracy theorists.')
        print(self.shopkeeper + ': Long ago West Lacdel was ambushed by bandits who slaughtered and stole from every villager they caught.')
        print(self.shopkeeper + ': After their conquest, the bandits occupied their new territory, however, legend says shortly after the attack, the Goddess known as Karma brought a heavy mist over the town.')
        print(self.shopkeeper + ": After several months, travelers entered the town to find no signs of life in the town. No bodies, no animals, not even the remnants from the previous slaughter. Most ghost stories originate from this town's eerie past.")
        print(self.shopkeeper + ': Few people live in here in West Lacdel but if you ask any one of the settlers, they will surely have a tale to tell about an encounter with the supernatural.')

class fort_aryndale(village):
    def __init__(self, items, name = None, shopkeeper = None):
        super().__init__(items)
        self.name = 'Fort Aryndale'
        self.shopkeeper = 'Karla Van Hilton'
    
    def backstory(self):
        print(self.shopkeeper + ': Long ago, these lands were ravaged by war. Fort Ayrndale, known as just Ayrndale back then, was at the center of a feud between the two neighboring towns Stalrder and Ruyafield.')
        print(self.shopkeeper + ": Eventually, Ayrndale was overtaken by Ruyafield in an effort to gain more military power in the war. Ruyafield’s new found advantage eventually gave them the winning edge in the war and brought the chaos to an end.")

class briwith(village):
    def __init__(self, items, name = None, shopkeeper = None):
        super().__init__(items)
        self.name = 'Briwith'
        self.shopkeeper = 'Charley Markets'
    
    def backstory(self):
        print(self.shopkeeper + ': Briwith is a sprawling, wealthy city due to the entrepreneurial focused culture. Many travelers from all over the world travel here to seek new opportunities and a shot at the high life.')
        print(self.shopkeeper + ': Few succeed but those who do, go very far. Inventions such as the wheeled carriage, arrow quiver, and yeezys originated here.')

class savage_hills(village):
    def __init__(self, items, name = None, shopkeeper = None):
        super().__init__(items)
        self.name = 'Savage Hills'
        self.shopkeeper = 'Brutus'
    
    def backstory(self):
        print(self.shopkeeper + ': This village used to be called Winterfell. It was used as a resting and trade point between the cities separated by the mountain range. The giant race has watched over these mountains for eons.')
        print(self.shopkeeper + ': About a year ago a mysterious figure wandered into town and people in the village started disappearing. Shortly after, creatures staring to appear along the paths surrounding the village attacking those who travel through.')
        print(self.shopkeeper + ': The mysterious figure ran off into the hills once people began to question him and he was never seen again. The giants have been angered and now attack anyone on sight. From time to time you can hear a loud roar coming from deeper in the mountain.')
        print(self.shopkeeper + ': Some say they’ve seen some sort of abomination creeping out in the caves, and others think its just an unlucky soul whose encountered a giant. Nowadays folks have been calling this place the Savage Hills.')

class hadsoria(village):
    def __init__(self, items, name = None, shopkeeper = None):
        super().__init__(items)
        self.name = 'Hadsoria'
        self.shopkeeper = "T'Aarik"
    
    def backstory(self):
        print(self.shopkeeper + ': Hadsoria is home to the king of Doriona. It was named after the massive lake that it was built near. Legends tell of a powerful creature that lives in and defends the great lake. Nobody knows just how deep the lake goes.')
        print(self.shopkeeper + ": Being one of the grand cities and home to the king, Hadsoria is teeming with wealth and people. In the center of the city you can find the King’s castle which is surrounded by another great wall.")

villages = {1: west_lacdel(all_items.first_shop),
            2: fort_aryndale(all_items.first_shop),
            3: briwith(all_items.first_shop),
            4: savage_hills(all_items.first_shop),
            5: hadsoria(all_items.first_shop)}