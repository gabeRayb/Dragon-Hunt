#Author: Gabriel Rayburn, Johnnie Clark
#Created 7/9/2020
#Open Source Project: Dragon Hunt

class item:
    name = ""
    desc = ""
    sell_price = 0.0
    
    def __init__(self,name,desc,sell_price):
        self.name = name
        self.desc = desc
        self.sell_price = sell_price
    def display(self):
        print("Name: ", self.name)
        print("Description: ", self.desc)
        print("Sell Price: ", self.sell_price)

class offensive(item):
    damage = 0.0
    # crit = 0.0
    
    
class defensive(item):
    armor = 0.0

#First shop
cow_hide_tunic = defensive()
ghostly_vale = defensive()
thicc_winter_coat = defensive()
elven_lace_boots = defensive()
hidden_mist_cowl = defensive()

assassins_spectical = offensive()
psychos_gloves = offensive()
bandits_hood = offensive()
sharpened_stick = offensive()
cursed_medallion = offensive()


#Second shop
military_fatigues = defensive()
buzzed_haircut = defensive()
officers_badge = defensive()
flack_vest = defensive()
ghillie_suit = defensive()

gun = offensive()
stunning_cane = offensive()
shrapnel_grenade = offensive()
iron_gloves = offensive()
tactical_knife = offensive()



ice_pick_earrings = offensive()
shark_tooth_charm = offensive()