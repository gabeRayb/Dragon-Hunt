#import pygame as pg

# #initialzie the pygame
# pg.init()

# #create window/screen for game
# window = pg.display.set_mode((800,600))
# pg.display.set_caption("Dragon Hunt")
# icon = pg.image.load('dragon.png')
# pg.display.set_icon(icon)

############################ PLAYER CHARACTER SETUP ############################

class player_setUp: # Base class for setting up a character
    def __init__(self, name, race, currExp = None, neededExp = None, level = None):
        self.name = name
        self.race = race
        self.currExp = 0
        self.neededExp = 100
        self.level = 1
        
    def print_stats(self):
        print('Name:', self.name)
        print('Race:', self.race)
        print('Experience: {}/{}'.format(self.currExp, self.neededExp))
        print('Level:', self.level)
        
    # def levelUp(self):
    #     self.health += self.health*0.1
    #     self.mana += self.mana*0.1
    #     self.phy_att = self.phy_att*0.1
    #     self.mag_att = self.mag_att*0.1
    #     self.defense = self.defense*0.1
        
class mage(player_setUp): 
    def __init__(self, name, race, player_class, health = None, mana = None, phy_att = None, mag_att = None, defense = None):
        super().__init__(name, race)
        self.player_class = player_class
        self.health = 100
        self.mana = 200
        self.phy_att = 5
        self.mag_att = 20
        self.defense = 10
        
    def print_stats(self):
        super().print_stats()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Physical Attack:', self.phy_att)
        print('Magical Attack:', self.mag_att)
        print('Defense:', self.defense)
        print('\n')
    
class warrior(player_setUp):
    def __init__(self, name, race, player_class, health = None, mana = None, phy_att = None, mag_att = None, defense = None):
        super().__init__(name, race)
        self.player_class = player_class
        self.health = 200
        self.mana = 100
        self.phy_att = 15
        self.mag_att = 10
        self.defense = 20
        
    def print_stats(self):
        super().print_stats()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Physical Attack:', self.phy_att)
        print('Magical Attack:', self.mag_att)
        print('Defense:', self.defense)
        print('\n')
    
class rogue(player_setUp):
    def __init__(self, name, race, player_class, health = None, mana = None, phy_att = None, mag_att = None, defense = None):
        super().__init__(name, race)
        self.player_class = player_class
        self.health = 150
        self.mana = 150
        self.phy_att = 20
        self.mag_att = 5
        self.defense = 15

    def print_stats(self):
        super().print_stats()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Physical Attack:', self.phy_att)
        print('Magical Attack:', self.mag_att)
        print('Defense:', self.defense)
        print('\n')
        
################################################################################

############################# PLAYER ABILITY SETUP #############################

#class abilities:
    
    
    
name = input('Enter character name: ')
race = input('Enter the race of your character: ')
pClass = input('What class would you like to play as? (Warrior, Mage, Rogue): ')
print('\n')

if pClass == 'Warrior':
    p1 = warrior(name, race, pClass)
    
if pClass == 'Mage':
    p1 = mage(name, race, pClass)
    
if pClass == 'Rogue':
    p1 = rogue(name, race, pClass)
    
p1 = mage(name, race, pClass)
p1.print_stats()

p2 = warrior('Big Smoke', 'Orc', 'Warrior')
p3 = rogue('Young Schmeat', 'Dwarf', 'Rogue')

p2.print_stats()
p3.print_stats()
# #game loop
# running = True
# while running:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             running = False



#pg.quit()