#Author: Gabriel Rayburn, Johnnie Clark
#Created 7/9/2020
#Open Source Project: Dragon Hunt

class item:
    def __init__(self,name,desc,sell_price):
        self.name = name
        self.desc = desc
        self.sell_price = sell_price
    def display(self):
        print("Name: ", self.name)
        print("Description: ", self.desc)
        print("Sell Price: ", self.sell_price)
class offensive(item):
    def __init__(self, name, desc, sell_price, dmg):
        super().__init__(name, desc, sell_price)
        self.dmg = dmg
    # crit = 0.0
    def display(self):
        super().display()
        print("Dmg: ", self.dmg)
class defensive(item):
    def __init__(self, name, desc, sell_price, armor):
        super().__init__(name, desc, sell_price)
        self.armor = armor
#Mage starting item
wand = offensive("Wand", "A wand given to those with no experience in magic.", 0, 10)

# #First shop ################################################################
cow_hide_tunic = defensive("Cow Hide Tunic", "Weak armor made from cows.", 5, 5)
ghostly_vale = defensive("Ghostly Vale", "Ghost armor", 5, 5)
thick_winter_coat = defensive("Thick Winter Coat", "Keeps you warm.", 5, 5)
elven_lace_boots = defensive("Elven Lace Boots", "Cool lookin boots.", 5, 5)
hidden_mist_cowl = defensive("Hidden Mist Cowl", "Good for hunting via bow and arrow.", 5, 5)
#
assassins_spectical = offensive("Assassin's Specticals", "They make you look real cool.", 7, 5)
psychos_gloves = offensive("Psycho's Gloves", "Wear these with your Michael Meyers costume.", 7, 5)
bandits_hood = offensive("Bandit's Hood", "You have in itch to steal.", 7, 5)
sharpened_stick = offensive("Sharpened Stick", "It's effective at poking.", 7, 5)
cursed_medallion = offensive("Cursed Medallion", "A strange glowing jewelry.", 7, 5)\

first_shop = {"Cow Hide Tunic": cow_hide_tunic, 
              "Ghostly Vale": ghostly_vale, 
              "Thick Winter Coat": thick_winter_coat, 
              "Elven Lace Boosts": elven_lace_boots, 
              "Hidden Mist Cowl": hidden_mist_cowl,
              "Assassin's Specticals": assassins_spectical, 
              "Psycho's Gloves": psychos_gloves, 
              "Bandit's Hood": bandits_hood, 
              "Sharpened Stick": sharpened_stick,
              "Cursed Medallion": cursed_medallion}
##############################################################################
# #Second shop ###############################################################
military_fatigues = defensive("Military Fatigues", "Where did you go?", 5, 5)
buzzed_haircut = defensive("Buzzed Haircut", "This makes you fit right in.", 5, 5)
officers_badge = defensive("Officer's Badge", "You're identifiable now.", 5, 5)
flack_vest = defensive("Flack Vest", "Effective against explosives.", 5, 5)
ghillie_suit = defensive("Hidden Mist Cowl", "Good for hunting via bow and arrow.", 5, 5)

gun = offensive("Gun", "It goes brrrrrr.", 7, 5)
stunning_cane = offensive("Stunning Cane", "A long taser.", 7, 5)
shrapnel_grenade = offensive("Shrapnel Grenade", "Makes a sharp bang.", 7, 5)
iron_gloves = offensive("Iron Gloves", "Imagine if Mike Tyson had these.", 7, 5)
tactical_knife = offensive("Tactical Knife", "It's sharp, be careful.", 7, 5)
##############################################################################


# ice_pick_earrings = offensive()
# shark_tooth_charm = offensive()